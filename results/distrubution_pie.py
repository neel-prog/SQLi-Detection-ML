import matplotlib.pyplot as plt

labels = [
    "Benign",
    "SQL Injection"
]

samples = [
    19517,
    11317
]

plt.figure(figsize=(7, 7))

plt.pie(
    samples,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Dataset Distribution After Cleaning")

plt.tight_layout()

plt.savefig("dataset_distribution.png", dpi=300)

plt.show()