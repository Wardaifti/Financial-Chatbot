# nlp.py
import spacy
import re

# Load the English model
nlp_spacy = spacy.load("en_core_web_sm")

# Known company mappings
COMMON_COMPANIES = {
    "google": "GOOGL",
    "apple": "AAPL",
    "tesla": "TSLA",
    "amazon": "AMZN",
    "meta": "META",
    "microsoft": "MSFT",
    "netflix": "NFLX",
    "nvidia": "NVDA",
    "facebook": "META",
    "alphabet": "GOOGL"
}

# Intent patterns
INTENTS = {
    "stock_price": re.compile(r"(price|stock|rate)", re.IGNORECASE),
    "company_financials": re.compile(r"(revenue|income|profit|market cap|eps|earnings)", re.IGNORECASE),
    "crypto_price": re.compile(r"(bitcoin|ethereum|crypto)", re.IGNORECASE),
    "forex_rate": re.compile(r"(usd|eur|exchange|forex)", re.IGNORECASE),
    "news": re.compile(r"(news|headlines|latest updates)", re.IGNORECASE),
}

# Detect intent
def detect_intent(query):
    for intent, pattern in INTENTS.items():
        if pattern.search(query):
            return intent
    return "unknown"

# Extract company using spaCy + common list
def extract_company(query):
    doc = nlp_spacy(query)
    for ent in doc.ents:
        if ent.label_ == "ORG":
            name = ent.text.lower()
            if name in COMMON_COMPANIES:
                return COMMON_COMPANIES[name]
    # fallback using lowercased words
    for word in query.lower().split():
        if word in COMMON_COMPANIES:
            return COMMON_COMPANIES[word]
    return None

