import sys
import pandas as pd
from utils import fetch_product_price

def analyze_prices(csv_path):
    df = pd.read_csv(csv_path)

    insights = []

    for _, row in df.iterrows():
        product_name = row["product_name"]
        print(f"Fetching price for {product_name}...")
        avg_price = fetch_product_price(product_name)

        insight = {
            "product_name": product_name,
            "our_price": row["our_price"],
            "average_market_price": avg_price,
            "price_difference": round(avg_price - row["our_price"], 2)
        }
        insights.append(insight)

    insights_df = pd.DataFrame(insights)
    insights_df.to_markdown("report.md", index=False)
    print("Analysis complete. Results saved to report.md")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/analysis.py data/products.csv")
        sys.exit(1)
    analyze_prices(sys.argv[1])
