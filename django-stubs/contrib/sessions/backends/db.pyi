from datetime import datetime
from typing import Any, Dict, Optional, Type, Union

from django.contrib.sessions.backends.base import SessionBase
from django.contrib.sessions.base_session import AbstractBaseSession
from django.contrib.sessions.models import Session
from django.db.models.base import Model


class SessionStore(SessionBase):
    accessed: bool
    serializer: Type[django.core.signing.JSONSerializer]
    def __init__(self, session_key: Optional[str] = ...) -> None: ...
    @classmethod
    def get_model_class(cls) -> Type[Session]: ...
    def model(self) -> Type[AbstractBaseSession]: ...
    def load(
        self
    ) -> Union[Dict[str, Model], Dict[str, int], Dict[str, str]]: ...
    def exists(self, session_key: Optional[str]) -> bool: ...
    modified: bool = ...
    def create(self) -> None: ...
    def create_model_instance(
        self,
        data: Union[
            Dict[str, Union[datetime, str]],
            Dict[str, Union[int, str]],
            Dict[str, Model],
        ],
    ) -> AbstractBaseSession: ...
    def save(self, must_create: bool = ...) -> None: ...
    def delete(self, session_key: Optional[str] = ...) -> None: ...
    @classmethod
    def clear_expired(cls) -> None: ...
