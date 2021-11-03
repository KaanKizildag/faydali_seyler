from typing_extensions import Protocol
import pandas as pd

veriler = pd.read_csv('kdd_analiz.csv')

labels = veriler.columns.tolist()

labels.remove('protocol_type')

veriler.drop(
    columns=labels,
    inplace=True
)

protocol_type = veriler['protocol_type'].values

# one hot encoding yapmak için kullanışlı bir yol
veriler = pd.get_dummies(
    data = protocol_type,
    #prefix='protocol_type'
)

print(veriler)
