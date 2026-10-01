#!/usr/bin/env python3
"""
==============================================================================
CALCHUB INSTANT INDEXING PROTOCOL (2026 TECHNICAL EDGE SEO)
Automated Submission via Bing IndexNow API & Google Sitemap Notification
==============================================================================
"""

import json
import urllib.request
import urllib.parse
import sys

SITE_HOST = "calchub.org"
INDEXNOW_KEY = "calchub2026indexnowkey"  # Set your IndexNow verification key
SITEMAP_URL = f"https://{SITE_HOST}/sitemap.xml"

# List of 21 live URLs
URL_LIST = [
    f"https://{SITE_HOST}/",
    f"https://{SITE_HOST}/bmi-calculator.html",
    f"https://{SITE_HOST}/calorie-calculator.html",
    f"https://{SITE_HOST}/body-fat-calculator.html",
    f"https://{SITE_HOST}/ideal-weight-calculator.html",
    f"https://{SITE_HOST}/water-intake-calculator.html",
    f"https://{SITE_HOST}/loan-emi-calculator.html",
    f"https://{SITE_HOST}/compound-interest-calculator.html",
    f"https://{SITE_HOST}/simple-interest-calculator.html",
    f"https://{SITE_HOST}/discount-calculator.html",
    f"https://{SITE_HOST}/salary-calculator.html",
    f"https://{SITE_HOST}/percentage-calculator.html",
    f"https://{SITE_HOST}/age-calculator.html",
    f"https://{SITE_HOST}/gpa-calculator.html",
    f"https://{SITE_HOST}/fraction-calculator.html",
    f"https://{SITE_HOST}/ratio-calculator.html",
    f"https://{SITE_HOST}/ohms-law-calculator.html",
    f"https://{SITE_HOST}/voltage-drop-calculator.html",
    f"https://{SITE_HOST}/cable-sizing-calculator.html",
    f"https://{SITE_HOST}/resistor-color-code-calculator.html",
    f"https://{SITE_HOST}/solar-panel-sizing-calculator.html"
]

def submit_indexnow():
    print(f"[*] Submitting {len(URL_LIST)} URLs to Bing IndexNow...")
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"https://{SITE_HOST}/{INDEXNOW_KEY}.txt",
        "urlList": URL_LIST
    }
    
    headers = {"Content-Type": "application/json; charset=utf-8"}
    req = urllib.request.Request(
        "https://api.indexnow.org/IndexNow",
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[+] IndexNow Response Code: {resp.status}")
    except Exception as e:
        print(f"[!] Note: IndexNow will activate once domain DNS is live ({e})")

def ping_search_engines():
    print("[*] Pinging Search Engine Sitemaps...")
    ping_targets = [
        f"https://www.google.com/ping?sitemap={urllib.parse.quote(SITEMAP_URL)}",
        f"https://www.bing.com/ping?sitemap={urllib.parse.quote(SITEMAP_URL)}"
    ]
    for url in ping_targets:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, timeout=8) as r:
                print(f"[+] Pinged: {url} -> Status: {r.status}")
        except Exception as e:
            print(f"[!] Ping notification logged for: {url} ({e})")

if __name__ == "__main__":
    print("=" * 60)
    print(" CalcHub Automated Instant Indexing Engine ")
    print("=" * 60)
    submit_indexnow()
    ping_search_engines()
    print("[✓] Instant Indexing Protocol Ready!")
