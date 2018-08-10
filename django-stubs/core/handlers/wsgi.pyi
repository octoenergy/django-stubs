from io import BytesIO
from typing import Any, Callable, Dict, Optional, Tuple, Union

from django.core.handlers import base
from django.http import HttpRequest
from django.http.request import QueryDict
from django.http.response import HttpResponse
from django.test.client import FakePayload
from django.utils.datastructures import MultiValueDict


class LimitedStream:
    stream: django.test.client.FakePayload = ...
    remaining: int = ...
    buffer: bytes = ...
    buf_size: int = ...
    def __init__(
        self,
        stream: Union[BytesIO, FakePayload, str],
        limit: int,
        buf_size: int = ...,
    ) -> None: ...
    def read(self, size: Optional[int] = ...) -> bytes: ...
    def readline(self, size: Optional[int] = ...) -> bytes: ...

class WSGIRequest(HttpRequest):
    content_params: Dict[str, str]
    content_type: str
    environ: Dict[
        str,
        Union[
            Tuple[int, int],
            _io.BytesIO,
            django.test.client.FakePayload,
            int,
            str,
        ],
    ] = ...
    path_info: str = ...
    path: str = ...
    META: Dict[
        str,
        Union[
            Tuple[int, int],
            _io.BytesIO,
            django.test.client.FakePayload,
            int,
            str,
        ],
    ] = ...
    method: str = ...
    encoding: Any = ...
    resolver_match: None = ...
    def __init__(
        self,
        environ: Union[
            Dict[
                str,
                Optional[
                    Union[Tuple[int, int], BytesIO, FakePayload, int, str]
                ],
            ],
            Dict[
                str,
                Union[
                    Dict[str, str],
                    Tuple[int, int],
                    BytesIO,
                    FakePayload,
                    int,
                    str,
                ],
            ],
        ],
    ) -> None: ...
    def GET(self) -> QueryDict: ...
    def COOKIES(self) -> Dict[str, str]: ...
    @property
    def FILES(self) -> MultiValueDict: ...
    POST: Any = ...

class WSGIHandler(base.BaseHandler):
    request_class: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(
        self,
        environ: Dict[
            str, Union[Tuple[int, int], BytesIO, FakePayload, int, str]
        ],
        start_response: Callable,
    ) -> HttpResponse: ...

def get_path_info(
    environ: Union[
        Dict[
            str,
            Optional[Union[Tuple[int, int], BytesIO, FakePayload, int, str]],
        ],
        Dict[
            str,
            Union[
                Dict[str, str], Tuple[int, int], BytesIO, FakePayload, int, str
            ],
        ],
    ]
) -> str: ...
def get_script_name(
    environ: Union[
        Dict[
            str,
            Optional[Union[Tuple[int, int], BytesIO, FakePayload, int, str]],
        ],
        Dict[
            str,
            Union[
                Dict[str, str], Tuple[int, int], BytesIO, FakePayload, int, str
            ],
        ],
    ]
) -> str: ...
def get_bytes_from_wsgi(
    environ: Union[
        Dict[
            str,
            Optional[Union[Tuple[int, int], BytesIO, FakePayload, int, str]],
        ],
        Dict[
            str,
            Union[
                Dict[str, str], Tuple[int, int], BytesIO, FakePayload, int, str
            ],
        ],
    ],
    key: str,
    default: str,
) -> bytes: ...
def get_str_from_wsgi(
    environ: Union[
        Dict[
            str,
            Optional[Union[Tuple[int, int], BytesIO, FakePayload, int, str]],
        ],
        Dict[
            str,
            Union[
                Dict[str, str], Tuple[int, int], BytesIO, FakePayload, int, str
            ],
        ],
    ],
    key: str,
    default: str,
) -> str: ...
