from datetime import date
from typing import Any, Dict, List, Optional, Tuple, Union

from django.contrib.admin.views.autocomplete import AutocompleteJsonView
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Page, Paginator
from django.db.models.query import QuerySet
from django.template.response import TemplateResponse
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View


class MultipleObjectMixin(ContextMixin):
    allow_empty: bool = ...
    queryset: Any = ...
    model: Any = ...
    paginate_by: Any = ...
    paginate_orphans: int = ...
    context_object_name: Any = ...
    paginator_class: Any = ...
    page_kwarg: str = ...
    ordering: Any = ...
    def get_queryset(self) -> Union[List[Dict[str, str]], QuerySet]: ...
    def get_ordering(self) -> Optional[Union[Tuple[str, str], str]]: ...
    def paginate_queryset(
        self, queryset: Union[List[Dict[str, str]], QuerySet], page_size: int
    ) -> Tuple[Paginator, Page, bool, bool]: ...
    def get_paginate_by(
        self, queryset: Optional[Union[List[Dict[str, str]], QuerySet]]
    ) -> Optional[int]: ...
    def get_paginator(
        self,
        queryset: Union[List[Dict[str, str]], QuerySet],
        per_page: int,
        orphans: int = ...,
        allow_empty_first_page: bool = ...,
        **kwargs: Any
    ) -> Paginator: ...
    def get_paginate_orphans(self) -> int: ...
    def get_allow_empty(self) -> bool: ...
    def get_context_object_name(
        self, object_list: Optional[Union[List[Dict[str, str]], QuerySet]]
    ) -> Optional[str]: ...
    def get_context_data(
        self, *, object_list: Optional[Any] = ..., **kwargs: Any
    ) -> Union[
        Dict[
            str,
            Optional[Union[List[Dict[str, str]], bool, MultipleObjectMixin]],
        ],
        Dict[
            str,
            Optional[
                Union[
                    bool,
                    date,
                    Page,
                    Paginator,
                    QuerySet,
                    MultipleObjectTemplateResponseMixin,
                ]
            ],
        ],
        Dict[str, Union[List[Dict[str, str]], bool, Page, Paginator, ListView]],
        Dict[str, Union[bool, AutocompleteJsonView, Page, Paginator, QuerySet]],
    ]: ...

class BaseListView(MultipleObjectMixin, View):
    object_list: Any = ...
    def get(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> TemplateResponse: ...

class MultipleObjectTemplateResponseMixin(TemplateResponseMixin):
    template_name_suffix: str = ...
    def get_template_names(self) -> List[str]: ...

class ListView(MultipleObjectTemplateResponseMixin, BaseListView): ...
