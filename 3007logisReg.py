import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

#1
"""
1. Binary
2. Multiclass
3. Binary
4. Binary
5. Multiclass

"""

#2
""" 
0.91 - class 1 
0.72 - class 1
0.49 - class 0
0.21 - class 0
0.50 - class 1

"""

#3
""" 
Class 1 - 2,5,0
Class 0 - -2,-5
due to-
P = \frac{1}{1 + e^{-z}}

"""

#4
""" 
Dataset: Age BP Cholesterol Heart Disease
Features: Age BP Cholesterol 
Target: Heart DIsease
Binary

"""

#5
""" df=pd.read_csv('heartdis.csv')
df=df.dropna()
X=df.drop('target',axis=1)
y=df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=100000)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(f"accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print(f"precision: {precision_score(y_test, y_pred)*100:.2f}%")

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
model=LogisticRegression(max_iter=100000)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(f"accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print(f"precision: {precision_score(y_test, y_pred)*100:.2f}%")

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=42)
model=LogisticRegression(max_iter=100000)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(f"accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print(f"precision: {precision_score(y_test, y_pred)*100:.2f}%") """

#6
""" 
o.5 :
class 1 - 0.91, 0.83, 0.71, 0.65, 0.52 
class 0 - 0.47, 0.31

0.7:
class 1 - 0.91, 0.83, 0.71
class 0 - 0.65, 0.52, 0.47, 0.31

0.65 and 0.52 changed classes

"""

#7
""" df = pd.read_csv("heartdis.csv").dropna()
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LogisticRegression(max_iter=100000)
model.fit(X_train, y_train)
probabilities = model.predict_proba(X_test)

prob_df = pd.DataFrame(
    {
        "Prob_No_Disease (Class 0)": probabilities[:20, 0],
        "Prob_Disease (Class 1)": probabilities[:20, 1],
        "Predicted_Class": (probabilities[:20, 1] >= 0.5).astype(int),
    }
)

pd.set_option("display.float_format", lambda x: f"{x * 100:.2f}%")
print(prob_df) """

#8
""" df = pd.read_csv('heartdis.csv')
df = df.dropna()
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=98)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print("True Negatives (TN):", tn)
print("False Positives (FP):", fp)
print("False Negatives (FN):", fn)
print("True Positives (TP):", tp)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Disease (0)', 'Disease (1)'],
            yticklabels=['No Disease (0)', 'Disease (1)']
)

plt.title('Confusion Matrix - Heart Disease Prediction')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.tight_layout()
plt.show() """

#9
""" url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
    "Outcome",
]

df = pd.read_csv(url, names=columns)
print("--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Target Class Distribution ---")
print(df["Outcome"].value_counts(normalize=True))

print("\n--- Standard Null Values ---")
print(df.isnull().sum())

zero_counts = (df[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]] == 0).sum()
print("\n--- Biological Missing Values (Zeros as missing data) ---")
print(zero_counts)

zero_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for col in zero_cols:
    df[col] = df[col].replace(0, df[col].median())

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n--- Model Performance ---")
print(f"Accuracy : {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall   : {recall * 100:.2f}%")
print(f"F1 Score : {f1 * 100:.2f}%")

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4.5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Diabetes (0)", "Diabetes (1)"],
    yticklabels=["No Diabetes (0)", "Diabetes (1)"],
)
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()
plt.show() """