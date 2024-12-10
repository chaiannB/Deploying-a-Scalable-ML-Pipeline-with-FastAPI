import pytest
import os
import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import load_model, inference, compute_model_metrics, train_model
# TODO: add necessary import


data = pd.read_csv("data/census.csv")

train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country"
]

X_train, y_train, encoder, lb = process_data(train, categorical_features=cat_features, label="salary", training=True)

file_dir ="Deploying-a-Sclable-ML-Pipeline-with-FastAPI"

# TODO: implement the first test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # this test makes sure that the metrics are within the right range 0-1
    """
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    metrics = compute_model_metrics(y_train, preds)
    for answer in metrics:
        assert -0.1 < answer <= 1


# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    # This test ensures that the predictions are being made in the right amount
    """
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    assert len(preds) == len(X_train)
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_load_model():
    """
    # This test ensures that the model is being loaded correctly using the load_model function
    """
    path = 'model/model.pkl'
    model = load_model(path)
    assert type(model) == sklearn.ensemble._forest.RandomForestClassifier


if __name__ == "__main__":
    test_compute_model_metrics()
    test_inference()
    test_load_model()
