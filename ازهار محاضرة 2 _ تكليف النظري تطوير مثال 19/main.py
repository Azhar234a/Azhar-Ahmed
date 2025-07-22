# news_scraper_rss.py
"""
يجمع عناوين أخبار عربية + إنجليزية عبر RSS
ويحفظها في news_headlines.csv ثم يعرض إحصاءات بسيطة.
"""

import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict

import feedparser
import pandas as pd
from dateutil import parser as dtp

###############################################################################
# 1. المصادر (اسم الموقع ← رابط RSS)
###############################################################################
RSS_FEEDS: Dict[str, str] = {
    # عربية
    "BBC Arabic":        "https://feeds.bbci.co.uk/arabic/rss.xml",
    "Al Jazeera Arabic": "https://www.aljazeera.net/aljazeera/rss/",
    "Sky News Arabia":   "https://www.skynewsarabia.com/rss/latest.xml",
    # إنجليزية
    "Reuters World":     "https://feeds.reuters.com/Reuters/worldNews",
    "BBC World":         "https://feeds.bbci.co.uk/news/world/rss.xml",
    "AP Top News":       "https://apnews.com/rss/apf-topnews",
}

OUT_CSV  = Path("news_headlines.csv")
ENCODING = "utf-8"

###############################################################################
# 2. جلب الأخبار من RSS
###############################################################################
def fetch_headlines() -> List[dict]:
    rows: List[dict] = []
    for site, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for e in feed.entries:
            # بعض الخلاصات تضع updated بدلاً من published
            pub_raw = e.get("published") or e.get("updated") or ""
            dt      = dtp.parse(pub_raw) if pub_raw else datetime.utcnow()
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            dt = dt.astimezone(timezone.utc)
            rows.append(
                {
                    "site": site,
                    "title": e.title.strip(),
                    "published_date": dt.date().isoformat(),
                    "published_time": dt.time().isoformat(timespec="minutes"),
                }
            )
    return rows

###############################################################################
# 3. كتابة CSV
###############################################################################
def write_csv(rows: List[dict]) -> None:
    header = ["site", "title", "published_date", "published_time"]
    with OUT_CSV.open("w", newline="", encoding=ENCODING) as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ Saved {len(rows)} rows → {OUT_CSV}")

###############################################################################
# 4. ملخّص Pandas (بدون وسيطة لا تدعمها إصدارات قديمة)
###############################################################################
def pandas_summary() -> None:
    df = pd.read_csv(OUT_CSV)
    print("\n== head() ==");   print(df.head())
    print("\nshape:", df.shape)
    print("\n== info() ==");   df.info()
    print("\n== describe() =="); print(df.describe(include="all"))

###############################################################################
# 5. التنفيذ
###############################################################################
if __name__ == "__main__":
    rows = fetch_headlines()
    if not rows:
        print("⚠️  لم تُجلب أي عناوين – تحقق من الاتصال أو من روابط RSS.")
    else:
        write_csv(rows)
        pandas_summary()
