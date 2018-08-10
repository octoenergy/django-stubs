from datetime import date, datetime, time, timedelta
from decimal import Decimal
from itertools import chain
from typing import (Any, Callable, Dict, Iterator, List, Optional, Set, Tuple,
                    Type, Union)
from unittest.mock import MagicMock
from uuid import UUID

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.base import Model, ModelState
from django.db.models.expressions import Col, Expression
from django.db.models.fields import Field
from django.db.models.fields.mixins import FieldCacheMixin
from django.db.models.fields.related import (ForeignKey, ForeignObject,
                                             OneToOneField)
from django.db.models.fields.related_descriptors import (ForwardManyToOneDescriptor,
                                                         ReverseOneToOneDescriptor)
from django.db.models.fields.reverse_related import ManyToOneRel
from django.db.models.functions.comparison import Greatest
from django.db.models.functions.text import Right
from django.db.models.query_utils import Q
from django.db.models.sql.query import Query, RawQuery

REPR_OUTPUT_SIZE: int
EmptyResultSet: Any

class BaseIterable:
    queryset: Any = ...
    chunked_fetch: Any = ...
    chunk_size: Any = ...
    def __init__(
        self,
        queryset: QuerySet,
        chunked_fetch: bool = ...,
        chunk_size: int = ...,
    ) -> None: ...

class ModelIterable(BaseIterable):
    chunk_size: int
    chunked_fetch: bool
    queryset: django.db.models.query.QuerySet
    def __iter__(self) -> Iterator[Model]: ...

class ValuesIterable(BaseIterable):
    chunk_size: int
    chunked_fetch: bool
    queryset: django.db.models.query.QuerySet
    def __iter__(
        self
    ) -> Iterator[
        Union[
            Dict[str, Optional[Union[int, str]]],
            Dict[str, Union[date, Decimal, float, int, str]],
        ]
    ]: ...

class ValuesListIterable(BaseIterable):
    chunk_size: int
    chunked_fetch: bool
    queryset: django.db.models.query.QuerySet
    def __iter__(self) -> Union[chain, map]: ...

class NamedValuesListIterable(ValuesListIterable):
    chunk_size: int
    chunked_fetch: bool
    queryset: django.db.models.query.QuerySet
    @staticmethod
    def create_namedtuple_class(*names: Any) -> Any: ...
    def __iter__(self) -> Any: ...

class FlatValuesListIterable(BaseIterable):
    chunk_size: int
    chunked_fetch: bool
    queryset: django.db.models.query.QuerySet
    def __iter__(
        self
    ) -> Iterator[Optional[Union[date, Decimal, float, int, str, UUID]]]: ...

