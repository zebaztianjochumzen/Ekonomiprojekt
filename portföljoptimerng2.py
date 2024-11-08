import cvxpy as cp
import numpy as np

# Antal tillgångar
num_assets = 4

# Förväntad avkastning (procent per år)
expected_returns = np.array([0.12, 0.18, 0.15, 0.10])

# Kovariansmatrisen (representerar risken mellan tillgångarna)
cov_matrix = np.array([
    [0.005, -0.010, 0.004, -0.002],
    [-0.010, 0.040, -0.002, 0.004],
    [0.004, -0.002, 0.023, 0.002],
    [-0.002, 0.004, 0.002, 0.010]
])

# Skapa variabler för portföljvikterna
weights = cp.Variable(num_assets)

# Begränsningar: summan av vikterna ska vara 1
constraints = [cp.sum(weights) == 1]

# Risknivå (standardavvikelse) och riskbegränsning
risk_level = 0.12
portfolio_variance = cp.quad_form(weights, cov_matrix)
constraints.append(portfolio_variance <= risk_level**2)

# Begränsningar för investeringsandelar: ex. minst 5% och max 50% per tillgång
min_allocation = 0.05
max_allocation = 0.5
constraints += [weights >= min_allocation, weights <= max_allocation]

# Transaktionskostnader - exempel på avgifter i procent per transaktion
transaction_costs = np.array([0.001, 0.0015, 0.002, 0.0012])
initial_weights = np.array([0.25, 0.25, 0.25, 0.25])  # existerande portföljvikter

# Absolut skillnad mellan nya och gamla vikter för att beräkna transaktionskostnader
delta_weights = cp.abs(weights - initial_weights)
transaction_cost = transaction_costs @ delta_weights

# Objektiv: maximera avkastningen minus transaktionskostnader
expected_return = expected_returns @ weights
objective = cp.Maximize(expected_return - transaction_cost)

# Formulera och lös problemet
problem = cp.Problem(objective, constraints)
problem.solve()

# Resultat
print("Optimal portföljfördelning med transaktionskostnader:")
for i, weight in enumerate(weights.value):
    print(f"Tillgång {i+1}: {weight:.2%}")

print(f"\nFörväntad avkastning för portföljen: {expected_return.value:.2%}")
print(f"Transaktionskostnad: {transaction_cost.value:.2%}")
print(f"Portföljens risk (standardavvikelse): {np.sqrt(portfolio_variance.value):.2%}")
