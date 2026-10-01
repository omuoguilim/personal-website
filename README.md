# My personal website

I’m Oluchi Muoguilim, a computer science and business student at Emory. I made this website to put my projects, experience and a little of my life in one place.

I wanted it to feel like a small computer desktop: pixel details, window-style panels and pink buttons. It includes my projects, toolbox, current work and a few things I’m doing outside class.

[Visit my website](https://omuoguilim.github.io/personal-website/)

I also publish a [second portfolio link](https://oluchi-muoguilim.superct3663.chatgpt.site). That site has a separate deployment.

## Projects and demos

I link to the source repositories for DoseBuddy, ShareCompass and my market regime research. The project buttons also open browser demos where available.

DoseBuddy’s repository contains the native Flutter app. Its browser demo is a separate Flutter web build with sample records. ShareCompass has an isolated browser demo alongside its Firebase account mode. I keep demo data separate from real accounts.

## Run locally

The portfolio uses HTML, CSS and JavaScript, so I don’t need a framework build to preview it.

```sh
python3 -m http.server 8000
```

I open `http://localhost:8000` from the project folder. GitHub Pages publication is configured in `.github/workflows/pages.yml`.

I keep the main page in `index.html`, styling in `styles.css` and interaction code in the JavaScript files. Demo applications have their own build and hosting setup.
