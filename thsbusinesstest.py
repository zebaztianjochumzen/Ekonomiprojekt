# Exempel på faktorer och vikter
factors = [
    "financial_stability", "technical_expertise", "sustainability",
    "market_presence", "previous_collaborations", "customer_satisfaction",
    "innovation_capability", "response_time", "cultural_fit",
    "cost_efficiency", "quality_standards", "scalability",
    "ethical_practices", "legal_compliance", "data_security",
    "geographical_coverage", "brand_reputation", "supply_chain_reliability",
    "risk_management", "R&D_investment"
]

# Vikter för varje faktor (exempelvärden)
weights = {
    "financial_stability": 0.15, "technical_expertise": 0.1, "sustainability": 0.1,
    "market_presence": 0.05, "previous_collaborations": 0.05, "customer_satisfaction": 0.1,
    "innovation_capability": 0.05, "response_time": 0.05, "cultural_fit": 0.05,
    "cost_efficiency": 0.1, "quality_standards": 0.05, "scalability": 0.05,
    "ethical_practices": 0.05, "legal_compliance": 0.05, "data_security": 0.05,
    "geographical_coverage": 0.05, "brand_reputation": 0.05, "supply_chain_reliability": 0.05,
    "risk_management": 0.05, "R&D_investment": 0.05
}

# Exempeldata för varje partner, normaliserad till värden mellan 0 och 1
partners = {
    "Partner_A": {
        "financial_stability": 0.9, "technical_expertise": 0.8, "sustainability": 0.7,
        "market_presence": 0.6, "previous_collaborations": 0.8, "customer_satisfaction": 0.9,
        "innovation_capability": 0.7, "response_time": 0.8, "cultural_fit": 0.6,
        "cost_efficiency": 0.7, "quality_standards": 0.9, "scalability": 0.8,
        "ethical_practices": 0.6, "legal_compliance": 0.9, "data_security": 0.8,
        "geographical_coverage": 0.7, "brand_reputation": 0.9, "supply_chain_reliability": 0.8,
        "risk_management": 0.7, "R&D_investment": 0.8
    },
    "Partner_B": {
        "financial_stability": 0.8, "technical_expertise": 0.9, "sustainability": 0.6,
        "market_presence": 0.7, "previous_collaborations": 0.6, "customer_satisfaction": 0.8,
        "innovation_capability": 0.8, "response_time": 0.7, "cultural_fit": 0.8,
        "cost_efficiency": 0.8, "quality_standards": 0.8, "scalability": 0.9,
        "ethical_practices": 0.7, "legal_compliance": 0.8, "data_security": 0.9,
        "geographical_coverage": 0.6, "brand_reputation": 0.8, "supply_chain_reliability": 0.7,
        "risk_management": 0.8, "R&D_investment": 0.7
    }
}

# Beräkna totalpoäng för varje partner
def calculate_total_score(partner_data, weights):
    score = sum(partner_data[factor] * weights[factor] for factor in factors)
    return score

# Rangordna partner baserat på totalpoäng
scores = {partner: calculate_total_score(data, weights) for partner, data in partners.items()}
sorted_partners = sorted(scores.items(), key=lambda item: item[1], reverse=True)

# Resultat
for partner, score in sorted_partners:
    print(f"{partner}: Total Score = {score:.2f}")

