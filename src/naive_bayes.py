import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Load dataset
data = pd.read_csv("data/dataset.csv")

print("Dataset shape:", data.shape)


# Separate input and output
X = data["request"]
y = data["label"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=10000
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


# Create Naive Bayes model
model = MultinomialNB()


# Train model
print("\nTraining Multinomial Naive Bayes model...")

model.fit(X_train, y_train)

print("Training completed!")


# Make predictions
predictions = model.predict(X_test)


# Evaluate model
accuracy = accuracy_score(y_test, predictions)
matrix = confusion_matrix(y_test, predictions)

print("\n" + "=" * 50)
print("MULTINOMIAL NAIVE BAYES RESULTS")
print("=" * 50)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

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