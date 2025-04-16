from flask import Flask, render_template, request
from nlp import detect_intent, extract_company
from fetch_data import get_stock_price, get_company_revenue

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chatbot():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        intent = detect_intent(user_input)

        if intent == "company_financials":
            company = extract_company(user_input)
            if company:
                response = get_company_revenue(company)
            else:
                response = "Please specify a company name for revenue info."
        
        elif intent == "stock_price":
            company = extract_company(user_input)
            if company:
                response = get_stock_price(company)
            else:
                response = "Please specify a valid company ticker or name."

        else:
            response = (
                "Hmm, I’m not quite sure what you mean. 🤔<br>"
                "But I can help you with stock prices and company revenues.<br>"
                "Try asking something like 'What’s Tesla’s stock price?' or 'Show me Google's revenue last year.' 📈"
            )

    return render_template("chat.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
