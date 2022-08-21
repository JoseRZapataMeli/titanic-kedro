"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import drop_rows_with_nan, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["titanic", "parameters"],
                outputs=["Data_train", "Data_test"],
                name="split",
            ),
            node(
                func=drop_rows_with_nan,
                inputs=["Data_train", "parameters"],
                outputs="Data_train_no_nan"
                
            ),
            node(
                func=drop_rows_with_nan,
                inputs=["Data_test", "parameters"],
                outputs="Data_test_no_nan"
                
            )
        ]
    )