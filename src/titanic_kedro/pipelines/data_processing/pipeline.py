"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (drop_cols, 
                    drop_rows_with_nan, 
                    split_data, 
                    get_data, 
                    drop_cols
  )


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [   
            node(
                func=get_data,
                inputs="parameters",
                outputs="Data_raw",
                name="get_data_raw",
            ),
            node(
                func=split_data,
                inputs=["titanic", "parameters"],
                outputs=["Data_train", "Data_test"],
                name="split",
            ),
            node(
                func=drop_cols,
                inputs=["Data_train", "parameters"],
                outputs="Data_train_drop_cols",
                name="drop_cols_node",
            ),
            node(
                func=drop_rows_with_nan,
                inputs=["Data_train", "parameters"],
                outputs="Data_train_no_nan"
                
            )
        ],
        tags=['dp_tag'],
    )