class QuerySet:
    model: Optional[Type[django.db.models.base.Model]] = ...
    query: django.db.models.sql.query.Query = ...
    def __init__(
        self,
        model: Optional[Type[Model]] = ...,
        query: Optional[Query] = ...,
        using: Optional[str] = ...,
        hints: Optional[Dict[str, Model]] = ...,
    ) -> None: ...
    def as_manager(cls): ...
    as_manager: Any = ...
    def __deepcopy__(
        self,
        memo: Dict[
            int,
            Union[
                Dict[str, Union[ModelState, int, str]],
                List[Union[Dict[str, Union[bool, str]], ModelState]],
                Model,
                ModelState,
            ],
        ],
    ) -> QuerySet: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Any: ...
    def __bool__(self) -> bool: ...
    def __getitem__(
        self, k: Union[int, slice, str]
    ) -> Optional[
        Union[
            Dict[str, Optional[Union[int, str]]],
            Dict[str, Union[datetime, int, str]],
            Dict[str, Union[Decimal, int]],
            Dict[str, Union[float, str]],
            List[Dict[str, Optional[Union[int, str]]]],
            List[Dict[str, Union[datetime, int, str]]],
            List[Dict[str, Union[Decimal, int]]],
            List[Optional[str]],
            List[Tuple[Union[int, str]]],
            List[date],
            List[Model],
            List[int],
            List[UUID],
            Tuple[Union[int, str]],
            date,
            Decimal,
            Model,
            QuerySet,
            int,
            str,
            UUID,
        ]
    ]: ...
    def __and__(self, other: QuerySet) -> QuerySet: ...
    def __or__(self, other: QuerySet) -> QuerySet: ...
    def iterator(self, chunk_size: int = ...) -> Iterator[Any]: ...
    def aggregate(
        self, *args: Any, **kwargs: Any
    ) -> Union[
        Dict[str, Optional[int]],
        Dict[str, Union[date, time]],
        Dict[str, Union[Decimal, float, int]],
        Dict[str, timedelta],
    ]: ...
    def count(self) -> int: ...
    def get(
        self, *args: Any, **kwargs: Any
    ) -> Union[
        Dict[str, Union[date, Decimal, float, int, str]],
        Tuple[Decimal],
        Tuple[str, int, int],
        Model,
        str,
    ]: ...
    def create(self, **kwargs: Any) -> Model: ...
    def bulk_create(
        self,
        objs: Union[Iterator[Any], List[Model]],
        batch_size: Optional[int] = ...,
    ) -> List[Model]: ...
    def get_or_create(
        self,
        defaults: Optional[
            Union[
                Dict[str, Union[Callable, str]],
                Dict[str, Union[date, str]],
                Dict[str, Model],
            ]
        ] = ...,
        **kwargs: Any
    ) -> Tuple[Model, bool]: ...
    def update_or_create(
        self,
        defaults: Optional[
            Union[
                Dict[str, Callable],
                Dict[str, Union[date, str]],
                Dict[str, Model],
            ]
        ] = ...,
        **kwargs: Any
    ) -> Tuple[Model, bool]: ...
    def earliest(
        self, *fields: Any, field_name: Optional[Any] = ...
    ) -> Model: ...
    def latest(
        self, *fields: Any, field_name: Optional[Any] = ...
    ) -> Model: ...
    def first(self) -> Optional[Union[Dict[str, int], Model]]: ...
    def last(self) -> Optional[Model]: ...
    def in_bulk(
        self,
        id_list: Optional[
            Union[
                Dict[int, Model],
                List[Model],
                List[int],
                List[str],
                Set[int],
                Tuple[int],
                frozenset,
            ]
        ] = ...,
        *,
        field_name: str = ...
    ) -> Union[Dict[int, Model], Dict[str, Model]]: ...
    def delete(self) -> Tuple[int, Dict[str, int]]: ...
    def update(self, **kwargs: Any) -> int: ...
    def exists(self) -> bool: ...
    def explain(
        self, *, format: Optional[Any] = ..., **options: Any
    ) -> str: ...
    def raw(
        self,
        raw_query: str,
        params: Optional[
            Union[
                Dict[str, str],
                List[datetime],
                List[Decimal],
                List[str],
                Set[str],
                Tuple[int],
            ]
        ] = ...,
        translations: Optional[Dict[str, str]] = ...,
        using: None = ...,
    ) -> RawQuerySet: ...
    def values(self, *fields: Any, **expressions: Any) -> QuerySet: ...
    def values_list(
        self, *fields: Any, flat: bool = ..., named: bool = ...
    ) -> QuerySet: ...
    def dates(
        self, field_name: str, kind: str, order: str = ...
    ) -> QuerySet: ...
    def datetimes(
        self, field_name: str, kind: str, order: str = ..., tzinfo: None = ...
    ) -> QuerySet: ...
    def none(self) -> QuerySet: ...
    def all(self) -> QuerySet: ...
    def filter(self, *args: Any, **kwargs: Any) -> QuerySet: ...
    def exclude(self, *args: Any, **kwargs: Any) -> QuerySet: ...
    def complex_filter(
        self,
        filter_obj: Union[
            Dict[str, Union[int, str]],
            Dict[str, datetime],
            Dict[str, QuerySet],
            Q,
            MagicMock,
        ],
    ) -> QuerySet: ...
    def union(self, *other_qs: Any, all: bool = ...) -> QuerySet: ...
    def intersection(self, *other_qs: Any) -> QuerySet: ...
    def difference(self, *other_qs: Any) -> QuerySet: ...
    def select_for_update(
        self, nowait: bool = ..., skip_locked: bool = ..., of: Tuple = ...
    ) -> QuerySet: ...
    def select_related(self, *fields: Any) -> QuerySet: ...
    def prefetch_related(self, *lookups: Any) -> QuerySet: ...
    def annotate(self, *args: Any, **kwargs: Any) -> QuerySet: ...
    def order_by(self, *field_names: Any) -> QuerySet: ...
    def distinct(self, *field_names: Any) -> QuerySet: ...
    def extra(
        self,
        select: Optional[Union[Dict[str, int], Dict[str, str]]] = ...,
        where: Optional[List[str]] = ...,
        params: Optional[Union[List[int], List[str]]] = ...,
        tables: Optional[List[str]] = ...,
        order_by: Optional[Union[List[str], Tuple[str]]] = ...,
        select_params: Optional[Union[List[int], List[str], Tuple[int]]] = ...,
    ) -> QuerySet: ...
    def reverse(self) -> QuerySet: ...
    def defer(self, *fields: Any) -> QuerySet: ...
    def only(self, *fields: Any) -> QuerySet: ...
    def using(self, alias: Optional[str]) -> QuerySet: ...
    @property
    def ordered(self) -> bool: ...
    @property
    def db(self) -> str: ...
    def resolve_expression(self, *args: Any, **kwargs: Any) -> Query: ...

