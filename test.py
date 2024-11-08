import yfinance as yf
import pandas as pd

# Exempelaktier att analysera
tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', "NVDA", "AZN", "BRK.B"]

# Skapa en funktion för att hämta nyckeltal från yfinance
def fetch_financial_data(ticker):
    stock = yf.Ticker(ticker)
    pe_ratio = stock.info.get('trailingPE')
    roe = stock.info.get('returnOnEquity')
    debt_to_equity = stock.info.get('debtToEquity')
    return pe_ratio, roe, debt_to_equity

# Hämta data för varje aktie
financial_data = {}
for ticker in tickers:
    pe_ratio, roe, debt_to_equity = fetch_financial_data(ticker)
    financial_data[ticker] = {
        "PE Ratio": pe_ratio,
        "ROE": roe,
        "Debt to Equity": debt_to_equity
    }

# Visa finansiella data
financial_df = pd.DataFrame(financial_data).T
print(financial_df)

# Skapa en poäng baserad på nyckeltal
def calculate_score(pe, roe, debt_eq):
    if pe and roe and debt_eq:  # Kontrollera att inga värden är None
        return 1 / pe + roe - debt_eq
    return None

# Beräkna poäng och sortera
scores = {ticker: calculate_score(data["PE Ratio"], data["ROE"], data["Debt to Equity"]) 
          for ticker, data in financial_data.items()}

sorted_stocks = sorted(scores.items(), key=lambda item: item[1] if item[1] is not None else -float('inf'), reverse=True)

# Visa resultat
for stock, score in sorted_stocks:
    print(f"{stock}: Score = {score:.2f}" if score is not None else f"{stock}: Data saknas")
