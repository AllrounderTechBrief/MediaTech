# Extract domain name like 'Adobe' or 'TV Tech' instead of full URL
source_name = url.split("//")[-1].split(".")[0].capitalize()

items.append({
    "title": title,
    "summary": summary[:200] + "...", # Truncate for cleaner UI
    "category": source_name,
    "source": url,
    "published": e.get('published', time.strftime('%Y-%m-%d'))
})