class InstanceCheckMeta(type):
    def __instancecheck__(self, instance: Union[QuerySet, str]) -> bool: ...

class EmptyQuerySet:
    def __init__(self, *args: Any, **kwargs: Any) -> Any: ...

class RawQuerySet:
    columns: List[str]
    model_fields: Dict[str, django.db.models.fields.Field]
    raw_query: str = ...
    model: Optional[Type[django.db.models.base.Model]] = ...
    query: django.db.models.sql.query.RawQuery = ...
    params: Union[
        Dict[str, str],
        List[datetime.datetime],
        List[decimal.Decimal],
        List[str],
        Set[str],
        Tuple,
    ] = ...
    translations: Dict[str, str] = ...
    def __init__(
        self,
        raw_query: str,
        model: Optional[Type[Model]] = ...,
        query: Optional[RawQuery] = ...,
        params: Optional[
            Union[
                Dict[str, str],
                List[datetime],
                List[Decimal],
                List[str],
                Set[str],
                Tuple,
            ]
        ] = ...,
        translations: Optional[Dict[str, str]] = ...,
        using: Optional[str] = ...,
        hints: Optional[Dict[Any, Any]] = ...,
    ) -> None: ...
    def resolve_model_init_order(
        self
    ) -> Tuple[List[str], List[int], List[Tuple[str, int]]]: ...
    def prefetch_related(self, *lookups: Any) -> RawQuerySet: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __iter__(self) -> Any: ...
    def iterator(self) -> Iterator[Model]: ...
    def __getitem__(
        self, k: Union[int, slice, str]
    ) -> Union[List[Model], Model]: ...
    @property
    def db(self) -> str: ...
    def using(self, alias: Any): ...
    def columns(self) -> List[str]: ...
    def model_fields(self) -> Dict[str, Field]: ...

class Prefetch:
    prefetch_through: str = ...
    prefetch_to: str = ...
    queryset: Optional[django.db.models.query.QuerySet] = ...
    to_attr: Optional[str] = ...
    def __init__(
        self,
        lookup: str,
        queryset: Optional[QuerySet] = ...,
        to_attr: Optional[str] = ...,
    ) -> None: ...
    def add_prefix(self, prefix: str) -> None: ...
    def get_current_prefetch_to(self, level: int) -> str: ...
    def get_current_to_attr(self, level: int) -> Tuple[str, Optional[bool]]: ...
    def get_current_queryset(self, level: int) -> Optional[QuerySet]: ...
    def __eq__(self, other: None) -> bool: ...
    def __hash__(self) -> int: ...

