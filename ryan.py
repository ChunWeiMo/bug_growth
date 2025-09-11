import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the function you want to fit the data to

def my_function(x, K, A, r, L, I):
    return K / (1 + A * np.exp(-r * (x-L))) + I

# Load the data from an Excel file
data = pd.read_excel(&#39;D:\ORP bacteria Growth.xlsx&#39;)

# Extract the x and y values from the data
x = data[&#39;Time&#39;]
y = data[&#39;ORP&#39;]

# Perform the curve fitting
# K = 450 # ORP increase
# A = 100 # Initial population size
# r = 1 # Growth rate
# L = 3 # Dormant phase
# I = 300 # inital ORP

init=[100,100,1,3,300]
params, _ = curve_fit(my_function, x, y,p0=init)

# Extract the fitted parameters
K_fit, A_fit, r_fit, L_fit, I_fit = params

# Generate x values for the fitted curve

x_fit = np.linspace(x.min(), x.max(), 100)

# Compute y values using the fitted parameters and x_fit
y_fit = my_function(x_fit, K_fit, A_fit, r_fit, L_fit, I_fit)

print(f&quot;Fitted parameters: K = {K_fit}, A = {A_fit}, r = {r_fit}, L = {L_fit}, I = {I_fit}&quot;)

# Plot the data and the fitted curve
plt.scatter(x, y, label=&#39;Data&#39;)
plt.plot(x_fit, y_fit, &#39;r-&#39;, label=&#39;Fitted Curve&#39;)
plt.xlabel(&#39;x&#39;)
plt.ylabel(&#39;y&#39;)
plt.title(&#39;Data Fitted to Function&#39;)
plt.legend()
plt.show()