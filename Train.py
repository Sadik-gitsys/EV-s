
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

df = pd.read_csv('ElectricCarData_Clean.csv')
df = df.replace('-', pd.NA)
X = df.drop(['PriceEuro','Brand','Model'], axis = 1)
y = df['PriceEuro']

numerical_col = [
    'AccelSec',
    'TopSpeed_KmH',
    'Range_Km',
    'Efficiency_WhKm',
    'FastCharge_KmH',
    'Seats'
]

categorical_col = [
    'RapidCharge',
    'PowerTrain',
    'PlugType',
    'BodyStyle',
    'Segment'
]

processor = ColumnTransformer([
    ('number', StandardScaler(), numerical_col),
    ('category', OneHotEncoder(),categorical_col)
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state =42)

X_train =processor.fit_transform(X_train)
X_test = processor.transform(X_test)

le = LinearRegression()
model = le.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print("R2 Score:", round(r2*100,2) ,"%")


joblib.dump(model, 'model.pkl')

joblib.dump(processor, 'processor.pkl')

print("Model saved successfully!")