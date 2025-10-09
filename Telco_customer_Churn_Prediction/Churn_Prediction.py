import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, f1_score
from xgboost import XGBClassifier



telco_df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
telco_df['TotalCharges'] = pd.to_numeric(telco_df['TotalCharges'], errors='coerce')
telco_df['Churn'] = telco_df['Churn'].map({'No':0, 'Yes':1})


y = telco_df["Churn"]
x = telco_df.drop("Churn", axis=1)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=1, stratify=y)

numerical_cols = x_train.select_dtypes(include=["number"]).columns
categorical_cols = x_train.select_dtypes(include=['object','category']).columns

#Preprocessing Steps
numerical_transformer = SimpleImputer(strategy='mean')

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numerical_transformer, numerical_cols),
    ('cat', categorical_transformer, categorical_cols)
])


#Model
XGB_Model = XGBClassifier(
                n_estimators=800,
                learning_rate=0.01,
                max_depth=3,
                min_child_weight=5,
                gamma=0,
                subsample=0.7,
                colsample_bytree=1.0,
                eval_metric='logloss',
                random_state=42    
            )

#Pipeline
my_pipeline = Pipeline(steps=[
                ('preprocessor', preprocessor),
                ('model',XGB_Model)
            ])
my_pipeline.fit(x_train,y_train,)

#Evaluation

preds = my_pipeline.predict(x_test)
print("Accuracy:", accuracy_score(y_test, preds))
print("F1 Score:", f1_score(y_test, preds))

#cross validation (K-fold)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)

cv_scores = cross_val_score(
    my_pipeline, x_train, y_train,
    cv=cv, scoring='accuracy'
)

print("CV Accuracy Scores:", cv_scores)
print("Mean CV Accuracy:", cv_scores.mean())

y_probs = my_pipeline.predict_proba(x_test)[:, 1]
thresholds = np.arange(0.1, 0.9, 0.05)
best_f1, best_thresh = 0, 0
for t in thresholds:
    preds = (y_probs > t).astype(int)
    f1 = f1_score(y_test, preds)
    if f1 > best_f1:
        best_f1, best_thresh = f1, t
print("Best threshold:", best_thresh, "Best F1:", best_f1)

