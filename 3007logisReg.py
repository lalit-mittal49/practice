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
df=pd.read_csv('heartdis.csv')
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
print(f"precision: {precision_score(y_test, y_pred)*100:.2f}%")

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