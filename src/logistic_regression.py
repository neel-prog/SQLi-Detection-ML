import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


data = pd.read_csv("data/dataset.csv")

print("Dataset shape:", data.shape)
print("\nLabel distribution:")
print(data["label"].value_counts())


X = data["request"]
y = data["label"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=10000
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print("\nTraining feature shape:", X_train.shape)
print("Testing feature shape:", X_test.shape)


model = LogisticRegression(max_iter=1000)

print("\nTraining model...")
model.fit(X_train, y_train)


predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
matrix = confusion_matrix(y_test, predictions)

print("\nAccuracy:", f"{accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(matrix)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=["Benign", "SQL Injection"],
        zero_division=0
    )
)