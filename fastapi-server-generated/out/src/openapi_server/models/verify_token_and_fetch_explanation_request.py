# coding: utf-8

"""
    Totoy API

    The Totoy REST API. Totoy translates and explains text, PDFs and scanned documents in 18 languages and 6 CEFR language levels

    The version of the OpenAPI document: 0.1.0
    Contact: support@totoy.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.explanation_request_history_inner import ExplanationRequestHistoryInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VerifyTokenAndFetchExplanationRequest(BaseModel):
    """
    VerifyTokenAndFetchExplanationRequest
    """ # noqa: E501
    document: Optional[StrictStr] = Field(description="Base64-encoded PDF, JPG or PNG file")
    input_language: Optional[StrictStr] = Field(default='auto', description="Input Language ID of the document (optional)")
    output_language: StrictStr = Field(description="Output Language ID for the generated explanation")
    output_language_level: Optional[StrictStr] = Field(default='b1', description="Output Language CEFR Level")
    history: Optional[List[ExplanationRequestHistoryInner]] = Field(description="Conversation history to provide context for the model about the document. Empty on initial question.")
    __properties: ClassVar[List[str]] = ["document", "input_language", "output_language", "output_language_level", "history"]

    @field_validator('input_language')
    def input_language_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('auto', 'ar', 'bs', 'de', 'es', 'en', 'fa', 'fr', 'hr', 'hu', 'it', 'pl', 'ro', 'sk', 'sl', 'sr', 'tl', 'tr', 'uk'):
            raise ValueError("must be one of enum values ('auto', 'ar', 'bs', 'de', 'es', 'en', 'fa', 'fr', 'hr', 'hu', 'it', 'pl', 'ro', 'sk', 'sl', 'sr', 'tl', 'tr', 'uk')")
        return value

    @field_validator('output_language')
    def output_language_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ar', 'bs', 'de', 'es', 'en', 'fa', 'fr', 'hr', 'hu', 'it', 'pl', 'ro', 'sk', 'sl', 'sr', 'tl', 'tr', 'uk'):
            raise ValueError("must be one of enum values ('ar', 'bs', 'de', 'es', 'en', 'fa', 'fr', 'hr', 'hu', 'it', 'pl', 'ro', 'sk', 'sl', 'sr', 'tl', 'tr', 'uk')")
        return value

    @field_validator('output_language_level')
    def output_language_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('a1', 'a2', 'b1', 'b2', 'c1', 'c2'):
            raise ValueError("must be one of enum values ('a1', 'a2', 'b1', 'b2', 'c1', 'c2')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VerifyTokenAndFetchExplanationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in history (list)
        _items = []
        if self.history:
            for _item in self.history:
                if _item:
                    _items.append(_item.to_dict())
            _dict['history'] = _items
        # set to None if document (nullable) is None
        # and model_fields_set contains the field
        if self.document is None and "document" in self.model_fields_set:
            _dict['document'] = None

        # set to None if history (nullable) is None
        # and model_fields_set contains the field
        if self.history is None and "history" in self.model_fields_set:
            _dict['history'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of VerifyTokenAndFetchExplanationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "document": obj.get("document"),
            "input_language": obj.get("input_language") if obj.get("input_language") is not None else 'auto',
            "output_language": obj.get("output_language"),
            "output_language_level": obj.get("output_language_level") if obj.get("output_language_level") is not None else 'b1',
            "history": [ExplanationRequestHistoryInner.from_dict(_item) for _item in obj.get("history")] if obj.get("history") is not None else None
        })
        return _obj


