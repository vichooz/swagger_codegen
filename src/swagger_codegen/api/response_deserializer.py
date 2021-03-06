import abc
from typing import Any
from typing import Optional

import pydantic

from swagger_codegen.api.types import ResponseType


class ResponseDeserializer(abc.ABC):
    @abc.abstractmethod
    def deserialize(self, deserialize_to: ResponseType, model_body):
        pass


class DefaultResponseDeserializer(ResponseDeserializer):
    def deserialize(self, deserialize_to: ResponseType, model_body) -> Optional[Any]:
        if deserialize_to is None:
            return None

        if model_body is None:
            return None

        class Config(pydantic.BaseConfig):
            arbitrary_types_allowed = True

        pydantic_validator_model = pydantic.create_model(
            "PydanticValidatorModel", __root__=(deserialize_to, ...), __config__=Config
        )
        return pydantic_validator_model(__root__=model_body).__root__
