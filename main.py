from matplotlib import pyplot as plt
import matplotlib
import numpy as np
# import lmfit
import pandas as pd
from scipy.optimize import curve_fit
import sys
import json


def exit_handler(message="Exiting program due to an error"):
    print(message)
    sys.exit(1)


def sigmoid(t, c_0, c_1, k, t0):
    return c_0 + c_1 / (1 + np.exp(-k * (t - t0)))


def load_csv_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading CSV data: {e}")
        exit_handler()


def fit_sigmoid(days, orps):
    output_to_json = {}
    for cl, orp in orps.items():
        c_0 = min(orp)
        c_1 = max(orp) - c_0
        k = 0.2
        t0 = 10.5
        initial_params = [c_0, c_1, k, t0]

        x_grid = np.linspace(min(days), max(days), 200)
        plt.scatter(days, orp, label=f"Cl {cl}", alpha=0.6)
        try:
            params, covariance = curve_fit(sigmoid, days, orp, p0=initial_params)
        except Exception as e:
            print(f"Error in curve fitting: {e}")
            exit_handler("Curve fitting failed")
        else:
            print(params)
            c_0_fitted, c_1_fitted, k_fitted, t0_fitted = params
            y_fitted = sigmoid(x_grid, c_0_fitted, c_1_fitted, k_fitted, t0_fitted)
            plt.plot(x_grid, y_fitted, label=f"Cl {cl}")
            output_to_json[cl] = params.tolist()
            
    with open("data/fit_params.json", "w") as f:
        json.dump(output_to_json, f)

def main():
    experiment_data_path = "data/bug_growth.csv"
    data = load_csv_data(experiment_data_path)
    if data is None:
        return

    days = np.array(data["Days"])

    orps = {
        0: np.array(data["0"]),
        1: np.array(data["1"]),
        2: np.array(data["2"]),
        5: np.array(data["5"]),
        10: np.array(data["10"]),
        20: np.array(data["20"])
    }

    plt.figure(figsize=(10, 6))

    fit_sigmoid(days, orps)

    plt.xlabel("Days")
    plt.ylabel("Orp")
    plt.title("Bacterial Growth Over Time at Different ORP Levels")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
