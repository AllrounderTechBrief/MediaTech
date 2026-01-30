import feedparser, json, time

# Feeds that reliably return RSS content
feeds = [
    "https://blog.adobe.com/en/topics/trends-research.rss",
    "https://feeds.feedburner.com/venturebeat/SZZv",
    "https://www.tvtechnology.com/.rss/full/",
    "https://www.broadcastprome.com/feed/",
    "https://www.cisco.com/c/r/newsroom/en/us/rss/security.xml"
]

items = []

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

for url in feeds:
    try:
        # Parse with headers
        d = feedparser.parse(url, request_headers=headers)

        # Skip empty feeds
        if not d.entries:
            print("EMPTY FEED:", url)
            continue

        for e in d.entries[:10]:
            title = e.get("title", "").strip()
            summary = e.get("summary", e.get("description", "")).strip()

            if not title:
                continue

            items.append({
                "title": title,
                "summary": summary,
                "category": "General",
                "source": url,
                "published": e.get("published", time.strftime("%Y-%m-%d"))
            })

    except Exception as ex:
        print("Error:", url, ex)
        continue

# If still empty, provide fallback
if not items:
    items = [{
        "title": "Fallback Article",
        "summary": "RSS temporarily unavailable.",
        "category": "General",
        "source": "local",
        "published": time.strftime("%Y-%m-%d")
    }]

with open("data.json", "w") as f:
    json.dump({"items": items}, f, indent=2)
