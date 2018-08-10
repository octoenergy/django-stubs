from collections import OrderedDict
from contextlib import _GeneratorContextManager
from decimal import Decimal
from io import StringIO
from typing import (Any, Callable, Dict, Iterator, List, Optional, Set, Tuple,
                    Type, Union)

from django.apps.registry import Apps
from django.conf import LazySettings
from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.views.main import ChangeList
from django.contrib.messages.storage.fallback import FallbackStorage
from django.db import DefaultConnectionProxy
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.base import Model
from django.forms.forms import BaseForm
from django.forms.widgets import Media
from django.template.base import Template
from django.template.context import Context
from django.test.runner import DiscoverRunner
from django.test.testcases import SimpleTestCase
from django.utils.safestring import SafeText
from django.views.generic.detail import SingleObjectTemplateResponseMixin


class Approximate:
    val: Union[decimal.Decimal, float] = ...
    places: int = ...
    def __init__(
        self, val: Union[Decimal, float], places: int = ...
    ) -> None: ...
    def __eq__(self, other: Union[Decimal, float]) -> bool: ...

class ContextList(list):
    def __getitem__(
        self, key: Union[int, str]
    ) -> Optional[
        Union[
            List[Union[List[str], str]],
            bool,
            AdminForm,
            ChangeList,
            FallbackStorage,
            Model,
            BaseForm,
            Media,
            Context,
            SingleObjectTemplateResponseMixin,
            str,
        ]
    ]: ...
    def get(self, key: str, default: Optional[str] = ...) -> str: ...
    def __contains__(self, key: str) -> bool: ...
    def keys(self) -> Set[str]: ...

class _TestState: ...

def setup_test_environment(debug: Optional[bool] = ...) -> None: ...
def teardown_test_environment() -> None: ...
def get_runner(
    settings: LazySettings, test_runner_class: Optional[str] = ...
) -> Type[Union[Any, DiscoverRunner]]: ...

class TestContextDecorator:
    attr_name: Any = ...
    kwarg_name: Any = ...
    def __init__(
        self, attr_name: Optional[str] = ..., kwarg_name: Optional[str] = ...
    ) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def __enter__(self) -> Optional[Apps]: ...
    def __exit__(
        self, exc_type: None, exc_value: None, traceback: None
    ) -> None: ...
    def decorate_class(
        self, cls: Type[SimpleTestCase]
    ) -> Type[SimpleTestCase]: ...
    def decorate_callable(self, func: Callable) -> Callable: ...
    def __call__(
        self,
        decorated: Union[
            Callable, Type[Union[SimpleTestCase, LoggingCaptureMixin]]
        ],
    ) -> Union[Callable, Type[Union[SimpleTestCase, LoggingCaptureMixin]]]: ...

class override_settings(TestContextDecorator):
    attr_name: None
    kwarg_name: None
    options: Union[
        Dict[str, Dict[str, Callable]],
        Dict[
            str,
            Dict[
                str,
                Union[
                    Dict[str, Optional[str]],
                    Dict[str, Union[Callable, Dict[str, int], str]],
                    Dict[str, Union[Dict[str, int], int, str]],
                ],
            ],
        ],
        Dict[
            str,
            List[
                Dict[
                    str, Union[Dict[str, List[Tuple[str, Dict[str, str]]]], str]
                ]
            ],
        ],
        Dict[
            str,
            List[
                Union[
                    Dict[str, Union[Dict[Any, Any], bool, str]],
                    Dict[str, Union[Dict[str, bool], bool, str]],
                ]
            ],
        ],
        Dict[
            str,
            List[
                Union[
                    Dict[str, Union[Dict[str, List[str]], str]],
                    Dict[str, Union[bool, str]],
                ]
            ],
        ],
        Dict[
            str,
            List[
                Union[
                    Dict[str, Union[Dict[str, bool], str]],
                    Dict[str, Union[Dict[str, int], str]],
                ]
            ],
        ],
        Dict[
            str,
            List[
                Union[
                    Dict[str, Union[Dict[str, int], str]],
                    Dict[str, Union[Dict[str, str], str]],
                ]
            ],
        ],
        Dict[str, List[unittest.mock.Mock]],
        Dict[str, Optional[Union[List[str], bool]]],
        Dict[str, Optional[Union[bool, str]]],
        Dict[str, Tuple[Tuple[str, str], Tuple[str, str]]],
        Dict[str, Type[Any]],
        Dict[str, Union[Callable, bool]],
        Dict[str, Union[Dict[int, None], bool]],
        Dict[str, Union[Dict[str, None], List[str]]],
        Dict[str, Union[Dict[str, Optional[str]], str]],
        Dict[
            str,
            Union[
                Dict[
                    str,
                    Union[
                        Dict[Any, Any],
                        Dict[str, Callable],
                        Dict[str, int],
                        Dict[str, str],
                    ],
                ],
                List[
                    Dict[str, Union[Dict[str, List[str]], List[str], bool, str]]
                ],
                List[Union[Tuple[str, str], str]],
                int,
                str,
            ],
        ],
        Dict[
            str,
            Union[
                Dict[
                    str,
                    Union[
                        Dict[str, Dict[str, Union[List[str], bool, str]]],
                        Dict[str, Dict[str, str]],
                        int,
                    ],
                ],
                str,
            ],
        ],
        Dict[
            str,
            Union[
                Dict[
                    str,
                    Union[
                        Dict[
                            str,
                            Union[
                                Callable,
                                Dict[str, Union[Dict[str, bool], bool]],
                            ],
                        ],
                        Dict[
                            str,
                            Union[Dict[str, Union[Dict[str, bool], bool]], int],
                        ],
                        Dict[
                            str,
                            Union[Dict[str, Union[Dict[str, bool], bool]], str],
                        ],
                        str,
                    ],
                ],
                List[str],
            ],
        ],
        Dict[
            str,
            Union[
                Dict[
                    str,
                    Union[
                        Dict[str, Union[Callable, str]],
                        Dict[str, Union[Dict[str, int], str]],
                        Dict[str, Union[int, str]],
                        Dict[str, str],
                    ],
                ],
                bool,
            ],
        ],
        Dict[str, Union[Dict[str, Union[Dict[str, str], str]], bool]],
        Dict[
            str,
            Union[
                List[
                    Dict[str, Union[Dict[str, List[Any]], List[Any], bool, str]]
                ],
                List[str],
            ],
        ],
        Dict[
            str,
            Union[
                List[Dict[str, Union[Dict[str, Tuple[str]], List[str], str]]],
                List[str],
                int,
                str,
            ],
        ],
        Dict[str, Union[List[Dict[str, Union[List[Any], bool, str]]], int]],
        Dict[str, Union[List[int], List[str], str]],
        Dict[str, Union[Tuple[str], str]],
        Dict[str, Union[float, str]],
        Dict[str, bytes],
    ] = ...
    def __init__(self, **kwargs: Any) -> None: ...
    wrapped: Union[django.conf.Settings, django.conf.UserSettingsHolder] = ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def save_options(
        self, test_func: Type[Union[SimpleTestCase, LoggingCaptureMixin]]
    ) -> None: ...
    def decorate_class(
        self, cls: Type[Union[SimpleTestCase, LoggingCaptureMixin]]
    ) -> Type[Union[SimpleTestCase, LoggingCaptureMixin]]: ...

