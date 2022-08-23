"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.2
"""
import logging
import pandas as pd
import mlflow

def train_model(classifier_fn, X_train: pd.DataFrame, y_train: pd.Series):
    """Trains the linear regression model.
    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.
    Returns:
        Trained model.
    """
    # heuristic model dont need to be trained
    pass
    return

def predict(test_df: pd.DataFrame, name:str) -> pd.Series:
    """ predictions for dataframe"""
    mlflow.set_experiment('titanic')
    mlflow.set_tag("Model Version", 0)
    mlflow.log_param(f"columns {name}",test_df.columns)
    mlflow.log_param(f"shape {name}",test_df.shape)

    test_df['pred'] = 0
    test_df.loc[(test_df['sex']=='female') & (test_df['pclass']<3), 'pred'] = 1
    test_df.loc[(test_df['age']<=5), 'pred'] = 1
    test_df.loc[(test_df['age']>=10) & (test_df['age']<=15), 'pred'] = 1
    
    logger = logging.getLogger(__name__)
    logger.info(f"test_df type {type(test_df['pred'])} ")

    return test_df['pred']