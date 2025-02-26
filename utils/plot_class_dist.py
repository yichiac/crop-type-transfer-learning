import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create the data
data = {
    'Dataset': ['CDL', 'NCCM', 'EuroCrops', 'SAS', 'SACT'],
    'Maize': [8992494, 9417948, 1759553, 0, 0],
    'Soybean': [7958444, 3955517, 192698, 22348399, 0],
    'Rice': [0, 2890754, 3970909, 0, 0],
    'Wheat': [4204954, 0, 7721286, 0, 6049292],
    'Others': [44143414, 48861366, 27418993, 43187601, 19065379]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set up the plot style
plt.figure(figsize=(12, 8))
width = 0.15
x = np.arange(len(df['Dataset']))

# Create bars for each crop type with colors matching the image
plt.bar(x - width*2, df['Maize'], width, label='Maize', color='#FFD700')  # Yellow
plt.bar(x - width, df['Soybean'], width, label='Soybean', color='#006400')  # Dark green
plt.bar(x, df['Rice'], width, label='Rice', color='#1E90FF')  # Light blue
plt.bar(x + width, df['Wheat'], width, label='Wheat', color='#8B4513')  # Brown
plt.bar(x + width*2, df['Others'], width, label='Others', color='#808080')  # Gray

# Customize the plot
plt.yscale('log')
plt.xlabel('Datasets')
plt.ylabel('Number of Pixels')
plt.title('Class Distribution Across Datasets')
plt.xticks(x, df['Dataset'])

# Adjust legend
plt.legend(bbox_to_anchor=(0.5, 1.15), loc='upper center', ncol=5)

# Set y-axis limits and format
plt.ylim(1e4, 1e8)
plt.grid(True, which="both", ls="-", alpha=0.2)

# Format y-axis labels with scientific notation
plt.gca().yaxis.set_major_formatter(plt.ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.tight_layout()
plt.savefig('class_distribution.png')

plt.show()