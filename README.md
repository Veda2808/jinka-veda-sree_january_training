**ASSIGNMENT-2**

This  data preprocessing techniques on the Netflix dataset to prepare it for machine learning tasks. Based on experimentation and data understanding, the following conclusions were drawn.
🔹 Missing Value Handling
Among different missing value handling methods (mean, median, and mode), mode-based imputation for categorical features and median-based handling for numerical features were found to work best.
Most missing values in the dataset were present in categorical columns such as director, cast, and country.
Filling these values using mode or a constant value ("Unknown") preserved the dataset size and avoided introducing incorrect assumptions.
For numerical data like release_year, the median is more robust than mean because it is not affected by extreme values.

📌 Final Choice:

Categorical → Mode / "Unknown"
Numerical → Median
🔹 Categorical Encoding Techniques
Different encoding techniques performed better depending on the type of categorical feature:
Label Encoding worked best for binary or low-cardinality features such as type (Movie / TV Show), as it is simple and does not increase dimensionality.
One-Hot Encoding was effective for nominal features like rating, where no natural order exists, preventing the model from assuming false relationships.
Ordinal Encoding performed well for features with a clear order, such as content ratings (G < PG < PG-13 < R < NC-17), because it preserves ranking information.
Frequency Encoding was most suitable for high-cardinality features like country, as it reduced dimensionality while retaining useful distribution information.
Target Encoding captured the relationship between categorical values and the target variable, making it useful when understanding category influence on predictions.

📌 Final Choice:
Encoding techniques were selected based on feature type, cardinality, and interpretability rather than using a single method for all features.
🔹 Feature Scaling Methods
Among the scaling techniques applied, Min-Max Scaling was found to be the most effective for this dataset.
Min-Max Scaling transformed values into a fixed range (0 to 1), making features easier to compare.
Z-score (Standardization) was useful when handling variations and centering data around zero.
Max Absolute Scaling and Vector Normalization were demonstrated for completeness but were less impactful for this dataset due to limited numerical features.

📌 Final Choice:

Min-Max Scaling for simplicity and interpretability
Z-score Scaling when variance handling is required
🔹 Outlier Treatment and Skewness Transformation
The numerical feature release_year was analyzed using descriptive statistics.
No extreme or unrealistic values were found, so outlier removal was not required.
The distribution of numerical features showed minimal skewness, making log or power transformations unnecessary.

📌 Key Observation:
Applying transformations only when required helps maintain the natural structure of the data and prevents over-processing.
🏁 Final Justification
The final preprocessing decisions were made to:
Preserve data integrity
Reduce unnecessary complexity
Maintain interpretability
Ensure model compatibility
Overall, the chosen preprocessing techniques created a clean, balanced, and machine-learning-ready dataset, while keeping the approach simple, efficient, and beginner-friendly.

**ASSIGNMENT-3**

## 📘 Detailed Description

This project demonstrates the complete implementation of a **Linear Regression model** using the **California Housing Dataset** obtained from Kaggle. The dataset contains more than **20,000 records**, making it suitable for building and evaluating a regression model. The objective of this assignment is to predict **median house prices** based on multiple housing and geographical features.
The dataset was first carefully analyzed to understand its structure, data types, and target variable. The target variable selected for this project is **`median_house_value`**, which is a continuous numerical variable, making it appropriate for Linear Regression.

### Data Cleaning
The dataset was checked for missing values and inconsistencies. Missing values in numerical columns were handled using **median imputation**, as the median is robust to outliers and works well with skewed data. The dataset also contained a categorical feature, **`ocean_proximity`**, which cannot be directly used by a Linear Regression model. Therefore, **One-Hot Encoding** was applied to convert this categorical feature into numerical form. After preprocessing, all features were numeric and ready for modeling.

### Exploratory Data Analysis (EDA)
EDA was performed to understand data distribution, feature relationships, and overall patterns. Scatter plots were used to analyze the relationship between important features and the target variable. A **correlation heatmap** was created to check the strength of relationships and detect multicollinearity among features.
From EDA, it was observed that **median income** has a strong positive correlation with house prices, while geographical features such as latitude and longitude also influence housing values. No extreme multicollinearity was found that would severely affect the Linear Regression model.

### Data Splitting
The dataset was split into **training and testing sets** to evaluate model performance on unseen data.
* **80%** of the data was used for training
* **20%** of the data was used for testing
This split helps ensure that the model generalizes well and does not simply memorize the training data.

### Model Building and Training
A **Linear Regression model** was built using the `sklearn` library. The model was trained on the training dataset, learning the relationship between the input features and the target variable. After training, predictions were made on the test dataset.

### Model Evaluation
The performance of the model was evaluated using two standard regression metrics:
* **Mean Squared Error (MSE)**
* **R² Score**
MSE measures the average squared difference between actual and predicted values, while R² indicates how well the model explains the variance in the target variable. Lower MSE and an R² value closer to 1 indicate better model performance.

### Model Improvement
To further improve performance and reduce MSE, additional steps such as **feature scaling using StandardScaler** and **regularization using Ridge Regression** were applied. These techniques helped improve model stability and generalization by reducing the effect of feature scale differences and overfitting.
---
## ✅ Conclusion
The California Housing dataset is well-suited for Linear Regression as the target variable is continuous and several input features show a clear linear relationship with house prices. Through proper data cleaning, encoding of categorical variables, and exploratory data analysis, the dataset was prepared effectively for modeling.
The Linear Regression model achieved a **reasonable Mean Squared Error and R² score**, indicating that it can explain a significant portion of the variance in house prices. Among all features, **median income** was found to have the strongest positive impact on house values, while geographical features also played an important role.
Although the model performs well, the relationships in the data are not perfectly linear, and some non-linear patterns exist. Therefore, while Linear Regression serves as a **good baseline model**, more advanced models such as Random Forest or Gradient Boosting could further improve prediction accuracy.
Overall, this assignment successfully demonstrates the **end-to-end process of Linear Regression**, including data preprocessing, visualization, model building, evaluation, and interpretation, fulfilling all the requirements specified in the assignment.
---
