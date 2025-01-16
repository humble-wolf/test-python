import sys
import pandas as pd
from utils import fetch_product_price

def analyze_prices(csv_path):
    df = pd.read_csv(csv_path)

    insights = []
    data_issues = []

    for _, row in df.iterrows():
        product_name = row["product_name"]

        if pd.isna(product_name) or pd.isna(row["our_price"]):
            data_issues.append(f"Missing data for product: {row}")
            continue

        print(f"Fetching price for {product_name}...")
        avg_price = fetch_product_price(product_name)

        if avg_price:
            insight = {
                "product_name": product_name,
                "our_price": row["our_price"],
                "average_market_price": avg_price,
                "price_difference": round(avg_price - row["our_price"], 2)
            }
            insights.append(insight)
        else:
            data_issues.append(f"No price data found for {product_name}")

    # Create report
    with open("report.md", "w") as report:
        report.write("# Data Analysis Report\n\n")

        report.write("## Data Quality Issues\n")
        if data_issues:
            for issue in data_issues:
                report.write(f"- {issue}\n")
        else:
            report.write("- No data quality issues found.\n")

        report.write("\n## Cleaned Data Summary\n")
        report.write(df.dropna().to_markdown(index=False))

        report.write("\n\n## External Data Integration Results\n")
        insights_df = pd.DataFrame(insights)
        if not insights_df.empty:
            report.write(insights_df.to_markdown(index=False))
        else:
            report.write("- No external data could be integrated.\n")

        report.write("\n\n## Business Insights\n")
        for insight in insights:
            if insight['price_difference'] > 0:
                report.write(f"- {insight['product_name']} is underpriced by ${insight['price_difference']:.2f}\n")
            elif insight['price_difference'] < 0:
                report.write(f"- {insight['product_name']} is overpriced by ${abs(insight['price_difference']):.2f}\n")
            else:
                report.write(f"- {insight['product_name']} is competitively priced.\n")

        report.write("\n## Future Recommendations\n")
        report.write("- Review pricing for underpriced or overpriced products.\n")
        report.write("- Continue market price monitoring regularly.\n")
        report.write("- Expand product line based on trending items.\n")

    print("Analysis complete. Results saved to report.md")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/analysis.py data/products.csv")
        sys.exit(1)
    analyze_prices(sys.argv[1])
