import yfinance as yf
from textblob import TextBlob
import numpy as np
from arch import arch_model

# Funktion för att hämta sentimentpoäng baserat på nyhetsrubriker
def get_sentiment_score(ticker):
    headlines = [
        f"Positive sentiment on {ticker}",
        f"{ticker} earnings show growth",
        f"Concerns over {ticker}'s future",
    ]
    sentiment_score = 0
    for headline in headlines:
        sentiment_score += TextBlob(headline).sentiment.polarity
    return sentiment_score / len(headlines)

# Funktion för att hämta data och beräkna volatilitet med GARCH
def load_data(symbols, start_date="2022-01-01", end_date=None, decay=0.94):
    data = yf.download(symbols, start=start_date, end=end_date)
    adj_close = data['Adj Close']
    daily_returns = adj_close.pct_change().dropna()
    
    annual_returns = daily_returns.mean() * 252
    garch_volatility = {}
    for symbol in symbols:
        model = arch_model(daily_returns[symbol] * 100, vol='Garch', p=1, q=1)
        garch_fitted = model.fit(disp="off")
        garch_volatility[symbol] = garch_fitted.conditional_volatility[-1] / 100
    
    vol_array = np.array([garch_volatility[symbol] for symbol in symbols])
    cov_matrix = np.outer(vol_array, vol_array) * daily_returns.corr().values
    return annual_returns, cov_matrix, data
