# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .node_parser import NodeParser


class HierarchicalNodeParser(pydantic.BaseModel):
    """
    Hierarchical node parser.

    Splits a document into a recursive hierarchy Nodes using a NodeParser.

    NOTE: this will return a hierarchy of nodes in a flat list, where there will be
    overlap between parent nodes (e.g. with a bigger chunk size), and child nodes
    per parent (e.g. with a smaller chunk size).

    For instance, this may return a list of nodes like:
    - list of top-level nodes with chunk size 2048
    - list of second-level nodes, where each node is a child of a top-level node,
        chunk size 512
    - list of third-level nodes, where each node is a child of a second-level node,
        chunk size 128
    """

    include_metadata: typing.Optional[bool] = pydantic.Field(
        description="Whether or not to consider metadata when splitting."
    )
    include_prev_next_rel: typing.Optional[bool] = pydantic.Field(
        description="Include prev/next node relationships."
    )
    callback_manager: typing.Optional[typing.Dict[str, typing.Any]]
    chunk_sizes: typing.Optional[typing.List[int]] = pydantic.Field(
        description="The chunk sizes to use when splitting documents, in order of level."
    )
    node_parser_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        description="List of ids for the node parsers to use when splitting documents, in order of level (first id used for first level, etc.)."
    )
    node_parser_map: typing.Dict[str, NodeParser] = pydantic.Field(
        description="Map of node parser id to node parser."
    )
    class_name: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
