import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from catboost import CatBoostClassifier


# Load dataset
data = pd.read_csv("data/dataset.csv")

print("Dataset shape:", data.shape)


# Separate features and labels
X = data["request"]
y = data["label"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# TF-IDF vectorization
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=10000
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# CatBoost model
model = CatBoostClassifier(
    iterations=300,
    depth=8,
    learning_rate=0.1,
    loss_function="Logloss",
    verbose=False,
    random_seed=42,
    thread_count=-1
)


# Train model
print("\nTraining CatBoost model...")

model.fit(X_train_tfidf, y_train)

print("Training completed!")


# Make predictions
predictions = model.predict(X_test_tfidf)

# Convert predictions to integers
predictions = predictions.astype(int).flatten()


# Evaluation
accuracy = accuracy_score(y_test, predictions)

matrix = confusion_matrix(y_test, predictions)


print("\n" + "=" * 50)
print("CATBOOST RESULTS")
print("=" * 50)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(matrix)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions,
        target_names=[
            "Benign",
            "SQL Injection"
        ],
        zero_division=0
    )
)