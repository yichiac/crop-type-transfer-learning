import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'font.size': 14})

# Data from the table
datasets = ['CDL', 'NCCM', 'EuroCrops', 'AgriFieldNet', 'SAS', 'SACT']
metrics = ['f1', 'precision', 'recall', 'accuracy', 'jaccard_index']
types = ['average', 'overall']
metrics_name = ['F1 Score', 'Precision', 'Recall', 'Accuracy', 'Jaccard Index']
types_name = ['Average', 'Overall']
all_metrics = []
all_metrics_name = []
for t in types:
    for m in metrics:
        all_metrics.append(f'{t}_{m}')

for m in metrics_name:
    for t in types_name:
        all_metrics_name.append(f'{t} {m}')

distributions = ['ood_plus_id', 'id_only']


ood_df = pd.read_excel('OOD.xlsx', header=None)

def extract_metrics(df):
    average_f1 = df.loc[df[0] == 'average_f1'].values[0][1:]
    average_precision = df.loc[df[0] == 'average_precision'].values[0][1:]
    average_recall = df.loc[df[0] == 'average_recall'].values[0][1:]
    average_accuracy = df.loc[df[0] == 'average_accuracy'].values[0][1:]
    average_jaccard_index = df.loc[df[0] == 'average_jaccard_index'].values[0][1:]
    overall_f1 = df.loc[df[0] == 'overall_f1'].values[0][1:]
    overall_precision = df.loc[df[0] == 'overall_precision'].values[0][1:]
    overall_recall = df.loc[df[0] == 'overall_recall'].values[0][1:]
    overall_accuracy = df.loc[df[0] == 'overall_accuracy'].values[0][1:]
    overall_jaccard_index = df.loc[df[0] == 'overall_jaccard_index'].values[0][1:]

    average_f1 = average_f1.tolist()
    average_precision = average_precision.tolist()
    average_recall = average_recall.tolist()
    average_accuracy = average_accuracy.tolist()
    average_jaccard_index = average_jaccard_index.tolist()
    overall_f1 = overall_f1.tolist()
    overall_precision = overall_precision.tolist()
    overall_recall = overall_recall.tolist()
    overall_accuracy = overall_accuracy.tolist()
    overall_jaccard_index = overall_jaccard_index.tolist()
    return average_f1, average_precision, average_recall, average_accuracy, average_jaccard_index, overall_f1, overall_precision, overall_recall, overall_accuracy, overall_jaccard_index

average_f1, average_precision, average_recall, average_accuracy, average_jaccard_index, overall_f1, overall_precision, overall_recall, overall_accuracy, overall_jaccard_index = extract_metrics(ood_df)