class modify_settings(override_settings):
    attr_name: None
    kwarg_name: None
    wrapped: Union[django.conf.Settings, django.conf.UserSettingsHolder]
    operations: List[
        Union[Tuple[str, Dict[str, List[str]]], Tuple[str, Dict[str, str]]]
    ] = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def save_options(self, test_func: Type[SimpleTestCase]) -> None: ...
    options: Dict[str, List[Union[Tuple[str, str], str]]] = ...
    def enable(self) -> None: ...

class override_system_checks(TestContextDecorator):
    attr_name: None
    kwarg_name: None
    registry: django.core.checks.registry.CheckRegistry = ...
    new_checks: List[Callable] = ...
    deployment_checks: Optional[List[Callable]] = ...
    def __init__(
        self,
        new_checks: List[Callable],
        deployment_checks: Optional[List[Callable]] = ...,
    ) -> None: ...
    old_checks: Set[Callable] = ...
    old_deployment_checks: Set[Callable] = ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...

class CaptureQueriesContext:
    connection: django.db.DefaultConnectionProxy = ...
    def __init__(
        self, connection: Union[DefaultConnectionProxy, DatabaseWrapper]
    ) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, index: int) -> Dict[str, str]: ...
    def __len__(self) -> int: ...
    @property
    def captured_queries(self) -> List[Dict[str, str]]: ...
    force_debug_cursor: bool = ...
    initial_queries: int = ...
    final_queries: Optional[int] = ...
    def __enter__(self) -> CaptureQueriesContext: ...
    def __exit__(
        self, exc_type: None, exc_value: None, traceback: None
    ) -> None: ...

class ignore_warnings(TestContextDecorator):
    attr_name: None
    kwarg_name: None
    ignore_kwargs: Union[
        Dict[str, Type[django.utils.deprecation.RemovedInDjango30Warning]],
        Dict[str, str],
    ] = ...
    filter_func: Callable = ...
    def __init__(self, **kwargs: Any) -> None: ...
    catch_warnings: warnings.catch_warnings = ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...

requires_tz_support: Any

def isolate_lru_cache(lru_cache_object: Callable) -> Iterator[None]: ...

class override_script_prefix(TestContextDecorator):
    attr_name: None
    kwarg_name: None
    prefix: str = ...
    def __init__(self, prefix: str) -> None: ...
    old_prefix: str = ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...

class LoggingCaptureMixin:
    logger: Any = ...
    old_stream: Any = ...
    logger_output: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...

class isolate_apps(TestContextDecorator):
    attr_name: Optional[str]
    kwarg_name: Optional[str]
    installed_apps: Tuple[str] = ...
    def __init__(self, *installed_apps: Any, **kwargs: Any) -> None: ...
    old_apps: django.apps.registry.Apps = ...
    def enable(self) -> Apps: ...
    def disable(self) -> None: ...
