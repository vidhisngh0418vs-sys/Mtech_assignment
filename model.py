# model.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def train_model():

    # Load data
    df = pd.read_csv("fuel_prices.csv")

    # Preprocessing
    df['price_date'] = pd.to_datetime(df['price_date'])

    df.fillna({
        'subsidy_cost_bn_usd': 0,
        'ev_adoption_pct': df['ev_adoption_pct'].median(),
        'avg_monthly_income_usd': df['avg_monthly_income_usd'].median()
    }, inplace=True)

    # Drop non-useful columns
    X = df.drop([
        'fuel_affordability_index',
        'country',
        'iso3',
        'price_date'
    ], axis=1)

    y = df['fuel_affordability_index']

    # Encode categorical
    X = pd.get_dummies(X, drop_first=True)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)
    print("Model MAE:", mae)

    # Save model
    joblib.dump(model, "fuel_model.pkl")

    print("Model saved as fuel_model.pkl")


if __name__ == "__main__":
    train_model()
