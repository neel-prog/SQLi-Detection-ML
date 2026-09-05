import matplotlib.pyplot as plt

models = [
    "Logistic Regression",
    "Multinomial NB",
    "Linear SVM",
    "XGBoost",
    "Random Forest",
    "CatBoost"
]

accuracy = [
    98.25,
    96.74,
    98.90,
    99.35,
    99.42,
    99.37
]

plt.figure(figsize=(10, 6))

bars = plt.bar(models, accuracy)

plt.title("Accuracy Comparison of Machine Learning Models")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy (%)")
plt.ylim(95, 100)

plt.xticks(rotation=25)

for bar, value in zip(bars, accuracy):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.05,
        f"{value:.2f}%",
        ha="center"
    )

plt.tight_layout()

plt.savefig("accuracy_comparison.png", dpi=300)

plt.show()