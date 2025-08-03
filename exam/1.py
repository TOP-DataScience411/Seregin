import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sklearn.metrics import mean_squared_error

data = np.load('data1.npz')
x = data['x']
y = data['y']

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue')
plt.title('Scatter')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('scatter_plot.png')
plt.close()

ransac = RANSACRegressor(min_samples=0.5, 
                          residual_threshold=0.4, 
                          random_state=42)
ransac.fit(x.reshape(-1, 1), y)

inlier_mask = ransac.inlier_mask_
outlier_mask = ~inlier_mask

plt.figure(figsize=(10, 6))
plt.scatter(x[inlier_mask], y[inlier_mask], color='green', label='Inlier', s=30)
plt.scatter(x[outlier_mask], y[outlier_mask], color='red', label='outlier', s=30)

line_x = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
line_y = ransac.predict(line_x)
plt.plot(line_x, line_y, color='orange', linewidth=2, label=' RANSAC')

plt.title('RANSAC')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.savefig('ransac_results.png')
plt.close()


