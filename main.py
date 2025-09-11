from matplotlib import pyplot as plt
import numpy as np
import lmfit
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
    
    print(data["Days"])
    
    days=np.array(data["Days"])
    orp_0=np.array(data["0"])  
    print(days)
    print(orp_0)
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
