import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Loading dataset...")

data = pd.read_parquet("dataset/cicids2017.csv")

# clean dataset
data.replace([np.inf, -np.inf], np.nan, inplace=True)
data.dropna(inplace=True)

# select features
features = [
'Flow Duration',
'Total Fwd Packets',
'Total Backward Packets',
'Flow Bytes/s',
'Flow Packets/s',
'Packet Length Mean',
'Packet Length Std'
]

X = data[features]
y = data['Label']

print("Training AI model...")

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "attack_type_model.pkl")

print("Model trained successfully")