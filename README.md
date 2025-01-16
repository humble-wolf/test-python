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
     SERPAPI_KEY=your_actual_serpapi_key
     ```

4. Run the analysis:
   ```bash
   python src/analysis.py data/products.csv
   ```

## Output
- **Report:** Generated in `report.md`.