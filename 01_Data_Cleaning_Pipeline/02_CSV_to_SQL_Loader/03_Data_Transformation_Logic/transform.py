import pandas as pd

def apply_transformation(df):
    """
    Data ko process karne ka basic logic:
    1. Agar salary column hai, toh bonus calculate karein.
    2. Data ko sort karein.
    """
    if 'salary' in df.columns:
        # 10% bonus add karna
        df['salary_with_bonus'] = df['salary'] * 1.10
    
    # Data ko sort karna
    df = df.sort_values(by='salary', ascending=False)
    
    return df

print("Transformation logic is defined successfully.")
