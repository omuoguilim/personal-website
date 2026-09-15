const year=document.querySelector('[data-year]');
const clock=document.querySelector('.clock');
year.textContent=new Date().getFullYear();
function tick(){clock.textContent=new Intl.DateTimeFormat([],{hour:'numeric',minute:'2-digit'}).format(new Date())}
tick();setInterval(tick,30000);
