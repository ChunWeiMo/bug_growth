from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import json
import sys
import pandas as pd
from sklearn.model_selection import GridSearchCV


def load_fit_params(file_path):
    if file_path is None:
        print("No parameters file provided.")
        sys.exit(1)
    with open("data/fit_params.json", "r") as f:
        fit_params = json.load(f)
    df = pd.DataFrame(fit_params)
    X = np.array([float(key) for key in fit_params.keys()]).reshape(-1, 1)
    Y = np.array(list(fit_params.values()))
    return X, Y


def main():
    params_path = "data/fit_params.json"
    X, Y = load_fit_params(params_path)

    model = RandomForestRegressor(n_estimators=500, random_state=42)
    model.fit(X, Y)

    print("\nFeature Importances:\n", model.feature_importances_)

    r2_score = model.score(X, Y)
    print("R² Score:", r2_score)

    X_new = np.array([[3.], [4.]])
    Y_pred = model.predict(X_new)
    print("\nPredictions for X_new:\n", Y_pred)


if __name__ == "__main__":
    main()
