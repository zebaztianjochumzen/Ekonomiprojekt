import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.optimizers import Adam

# LSTM-modell för tidsserieprognos
def predict_returns_with_lstm(data, symbol):
    returns = data['Adj Close'][symbol].pct_change().dropna()
    X, y = [], []
    for i in range(60, len(returns)):
        X.append(returns[i-60:i].values)
        y.append(returns[i])
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
    model.fit(X, y, epochs=10, batch_size=16, verbose=0)
    
    return model.predict(X[-1].reshape(1, X.shape[1], 1))[0][0]

# Ensemblemodell med Gradient Boosting
def predict_returns_with_ensemble(data, symbol):
    returns = data['Adj Close'][symbol].pct_change().dropna()
    X, y = np.arange(len(returns)).reshape(-1, 1), returns.values
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
    model.fit(X, y)
    return model.predict([[len(returns)]])[0]
