# Funktion för att generera köp/säljsignaler baserat på analys
def generate_signals(fundamentals, predictions, sentiment_scores, macro_factors):
    signals = {}
    for symbol in fundamentals.index:
        buy_signal = (
            fundamentals.loc[symbol, "PE"] < 15 and
            fundamentals.loc[symbol, "Profit Growth"] > 0.1 and
            predictions[symbol] > 0 and
            sentiment_scores[symbol] > 0 and
            macro_factors["GDP Growth"] > 0.015 and
            macro_factors["Interest Rate"] < 0.02
        )
        signals[symbol] = "Buy" if buy_signal else "Hold"
    return signals
