# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.add_user201_response import AddUser201Response
from openapi_server.models.add_user_request import AddUserRequest
from openapi_server.models.document_translation_request import DocumentTranslationRequest
from openapi_server.models.explanation200_response import Explanation200Response
from openapi_server.models.explanation401_response import Explanation401Response
from openapi_server.models.explanation_request import ExplanationRequest
from openapi_server.models.get_user200_response import GetUser200Response
from openapi_server.models.insert_document200_response import InsertDocument200Response
from openapi_server.models.insert_document_request import InsertDocumentRequest
from openapi_server.models.translation200_response import Translation200Response
from openapi_server.models.translation_request import TranslationRequest
from openapi_server.models.v1_auth_get200_response import V1AuthGet200Response
from openapi_server.models.v1_auth_get403_response import V1AuthGet403Response
from openapi_server.models.verify_token_and_fetch_explanation200_response import VerifyTokenAndFetchExplanation200Response
from openapi_server.models.verify_token_and_fetch_explanation400_response import VerifyTokenAndFetchExplanation400Response
from openapi_server.models.verify_token_and_fetch_explanation401_response import VerifyTokenAndFetchExplanation401Response
from openapi_server.models.verify_token_and_fetch_explanation_request import VerifyTokenAndFetchExplanationRequest
from openapi_server.security_api import get_token_subscriptionAuth, get_token_bearerAuth

class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    def add_user(
        self,
        add_user_request: AddUserRequest,
    ) -> AddUser201Response:
        ...


    def document_translation(
        self,
        document_translation_request: DocumentTranslationRequest,
    ) -> Explanation200Response:
        ...


    def explanation(
        self,
        explanation_request: ExplanationRequest,
    ) -> Explanation200Response:
        ...


    def get_user(
        self,
        userId: str,
    ) -> GetUser200Response:
        ...


    def insert_document(
        self,
        insert_document_request: InsertDocumentRequest,
    ) -> InsertDocument200Response:
        ...


    def translation(
        self,
        translation_request: TranslationRequest,
    ) -> Translation200Response:
        ...


    def v1_auth_get(
        self,
    ) -> V1AuthGet200Response:
        """This endpoint provides a access token."""
        ...


    def verify_token_and_fetch_explanation(
        self,
        verify_token_and_fetch_explanation_request: VerifyTokenAndFetchExplanationRequest,
    ) -> VerifyTokenAndFetchExplanation200Response:
        ...
