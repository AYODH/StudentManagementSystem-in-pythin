# Student Progression Outcome Predictor

This project is designed to predict student progression outcomes at the end of each academic year based on the number of credits they have achieved in pass, defer, and fail categories. The program validates user inputs, calculates progression outcomes, and provides a graphical representation using a histogram.

# Features

- **Data Loading**: Load data from CSV files.
- **Data Preprocessing**: Handle missing values and normalize numerical features.
- **Data Splitting**: Separate features and target variable, and split data into training and testing sets.
- **Model Training**: Train a Random Forest classifier.
- **Model Evaluation**: Evaluate the trained model using accuracy and classification report.
- **Model Saving/Loading**: Save the trained model to a file and load it for future use.
- **Progression Outcome Calculation**: Determines if a student progresses, trails, retrieves modules, or is excluded based on their credits.
- **Histogram Display**: Uses the `graphics.py` module to create a histogram of the progression outcomes.

# Installation

To use this project, you'll need to have Python installed along with the following packages:

- `numpy`
- `pandas`
- `scikit-learn`
- `joblib`

# Functions

- `load_data(file_path)`: Loads data from a CSV file.
- `preprocess_data(df)`: Fills missing values and normalizes numerical features.
- `split_data(df, target_column)`: Splits the data into features and target.
- `train_test_split(X, y, test_size=0.2, random_state=42)`: Splits data into training and testing sets.
- `train_model(X_train, y_train)`: Trains a Random Forest classifier.
- `evaluate_model(model, X_test, y_test)`: Evaluates the trained model.
- `save_model(model, file_path)`: Saves the trained model to a file.
- `load_model(file_path)`: Loads a trained model from a file.

# Example Outputs

### Part 1
```
Enter your credits at pass: 100
Enter your credits at defer: 20
Enter your credits at fail: 0
Progress (module trailer)
```

### Part 2
```
Part 2:
Progress - 120, 0, 0
Progress (module trailer) - 100, 0, 20
Module retriever - 80, 20, 20
```

### Part 3
```
Part 3:
Progress - 120, 0, 0
Progress (module trailer) - 100, 0, 20
Module retriever - 80, 20, 20
