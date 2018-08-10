from decimal import Decimal
from typing import Any, List, Optional, Tuple, Union

from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.expressions import Combinable, Expression, Func
from django.db.models.fields import Field
from django.db.models.query_utils import Q
from django.db.models.sql.compiler import SQLCompiler
from django.db.models.sql.query import Query
from django.db.models.sql.where import WhereNode


class Aggregate(Func):
    contains_aggregate: bool = ...
    name: Any = ...
    filter_template: str = ...
    window_compatible: bool = ...
    filter: Any = ...
    def __init__(
        self, *args: Any, filter: Optional[Any] = ..., **kwargs: Any
    ) -> None: ...
    def get_source_fields(self) -> Union[List[None], List[Field]]: ...
    def get_source_expressions(self) -> List[Union[Combinable, WhereNode]]: ...
    def set_source_expressions(
        self, exprs: List[Union[Expression, WhereNode]]
    ) -> None: ...
    def resolve_expression(
        self,
        query: Query = ...,
        allow_joins: bool = ...,
        reuse: None = ...,
        summarize: bool = ...,
        for_save: bool = ...,
    ) -> Aggregate: ...
    @property
    def default_alias(self) -> str: ...
    def get_group_by_cols(self) -> List[Any]: ...
    def as_sql(
        self,
        compiler: SQLCompiler,
        connection: DatabaseWrapper,
        **extra_context: Any
    ) -> Tuple[
        str, Union[List[Union[int, str]], List[Decimal], List[float]]
    ]: ...

class Avg(Aggregate):
    filter: None
    function: str = ...
    name: str = ...
    def as_mysql(self, compiler: Any, connection: Any): ...
    def as_oracle(self, compiler: Any, connection: Any): ...

class Count(Aggregate):
    filter: None
    function: str = ...
    name: str = ...
    template: str = ...
    output_field: Any = ...
    def __init__(
        self,
        expression: str,
        distinct: bool = ...,
        filter: Optional[Q] = ...,
        **extra: Any
    ) -> None: ...
    def convert_value(
        self,
        value: Optional[int],
        expression: Count,
        connection: DatabaseWrapper,
    ) -> int: ...

class Max(Aggregate):
    filter: None
    function: str = ...
    name: str = ...

class Min(Aggregate):
    filter: None
    function: str = ...
    name: str = ...

class StdDev(Aggregate):
    filter: None
    name: str = ...
    output_field: Any = ...
    function: str = ...
    def __init__(
        self, expression: str, sample: bool = ..., **extra: Any
    ) -> None: ...

class Sum(Aggregate):
    filter: None
    function: str = ...
    name: str = ...
    def as_mysql(self, compiler: Any, connection: Any): ...
    def as_oracle(self, compiler: Any, connection: Any): ...

class Variance(Aggregate):
    filter: None
    name: str = ...
    output_field: Any = ...
    function: str = ...
    def __init__(
        self, expression: str, sample: bool = ..., **extra: Any
    ) -> None: ...
