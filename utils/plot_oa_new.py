import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 14})

# Data from the table
datasets = ['CDL', 'NCCM', 'EuroCrops', 'SAS', 'SACT']
ood_plus_id = {
    'CDL': [74.51, 77.34, 79.22, 84.76],
    'NCCM': [69.35, 73.45, 82.26, 89.17],
    'EuroCrops': [61.48, 68.20, 74.77, 80.46],
    'SAS': [59.32, 68.19, 80.11, 85.49],
    'SACT': [71.47, 64.86, 76.12, 79.88],
}

id_only = {
    'CDL': [58.89, 77.69, 85.20],
    'NCCM': [54.91, 84.87, 80.77],
    'EuroCrops': [66.49, 74.41, 90.13],
    'SAS': [69.92, 80.10, 87.12],
    'SACT': [58.85, 73.48, 80.71],
}

dataset_colors = {
    "CDL": [255/255, 20/255, 147/255],  # Convert to normalized RGB
    "EuroCrops": [255/255, 165/255, 0/255],
    "NCCM": [240/255, 230/255, 140/255],
    "SACT": [255/255, 0/255, 255/255],
    "SAS": [0/255, 255/255, 127/255],
}

# x-axis values for OOD + ID and ID only
x_values_ood_plus_id = [0, 10, 100, 900]
x_values_id_only = [10, 100, 900]

# Set up color map
# colors = plt.cm.get_cmap('tab10', len(datasets))

# Plotting the data
plt.figure(figsize=(12, 8))

for dataset in datasets:
    plt.plot(
        x_values_ood_plus_id,
        ood_plus_id[dataset],
        linestyle='-',
        marker='o',
        color=dataset_colors[dataset],
        linewidth=2.5,
        markersize=10,
        label=f'{dataset} (OOD + ID)'
    )
    plt.plot(
        x_values_id_only,
        id_only[dataset],
        linestyle='--',
        marker='*',
        color=dataset_colors[dataset],
        linewidth=2.5,
        markersize=10,
        label=f'{dataset} (ID Only)'
    )

# Set the x-axis to show specific ticks
# plt.xticks(range(0, 1000, 100))
plt.xscale('log')
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.xticks([1, 10, 100, 1000], ['1', '10', '100', '900'])


# Adding labels and title
plt.xlabel('Number of ID Samples')
plt.ylabel('Overall Accuracy (%)')
plt.grid(True)

# Adjust layout to make space for the legend
plt.tight_layout(rect=[0, 0.15, 1, 1])

# Move legend to the bottom of the plot
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=5, fontsize=12)

# Save the plot
plt.savefig('oa_curve.png', dpi=300)

# Show the plot
plt.show()
