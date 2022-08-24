"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.2
"""
import logging
import pandas as pd
from typing import Any, Dict
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

def impute_age_test(data:pd.DataFrame, title_ages: Dict[str, Any])-> pd.DataFrame:
    """
    Impute the age of the test data.
    """
    data = data.dropna(how='all')
    data['title'] = data['name'].str.extract('([A-Za-z]+)\\.', expand=True)

    mapping = {'Mlle': 'Miss', 'Major': 'Mr', 'Col': 'Mr', 'Sir': 'Mr',
               'Don': 'Mr', 'Mme': 'Mrs', 'Jonkheer': 'Mr', 'Lady': 'Mrs',
               'Capt': 'Mr', 'Countess': 'Mrs', 'Ms': 'Miss', 'Dona': 'Mrs'}

    data.replace({'title': mapping}, inplace=True)

    # crear columna con el promedio de las edades por titulo
    data['age_med'] = data['title'].apply(lambda x: title_ages[x])

    # realizar imputacion de las edades faltantes
    data['age'].fillna(data['age_med'], inplace=True)
    del data['age_med']
    return data
