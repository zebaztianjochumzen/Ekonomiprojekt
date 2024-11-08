import cvxpy as cp
from scipy.stats import norm

def optimize_portfolio_with_cvar(returns, cov_matrix, risk_free_rate, alpha=0.05):
    num_assets = len(returns)
    weights = cp.Variable(num_assets)
    
    portfolio_return = returns @ weights
    portfolio_risk = cp.quad_form(weights, cov_matrix)
    VaR = -norm.ppf(1 - alpha) * cp.sqrt(portfolio_risk)
    CVaR = VaR + (norm.pdf(norm.ppf(1 - alpha)) / (1 - alpha)) * cp.sqrt(portfolio_risk)
    
    objective = cp.Maximize((portfolio_return - risk_free_rate) / CVaR)
    constraints = [cp.sum(weights) == 1, weights >= 0]
    problem = cp.Problem(objective, constraints)
    problem.solve()
    
    return weights.value
