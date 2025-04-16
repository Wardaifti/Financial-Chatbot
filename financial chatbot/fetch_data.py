import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load your API keys
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
FMP_API_KEY = os.getenv("FMP_API_KEY")
ALPHA_VANTAGE_KEY = os.getenv("alpha_vantage")
TWELVE_DATA_KEY = os.getenv("twelve_data")

# ---------------------------
# Using Financial Modeling Prep (FMP)
# ---------------------------
def get_company_revenue(symbol):
    try:
        url = f"https://financialmodelingprep.com/api/v3/income-statement/{symbol.upper()}?limit=1&apikey={FMP_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data and "revenue" in data[0]:
            revenue = data[0]["revenue"]
            fiscal_date = data[0]["date"]
            return f"{symbol.upper()}'s revenue for {fiscal_date} was ${int(revenue):,}."
        else:
            return f"Revenue data not available for {symbol.upper()}."
    except Exception as e:
        return f"Error fetching revenue: {str(e)}"

# ---------------------------
# Using FMP for Stock Price
# ---------------------------
def get_stock_price(symbol):
    try:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol.upper()}?apikey={FMP_API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data and "price" in data[0]:
            price = data[0]["price"]
            return f"The current stock price of {symbol.upper()} is ${price:.2f}."
        else:
            return f"Price not available for {symbol.upper()}."
    except Exception as e:
        return f"Error fetching stock price: {str(e)}"

# ---------------------------
# Using NewsAPI for Financial News
# ---------------------------
def get_financial_news(query="finance"):
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        articles = response.json().get("articles", [])[:3]  # top 3 headlines
        if not articles:
            return "No recent financial news found."

        news_list = [f"📰 {article['title']} - {article['source']['name']}" for article in articles]
        return "<br>".join(news_list)
    except Exception as e:
        return f"Error fetching news: {str(e)}"

# ---------------------------
# (Optional) Add more functions using Alpha Vantage, Twelve Data, or Finnhub
# ---------------------------
# Example: You can add crypto or forex support later with these APIs

