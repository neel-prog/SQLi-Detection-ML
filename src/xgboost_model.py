import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from xgboost import XGBClassifier


# ==========================================
# LOAD DATASET
# ==========================================

data = pd.read_csv("data/dataset.csv")

print("Dataset shape:", data.shape)


# ==========================================
# SEPARATE FEATURES AND LABELS
# ==========================================

X = data["request"]
y = data["label"]


# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# TF-IDF VECTORIZATION
# ==========================================

vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=10000
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


# ==========================================
# XGBOOST MODEL
# ==========================================

model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    eval_metric="logloss",
    random_state=42,
    n_jobs=-1
)


# ==========================================
# TRAIN MODEL
# ==========================================

print("\nTraining XGBoost model...")

model.fit(X_train, y_train)

print("Training completed!")


# ==========================================
# MAKE PREDICTIONS
# ==========================================

predictions = model.predict(X_test)


# ==========================================
# EVALUATION
# ==========================================

accuracy = accuracy_score(y_test, predictions)

matrix = confusion_matrix(y_test, predictions)


print("\n" + "=" * 50)
print("XGBOOST RESULTS")
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