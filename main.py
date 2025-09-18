from matplotlib import pyplot as plt
import matplotlib
import numpy as np
# import lmfit
import pandas as pd
from scipy.optimize import curve_fit


def sigmoid(t, c_0, c_1, k, t0):
    return c_0 + c_1 / (1 + np.exp(-k * (t - t0)))


def load_csv_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading CSV data: {e}")
        return None


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

    # put for loop here to traverse the data
    # Plot each ORP condition with its sigmoid estimate
    plt.figure(figsize=(10, 6))

    plt.scatter(days, orps[0], label=f"Cl (data)", alpha=0.6)

    # Example sigmoid parameters (can be improved or fitted)
    c_0 = min(orps[0])
    c_1 = max(orps[0]) - c_0

    k_s = np.linspace(0.1, 0.3, 5)
    t0_init = np.median(days)  # midpoint of sigmoid
    delta_t0_s = np.linspace(-10, -1, 5)
    t0_s = t0_init + delta_t0_s
    x_vals = np.linspace(min(days), max(days), 200)
    k = 0.2
    t0 = 10.5
    params, _ = curve_fit(sigmoid, days, orps[0], p0=[c_0, c_1, k, t0])
    c_0_fitted, c_1_fitted, k_fitted, t0_fitted = params
    y_fitted = sigmoid(x_vals, c_0_fitted, c_1_fitted, k_fitted, t0_fitted)
    plt.plot(x_vals, y_fitted, label=f"Cl (fit)", color="blue")
    plt.xlabel("Days")
    plt.ylabel("Orp")
    plt.title("Bacterial Growth Over Time at Different ORP Levels")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
