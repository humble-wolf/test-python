from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

def get_product_price(product_name):
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
        title = product.get("title")
        price = product.get("extracted_price")
        source = product.get("source")
        
        if price:
            print(f"Product: {title}")
            print(f"Price: {price}")
            print(f"Store: {source}\n")
            prices.append(price)

    if prices:
        avg_price = sum(prices) / len(prices)
        print(f"\nAverage Price: ${avg_price:.2f}")
        return avg_price
    else:
        print("No prices found.")
        return None

get_product_price("Coffee Beans 1lb")
