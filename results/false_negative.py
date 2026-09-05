import matplotlib.pyplot as plt

models = [
    "Logistic Regression",
    "Multinomial NB",
    "Linear SVM",
    "XGBoost",
    "Random Forest",
    "CatBoost"
]

false_negatives = [
    83,
    160,
    41,
    36,
    34,
    35
]

plt.figure(figsize=(10, 6))

bars = plt.bar(models, false_negatives)

plt.title("False Negatives: Missed SQL Injection Attacks")

plt.xlabel("Machine Learning Model")
plt.ylabel("Number of False Negatives")

plt.xticks(rotation=25)

for bar, value in zip(bars, false_negatives):

    plt.text(
        bar.get_x() + bar.get_width()/2,
        value + 2,
        str(value),
        ha="center"
    )

plt.tight_layout()

plt.savefig("false_negatives_comparison.png", dpi=300)

plt.show()