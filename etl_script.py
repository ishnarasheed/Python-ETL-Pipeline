import pandas as pd

def run_etl():
    # 1. Extract: Sample data loaded
    try:
        df = pd.read_csv('data.csv')
        print("Data Extracted Successfully!")
        
        # 2. Transform: Cleaning
        # Column names ko lower-case karna
        df.columns = [c.lower().strip() for c in df.columns]
        # Missing values ko 0 se fill karna
        df.fillna(0, inplace=True)
        print("Data Transformed Successfully!")
        
        # 3. Load: Result save karna
        df.to_csv('cleaned_data.csv', index=False)
        print("Data Loaded to cleaned_data.csv!")
        
    except FileNotFoundError:
        print("Error: data.csv file not found.")

if __name__ == "__main__":
    run_etl()
