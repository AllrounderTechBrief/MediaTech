function render(cat=null) {
    let g = document.getElementById('grid');
    g.innerHTML = '';
    
    data.filter(i => !cat || i.category === cat).forEach(n => {
        let c = document.createElement('div');
        c.className = 'card';
        
        // Dynamic Favicon Extraction
        const domain = new URL(n.source).hostname;
        const favicon = `https://www.google.com/s2/favicons?sz=64&domain=${domain}`;

        c.innerHTML = `
            <div class="meta">
                <img src="${favicon}" style="width:16px; vertical-align:middle; margin-right:5px;">
                ${n.category || 'BROADCAST IT'} 
            </div>
            <h2>${n.title}</h2>
            <div class='summary'>${n.summary.substring(0, 150)}...</div>
        `;
        g.appendChild(c);
    });
}
