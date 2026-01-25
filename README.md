This project applied multiple data preprocessing techniques on the Netflix dataset to prepare it for machine learning tasks. Based on experimentation and data understanding, the following conclusions were drawn.

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
