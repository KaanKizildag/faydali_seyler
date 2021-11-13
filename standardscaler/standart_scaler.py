from sklearn.preprocessing import StandardScaler
import numpy as np

standard_scaler = StandardScaler()

data = np.array([
    [1,34,253],
    [3,523,352],
    [2,75,75]
])

standard_scaler.fit(data)

res = standard_scaler.transform(data)

print('verilerin ilk hali:\n', data)
print('ölçeklenmiş hali\n', res)