def normalize_prefetch_lookups(
    lookups: reversed, prefix: None = ...
) -> List[Prefetch]: ...
def prefetch_related_objects(
    model_instances: Union[List[Model], List[UUID]], *related_lookups: Any
) -> None: ...
def get_prefetcher(
    instance: Model, through_attr: str, to_attr: str
) -> Union[
    Tuple[None, bool, bool, bool],
    Tuple[GenericForeignKey, GenericForeignKey, bool, bool],
    Tuple[ForwardManyToOneDescriptor, ForwardManyToOneDescriptor, bool, bool],
    Tuple[ReverseOneToOneDescriptor, ReverseOneToOneDescriptor, bool, bool],
]: ...
def prefetch_one_level(
    instances: List[Model],
    prefetcher: Union[
        GenericForeignKey, ForwardManyToOneDescriptor, ReverseOneToOneDescriptor
    ],
    lookup: Prefetch,
    level: int,
) -> Tuple[List[Model], List[Prefetch]]: ...

class RelatedPopulator:
    db: str = ...
    cols_start: int = ...
    cols_end: int = ...
    init_list: List[str] = ...
    reorder_for_init: Optional[operator.itemgetter] = ...
    model_cls: Type[django.db.models.base.Model] = ...
    pk_idx: int = ...
    related_populators: List[django.db.models.query.RelatedPopulator] = ...
    local_setter: Callable = ...
    remote_setter: Callable = ...
    def __init__(
        self,
        klass_info: Union[
            Dict[
                str,
                Union[
                    Callable,
                    List[
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[Any],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            ForeignKey,
                                        ],
                                    ]
                                ],
                                List[int],
                                Type[Model],
                                bool,
                                ForeignKey,
                            ],
                        ]
                    ],
                    List[int],
                    Type[Model],
                    bool,
                    ForeignKey,
                ],
            ],
            Dict[
                str,
                Union[
                    Callable,
                    List[
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[Any],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            OneToOneField,
                                        ],
                                    ]
                                ],
                                List[int],
                                Type[Model],
                                bool,
                                OneToOneField,
                            ],
                        ]
                    ],
                    List[int],
                    Type[Model],
                    bool,
                    ForeignKey,
                ],
            ],
            Dict[
                str,
                Union[
                    Callable,
                    List[
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[
                                                Dict[
                                                    str,
                                                    Union[
                                                        Callable,
                                                        List[Any],
                                                        List[int],
                                                        Type[Model],
                                                        bool,
                                                        ForeignKey,
                                                    ],
                                                ]
                                            ],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            ForeignKey,
                                        ],
                                    ]
                                ],
                                List[int],
                                Type[Model],
                                bool,
                                ForeignKey,
                            ],
                        ]
                    ],
                    List[int],
                    Type[Model],
                    bool,
                    ForeignKey,
                ],
            ],
            Dict[
                str,
                Union[
                    Callable,
                    List[
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[
                                                Dict[
                                                    str,
                                                    Union[
                                                        Callable,
                                                        List[
                                                            Dict[
                                                                str,
                                                                Union[
                                                                    Callable,
                                                                    List[Any],
                                                                    List[int],
                                                                    Type[Model],
                                                                    bool,
                                                                    ForeignKey,
                                                                ],
                                                            ]
                                                        ],
                                                        List[int],
                                                        Type[Model],
                                                        bool,
                                                        ForeignKey,
                                                    ],
                                                ]
                                            ],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            ForeignKey,
                                        ],
                                    ]
                                ],
                                List[int],
                                Type[Model],
                                bool,
                                ForeignKey,
                            ],
                        ]
                    ],
                    List[int],
                    Type[Model],
                    bool,
                    ForeignKey,
                ],
            ],
            Dict[
                str,
                Union[
                    Callable,
                    List[
                        Union[
                            Dict[
                                str,
                                Union[
                                    Callable,
                                    List[Any],
                                    List[int],
                                    Type[Model],
                                    bool,
                                    ForeignKey,
                                ],
                            ],
                            Dict[
                                str,
                                Union[
                                    Callable,
                                    List[Any],
                                    List[int],
                                    Type[Model],
                                    bool,
                                    OneToOneField,
                                ],
                            ],
                        ]
                    ],
                    List[int],
                    Type[Model],
                    bool,
                    FieldCacheMixin,
                ],
            ],
        ],
        select: List[Tuple[Expression, Tuple[str, List[int]], Optional[str]]],
        db: str,
    ) -> None: ...
    def populate(
        self,
        row: Union[
            List[Optional[Union[date, int, str]]],
            List[Union[date, Decimal, float, int, str]],
            List[Union[datetime, time, Decimal, int, str]],
            Tuple[int, None, None],
            Tuple[int, None, str, None, None, None],
            Tuple[int, Union[int, str], Union[int, str]],
            Tuple[int, int, None, None, None, None],
            Tuple[int, int, None, None, int, str, str, None, None, None],
            Tuple[
                int, str, None, None, None, None, None, None, None, None, None
            ],
            Tuple[int, str, None, None, int, int, int, str],
            Tuple[int, str, None, None, int, str, int, int, str, int, str],
            Tuple[int, str, None, int, None, None, None],
            Tuple[int, str, None, int, int, str],
            Tuple[int, str, None, int, str, int],
            Tuple[str, int, int, int, str, int],
        ],
        from_obj: Model,
    ) -> None: ...

