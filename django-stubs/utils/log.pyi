import logging.config
from logging import LogRecord
from typing import Any, Callable, Dict, List, Optional, Union

from django.core.mail.backends.locmem import EmailBackend

request_logger: Any
DEFAULT_LOGGING: Any

def configure_logging(
    logging_config: str,
    logging_settings: Dict[
        str,
        Union[
            Dict[
                str,
                Union[
                    Dict[str, Union[List[str], bool, str]],
                    Dict[str, Union[List[str], str]],
                ],
            ],
            Dict[str, Union[Dict[str, Union[List[str], str]], Dict[str, str]]],
            int,
        ],
    ],
) -> None: ...

class AdminEmailHandler(logging.Handler):
    filters: List[django.utils.log.RequireDebugFalse]
    formatter: None
    level: int
    lock: _thread.RLock
    include_html: bool = ...
    email_backend: Optional[str] = ...
    def __init__(
        self, include_html: bool = ..., email_backend: None = ...
    ) -> None: ...
    def emit(self, record: LogRecord) -> None: ...
    def send_mail(
        self, subject: str, message: str, *args: Any, **kwargs: Any
    ) -> None: ...
    def connection(self) -> EmailBackend: ...
    def format_subject(self, subject: str) -> str: ...

class CallbackFilter(logging.Filter):
    callback: Callable = ...
    def __init__(self, callback: Callable) -> None: ...
    def filter(self, record: str) -> int: ...

class RequireDebugFalse(logging.Filter):
    name: str
    nlen: int
    def filter(self, record: Union[LogRecord, str]) -> bool: ...

class RequireDebugTrue(logging.Filter):
    name: str
    nlen: int
    def filter(self, record: Union[LogRecord, str]) -> bool: ...

class ServerFormatter(logging.Formatter):
    datefmt: None
    style: django.core.management.color.Style = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def format(self, record: LogRecord) -> str: ...
    def uses_server_time(self) -> bool: ...

def log_response(
    message: str,
    *args: Any,
    response: Optional[Any] = ...,
    request: Optional[Any] = ...,
    logger: Any = ...,
    level: Optional[Any] = ...,
    exc_info: Optional[Any] = ...
) -> None: ...
