from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

from django.db.models.fields import Field


class BaseSerializer:
    value: Any = ...
    def __init__(
        self,
        value: Union[
            Callable,
            List[Tuple[str, str]],
            Set[Tuple[str, str]],
            Tuple[str, Union[Field, str]],
            Field,
            int,
            str,
        ],
    ) -> None: ...
    def serialize(self) -> None: ...

class BaseSequenceSerializer(BaseSerializer):
    def serialize(self) -> Tuple[str, Set[str]]: ...

class BaseSimpleSerializer(BaseSerializer):
    value: str
    def serialize(self) -> Tuple[str, Set[Any]]: ...

class DatetimeSerializer(BaseSerializer):
    value: Any = ...
    def serialize(self): ...

class DateSerializer(BaseSerializer):
    def serialize(self): ...

class DecimalSerializer(BaseSerializer):
    def serialize(self): ...

class DeconstructableSerializer(BaseSerializer):
    @staticmethod
    def serialize_deconstructed(
        path: str, args: List[Any], kwargs: Dict[str, Union[Callable, int, str]]
    ) -> Tuple[str, Set[str]]: ...
    def serialize(self): ...

class DictionarySerializer(BaseSerializer):
    def serialize(self): ...

class EnumSerializer(BaseSerializer):
    def serialize(self): ...

class FloatSerializer(BaseSimpleSerializer):
    def serialize(self): ...

class FrozensetSerializer(BaseSequenceSerializer): ...

class FunctionTypeSerializer(BaseSerializer):
    value: Callable
    def serialize(self) -> Tuple[str, Set[str]]: ...

class FunctoolsPartialSerializer(BaseSerializer):
    def serialize(self): ...

class IterableSerializer(BaseSerializer):
    def serialize(self): ...

class ModelFieldSerializer(DeconstructableSerializer):
    value: django.db.models.fields.AutoField
    def serialize(self) -> Tuple[str, Set[str]]: ...

class ModelManagerSerializer(DeconstructableSerializer):
    def serialize(self): ...

class OperationSerializer(BaseSerializer):
    def serialize(self): ...

class RegexSerializer(BaseSerializer):
    def serialize(self): ...

class SequenceSerializer(BaseSequenceSerializer): ...
class SetSerializer(BaseSequenceSerializer): ...

class SettingsReferenceSerializer(BaseSerializer):
    def serialize(self): ...

class TimedeltaSerializer(BaseSerializer):
    def serialize(self): ...

class TimeSerializer(BaseSerializer):
    def serialize(self): ...

class TupleSerializer(BaseSequenceSerializer): ...

class TypeSerializer(BaseSerializer):
    def serialize(self): ...

class UUIDSerializer(BaseSerializer):
    def serialize(self): ...

def serializer_factory(
    value: Union[
        Callable,
        List[Tuple[str, str]],
        Set[Tuple[str, str]],
        Tuple[str, Union[Field, str]],
        Field,
        int,
        str,
    ]
) -> BaseSerializer: ...
