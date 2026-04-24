import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    return data

def inspect_data(data):
    print("First 5 rows:\n", data.head())
    print("\nShape:", data.shape)
    print("\nColumns:\n", data.columns)

def clean_data(data):
    # Missing values
    print("\nMissing Values:\n", data.isnull().sum())

    # Fill missing values
    data['Marks'].fillna(data['Marks'].mean(), inplace=True)
    data['StudyHours'].fillna(data['StudyHours'].median(), inplace=True)

    # Remove outliers
    data = data[(data['StudyHours'] <= 15) & (data['Marks'] <= 100)]

    return data

def feature_engineering(data):
    # Performance column
    def performance(marks):
        if marks >= 80:
            return "Excellent"
        elif marks >= 60:
            return "Good"
        else:
            return "Needs Improvement"

    data['Performance'] = data['Marks'].apply(performance)

    # Effort Score
    data['EffortScore'] = data['StudyHours'] * data['Attendance']

    return data