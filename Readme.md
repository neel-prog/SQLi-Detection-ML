# SQL Injection Detection Using Machine Learning

A machine learning project that detects whether an SQL query or request-like input is **benign** or contains a possible **SQL Injection attack**.

The project compares multiple machine learning algorithms using the same dataset and feature extraction method.

---

## 📌 Project Overview

SQL Injection is a common web application attack where malicious SQL code is inserted into an application's input.

For example, instead of entering normal user input, an attacker may try to manipulate an SQL query to bypass authentication or access database information.

Traditional detection methods often depend on fixed rules or known signatures. In this project, machine learning is used to learn patterns from both benign and malicious SQL inputs.

The trained models classify an input into:

* `0` → Benign
* `1` → SQL Injection

---

## 🎯 Objectives

The main objectives of this project are:

* Detect SQL Injection attacks using machine learning.
* Preprocess and clean the dataset.
* Convert SQL text into numerical features using TF-IDF.
* Compare different machine learning algorithms.
* Evaluate models using accuracy, precision, recall, and confusion matrices.
* Identify the best-performing model.

---

## 📊 Dataset

The dataset was obtained from Kaggle.

* Original dataset size: **30,919 samples**
* Dataset size after cleaning: **30,834 samples**
* Benign samples: **19,517**
* SQL Injection samples: **11,317**

The dataset contains:

| Column    | Description                     |
| --------- | ------------------------------- |
| `request` | SQL query or request-like input |
| `label`   | Classification label            |

### Labels

```text
0 → Benign Input
1 → SQL Injection
```

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Checked for missing values.
3. Removed invalid or empty records.
4. Selected the input text and labels.
5. Split the dataset into training and testing data.
6. Used a stratified split to maintain class distribution.

### Train-Test Split

```text
Training Samples: 24,667
Testing Samples:  6,167
```

The dataset was divided using:

```text
80% → Training Data
20% → Testing Data
```

A `random_state` of `42` was used.

---

## 🔤 Feature Extraction

Machine learning models cannot directly understand SQL queries as text.

So, **TF-IDF (Term Frequency-Inverse Document Frequency)** was used to convert the input text into numerical features.

Configuration used:

```python
ngram_range=(1, 2)
max_features=10000
```

This means the model uses:

* **Unigrams** → Single words or tokens
* **Bigrams** → Two consecutive words or tokens

### Feature Matrix

```text
Training Shape: (24667, 10000)
Testing Shape:  (6167, 10000)
```

---

## 🤖 Machine Learning Models

The following six algorithms were compared:

1. Logistic Regression
2. Multinomial Naive Bayes
3. Linear Support Vector Machine
4. XGBoost
5. Random Forest
6. CatBoost

Each model was trained using the same training data and tested using the same testing data.

---

## 📈 Results

### Accuracy Comparison

| Model                   |   Accuracy |
| ----------------------- | ---------: |
| Logistic Regression     |     98.25% |
| Multinomial Naive Bayes |     96.74% |
| Linear SVM              |     98.90% |
| XGBoost                 |     99.35% |
| **Random Forest**       | **99.42%** |
| CatBoost                |     99.37% |

### Best Performing Model

🏆 **Random Forest**

```text
Accuracy: 99.42%
```

Random Forest achieved the highest accuracy among all tested models.

---

## 🔍 Confusion Matrices

### Logistic Regression

```text
[[3879   25]
 [  83 2180]]
```

### Multinomial Naive Bayes

```text
[[3863   41]
 [ 160 2103]]
```

### Linear SVM

```text
[[3877   27]
 [  41 2222]]
```

### XGBoost

```text
[[3900    4]
 [  36 2227]]
```

### Random Forest

```text
[[3902    2]
 [  34 2229]]
```

### CatBoost

```text
[[3900    4]
 [  35 2228]]
```

---

## 🛡️ Why False Negatives Matter

