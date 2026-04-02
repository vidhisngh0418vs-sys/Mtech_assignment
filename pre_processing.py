

def preprocess():
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    df = pd.read_csv("asia_fuel_prices_detailed.csv")
    df['price_date'] = pd.to_datetime(df['price_date'])
    df['fuel_subsidy_active'] = df['fuel_subsidy_active'].astype(int)  

    df.fillna({
    'subsidy_cost_bn_usd': 0,
    'ev_adoption_pct': df['ev_adoption_pct'].median(),
    'avg_monthly_income_usd': df['avg_monthly_income_usd'].median()
}, inplace=True)
    # Fuel burden
    df['fuel_burden'] = df['gasoline_usd_per_liter'] / df['avg_monthly_income_usd']

# Energy risk index
    df['energy_risk'] = (
    df['oil_import_dependency_pct'] * 0.6 +
    df['gasoline_usd_per_liter'] * 0.4
)

# Green score
    df['green_score'] = df['ev_adoption_pct'] - df['co2_transport_mt']

    num_cols = df.select_dtypes(include='number').columns
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