average_f1_ood_plus_id = {
    'CDL': average_f1[0:4],
    'NCCM': average_f1[4:8],
    'EuroCrops': average_f1[8:12],
    'AgriFieldNet': average_f1[12:16],
    'SAS': average_f1[16:20],
    'SACT': average_f1[20:24],
}
average_precision_ood_plus_id = {
    'CDL': average_precision[0:4],
    'NCCM': average_precision[4:8],
    'EuroCrops': average_precision[8:12],
    'AgriFieldNet': average_precision[12:16],
    'SAS': average_precision[16:20],
    'SACT': average_precision[20:24],
}
average_recall_ood_plus_id = {
    'CDL': average_recall[0:4],
    'NCCM': average_recall[4:8],
    'EuroCrops': average_recall[8:12],
    'AgriFieldNet': average_recall[12:16],
    'SAS': average_recall[16:20],
    'SACT': average_recall[20:24],
}
average_accuracy_ood_plus_id = {
    'CDL': average_accuracy[0:4],
    'NCCM': average_accuracy[4:8],
    'EuroCrops': average_accuracy[8:12],
    'AgriFieldNet': average_accuracy[12:16],
    'SAS': average_accuracy[16:20],
    'SACT': average_accuracy[20:24],
}
average_jaccard_index_ood_plus_id = {
    'CDL': average_jaccard_index[0:4],
    'NCCM': average_jaccard_index[4:8],
    'EuroCrops': average_jaccard_index[8:12],
    'AgriFieldNet': average_jaccard_index[12:16],
    'SAS': average_jaccard_index[16:20],
    'SACT': average_jaccard_index[20:24],
}
overall_f1_ood_plus_id = {
    'CDL': overall_f1[0:4],
    'NCCM': overall_f1[4:8],
    'EuroCrops': overall_f1[8:12],
    'AgriFieldNet': overall_f1[12:16],
    'SAS': overall_f1[16:20],
    'SACT': overall_f1[20:24],
}
overall_precision_ood_plus_id = {
    'CDL': overall_precision[0:4],
    'NCCM': overall_precision[4:8],
    'EuroCrops': overall_precision[8:12],
    'AgriFieldNet': overall_precision[12:16],
    'SAS': overall_precision[16:20],
    'SACT': overall_precision[20:24],
}
overall_recall_ood_plus_id = {
    'CDL': overall_recall[0:4],
    'NCCM': overall_recall[4:8],
    'EuroCrops': overall_recall[8:12],
    'AgriFieldNet': overall_recall[12:16],
    'SAS': overall_recall[16:20],
    'SACT': overall_recall[20:24],
}
overall_accuracy_ood_plus_id = {
    'CDL': overall_accuracy[0:4],
    'NCCM': overall_accuracy[4:8],
    'EuroCrops': overall_accuracy[8:12],
    'AgriFieldNet': overall_accuracy[12:16],
    'SAS': overall_accuracy[16:20],
    'SACT': overall_accuracy[20:24],
}
overall_jaccard_index_ood_plus_id = {
    'CDL': overall_jaccard_index[0:4],
    'NCCM': overall_jaccard_index[4:8],
    'EuroCrops': overall_jaccard_index[8:12],
    'AgriFieldNet': overall_jaccard_index[12:16],
    'SAS': overall_jaccard_index[16:20],
    'SACT': overall_jaccard_index[20:24],
}


id_df = pd.read_excel('ID.xlsx', header=None)
average_f1, average_precision, average_recall, average_accuracy, average_jaccard_index, overall_f1, overall_precision, overall_recall, overall_accuracy, overall_jaccard_index = extract_metrics(id_df)