def get_related_populators(
    klass_info: Union[
        Dict[
            str,
            Union[
                Callable,
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[Any],
                            List[int],
                            Type[Model],
                            bool,
                            ForeignObject,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
                bool,
                OneToOneField,
            ],
        ],
        Dict[
            str,
            Union[
                Callable,
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[
                                Dict[
                                    str,
                                    Union[
                                        Callable,
                                        List[Any],
                                        List[int],
                                        Type[Model],
                                        bool,
                                        ForeignKey,
                                    ],
                                ]
                            ],
                            List[int],
                            Type[Model],
                            bool,
                            ManyToOneRel,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
                bool,
                FieldCacheMixin,
            ],
        ],
        Dict[
            str,
            Union[
                Callable,
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[
                                Dict[
                                    str,
                                    Union[
                                        Callable,
                                        List[Any],
                                        List[int],
                                        Type[Model],
                                        bool,
                                        OneToOneField,
                                    ],
                                ]
                            ],
                            List[int],
                            Type[Model],
                            bool,
                            OneToOneField,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
                bool,
                ForeignKey,
            ],
        ],
        Dict[
            str,
            Union[
                Callable,
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[
                                Dict[
                                    str,
                                    Union[
                                        Callable,
                                        List[
                                            Dict[
                                                str,
                                                Union[
                                                    Callable,
                                                    List[
                                                        Dict[
                                                            str,
                                                            Union[
                                                                Callable,
                                                                List[
                                                                    Dict[
                                                                        str,
                                                                        Union[
                                                                            Callable,
                                                                            List[
                                                                                Any
                                                                            ],
                                                                            List[
                                                                                int
                                                                            ],
                                                                            Type[
                                                                                Model
                                                                            ],
                                                                            bool,
                                                                            ForeignKey,
                                                                        ],
                                                                    ]
                                                                ],
                                                                List[int],
                                                                Type[Model],
                                                                bool,
                                                                ForeignKey,
                                                            ],
                                                        ]
                                                    ],
                                                    List[int],
                                                    Type[Model],
                                                    bool,
                                                    ForeignKey,
                                                ],
                                            ]
                                        ],
                                        List[int],
                                        Type[Model],
                                        bool,
                                        ForeignKey,
                                    ],
                                ]
                            ],
                            List[int],
                            Type[Model],
                            bool,
                            ForeignKey,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
                bool,
                ForeignKey,
            ],
        ],
        Dict[
            str,
            Union[
                Callable,
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[
                                Dict[
                                    str,
                                    Union[
                                        Callable,
                                        List[
                                            Dict[
                                                str,
                                                Union[
                                                    Callable,
                                                    List[
                                                        Dict[
                                                            str,
                                                            Union[
                                                                Callable,
                                                                List[
                                                                    Dict[
                                                                        str,
                                                                        Union[
                                                                            Callable,
                                                                            List[
                                                                                Dict[
                                                                                    str,
                                                                                    Union[
                                                                                        Callable,
                                                                                        List[
                                                                                            Any
                                                                                        ],
                                                                                        List[
                                                                                            int
                                                                                        ],
                                                                                        Type[
                                                                                            Model
                                                                                        ],
                                                                                        bool,
                                                                                        ForeignKey,
                                                                                    ],
                                                                                ]
                                                                            ],
                                                                            List[
                                                                                int
                                                                            ],
                                                                            Type[
                                                                                Model
                                                                            ],
                                                                            bool,
                                                                            ForeignKey,
                                                                        ],
                                                                    ]
                                                                ],
                                                                List[int],
                                                                Type[Model],
                                                                bool,
                                                                ForeignKey,
                                                            ],
                                                        ]
                                                    ],
                                                    List[int],
                                                    Type[Model],
                                                    bool,
                                                    ForeignKey,
                                                ],
                                            ]
                                        ],
                                        List[int],
                                        Type[Model],
                                        bool,
                                        ForeignKey,
                                    ],
                                ]
                            ],
                            List[int],
                            Type[Model],
                            bool,
                            ForeignKey,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
                bool,
                ForeignKey,
            ],
        ],
        Dict[
            str,
            Union[
                Callable,
                List[
                    Union[
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[Any],
                                List[int],
                                Type[Model],
                                bool,
                                ForeignKey,
                            ],
                        ],
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[Any],
                                List[int],
                                Type[Model],
                                bool,
                                OneToOneField,
                            ],
                        ],
                    ]
                ],
                List[int],
                Type[Model],
                bool,
                OneToOneField,
            ],
        ],
        Dict[
            str,
            Union[
                Callable,
                List[
                    Union[
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[Any],
                                List[int],
                                Type[Model],
                                bool,
                                ForeignKey,
                            ],
                        ],
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[Any],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            ForeignKey,
                                        ],
                                    ]
                                ],
                                List[int],
                                Type[Model],
                                bool,
                                ForeignKey,
                            ],
                        ],
                    ]
                ],
                List[int],
                Type[Model],
                bool,
                FieldCacheMixin,
            ],
        ],
        Dict[
            str,
            Union[
                Callable,
                List[
                    Union[
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[
                                                Dict[
                                                    str,
                                                    Union[
                                                        Callable,
                                                        List[Any],
                                                        List[int],
                                                        Type[Model],
                                                        bool,
                                                        ForeignKey,
                                                    ],
                                                ]
                                            ],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            ForeignKey,
                                        ],
                                    ]
                                ],
                                List[int],
                                Type[Model],
                                bool,
                                ForeignKey,
                            ],
                        ],
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[
                                                Dict[
                                                    str,
                                                    Union[
                                                        Callable,
                                                        List[
                                                            Dict[
                                                                str,
                                                                Union[
                                                                    Callable,
                                                                    List[Any],
                                                                    List[int],
                                                                    Type[Model],
                                                                    bool,
                                                                    ForeignKey,
                                                                ],
                                                            ]
                                                        ],
                                                        List[int],
                                                        Type[Model],
                                                        bool,
                                                        ForeignKey,
                                                    ],
                                                ]
                                            ],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            ForeignKey,
                                        ],
                                    ]
                                ],
                                List[int],
                                Type[Model],
                                bool,
                                ForeignKey,
                            ],
                        ],
                    ]
                ],
                List[int],
                Type[Model],
                bool,
                ForeignKey,
            ],
        ],
        Dict[
            str,
            Union[
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[Any],
                            List[int],
                            Type[Model],
                            bool,
                            ManyToOneRel,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
            ],
        ],
        Dict[
            str,
            Union[
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[
                                Dict[
                                    str,
                                    Union[
                                        Callable,
                                        List[
                                            Dict[
                                                str,
                                                Union[
                                                    Callable,
                                                    List[Any],
                                                    List[int],
                                                    Type[Model],
                                                    bool,
                                                    ForeignKey,
                                                ],
                                            ]
                                        ],
                                        List[int],
                                        Type[Model],
                                        bool,
                                        ForeignKey,
                                    ],
                                ]
                            ],
                            List[int],
                            Type[Model],
                            bool,
                            OneToOneField,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
            ],
        ],
        Dict[
            str,
            Union[
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[
                                Dict[
                                    str,
                                    Union[
                                        Callable,
                                        List[
                                            Dict[
                                                str,
                                                Union[
                                                    Callable,
                                                    List[Any],
                                                    List[int],
                                                    Type[Model],
                                                    bool,
                                                    OneToOneField,
                                                ],
                                            ]
                                        ],
                                        List[int],
                                        Type[Model],
                                        bool,
                                        OneToOneField,
                                    ],
                                ]
                            ],
                            List[int],
                            Type[Model],
                            bool,
                            ForeignKey,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
            ],
        ],
        Dict[
            str,
            Union[
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[
                                Dict[
                                    str,
                                    Union[
                                        Callable,
                                        List[
                                            Dict[
                                                str,
                                                Union[
                                                    Callable,
                                                    List[
                                                        Dict[
                                                            str,
                                                            Union[
                                                                Callable,
                                                                List[
                                                                    Dict[
                                                                        str,
                                                                        Union[
                                                                            Callable,
                                                                            List[
                                                                                Dict[
                                                                                    str,
                                                                                    Union[
                                                                                        Callable,
                                                                                        List[
                                                                                            Dict[
                                                                                                str,
                                                                                                Union[
                                                                                                    Callable,
                                                                                                    List[
                                                                                                        Any
                                                                                                    ],
                                                                                                    List[
                                                                                                        int
                                                                                                    ],
                                                                                                    Type[
                                                                                                        Model
                                                                                                    ],
                                                                                                    bool,
                                                                                                    ForeignKey,
                                                                                                ],
                                                                                            ]
                                                                                        ],
                                                                                        List[
                                                                                            int
                                                                                        ],
                                                                                        Type[
                                                                                            Model
                                                                                        ],
                                                                                        bool,
                                                                                        ForeignKey,
                                                                                    ],
                                                                                ]
                                                                            ],
                                                                            List[
                                                                                int
                                                                            ],
                                                                            Type[
                                                                                Model
                                                                            ],
                                                                            bool,
                                                                            ForeignKey,
                                                                        ],
                                                                    ]
                                                                ],
                                                                List[int],
                                                                Type[Model],
                                                                bool,
                                                                ForeignKey,
                                                            ],
                                                        ]
                                                    ],
                                                    List[int],
                                                    Type[Model],
                                                    bool,
                                                    ForeignKey,
                                                ],
                                            ]
                                        ],
                                        List[int],
                                        Type[Model],
                                        bool,
                                        ForeignKey,
                                    ],
                                ]
                            ],
                            List[int],
                            Type[Model],
                            bool,
                            ForeignKey,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
            ],
        ],
        Dict[
            str,
            Union[
                List[
                    Dict[
                        str,
                        Union[
                            Callable,
                            List[
                                Union[
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[Any],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            ForeignKey,
                                        ],
                                    ],
                                    Dict[
                                        str,
                                        Union[
                                            Callable,
                                            List[Any],
                                            List[int],
                                            Type[Model],
                                            bool,
                                            OneToOneField,
                                        ],
                                    ],
                                ]
                            ],
                            List[int],
                            Type[Model],
                            bool,
                            OneToOneField,
                        ],
                    ]
                ],
                List[int],
                Type[Model],
            ],
        ],
        Dict[
            str,
            Union[
                List[
                    Union[
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[Any],
                                List[int],
                                Type[User],
                                bool,
                                ForeignKey,
                            ],
                        ],
                        Dict[
                            str,
                            Union[
                                Callable,
                                List[Any],
                                List[int],
                                Type[ContentType],
                                bool,
                                ForeignKey,
                            ],
                        ],
                    ]
                ],
                List[int],
                Type[Model],
            ],
        ],
    ],
    select: Union[
        List[
            Union[
                Tuple[Optional[str], Optional[str], Optional[str]],
                Tuple[Col, Tuple[str, List[Any]], None],
            ]
        ],
        List[
            Union[
                Tuple[Col, Tuple[str, List[Any]], None],
                Tuple[Greatest, Tuple[str, List[datetime]], str],
            ]
        ],
        List[
            Union[
                Tuple[Col, Tuple[str, List[Any]], None],
                Tuple[Right, Tuple[str, List[int]], str],
            ]
        ],
    ],
    db: str,
) -> List[RelatedPopulator]: ...
