from matplotlib import pyplot as plt
import matplotlib
import numpy as np
# import lmfit
import pandas as pd


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

    #put for loop here to traverse the data
       # Plot each ORP condition with its sigmoid estimate
    plt.figure(figsize=(10, 6))
    
    plt.scatter(days, orps[0], label=f"Cl {"cl = 0"} (data)", alpha=0.6)
    
    # Example sigmoid parameters (can be improved or fitted)
    c_0 = min(orps[0])
    c_1 = max(orps[0]) - c_0
    
    k_s = np.linspace(0.1, 0.3, 5)
    t0_init = np.median(days)  # midpoint of sigmoid
    print(t0_init)
    delta_t0_s= np.linspace(-10, -1, 5)
    t0_s = t0_init + delta_t0_s
    # t0 = t0_init - 4
    # Generate sigmoid values
    x_vals = np.linspace(min(days), max(days), 200)
    # k = 0.2
    t0= 10.5
    for k in k_s:
        y_vals = sigmoid(x_vals, c_0, c_1, k, t0)
    
    
    # for t0 in t0_s:
    #     y_vals = sigmoid(x_vals, c_0, c_1, k, t0)
    
    # Plot sigmoid curve
        plt.plot(x_vals, y_vals, linestyle=':', label=f"k: {k}")
        # plt.plot(x_vals, y_vals, linestyle=':', label=f"t0: {t0}")

    plt.xlabel("Days")
    plt.ylabel("Orp")
    plt.title("Bacterial Growth Over Time at Different ORP Levels")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
