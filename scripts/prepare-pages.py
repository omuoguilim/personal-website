"""Package the verified app builds under the GitHub Pages project path."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import time
import urllib.request

manifest = json.loads(Path('demo-assets-manifest.json').read_text())
output = Path('_site')

def download(entry):
    path = entry['path']
    for attempt in range(3):
        try:
            request = urllib.request.Request(manifest['origin'] + '/' + path, headers={'User-Agent': 'Portfolio-Pages-Build'})
            with urllib.request.urlopen(request, timeout=90) as response:
                data = response.read()
            if hashlib.sha256(data).hexdigest() != entry['sha256']:
                raise ValueError('Asset changed: ' + path + ' length=' + str(len(data)) + ' sha=' + hashlib.sha256(data).hexdigest() + ' preview=' + repr(data[-1600:]))
            destination = output / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.suffix in {'.html', '.js', '.css', '.json'}:
                text = data.decode('utf-8')
                text = text.replace('/demos/', '/personal-website/demos/')
                text = text.replace('/apps/sharecompass/', '/personal-website/apps/sharecompass/')
                data = text.encode('utf-8')
            destination.write_bytes(data)
            return path
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for path in pool.map(download, manifest['files']):
        print('Prepared', path)

wrapper = output / 'demos/dosebuddy/index.html'
text = wrapper.read_text()
assert 'src="app/index.html' in text
assert 'href="app/index.html"' in text
assert 'chatgpt.site' not in text
assert '<base href="/personal-website/demos/dosebuddy/app/">' in (output / 'demos/dosebuddy/app/index.html').read_text()
assert 'chatgpt.site' not in (output / 'index.html').read_text()
