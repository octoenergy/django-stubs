from collections import OrderedDict
from datetime import datetime
from typing import (Any, Callable, Dict, Iterator, List, Optional, Tuple, Type,
                    Union)
from unittest.case import TestCase
from uuid import UUID

from django.contrib.sitemaps import Sitemap
from django.core.files.uploadedfile import InMemoryUploadedFile, UploadedFile
from django.db.models.base import Model
from django.db.models.expressions import Combinable
from django.test.testcases import SerializeMixin
from django.test.utils import LoggingCaptureMixin
from django.urls.converters import (IntConverter, PathConverter, SlugConverter,
                                    StringConverter, UUIDConverter)


class OrderedSet:
    dict: collections.OrderedDict = ...
    def __init__(
        self,
        iterable: Optional[
            Union[
                List[Optional[int]],
                List[Tuple[str, str]],
                List[Union[Combinable, str]],
                List[datetime],
                List[UUID],
                OrderedDict,
            ]
        ] = ...,
    ) -> None: ...
    def add(
        self,
        item: Union[
            Type[Model], SerializeMixin, LoggingCaptureMixin, int, TestCase
        ],
    ) -> None: ...
    def remove(self, item: Any) -> None: ...
    def discard(self, item: Any) -> None: ...
    def __iter__(self): ...
    def __contains__(self, item: Any): ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...

class MultiValueDictKeyError(KeyError): ...

class MultiValueDict(dict):
    def __init__(
        self,
        key_to_list_mapping: Union[
            Dict[str, List[List[Any]]],
            Dict[str, List[int]],
            Dict[str, Optional[List[str]]],
            List[Tuple[str, Union[List[List[Any]], List[str]]]],
            Tuple,
        ] = ...,
    ) -> None: ...
    def __getitem__(
        self, key: str
    ) -> Optional[Union[List[str], UploadedFile, str]]: ...
    def __setitem__(
        self, key: str, value: Optional[Union[int, str]]
    ) -> None: ...
    def __copy__(self) -> MultiValueDict: ...
    def __deepcopy__(self, memo: Any): ...
    def get(
        self, key: str, default: Optional[Union[int, str]] = ...
    ) -> Optional[Union[InMemoryUploadedFile, int, str]]: ...
    def getlist(
        self, key: Optional[Union[Callable, str]], default: Any = ...
    ) -> Any: ...
    def setlist(self, key: Union[Callable, str], list_: List[str]) -> None: ...
    def setdefault(self, key: str, default: str = ...) -> str: ...
    def setlistdefault(
        self, key: Union[Callable, str], default_list: None = ...
    ) -> Union[
        List[
            Union[
                Tuple[
                    List[Tuple[str, List[Any]]],
                    str,
                    Dict[str, Dict[str, Type[Sitemap]]],
                    Dict[Any, Any],
                ],
                Tuple[
                    List[Tuple[str, List[str]]],
                    str,
                    Dict[str, int],
                    Union[
                        Dict[Any, Any],
                        Dict[str, IntConverter],
                        Dict[str, PathConverter],
                        Dict[str, SlugConverter],
                        Dict[str, StringConverter],
                        Dict[str, UUIDConverter],
                    ],
                ],
                Tuple[
                    List[Union[Tuple[str, List[Any]], Tuple[str, List[str]]]],
                    str,
                    Dict[Any, Any],
                    Union[
                        Dict[Any, Any],
                        Dict[str, Any],
                        Dict[str, IntConverter],
                        Dict[str, StringConverter],
                    ],
                ],
            ]
        ],
        List[UploadedFile],
        List[str],
    ]: ...
    def appendlist(
        self,
        key: Union[Callable, str],
        value: Union[
            Tuple[
                List[Tuple[str, List[Any]]],
                str,
                Dict[str, Dict[str, Sitemap]],
                Dict[Any, Any],
            ],
            Tuple[
                List[Tuple[str, List[str]]],
                str,
                Dict[str, Union[int, str]],
                Dict[str, Union[IntConverter, StringConverter]],
            ],
            Tuple[
                List[Union[Tuple[str, List[Any]], Tuple[str, List[str]]]],
                str,
                Dict[str, Union[Dict[str, Type[Sitemap]], str]],
                Dict[str, UUIDConverter],
            ],
            UploadedFile,
            str,
        ],
    ) -> None: ...
    def items(self) -> Iterator[Tuple[str, Union[UploadedFile, str]]]: ...
    def lists(self): ...
    def values(self) -> Iterator[str]: ...
    def copy(self) -> MultiValueDict: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def dict(self) -> Dict[str, str]: ...

class ImmutableList(tuple):
    warning: str = ...
    def __new__(
        cls: Type[ImmutableList], *args: Any, warning: str = ..., **kwargs: Any
    ) -> ImmutableList: ...
    def complain(self, *wargs: Any, **kwargs: Any) -> Any: ...
    __delitem__: Any = ...
    __delslice__: Any = ...
    __iadd__: Any = ...
    __imul__: Any = ...
    __setitem__: Any = ...
    __setslice__: Any = ...
    append: Any = ...
    extend: Any = ...
    insert: Any = ...
    pop: Any = ...
    remove: Any = ...
    sort: Any = ...
    reverse: Any = ...

class DictWrapper(dict):
    func: Callable = ...
    prefix: str = ...
    def __init__(
        self, data: Dict[str, str], func: Callable, prefix: str
    ) -> None: ...
    def __getitem__(self, key: str) -> Optional[Union[int, str]]: ...
