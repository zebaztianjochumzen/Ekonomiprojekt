import cvxpy as cp
import numpy as np

# Antal tillgångar
num_assets = 4

# Förväntad avkastning (antag procent per år)
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

# Begränsningar: vikterna måste summera till 1 och vara positiva
constraints = [
    cp.sum(weights) == 1,
    weights >= 0
]

# Portföljens risknivå (standardavvikelse, här som exempel 10%)
risk_level = 0.1

# Riskbegränsning: kvadratisk risk (viktad kovarians)
portfolio_variance = cp.quad_form(weights, cov_matrix)
constraints.append(portfolio_variance <= risk_level**2)

# Objektivfunktion: maximera den förväntade avkastningen
objective = cp.Maximize(expected_returns @ weights)

# Formulera och lös problemet
problem = cp.Problem(objective, constraints)
problem.solve()

# Resultat
print("Optimal portföljfördelning:")
for i, weight in enumerate(weights.value):
    print(f"Tillgång {i+1}: {weight:.2%}")

print(f"\nFörväntad avkastning för portföljen: {expected_returns @ weights.value:.2%}")
print(f"Portföljens risk (standardavvikelse): {np.sqrt(portfolio_variance.value):.2%}")
