# This file was auto-generated by Fern from our API Definition.

import typing

from .eval_dataset_execution_config import EvalDatasetExecutionConfig
from .run_transform_asset_config import RunTransformAssetConfig

EvalDatasetExecutionRunConfigPerOpValue = typing.Union[
    RunTransformAssetConfig, EvalDatasetExecutionConfig
]
