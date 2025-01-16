# Product Price Analysis Tool

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/humble-wolf/test-python
   cd test-python
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   ```

3. **Set up your SerpAPI Key:**
   - Sign up at [SerpAPI](https://serpapi.com/) to get your API key.
   - Create a `.env` file with your SerpAPI key:
     ```bash
     cp .env.example .env
     ```
   - Replace `your_serpapi_key_here` with your actual key:
     ```env
     SERPAPI_KEY=5aff133e29fd5445866d4ec9cc53c7ed8278c0e36bbe6fa9deb00d693e88aa93
     ```

4. Run the analysis:
   ```bash
   python src/analysis.py data/products.csv
   ```

## Approach
- Reads product data from `products.csv`.
- Fetches market prices using SerpAPI (Google Shopping).
- Compares our prices to market prices and generates insights.

## Known Issues/Limitations
- Free SerpAPI tier limits the number of searches.
- Results depend on available product data in Google Shopping.

## Time Spent on Components
- Project Setup: 5 minutes
- Data Integration: 30 minutes
- Analysis & Reporting: 10 minutes
- Testing & Debugging: 5 minutes

## Output
- **Report:** Generated in `report.md`.