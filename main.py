from src.prepprocess import load_data, inspect_data, clean_data, feature_engineering
from src.analysis import analyze_data, group_analysis

def main():
    path = "data/student_dataset.csv"

    data = load_data(path)
    inspect_data(data)

    data = clean_data(data)
    data = feature_engineering(data)

    analyze_data(data)
    group_analysis(data)

if __name__ == "__main__":
    main()