In a cybersecurity project, accuracy alone is not enough.

A **False Negative** means that an SQL Injection attack was incorrectly classified as benign.

| Model                   | False Negatives |
| ----------------------- | --------------: |
| Logistic Regression     |              83 |
| Multinomial Naive Bayes |             160 |
| Linear SVM              |              41 |
| XGBoost                 |              36 |
| **Random Forest**       |          **34** |
| CatBoost                |              35 |

Random Forest had the lowest number of false negatives among the tested models.

This is important because fewer false negatives mean fewer malicious inputs are missed.

---

## 📊 Visualizations

The project includes graphs to make model comparison easier.

### 1. Accuracy Comparison

Compares the overall accuracy of all six machine learning models.

```text
Logistic Regression
Multinomial Naive Bayes
Linear SVM
XGBoost
Random Forest
CatBoost
```

### 2. Precision vs Recall

Shows how accurately each model detects SQL Injection attacks and how many attacks it successfully identifies.

### 3. False Negatives Comparison

Shows how many SQL Injection attacks were missed by each model.

### 4. Dataset Distribution

Shows the distribution between benign and malicious samples.

---

## 📁 Project Structure

```text
SQL-Injection-Detection-ML/
│
├── data/
│   └── dataset.csv
│
├── graphs/
│   ├── accuracy_comparison.png
│   ├── precision_recall_comparison.png
│   ├── false_negatives_comparison.png
│   └── dataset_distribution.png
│
├── src/
│   ├── data_preprocessing.py
│   ├── train_models.py
│   └── visualization.py
│
├── models/
│   └── trained_models/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/SQL-Injection-Detection-ML.git
```

Move into the project directory:

```bash
cd SQL-Injection-Detection-ML
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

The main libraries used in this project are:

```text
pandas
numpy
scikit-learn
matplotlib
xgboost
catboost
```

You can create a `requirements.txt` file containing:

```text
pandas
numpy
scikit-learn
matplotlib
xgboost
catboost
```

Then install everything using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

Run the preprocessing and model training scripts:

```bash
python src/train_models.py
```

To generate graphs:

```bash
python src/visualization.py
```

---

## 📏 Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Accuracy

Shows the percentage of total predictions that were correct.

### Precision

Shows how many inputs predicted as SQL Injection were actually malicious.

### Recall

Shows how many actual SQL Injection attacks were successfully detected.

### F1-Score

Combines precision and recall into a single score.

---

## 🔮 Future Improvements

There are several ways this project can be improved:

* Test the models using additional datasets.
* Use real-world HTTP request data.
* Test character-level features.
* Try word embeddings.
* Compare deep learning models.
* Test transformer-based models.
* Build a real-time SQL Injection detection API.
* Integrate the model with a web application firewall.

---

## ⚠️ Limitations

The models were tested mainly using one dataset.

A high accuracy score on this dataset does not guarantee the same performance against every real-world SQL Injection attack.

Attackers may use new payloads or obfuscation techniques that were not present in the training data.

For this reason, the model should be treated as an additional detection layer and not as a replacement for secure coding practices such as:

* Parameterized queries
* Prepared statements
* Proper input validation
* Least privilege database access

---

## 📚 References

* Kaggle SQL Injection Dataset
* Scikit-learn Documentation
* Research papers related to machine learning-based SQL Injection detection

---

## 👨‍💻 Author

**Neel Kiran Sankpal**

B.Tech Computer Science and Engineering
Specialization: Cybersecurity

---

## ⭐ Final Result

Out of the six machine learning models tested, **Random Forest achieved the best performance**.

```text
🏆 Best Model: Random Forest
📊 Accuracy: 99.42%
🛡️ Lowest False Negatives: 34
```

This project shows how machine learning can be used as an additional layer for detecting suspicious SQL input and possible SQL Injection attacks.

---

If you found this project useful, consider giving the repository a ⭐.
