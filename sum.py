import pandas as pd
import sys

def calculate_sum(filename):
    df = pd.read_csv(filename)
    return df

if __name__ == "__main__":
    
    filename = sys.argv[1]

    df = calculate_sum(filename)
    
    cols = df.columns
    
    for col in cols:
        sum = df[col].sum()
        print(f'col={col} sum={sum}')



