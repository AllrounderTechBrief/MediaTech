import feedparser, json, time

# Improved list of high-quality Broadcast & Media Tech feeds
feeds = [
    ("Adobe Trends", "https://blog.adobe.com/en/topics/trends-research.rss"),
    ("TV Tech", "https://www.tvtechnology.com/.rss/full/"),
    ("Broadcast Pro", "https://www.broadcastprome.com/feed/"),
    ("The Verge (Tech)", "https://www.theverge.com/rss/index.xml"),
    ("Cisco Security", "https://newsroom.cisco.com/c/r/newsroom/en/us/rss/security.xml"),
    ("ZDNet AI", "https://www.zdnet.com/topic/artificial-intelligence/rss.xml"),
    ("Avid News", "https://www.avid.com/blog/rss.xml")
]

items = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def get_image(entry):
    """Deep search for images in typical RSS structures."""
    # 1. Check media:content
    if 'media_content' in entry and entry.media_content:
        return entry.media_content[0]['url']
    # 2. Check enclosures
    if 'links' in entry:
        for link in entry.links:
            if 'image' in link.get('type', ''):
                return link.get('href')
    # 3. Check for image in summary/description HTML (Optional fallback)
    return "assets/placeholder.jpg" # Default if none found

for name, url in feeds:
    try:
        d = feedparser.parse(url, request_headers=headers)
        if not d.entries: continue

        for e in d.entries[:8]:
            items.append({
                "title": e.get("title", "").strip(),
                "summary": e.get("summary", e.get("description", ""))[:200] + "...",
                "category": name,
                "link": e.get("link", "#"),
                "image": get_image(e),
                "source_domain": url.split('/')[2],
                "published": e.get("published", time.strftime('%Y-%m-%d'))
            })
    except Exception as ex:
        print(f"Error on {name}: {ex}")

with open("data.json", "w") as f:
    json.dump({"items": items}, f, indent=2)
