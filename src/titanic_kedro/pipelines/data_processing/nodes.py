"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""
from typing import Any, Dict, Tuple
import pandas as pd

def get_data(parameters: Dict[str, Any]) -> pd.DataFrame:
    """Downloads data from url.
    Args:
        url: Url to download data from.
    Returns: dataframe containing data.
    """
    return pd.read_csv(parameters['url'])


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
        frac=parameters['split']["train_fraction"], random_state=parameters['split']["random_state"]
    )
    data_test = data.drop(data_train.index)
    return data_train, data_test

def drop_cols(data: pd.DataFrame, parameters: Dict[str, Any]) -> pd.DataFrame:
    """Drops columns from a list.
    Args:
        data: Data frame containing features and target.
        parameters: Dict Parameters defined in conf/base/parameters/data_processing.yml

    Returns:
        Dataframe with dropped columns.
    """

    return data.drop(parameters['cols_to_drop'],axis=1)    

def drop_rows_with_nan(data: pd.DataFrame) -> pd.DataFrame:
    """Drops rows with NaN values.

    Args:
        data: Data containing features and target.
    Returns:
        Data without rows with NaN values.
    """

    return data.dropna(axis=0))    