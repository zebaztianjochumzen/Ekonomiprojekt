from data_fetch import load_data, get_sentiment_score
from prediction_models import predict_returns_with_lstm, predict_returns_with_ensemble
from signal_generation import generate_signals
from portfolio_optimization import optimize_portfolio_with_cvar
from backtesting import backtest_model

# Parametrar
symbols = input("Ange aktiesymboler (t.ex. 'AAPL, MSFT, TSLA'): ").split(',')
total_capital = float(input("Ange totalt investerbart kapital i kronor: "))
risk_free_rate = 0.02  # Riskfri ränta

# Datahämtning och analys
annual_returns, cov_matrix, data = load_data(symbols)
predictions = {symbol: predict_returns_with_ensemble(data, symbol) for symbol in symbols}
sentiment_scores = {symbol: get_sentiment_score(symbol) for symbol in symbols}
macro_factors = {"GDP Growth": 0.02, "Interest Rate": 0.01}  # Dummy-värden

# Generera signaler
fundamentals = pd.DataFrame({
    symbol: {"PE": 14, "Profit Growth": 0.12} for symbol in symbols
}).T
signals = generate_signals(fundamentals, predictions, sentiment_scores, macro_factors)

# Portföljoptimering
buy_symbols = [symbol for symbol, signal in signals.items() if signal == "Buy"]
buy_indices = [symbols.index(sym) for sym in buy_symbols]
filtered_returns = annual_returns[buy_indices]
filtered_cov_matrix = cov_matrix[buy_indices, :][:, buy_indices]

optimal_weights = optimize_portfolio_with_cvar(filtered_returns.values, filtered_cov_matrix, risk_free_rate)

# Backtesting
portfolio_value_series = backtest_model(data[buy_symbols], optimal_weights, total_capital)

print("Backtesting-resultat:", portfolio_value_series[-1])
