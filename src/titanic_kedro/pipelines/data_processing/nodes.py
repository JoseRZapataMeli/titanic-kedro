"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""
import logging
from typing import Any, Dict, Tuple
import pandas as pd

logger = logging.getLogger(__name__)


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
    data = data.drop(columns=parameters['cols_to_drop'], axis=1)
    logger.info(f"Shape = {data.shape} after dropping columns")
    return data


def drop_rows_with_nan(data: pd.DataFrame) -> pd.DataFrame:
    """Drops rows with NaN values.

    Args:
        data: Data containing features and target.
    Returns:
        Data without rows with NaN values.
    """
    data = data.dropna(axis=0)
    logger.info(f"Shape = {data.shape} after dropping nan rows")
    return data


def impute_age(data: pd.DataFrame) -> pd.DataFrame:
    """Imputes age columns based on People title

    Args:
        data: Data frame containing features and target.
    Returns:
        Data without rows with NaN values in age Colum.
    """
    data = data.dropna(how='all')
    data['title'] = data['name'].str.extract('([A-Za-z]+)\\.', expand=True)

    mapping = {'Mlle': 'Miss', 'Major': 'Mr', 'Col': 'Mr', 'Sir': 'Mr',
               'Don': 'Mr', 'Mme': 'Mrs', 'Jonkheer': 'Mr', 'Lady': 'Mrs',
               'Capt': 'Mr', 'Countess': 'Mrs', 'Ms': 'Miss', 'Dona': 'Mrs'}

    data.replace({'title': mapping}, inplace=True)

    # imputation
    title_ages = dict(data.groupby('title')['age'].median())

    # crear columna con el promedio de las edades por titulo
    data['age_med'] = data['title'].apply(lambda x: title_ages[x])

    # realizar imputacion de las edades faltantes
    data['age'].fillna(data['age_med'], inplace=True)
    del data['age_med']
    logger.info(f"Shape = {data.shape} after impute age")
    return data, title_ages
