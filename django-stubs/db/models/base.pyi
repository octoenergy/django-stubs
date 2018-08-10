from datetime import date
from decimal import Decimal
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type, Union
from uuid import UUID

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.sessions.base_session import AbstractBaseSession
from django.core.checks.messages import Warning
from django.core.exceptions import (MultipleObjectsReturned,
                                    ObjectDoesNotExist, ValidationError)
from django.db.models.fields import CharField, Field
from django.db.models.fields.related import ForeignKey
from django.db.models.manager import Manager
from django.db.models.options import Options


class Deferred: ...

DEFERRED: Any

def subclass_exception(
    name: str,
    bases: Tuple[
        Union[Type[MultipleObjectsReturned], Type[ObjectDoesNotExist]]
    ],
    module: str,
    attached_to: Type[Model],
) -> Type[Union[MultipleObjectsReturned, ObjectDoesNotExist]]: ...

class ModelBase(type):
    def __new__(
        cls: Type[ModelBase],
        name: str,
        bases: Tuple[Type[Model]],
        attrs: Union[
            Dict[
                str,
                Union[
                    Callable,
                    Tuple[Tuple[int, str], Tuple[int, str]],
                    Type[AbstractUser.Meta],
                    Field,
                    property,
                    str,
                ],
            ],
            Dict[
                str,
                Union[
                    Callable, Type[Any], Type[PermissionsMixin.Meta], Field, str
                ],
            ],
            Dict[str, Union[Callable, Type[Any], CharField, Manager, str]],
            Dict[
                str,
                Union[
                    Callable,
                    Type[AbstractBaseSession.Meta],
                    classmethod,
                    GenericForeignKey,
                    Field,
                    Manager,
                    str,
                ],
            ],
            Dict[
                str,
                Union[
                    Tuple[
                        Tuple[str, Tuple[Tuple[str, str], Tuple[str, str]]],
                        Tuple[str, str],
                    ],
                    CharField,
                    str,
                ],
            ],
        ],
        **kwargs: Any
    ) -> Type[Model]: ...
    def add_to_class(
        cls,
        name: str,
        value: Optional[
            Union[
                Callable,
                List[str],
                Tuple[Tuple[int, str], Tuple[int, str]],
                Tuple[
                    Tuple[str, Tuple[Tuple[str, str], Tuple[str, str]]],
                    Tuple[str, str],
                ],
                Type[Union[MultipleObjectsReturned, ObjectDoesNotExist]],
                bool,
                classmethod,
                GenericForeignKey,
                Field,
                Manager,
                Options,
                property,
                str,
            ]
        ],
    ) -> None: ...

class ModelStateFieldsCacheDescriptor:
    def __get__(
        self, instance: ModelState, cls: Type[ModelState] = ...
    ) -> Dict[Any, Any]: ...

class ModelState:
    db: Any = ...
    adding: bool = ...
    fields_cache: Any = ...

class Model:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def from_db(
        cls,
        db: str,
        field_names: List[str],
        values: Union[
            List[Optional[Union[date, int, str]]],
            List[Optional[UUID]],
            List[Union[Decimal, int]],
            List[Union[int, UUID]],
            List[Union[str, UUID]],
            Tuple[Union[int, str]],
        ],
    ) -> Model: ...
    def __eq__(
        self,
        other: Optional[
            Union[Dict[Any, Any], List[Any], Tuple, Model, int, str]
        ],
    ) -> bool: ...
    def __hash__(self) -> int: ...
    def __reduce__(self): ...
    pk: Any = ...
    def get_deferred_fields(self) -> Set[str]: ...
    def refresh_from_db(
        self, using: None = ..., fields: Optional[List[str]] = ...
    ) -> None: ...
    def serializable_value(self, field_name: str) -> Union[int, str]: ...
    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[List[str]] = ...,
    ) -> None: ...
    def save_base(
        self,
        raw: bool = ...,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: str = ...,
        update_fields: Optional[frozenset] = ...,
    ) -> None: ...
    def delete(
        self, using: None = ..., keep_parents: bool = ...
    ) -> Tuple[int, Dict[str, int]]: ...
    def prepare_database_save(self, field: ForeignKey) -> UUID: ...
    def clean(self) -> None: ...
    def validate_unique(self, exclude: List[str] = ...) -> None: ...
    def date_error_message(
        self, lookup_type: Any, field_name: Any, unique_for: Any
    ): ...
    def unique_error_message(
        self, model_class: Type[Model], unique_check: Tuple[str, str]
    ) -> ValidationError: ...
    def full_clean(
        self, exclude: Optional[List[str]] = ..., validate_unique: bool = ...
    ) -> None: ...
    def clean_fields(self, exclude: List[str] = ...) -> None: ...
    @classmethod
    def check(cls, **kwargs: Any) -> List[Warning]: ...

def method_set_order(
    self, ordered_obj: Any, id_list: Any, using: Optional[Any] = ...
) -> None: ...
def method_get_order(self, ordered_obj: Any): ...
def make_foreign_order_accessors(
    model: Type[Model], related_model: Type[Model]
) -> None: ...
def model_unpickle(model_id: Any): ...
