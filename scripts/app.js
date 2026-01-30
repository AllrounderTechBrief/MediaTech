function render(cat = null) {
    const grid = document.getElementById('grid');
    grid.innerHTML = '';

    data.filter(i => !cat || i.category === cat).forEach(item => {
        const card = document.createElement('div');
        card.className = 'card';
        
        // Use Google's favicon service for the source icon
        const favicon = `https://www.google.com/s2/favicons?sz=64&domain=${item.source_domain}`;

        card.innerHTML = `
            <a href="${item.link}" target="_blank" style="text-decoration:none; color:inherit;">
                <img src="${item.image}" class="card-img" onerror="this.src='https://via.placeholder.com/400x200?text=MediaTech'">
                <div class="card-content">
                    <div class="source-tag">
                        <img src="${favicon}" style="width:14px; margin-right:5px;">
                        ${item.category}
                    </div>
                    <h2>${item.title}</h2>
                    <p style="color:#aaa; font-size:0.9rem;">${item.summary}</p>
                </div>
            </a>
        `;
        grid.appendChild(card);
    });
}
