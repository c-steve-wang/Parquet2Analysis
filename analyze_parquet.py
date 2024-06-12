import pandas as pd
import sqlite3
import statsmodels.api as sm

# Read the Parquet file
def read_parquet(file_path):
    return pd.read_parquet(file_path)

# Create a SQLite database in memory and load the DataFrame
def create_sqlite_db(df):
    conn = sqlite3.connect(":memory:")
    df.to_sql("parquet_data", conn, index=False, if_exists="replace")
    return conn

# Analyze the data
def analyze_data(conn, value_names):
    results = {}
    for value_name in value_names:
        query = f"""
        SELECT {value_name}, COUNT(*)
        FROM parquet_data
        GROUP BY {value_name}
        ORDER BY COUNT(*) DESC
        """
        results[value_name] = pd.read_sql(query, conn)
    return results

# Data description
def describe_data(df):
    return df.describe()

# Linear regression with p-value output
def linear_regression(df, dependent_var, independent_vars):
    X = df[independent_vars]
    X = sm.add_constant(X)  # Adds a constant term to the predictor
    y = df[dependent_var]

    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)

    # Summarize the model
    summary = model.summary()
    return summary

# Main function
def main(file_path, value_names, dependent_var, independent_vars, functions):
    df = read_parquet(file_path)
    conn = create_sqlite_db(df)
    
    if "description" in functions:
        # Data Description
        description = describe_data(df)
        print("Data Description:")
        print(description)
    
    if "analyze" in functions:
        # Value Analysis
        results = analyze_data(conn, value_names)
        for value_name, result in results.items():
            print(f"\nValue Analysis for {value_name}:")
            print(result)
    
    if "regression" in functions:
        # Linear Regression Analysis
        regression_result = linear_regression(df, dependent_var, independent_vars)
        print("\nLinear Regression Analysis:")
        print(regression_result)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Read, parse, and analyze a Parquet file.")
    parser.add_argument("file_path", type=str, help="Path to the Parquet file.")
    parser.add_argument("--value_names", type=str, nargs='+', required=True, help="The names of the values we are interested in.")
    parser.add_argument("--dependent_var", type=str, required=True, help="The dependent variable for regression analysis.")
    parser.add_argument("--independent_vars", type=str, nargs='+', required=True, help="The independent variables for regression analysis.")
    parser.add_argument("--functions", type=str, nargs='+', choices=["description", "analyze", "regression"], required=True, help="The functions to perform: description, analyze, regression.")
    
    args = parser.parse_args()
    
    main(args.file_path, args.value_names, args.dependent_var, args.independent_vars, args.functions)
