from typing import Any, Dict, List, Optional, Tuple, Union

from django.template.base import Origin, Template
from django.template.engine import Engine

from .base import Loader as BaseLoader


class Loader(BaseLoader):
    engine: django.template.engine.Engine
    template_cache: Dict[Any, Any] = ...
    get_template_cache: Union[
        Dict[
            str,
            Union[
                Type[django.template.exceptions.TemplateDoesNotExist],
                django.template.base.Template,
            ],
        ],
        Dict[
            str,
            Union[
                django.template.base.Template,
                django.template.exceptions.TemplateDoesNotExist,
            ],
        ],
    ] = ...
    loaders: List[django.template.loaders.base.Loader] = ...
    def __init__(
        self,
        engine: Engine,
        loaders: Union[List[Tuple[str, Dict[str, str]]], List[str]],
    ) -> None: ...
    def get_contents(self, origin: Origin) -> str: ...
    def get_template(
        self, template_name: str, skip: Optional[List[Origin]] = ...
    ) -> Template: ...
    def get_template_sources(self, template_name: str) -> None: ...
    def cache_key(
        self, template_name: str, skip: Optional[List[Origin]] = ...
    ) -> str: ...
    def generate_hash(self, values: List[str]) -> str: ...
    def reset(self) -> None: ...
