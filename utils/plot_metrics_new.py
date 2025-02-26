import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'font.size': 14})

# Data from the table
datasets = ['CDL', 'NCCM', 'EuroCrops', 'SAS', 'SACT']
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

distributions = ['ood_plus_id', 'id_only', 'balanced_ood_plus_id']

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
    'CDL': [average_f1[i] for i in range(0, 20, 5)],
    'NCCM': [average_f1[i] for i in range(1, 20, 5)],
    'EuroCrops': [average_f1[i] for i in range(2, 20, 5)],
    'SAS': [average_f1[i] for i in range(3, 20, 5)],
    'SACT': [average_f1[i] for i in range(4, 20, 5)],
}
average_precision_ood_plus_id = {
    'CDL': [average_precision[i] for i in range(0, 20, 5)],
    'NCCM': [average_precision[i] for i in range(1, 20, 5)],
    'EuroCrops': [average_precision[i] for i in range(2, 20, 5)],
    'SAS': [average_precision[i] for i in range(3, 20, 5)],
    'SACT': [average_precision[i] for i in range(4, 20, 5)],
}
average_recall_ood_plus_id = {
    'CDL': [average_recall[i] for i in range(0, 20, 5)],
    'NCCM': [average_recall[i] for i in range(1, 20, 5)],
    'EuroCrops': [average_recall[i] for i in range(2, 20, 5)],
    'SAS': [average_recall[i] for i in range(3, 20, 5)],
    'SACT': [average_recall[i] for i in range(4, 20, 5)],
}
average_accuracy_ood_plus_id = {
    'CDL': [average_accuracy[i] for i in range(0, 20, 5)],
    'NCCM': [average_accuracy[i] for i in range(1, 20, 5)],
    'EuroCrops': [average_accuracy[i] for i in range(2, 20, 5)],
    'SAS': [average_accuracy[i] for i in range(3, 20, 5)],
    'SACT': [average_accuracy[i] for i in range(4, 20, 5)],
}
average_jaccard_index_ood_plus_id = {
    'CDL': [average_jaccard_index[i] for i in range(0, 20, 5)],
    'NCCM': [average_jaccard_index[i] for i in range(1, 20, 5)],
    'EuroCrops': [average_jaccard_index[i] for i in range(2, 20, 5)],
    'SAS': [average_jaccard_index[i] for i in range(3, 20, 5)],
    'SACT': [average_jaccard_index[i] for i in range(4, 20, 5)],
}
overall_f1_ood_plus_id = {
    'CDL': [overall_f1[i] for i in range(0, 20, 5)],
    'NCCM': [overall_f1[i] for i in range(1, 20, 5)],
    'EuroCrops': [overall_f1[i] for i in range(2, 20, 5)],
    'SAS': [overall_f1[i] for i in range(3, 20, 5)],
    'SACT': [overall_f1[i] for i in range(4, 20, 5)],
}
overall_precision_ood_plus_id = {
    'CDL': [overall_precision[i] for i in range(0, 20, 5)],
    'NCCM': [overall_precision[i] for i in range(1, 20, 5)],
    'EuroCrops': [overall_precision[i] for i in range(2, 20, 5)],
    'SAS': [overall_precision[i] for i in range(3, 20, 5)],
    'SACT': [overall_precision[i] for i in range(4, 20, 5)],
}
overall_recall_ood_plus_id = {
    'CDL': [overall_recall[i] for i in range(0, 20, 5)],
    'NCCM': [overall_recall[i] for i in range(1, 20, 5)],
    'EuroCrops': [overall_recall[i] for i in range(2, 20, 5)],
    'SAS': [overall_recall[i] for i in range(3, 20, 5)],
    'SACT': [overall_recall[i] for i in range(4, 20, 5)],
}
overall_accuracy_ood_plus_id = {
    'CDL': [overall_accuracy[i] for i in range(0, 20, 5)],
    'NCCM': [overall_accuracy[i] for i in range(1, 20, 5)],
    'EuroCrops': [overall_accuracy[i] for i in range(2, 20, 5)],
    'SAS': [overall_accuracy[i] for i in range(3, 20, 5)],
    'SACT': [overall_accuracy[i] for i in range(4, 20, 5)],
}
overall_jaccard_index_ood_plus_id = {
    'CDL': [overall_jaccard_index[i] for i in range(0, 20, 5)],
    'NCCM': [overall_jaccard_index[i] for i in range(1, 20, 5)],
    'EuroCrops': [overall_jaccard_index[i] for i in range(2, 20, 5)],
    'SAS': [overall_jaccard_index[i] for i in range(3, 20, 5)],
    'SACT': [overall_jaccard_index[i] for i in range(4, 20, 5)],
}

balanced_ood_df = pd.read_excel('Balanced_OOD.xlsx', header=None)
average_f1, average_precision, average_recall, average_accuracy, average_jaccard_index, overall_f1, overall_precision, overall_recall, overall_accuracy, overall_jaccard_index = extract_metrics(balanced_ood_df)

