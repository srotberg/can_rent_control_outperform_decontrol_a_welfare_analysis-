# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt



# Data for Panel a
age_a = list(range(26, 86))
data_percentage_a = [
    26.49, 31.40, 34.79, 38.85, 42.90, 45.81, 48.41, 53.05, 55.01, 56.48,
    58.71, 61.14, 62.92, 63.66, 65.44, 67.51, 67.35, 68.90, 69.00, 69.82,
    70.15, 71.07, 71.12, 72.45, 72.42, 72.89, 73.22, 74.18, 74.25, 73.95,
    74.69, 74.39, 74.46, 75.19, 74.85, 75.81, 75.29, 76.02, 75.84, 75.21,
    76.34, 75.71, 77.02, 74.70, 75.24, 75.90, 74.46, 76.00, 74.74, 75.22,
    75.83, 76.18, 74.96, 75.06, 75.02, 75.18, 76.08, 73.32, 74.23, 74.85
]
model_percentage_a = [
    0.00, 0.00, 2.37, 4.91, 32.58, 62.15, 66.90, 62.63, 56.32, 56.07,
    62.03, 64.60, 67.33, 68.05, 68.95, 69.01, 70.22, 71.46, 71.83, 69.95,
    73.41, 74.62, 79.41, 81.64, 82.83, 83.31, 83.29, 82.72, 82.37, 82.07,
    82.07, 81.80, 81.45, 81.04, 67.84, 68.06, 68.44, 69.08, 69.99, 70.97,
    62.91, 62.94, 62.96, 62.92, 62.87, 62.82, 62.79, 62.80, 62.73, 62.59,
    62.46, 62.36, 62.25, 62.14, 58.70, 57.20, 55.98, 55.06, 54.17, 32.48
]

# Data for Panel b
age_b = ['26-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']
data_percentage_b = [49.00, 49.70, 48.51, 37.20, 34.44, 23.84, 17.96, 14.39, 8.45, 6.33, 4.96, 0.43]
model_percentage_b = [77.33, 72.83, 65.58, 57.03, 45.75, 32.54, 17.14, 6.37, 0.63, 0.00, 0.00, 0.00]
# Plotting
plt.figure(figsize=(14, 6))

# Panel a
plt.subplot(1, 2, 1)
plt.plot(age_a, data_percentage_a, label='Data')
plt.plot(age_a, model_percentage_a, label='Model')
plt.title('Panel a: Homeownership by age',  fontsize=18)
plt.xlabel('Age', fontsize=16)
plt.ylabel('Percentage', fontsize=16)
plt.xticks(rotation=45)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend()
plt.grid(False)

# Panel b
plt.subplot(1, 2, 2)
plt.plot(age_b, data_percentage_b, label='Data')
plt.plot(age_b, model_percentage_b, label='Model')
plt.title('Panel b: LTV by age group', fontsize=18)
plt.xlabel('Age Group',fontsize=16)
plt.ylabel('Percentage',fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
plt.legend()
plt.grid(False)

# Adjust layout
plt.tight_layout()

# Save as PDF
plt.savefig('LTV_Homeowner.pdf')
# Show plot
plt.show()