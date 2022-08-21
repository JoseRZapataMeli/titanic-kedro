"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.2
"""

from kedro.pipeline import Pipeline, node, pipeline

from titanic_kedro.pipelines.data_science.nodes import predict


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = predict,
                inputs = "Data_train_no_nan",
                outputs = "predictions_train",
                name = "predict_train"
            ),
            node(
                func = predict,
                inputs = "Data_test_no_nan",
                outputs = "predictions_test",
                name = "predict_test"
            )
        ],
        tags=['ds_tag'],
    
    )
