from decimal import Decimal
from typing import Any, Type

from pydantic import ValidationError

from cbot.utils.classifiers import MODEL


def validate(model: Type[MODEL], params: Any) -> MODEL:
    return model.model_validate(params)


def default_serializer(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError
