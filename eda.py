def run_eda(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
#Correlation heatmap
    sns.heatmap(df.corr(), cmap='coolwarm')
  #Affordability Analysis
    sns.scatterplot(
    x='avg_monthly_income_usd',
    y='gasoline_usd_per_liter',
    hue='sub_region',
    data=df
)

#subsidy impact
    sns.boxplot(x='fuel_subsidy_active', y='gasoline_usd_per_liter', data=df)
  #EV ADOPTION vs Fuel price
    sns.scatterplot(
    x='gasoline_usd_per_liter',
    y='ev_adoption_pct',
    data=df
)
  #top risk countries
    df.sort_values('energy_risk', ascending=False).head(10)
  #Binning
    df['affordability_level'] = pd.cut(
    df['fuel_affordability_index'],
    bins=3,
    labels=['Low', 'Medium', 'High']
)
  #Encoding
    df = pd.get_dummies(df, columns=['sub_region'], drop_first=True)

 