average_f1_balanced_ood_plus_id = {
    'CDL': [average_f1[i] for i in range(0, 15, 5)],
    'NCCM': [average_f1[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_f1[i] for i in range(2, 15, 5)],
    'SAS': [average_f1[i] for i in range(3, 15, 5)],
    'SACT': [average_f1[i] for i in range(4, 15, 5)],
}
average_precision_balanced_ood_plus_id = {
    'CDL': [average_precision[i] for i in range(0, 15, 5)],
    'NCCM': [average_precision[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_precision[i] for i in range(2, 15, 5)],
    'SAS': [average_precision[i] for i in range(3, 15, 5)],
    'SACT': [average_precision[i] for i in range(4, 15, 5)],
}
average_recall_balanced_ood_plus_id = {
    'CDL': [average_recall[i] for i in range(0, 15, 5)],
    'NCCM': [average_recall[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_recall[i] for i in range(2, 15, 5)],
    'SAS': [average_recall[i] for i in range(3, 15, 5)],
    'SACT': [average_recall[i] for i in range(4, 15, 5)],
}
average_accuracy_balanced_ood_plus_id = {
    'CDL': [average_accuracy[i] for i in range(0, 15, 5)],
    'NCCM': [average_accuracy[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_accuracy[i] for i in range(2, 15, 5)],
    'SAS': [average_accuracy[i] for i in range(3, 15, 5)],
    'SACT': [average_accuracy[i] for i in range(4, 15, 5)],
}
average_jaccard_index_balanced_ood_plus_id = {
    'CDL': [average_jaccard_index[i] for i in range(0, 15, 5)],
    'NCCM': [average_jaccard_index[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_jaccard_index[i] for i in range(2, 15, 5)],
    'SAS': [average_jaccard_index[i] for i in range(3, 15, 5)],
    'SACT': [average_jaccard_index[i] for i in range(4, 15, 5)],
}
overall_f1_balanced_ood_plus_id = {
    'CDL': [overall_f1[i] for i in range(0, 15, 5)],
    'NCCM': [overall_f1[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_f1[i] for i in range(2, 15, 5)],
    'SAS': [overall_f1[i] for i in range(3, 15, 5)],
    'SACT': [overall_f1[i] for i in range(4, 15, 5)],
}
overall_precision_balanced_ood_plus_id = {
    'CDL': [overall_precision[i] for i in range(0, 15, 5)],
    'NCCM': [overall_precision[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_precision[i] for i in range(2, 15, 5)],
    'SAS': [overall_precision[i] for i in range(3, 15, 5)],
    'SACT': [overall_precision[i] for i in range(4, 15, 5)],
}
overall_recall_balanced_ood_plus_id = {
    'CDL': [overall_recall[i] for i in range(0, 15, 5)],
    'NCCM': [overall_recall[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_recall[i] for i in range(2, 15, 5)],
    'SAS': [overall_recall[i] for i in range(3, 15, 5)],
    'SACT': [overall_recall[i] for i in range(4, 15, 5)],
}
overall_accuracy_balanced_ood_plus_id = {
    'CDL': [overall_accuracy[i] for i in range(0, 15, 5)],
    'NCCM': [overall_accuracy[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_accuracy[i] for i in range(2, 15, 5)],
    'SAS': [overall_accuracy[i] for i in range(3, 15, 5)],
    'SACT': [overall_accuracy[i] for i in range(4, 15, 5)],
}
overall_jaccard_index_balanced_ood_plus_id = {
    'CDL': [overall_jaccard_index[i] for i in range(0, 15, 5)],
    'NCCM': [overall_jaccard_index[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_jaccard_index[i] for i in range(2, 15, 5)],
    'SAS': [overall_jaccard_index[i] for i in range(3, 15, 5)],
    'SACT': [overall_jaccard_index[i] for i in range(4, 15, 5)],
}

id_df = pd.read_excel('ID.xlsx', header=None)
average_f1, average_precision, average_recall, average_accuracy, average_jaccard_index, overall_f1, overall_precision, overall_recall, overall_accuracy, overall_jaccard_index = extract_metrics(id_df)

average_f1_id = {
    'CDL': [average_f1[i] for i in range(0, 15, 5)],
    'NCCM': [average_f1[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_f1[i] for i in range(2, 15, 5)],
    'SAS': [average_f1[i] for i in range(3, 15, 5)],
    'SACT': [average_f1[i] for i in range(4, 15, 5)],
}
average_precision_id = {
    'CDL': [average_precision[i] for i in range(0, 15, 5)],
    'NCCM': [average_precision[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_precision[i] for i in range(2, 15, 5)],
    'SAS': [average_precision[i] for i in range(3, 15, 5)],
    'SACT': [average_precision[i] for i in range(4, 15, 5)],
}
average_recall_id = {
    'CDL': [average_recall[i] for i in range(0, 15, 5)],
    'NCCM': [average_recall[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_recall[i] for i in range(2, 15, 5)],
    'SAS': [average_recall[i] for i in range(3, 15, 5)],
    'SACT': [average_recall[i] for i in range(4, 15, 5)],
}
average_accuracy_id = {
    'CDL': [average_accuracy[i] for i in range(0, 15, 5)],
    'NCCM': [average_accuracy[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_accuracy[i] for i in range(2, 15, 5)],
    'SAS': [average_accuracy[i] for i in range(3, 15, 5)],
    'SACT': [average_accuracy[i] for i in range(4, 15, 5)],
}
average_jaccard_index_id = {
    'CDL': [average_jaccard_index[i] for i in range(0, 15, 5)],
    'NCCM': [average_jaccard_index[i] for i in range(1, 15, 5)],
    'EuroCrops': [average_jaccard_index[i] for i in range(2, 15, 5)],
    'SAS': [average_jaccard_index[i] for i in range(3, 15, 5)],
    'SACT': [average_jaccard_index[i] for i in range(4, 15, 5)],
}
overall_f1_id = {
    'CDL': [overall_f1[i] for i in range(0, 15, 5)],
    'NCCM': [overall_f1[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_f1[i] for i in range(2, 15, 5)],
    'SAS': [overall_f1[i] for i in range(3, 15, 5)],
    'SACT': [overall_f1[i] for i in range(4, 15, 5)],
}
overall_precision_id = {
    'CDL': [overall_precision[i] for i in range(0, 15, 5)],
    'NCCM': [overall_precision[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_precision[i] for i in range(2, 15, 5)],
    'SAS': [overall_precision[i] for i in range(3, 15, 5)],
    'SACT': [overall_precision[i] for i in range(4, 15, 5)],
}
overall_recall_id = {
    'CDL': [overall_recall[i] for i in range(0, 15, 5)],
    'NCCM': [overall_recall[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_recall[i] for i in range(2, 15, 5)],
    'SAS': [overall_recall[i] for i in range(3, 15, 5)],
    'SACT': [overall_recall[i] for i in range(4, 15, 5)],
}
overall_accuracy_id = {
    'CDL': [overall_accuracy[i] for i in range(0, 15, 5)],
    'NCCM': [overall_accuracy[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_accuracy[i] for i in range(2, 15, 5)],
    'SAS': [overall_accuracy[i] for i in range(3, 15, 5)],
    'SACT': [overall_accuracy[i] for i in range(4, 15, 5)],
}
overall_jaccard_index_id = {
    'CDL': [overall_jaccard_index[i] for i in range(0, 15, 5)],
    'NCCM': [overall_jaccard_index[i] for i in range(1, 15, 5)],
    'EuroCrops': [overall_jaccard_index[i] for i in range(2, 15, 5)],
    'SAS': [overall_jaccard_index[i] for i in range(3, 15, 5)],
    'SACT': [overall_jaccard_index[i] for i in range(4, 15, 5)],
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

dictionaries_balanced_ood_plus_id = [
    average_f1_balanced_ood_plus_id,
    overall_f1_balanced_ood_plus_id,
    average_precision_balanced_ood_plus_id,
    overall_precision_balanced_ood_plus_id,
    average_recall_balanced_ood_plus_id,
    overall_recall_balanced_ood_plus_id,
    average_accuracy_balanced_ood_plus_id,
    overall_accuracy_balanced_ood_plus_id,
    average_jaccard_index_balanced_ood_plus_id,
    overall_jaccard_index_balanced_ood_plus_id
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

# setup x-axis values
x_values_ood_plus_id = [0, 10, 100, 900]
x_values_balanced_ood_plus_id = [10, 100, 900]
x_values_id_only = [10, 100, 900]

colors = plt.cm.get_cmap('tab10', len(datasets))

fig, axs = plt.subplots(5, 2, figsize=(16, 20))
axs = axs.flatten()

for idx, ax in enumerate(axs):
    ood_plus_id = dictionaries_ood_plus_id[idx]
    balanced_ood_plus_id = dictionaries_balanced_ood_plus_id[idx]
    id_only = dictionaries_id[idx]

    for i, dataset in enumerate(datasets):
        ax.plot(x_values_id_only, id_only[dataset], linestyle='-', marker='o', color=colors(i), linewidth=1, markersize=6, label=f'{dataset} (ID Only)')
        ax.plot(x_values_ood_plus_id, ood_plus_id[dataset], linestyle='--', marker='^', color=colors(i), linewidth=1, markersize=6, label=f'{dataset} (OOD + ID)')
        ax.plot(x_values_balanced_ood_plus_id, balanced_ood_plus_id[dataset], linestyle='-.', marker='s', color=colors(i), linewidth=1, markersize=6, label=f'{dataset} (Balanced OOD + ID)')

    ax.grid(True)
    ax.set_xticks(range(0, 1000, 100))
    ax.set_title(all_metrics_name[idx])
    if idx >= 8:
        ax.set_xlabel('Number of ID Samples')

fig.tight_layout(rect=[0, 0.075, 1, 1])
plt.legend(loc='upper center', bbox_to_anchor=(-0.05, -0.3), ncol=5, fontsize=12)

plt.savefig('metrics_curve_new.png', dpi=300)
plt.show()
