import pandas as pd

def clean_data(input_file):
    # Load dataset
    df = pd.read_csv(input_file)
    
    # Remove null values
    df_cleaned = df.dropna()
    
    # Normalize column names
    df_cleaned.columns = [c.lower().replace(" ", "_") for c in df_cleaned.columns]
    
    return df_cleaned

print("Data cleaning logic is ready.")
