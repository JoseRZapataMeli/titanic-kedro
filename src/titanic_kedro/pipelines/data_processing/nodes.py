"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""
from typing import Any, Dict, Tuple
import pandas as pd



def split_data(
    data: pd.DataFrame, parameters: Dict[str, Any]
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Splits data into training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters.yml.
    Returns:
        Split data.
    """

    data_train = data.sample(
        frac=parameters["train_fraction"], random_state=parameters["random_state"]
    )
    data_test = data.drop(data_train.index)
    return data_train, data_test