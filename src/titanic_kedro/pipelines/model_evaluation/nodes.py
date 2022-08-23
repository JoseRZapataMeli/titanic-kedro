"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.2
"""
import logging
import pandas as pd
from sklearn.metrics import accuracy_score
import mlflow

def evaluate_model(predictions: pd.Series, test_labels: pd.Series,name:str):
    """
    Evaluate the model by calculating the accuracy score.
    """
    score = accuracy_score(test_labels['survived'].values, predictions.values)
    logger = logging.getLogger(__name__)
    logger.info(f"Model accuracy {name}= {score}")
    mlflow.set_experiment('titanic')
    mlflow.log_metric(f"accuracy {name}", score)
    mlflow.set_tag("Model Version", 0)
    # parse the score to a string with only 4 decimal places
    return f"{score:.4f}"