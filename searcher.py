import feedparser
from tavily import TavilyClient
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_KEY = os.getenv("TAVILY_API_KEY")

def search_tavily(query: str, max_results: int = 5) -> list:
    client = TavilyClient(api_key=TAVILY_KEY)
    results = client.search(query=query, max_results=max_results)
    items = []
    for r in results.get("results", []):
        items.append({
            "title": r.get("title"),
            "url": r.get("url"),
            "content": r.get("content"),
            "source": "tavily_search",
            "date_found": str(date.today()),
            "category": "AI_NEWS"
        })
    return items

def fetch_rss(feed_url: str, category: str) -> list:
    feed = feedparser.parse(feed_url)
    items = []
    for entry in feed.entries[:5]:
        items.append({
            "title": entry.get("title"),
            "url": entry.get("link"),
            "content": entry.get("summary", ""),
            "source": feed.feed.get("title", feed_url),
            "date_found": str(date.today()),
            "category": category
        })
    return items

def collect_all_updates() -> list:
    updates = []
    updates += search_tavily("latest AI news today 2026", max_results=5)
    updates += search_tavily("AI internship hiring fresher 2026 India", max_results=5)
    updates += fetch_rss("https://techcrunch.com/category/artificial-intelligence/feed/", "AI_NEWS")
    updates += fetch_rss("https://venturebeat.com/ai/feed/", "AI_NEWS")
    return updates