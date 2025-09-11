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
    
    for cloride_concentration, orp in orps.items():
        # Scatter plot of the actual data
        print(cloride_concentration, orp)
        plt.scatter(days, orp, label=f"Cl {cloride_concentration} (data)", alpha=0.6)
        
    #     # Example sigmoid parameters (can be improved or fitted)
        c_0 = min(orp)
        c_1 = max(orp) - c_0
        k = 0.3  # growth rate
        t0 = np.median(days)  # midpoint of sigmoid
        
        # Generate sigmoid values
        x_vals = np.linspace(min(days), max(days), 200)
        y_vals = sigmoid(x_vals, c_0, c_1, k, t0)
        
        # Plot sigmoid curve
        plt.plot(x_vals, y_vals, linestyle='--', label=f"ORP {cloride_concentration} (sigmoid fit)")

    plt.xlabel("Days")
    plt.ylabel("Orp")
    plt.title("Bacterial Growth Over Time at Different ORP Levels")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # x = []
    # y = []
    # for row in data:
    #     x.append(row[0])
    #     y.append(row[1])
    # print(x)
    # print(y)
    # plt.scatter(x, y)
    # # plt.show()

    # # a=np.linspace(150,200,5)
    # a=180
    # # b = np.linspace(1,5,5)
    # b = 3
    # # c = 0.5
    # c = 0.2
    # sigmoid=[]

    # for i in x:
    #     y= a / (1 + np.exp(b-c*i))+410
    #     sigmoid.append(y)
    # print(sigmoid)
    # plt.plot(x, sigmoid)
    # # plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()
