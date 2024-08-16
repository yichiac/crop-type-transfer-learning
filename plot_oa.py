import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 14})

# Data from the table
datasets = ['CDL', 'NCCM', 'EuroCrops', 'AgriFieldNet', 'SAS', 'SACT']
ood_plus_id = {
    'CDL': [71.31, 77.74, 79.20, 85.59],
    'NCCM': [68.14, 75.12, 84.79, 90.06],
    'EuroCrops': [61.52, 67.72, 73.56, 80.58],
    'AgriFieldNet': [49.87, 46.53, 41.95, 29.36],
    'SAS': [59.33, 66.92, 78.86, 86.25],
    'SACT': [65.38, 68.09, 74.35, 79.31],
}
id_only = {
    'CDL': [69.78, 77.53, 85.05],
    'NCCM': [72.63, 85.89, 90.12],
    'EuroCrops': [68.19, 75.17, 82.05],
    'AgriFieldNet': [29.04, 40.46, 51.90],
    'SAS': [66.50, 78.34, 85.01],
    'SACT': [68.83, 73.47, 80.37],
}

# x-axis values for OOD + ID and ID only
x_values_ood_plus_id = [0, 10, 100, 900]
x_values_id_only = [10, 100, 900]

# Set up color map
colors = plt.cm.get_cmap('tab10', len(datasets))

# Plotting the data
plt.figure(figsize=(12, 8))

for i, dataset in enumerate(datasets):
    plt.plot(x_values_ood_plus_id, ood_plus_id[dataset], linestyle='-', marker='o', color=colors(i), linewidth=2.5, label=f'{dataset} (OOD + ID)')
    plt.plot(x_values_id_only, id_only[dataset], linestyle='--', marker='*', color=colors(i), linewidth=2.5, label=f'{dataset} (ID Only)')

# Set the x-axis to show specific ticks
plt.xticks(range(0, 1000, 100))

# Adding labels and title
plt.xlabel('Number of ID Samples')
plt.ylabel('Overall Accuracy (%)')
plt.grid(True)

# Adjust layout to make space for the legend
plt.tight_layout(rect=[0, 0.15, 1, 1])

# Move legend to the bottom of the plot
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=3, fontsize=12)


# Show the plot
plt.show()
