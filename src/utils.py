from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_product_price(product_name):
    search = GoogleSearch({
        "q": product_name,
        "tbm": "shop",
        "hl": "en",
        "gl": "us",
        "api_key": os.getenv("SERPAPI_KEY")
    })

    results = search.get_json()
    
    products = results.get("shopping_results", [])
    
    prices = []

    for product in products:
        price = product.get("extracted_price")
        
        if price:
            prices.append(price)

    if prices:
        avg_price = sum(prices) / len(prices)
        return avg_price
    else:
        return None
