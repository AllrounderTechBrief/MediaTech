
import feedparser, json
feeds=[
"https://blog.adobe.com/en/topics/trends-research.rss",
"https://www.avid.com/blog/rss.xml",
"https://feeds.feedburner.com/venturebeat/SZZv",
"https://www.tvtechnology.com/.rss/full/",
"https://www.thebroadcastbridge.com/home/rss",
"https://newsroom.cisco.com/c/r/newsroom/en/us/rss/security.xml",
"https://www.ncsc.gov.uk/information/rss-feeds",
"https://www.broadcastprome.com/feed/"
]
items=[]
for url in feeds:
 d=feedparser.parse(url)
 for e in d.entries[:10]: items.append({"title":e.title,"summary":e.get('summary',''),"category":"General","source":url})
with open('data.json','w') as f: json.dump({"items":items},f,indent=2)
