import matplotlib.pyplot as plt
import numpy as np

models = [
    "Logistic Regression",
    "Multinomial NB",
    "Linear SVM",
    "XGBoost",
    "Random Forest",
    "CatBoost"
]

precision = [
    0.99,
    0.98,
    0.99,
    1.00,
    1.00,
    1.00
]

recall = [
    0.96,
    0.93,
    0.98,
    0.98,
    0.98,
    0.98
]

x = np.arange(len(models))
width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(x - width/2, precision, width, label="Precision")
plt.bar(x + width/2, recall, width, label="Recall")

plt.title("SQL Injection Detection: Precision vs Recall")

plt.xlabel("Machine Learning Model")
plt.ylabel("Score")

plt.ylim(0.90, 1.02)

plt.xticks(x, models, rotation=25)

plt.legend()

plt.tight_layout()

plt.savefig("precision_recall_comparison.png", dpi=300)

plt.show()