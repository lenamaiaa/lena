import pandas as pd
from sklearn.model_selection import train_test_split




dict = {
     'x': [i for i in range(-1000, 1000)],
     'y': [i for i in range(-1000, 1000)],
}



df = pd.DataFrame(dict)
df['output'] = df['x'] > 50
df['output'] = df['output'].astype(int)

input = df[['x', 'y']]
output = df['output']

train, test = train_test_split(df, test_size=0.2, shuffle=True)
train_df = pd.DataFrame(train)
test_df = pd.DataFrame(test)
print(train_df.head)
print(test_df.head)
