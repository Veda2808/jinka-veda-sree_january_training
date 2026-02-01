# 🚢 Titanic Survival Prediction Using Supervised Machine Learning

## 📌 Project Title

**Titanic Survival Prediction Using Multiple Supervised Machine Learning Algorithms**

---

## 🎯 Problem Statement

The objective of this project is to build machine learning models that can predict whether a passenger survived the Titanic disaster based on various features such as passenger class, gender, age, fare, and family members.

This project demonstrates the complete supervised machine learning workflow including data preprocessing, feature engineering, model training, and performance evaluation.

---

## 📊 Dataset Description

The dataset used in this project is the **Titanic dataset from Kaggle**, which contains passenger information from the Titanic shipwreck.

### Dataset Features:

* PassengerId – Unique ID for each passenger
* Survived – Survival status (0 = No, 1 = Yes)
* Pclass – Passenger class
* Name – Passenger name
* Sex – Gender
* Age – Age of passenger
* SibSp – Number of siblings/spouses aboard
* Parch – Number of parents/children aboard
* Ticket – Ticket number
* Fare – Ticket fare
* Cabin – Cabin number
* Embarked – Port of embarkation

👉 The dataset file is included in this repository as required.

---

## 🧹 Data Cleaning & Preprocessing

Proper data preprocessing was performed before applying machine learning algorithms.

### ✔ Handling Missing Values

* The **Cabin** column contained a large number of missing values (>70%).
* Imputing such a large portion could introduce bias.
* Therefore, the Cabin column was **removed** from the dataset.

### ✔ Removing Irrelevant Features

The following columns were dropped because they do not contribute meaningful information for prediction:

* **Name** → Unique for each passenger
* **Ticket** → Random alphanumeric values
* **PassengerId** → Identifier only

Removing these features helps improve model performance and reduces noise.

---

### ✔ Encoding Categorical Variables

Machine learning models require numeric input.

* **Sex** column was converted into numeric format:

  * Male → 0
  * Female → 1

* **Embarked** column was transformed using one-hot encoding.

---

### ✔ Detecting Outliers

Boxplots were used to visually inspect the dataset for potential outliers.
Outliers were retained since they may represent real passenger variations.

---

### ✔ Feature Scaling

Feature scaling was applied using **StandardScaler** to normalize the data.

This step is especially important for algorithms such as:

* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)

Scaling ensures all features contribute equally to the model.

---

### ✔ Train-Test Split

The dataset was split into:

* **80% Training Data**
* **20% Testing Data**

This allows proper evaluation of model performance on unseen data.

---

## 🤖 Algorithms Used

The following supervised learning algorithms were implemented:

1. Linear Regression
2. Logistic Regression
3. Decision Tree
4. Random Forest
5. K-Nearest Neighbors (KNN)
6. Support Vector Machine (SVM)

Multiple models were trained to compare performance and identify the most effective algorithm.

---

## 📏 Evaluation Metrics

Since this is a classification problem, the following metrics were used:

* Accuracy
* Precision
* Recall
* F1 Score

Accuracy was primarily used to compare model performance.

---

## 📊 Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 81%      |
| Decision Tree       | 71%      |
| Random Forest       | 83%      |
| KNN                 | 81%      |
| SVM                 | 81%      |
| Linear Regression   | 78%      |

👉 Replace **XX** with your actual scores.

---

## 🏆 Conclusion / Observations

* Data preprocessing significantly improved model readiness and performance.
* Random Forest generally produced the highest accuracy due to its ensemble learning capability and reduced overfitting.
* Logistic Regression performed well because the dataset has structured relationships between features and survival.
* KNN and SVM benefited greatly from feature scaling.
* Linear Regression was less suitable since the problem is classification-based.

### ✅ Key Insight:

Passenger survival was strongly influenced by factors such as gender, passenger class, and fare.

---

## 🚀 Final Outcome

This project successfully demonstrates the end-to-end implementation of supervised machine learning, from raw data preprocessing to model evaluation and comparison.

---

## 📂 Repository Structure

```
Test04/
│
├── dataset/
│   └── tested.csv
│
├── notebook/
│   └── titanic_models.ipynb
│
├── README.md
```

