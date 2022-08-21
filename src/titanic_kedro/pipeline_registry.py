"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline
from titanic_kedro.pipelines import (
    data_processing as dp,
    data_science as ds,
    model_evaluation as me
)



def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    model_evaluation_pipeline = me.create_pipeline()

    return {
            "dp": data_processing_pipeline,
            "ds": data_science_pipeline,
            "me": model_evaluation_pipeline,
            "__default__": data_processing_pipeline + data_science_pipeline + model_evaluation_pipeline
            }
