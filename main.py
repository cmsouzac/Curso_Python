import pandas as pd

data = {
    'CAT': ['A', 'A', 'B', 'B', 'B'],
    'QTD': [2, 5, 20, 10, 5],
    'VL': [5, 10, 2, 1, 4]
}

df = pd.DataFrame(data)
print(df)