average_f1_id = {
    'CDL': average_f1[0:3],
    'NCCM': average_f1[3:6],
    'EuroCrops': average_f1[6:9],
    'AgriFieldNet': average_f1[9:12],
    'SAS': average_f1[12:15],
    'SACT': average_f1[15:18],
}
average_precision_id = {
    'CDL': average_precision[0:3],
    'NCCM': average_precision[3:6],
    'EuroCrops': average_precision[6:9],
    'AgriFieldNet': average_precision[9:12],
    'SAS': average_precision[12:15],
    'SACT': average_precision[15:18],
}
average_recall_id = {
    'CDL': average_recall[0:3],
    'NCCM': average_recall[3:6],
    'EuroCrops': average_recall[6:9],
    'AgriFieldNet': average_recall[9:12],
    'SAS': average_recall[12:15],
    'SACT': average_recall[15:18],
}
average_accuracy_id = {
    'CDL': average_accuracy[0:3],
    'NCCM': average_accuracy[3:6],
    'EuroCrops': average_accuracy[6:9],
    'AgriFieldNet': average_accuracy[9:12],
    'SAS': average_accuracy[12:15],
    'SACT': average_accuracy[15:18],
}
average_jaccard_index_id = {
    'CDL': average_jaccard_index[0:3],
    'NCCM': average_jaccard_index[3:6],
    'EuroCrops': average_jaccard_index[6:9],
    'AgriFieldNet': average_jaccard_index[9:12],
    'SAS': average_jaccard_index[12:15],
    'SACT': average_jaccard_index[15:18],
}
overall_f1_id = {
    'CDL': overall_f1[0:3],
    'NCCM': overall_f1[3:6],
    'EuroCrops': overall_f1[6:9],
    'AgriFieldNet': overall_f1[9:12],
    'SAS': overall_f1[12:15],
    'SACT': overall_f1[15:18],
}
overall_precision_id = {
    'CDL': overall_precision[0:3],
    'NCCM': overall_precision[3:6],
    'EuroCrops': overall_precision[6:9],
    'AgriFieldNet': overall_precision[9:12],
    'SAS': overall_precision[12:15],
    'SACT': overall_precision[15:18],
}
overall_recall_id = {
    'CDL': overall_recall[0:3],
    'NCCM': overall_recall[3:6],
    'EuroCrops': overall_recall[6:9],
    'AgriFieldNet': overall_recall[9:12],
    'SAS': overall_recall[12:15],
    'SACT': overall_recall[15:18],
}
overall_accuracy_id = {
    'CDL': overall_accuracy[0:3],
    'NCCM': overall_accuracy[3:6],
    'EuroCrops': overall_accuracy[6:9],
    'AgriFieldNet': overall_accuracy[9:12],
    'SAS': overall_accuracy[12:15],
    'SACT': overall_accuracy[15:18],
}
overall_jaccard_index_id = {
    'CDL': overall_jaccard_index[0:3],
    'NCCM': overall_jaccard_index[3:6],
    'EuroCrops': overall_jaccard_index[6:9],
    'AgriFieldNet': overall_jaccard_index[9:12],
    'SAS': overall_jaccard_index[12:15],
    'SACT': overall_jaccard_index[15:18],
}

dictionaries_ood_plus_id = [
    average_f1_ood_plus_id,
    overall_f1_ood_plus_id,
    average_precision_ood_plus_id,
    overall_precision_ood_plus_id,
    average_recall_ood_plus_id,
    overall_recall_ood_plus_id,
    average_accuracy_ood_plus_id,
    overall_accuracy_ood_plus_id,
    average_jaccard_index_ood_plus_id,
    overall_jaccard_index_ood_plus_id
]

dictionaries_id = [
    average_f1_id,
    overall_f1_id,
    average_precision_id,
    overall_precision_id,
    average_recall_id,
    overall_recall_id,
    average_accuracy_id,
    overall_accuracy_id,
    average_jaccard_index_id,
    overall_jaccard_index_id
]

# x-axis values for OOD + ID and ID only
x_values_ood_plus_id = [0, 10, 100, 900]
x_values_id_only = [10, 100, 900]

# Set up color map
colors = plt.cm.get_cmap('tab10', len(datasets))

fig, axs = plt.subplots(5, 2, figsize=(14, 20))
axs = axs.flatten()

for idx, ax in enumerate(axs):
    ood_plus_id = dictionaries_ood_plus_id[idx]
    id_only = dictionaries_id[idx]

    for i, dataset in enumerate(datasets):
        ax.plot(x_values_ood_plus_id, ood_plus_id[dataset], linestyle='-', marker='o', color=colors(i), linewidth=2, markersize=8, label=f'{dataset} (OOD + ID)')
        ax.plot(x_values_id_only, id_only[dataset], linestyle='--', marker='*', color=colors(i), linewidth=2, markersize=8, label=f'{dataset} (ID Only)')

    ax.grid(True)
    ax.set_xticks(range(0, 1000, 100))
    ax.set_title(all_metrics_name[idx])
    if idx >= 8:
        ax.set_xlabel('Number of ID Samples')

# Adjust the layout
fig.tight_layout(rect=[0, 0.075, 1, 1])

# Move legend to the bottom of the plot
plt.legend(loc='upper center', bbox_to_anchor=(0, -0.3), ncol=3, fontsize=12)

# Save the plot
plt.savefig('metrics_curve.png', dpi=300)

# Show the plot
plt.show()
