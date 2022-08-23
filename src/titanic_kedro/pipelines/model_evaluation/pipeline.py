"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import evaluate_model
from ..data_processing.nodes import drop_cols, drop_rows_with_nan

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=evaluate_model,
                inputs=["predictions_train", "Data_train_no_nan",'params:train'],
                outputs="score_train",
                name="train_model_evaluation"
            ),
            node(
                func=drop_cols,
                inputs=["Data_test", "parameters"],
                outputs="Data_test_drop_cols",
                name="drop_cols-test",
            ),
            node(
                func=drop_rows_with_nan,
                inputs="Data_test_drop_cols",
                outputs="Data_test_no_nan",
                name="drop_rows_no_nan-test",
            ),
            node(
                func=evaluate_model,
                inputs=["predictions_test", "Data_test_no_nan",'params:test'],
                outputs="score_test",
                name="test_model_evaluation"
            )            
        ],
        tags=['me_tag'],
    )