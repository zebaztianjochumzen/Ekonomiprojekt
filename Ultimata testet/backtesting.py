def backtest_model(data, weights, initial_capital=1000000):
    portfolio_value = initial_capital
    daily_returns = data.pct_change().dropna()
    
    portfolio_returns = daily_returns @ weights
    portfolio_value_series = [portfolio_value]
    
    for ret in portfolio_returns:
        portfolio_value *= (1 + ret)
        portfolio_value_series.append(portfolio_value)
    
    return portfolio_value_series
