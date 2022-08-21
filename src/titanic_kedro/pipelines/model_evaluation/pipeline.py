"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import evaluate_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=evaluate_model,
                inputs=["predictions_train", "Data_train_no_nan"],
                outputs="train_score",
                name="train_model_evaluation"
            ),
            node(
                func=evaluate_model,
                inputs=["predictions_test", "Data_test_no_nan"],
                outputs="test_score",
                name="test_model_evaluation"
            )            
        ],
        tags=['me_tag'],
    )