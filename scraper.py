import requests
from bs4 import BeautifulSoup
import re
import statistics
import time
import os
import json

# Your Reverb API Token (Will be passed in via GitHub Secrets)
REVERB_TOKEN = os.environ.get("REVERB_API_TOKEN", "")

# Map your unique markdown tags to both Reverb and eBay search parameters
INSTRUMENTS = {
    "OM-27": {
        "reverb": "Suzuki Omnichord OM-27",
        "ebay": "Suzuki Omnichord OM-27 -adapter -overlay"
    },
    "OM-84": {
        "reverb": "Suzuki Omnichord OM-84",
        "ebay": "Suzuki Omnichord OM-84 -adapter"
    },
    "QCHORD": {
        "reverb": "Suzuki QChord QC-1",
        "ebay": "Suzuki QChord QC-1"
    },
    "POLY800": {
        "reverb": "Korg Poly-800",
        "ebay": "Korg Poly-800 synthesizer"
    }
}

def get_reverb_price(query):
    """Fetches the estimated market value directly from Reverb's Price Guide API."""
    if not REVERB_TOKEN:
        print("  -> Reverb token missing. Skipping Reverb...")
        return None

    url = f"https://api.reverb.com/api/priceguide?query={query}"
    headers = {
        "Authorization": f"Bearer {REVERB_TOKEN}",
        "Accept": "application/hal+json",
        "Accept-Version": "3.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Check if Reverb found a matching price guide
        if data.get('price_guides'):
            guide = data['price_guides'][0]
            # Reverb provides a low and high estimate; we calculate the median
            low = float(guide['estimated_value']['bottom_price'])
            high = float(guide['estimated_value']['top_price'])
            return round((low + high) / 2, 2)
            
    except requests.exceptions.RequestException as e:
        print(f"  -> Reverb API Error for {query}: {e}")
        
    return None

def get_ebay_price(query):
    """Fallback scraper for eBay sold listings."""
    url = f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ', '+')}&LH_Sold=1&LH_Complete=1&_ipg=60"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    prices = []

    for item in soup.find_all('div', class_='s-item__info'):
        price_element = item.find('span', class_='s-item__price')
        if not price_element:
            continue
            
        price_text = price_element.text.strip()
        if 'to' in price_text.lower():
            continue
            
        clean_price_str = re.sub(r'[^\d.]', '', price_text)
        try:
            if clean_price_str:
                prices.append(float(clean_price_str))
        except ValueError:
            continue

    if not prices:
        return None
        
    if len(prices) > 4:
        prices.sort()
        # Trim extreme values
        trim = max(1, len(prices) // 10)
        prices = prices[trim:-trim]
        
    return round(statistics.mean(prices), 2)

def update_readme(market_data):
    """Replaces the HTML placeholder tags in your markdown file with live data."""
    readme_path = 'README.md'
    
    if not os.path.exists(readme_path):
        print("README.md not found. Ensure the script is running in the repository root.")
        return

    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for model_id, avg_price in market_data.items():
        if avg_price == "N/A":
            continue
            
        # Regex to find: <!-- PRICE_MODEL_START -->ANY_TEXT<!-- PRICE_MODEL_END -->
        pattern = rf'(<!-- PRICE_{model_id}_START -->).*?(<!-- PRICE_{model_id}_END -->)'
        replacement = rf'\1{avg_price}\2'
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print("Market data successfully written to README.md.")

def main():
    market_report = {}
    print("Starting Hybrid Market Tracker (Reverb + eBay)...\n")
    
    for model_id, queries in INSTRUMENTS.items():
        print(f"Fetching data for {model_id}...")
        
        # 1. Try Reverb First
        price = get_reverb_price(queries['reverb'])
        
        # 2. Fallback to eBay if Reverb fails or returns nothing
        if price is None:
            print(f"  -> Reverb failed or returned no data. Falling back to eBay...")
            price = get_ebay_price(queries['ebay'])
            # Be polite to eBay servers
            time.sleep(3) 
            
        final_price = f"${price:.2f}" if price else "N/A"
        market_report[model_id] = final_price
        print(f"  -> Value: {final_price}")
        
    update_readme(market_report)

if __name__ == "__main__":
    main()
