# Tokyo Real Estate Price Prediction

This project aims to predict real estate transaction prices in Tokyo using machine learning models.  
It leverages structured property data (from SQLite databases) and advanced regression algorithms to estimate the TradePrice of housing units.

## Project Overview

The dataset includes information about:
- Property type and location  
- Area and building details  
- Accessibility to the nearest station  
- Year and quarter of the transaction  

The goal is to build and evaluate predictive models that accurately estimate the transaction price of properties.

## Models Tested

Four regression models were evaluated for performance:

| Model | MAE | RMSE | R² |
|--------|--------|--------|--------|
| Linear Regression | 7,331,454.88 | 9,678,524.30 | 0.6586 |
| Random Forest Regressor | 4,770,641.37 | 6,769,079.75 | 0.8330 |
| XGBoost Regressor | 4,719,700.00 | 6,653,864.38 | 0.8387 |
| LightGBM Regressor | 4,745,790.93 | 6,671,558.91 | 0.8378 |


## Best Model: XGBoost

The XGBoost model achieved the best overall results after hyperparameter tuning.

**Best Parameters:**
```python
{
  'colsample_bytree': 0.8,
  'learning_rate': 0.1,
  'max_depth': 8,
  'n_estimators': 200,
  'subsample': 1.0
}
```

**Performance Metrics:**

| Metric | Value |
|---------|--------|
| MAE | 4,584,758.50 |
| RMSE | 6,518,892.09 |
| R² | 0.8451 |
| RMSLE | 0.2614 |
| MAPE | 20.29% |
## License

This project is released under the MIT License.
