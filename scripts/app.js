
let data=[]; let mostRead={}; let slideIndex=0;
setInterval(()=>{const s=document.querySelectorAll('.slide');s.forEach(x=>x.classList.remove('active'));s[slideIndex].classList.add('active');slideIndex=(slideIndex+1)%s.length;},6000);
fetch('data.json').then(r=>r.json()).then(j=>{data=j.items;renderTicker();renderTopStories();renderTabs();render();});
function renderTicker(){document.getElementById('ticker-text').innerText=data.slice(0,10).map(x=>x.title).join(' ⚡ ');} 
function renderTopStories(){let ul=document.getElementById('top-stories');ul.innerHTML='';data.slice(0,5).forEach(i=>{let li=document.createElement('li');li.textContent=i.title;ul.appendChild(li);});}
function renderTabs(){let t=document.getElementById('tabs');[...new Set(data.map(i=>i.category||'General'))].forEach(c=>{let b=document.createElement('button');b.textContent=c;b.onclick=()=>render(c);t.appendChild(b);});}
function render(cat=null){let g=document.getElementById('grid');g.innerHTML='';data.filter(i=>!cat||i.category===cat).forEach(n=>{let c=document.createElement('div');c.className='card';c.innerHTML=`<h2>${n.title}</h2><span class='toggle'>Show</span><div class='summary'>${n.summary}</div>`;c.querySelector('.toggle').onclick=()=>{let s=c.querySelector('.summary');s.style.display=s.style.display=='block'?'none':'block';mostRead[n.title]=(mostRead[n.title]||0)+1;};g.appendChild(c);});}
