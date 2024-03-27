# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
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

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/v1/user",
    responses={
        201: {"model": AddUser201Response, "description": "User successfully created."},
        400: {"description": "Invalid input provided."},
        401: {"model": Explanation401Response, "description": "Unauthorized"},
    },
    tags=["default"],
    summary="Adds a new user to the system",
    response_model_by_alias=True,
)
async def add_user(
    add_user_request: AddUserRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> AddUser201Response:
    ...


@router.post(
    "/v1/document-translation",
    responses={
        200: {"model": Explanation200Response, "description": "Successful"},
        401: {"model": Explanation401Response, "description": "Unauthorized"},
    },
    tags=["default"],
    summary="Translates a document to a target language",
    response_model_by_alias=True,
)
async def document_translation(
    document_translation_request: DocumentTranslationRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> Explanation200Response:
    ...


@router.post(
    "/v1/explanation",
    responses={
        200: {"model": Explanation200Response, "description": "Successful"},
        401: {"model": Explanation401Response, "description": "Unauthorized"},
    },
    tags=["default"],
    summary="Explains a given document in a specified output language and CEFR level",
    response_model_by_alias=True,
)
async def explanation(
    explanation_request: ExplanationRequest = Body(None, description=""),
    token_subscriptionAuth: TokenModel = Security(
        get_token_subscriptionAuth
    ),
) -> Explanation200Response:
    ...


@router.get(
    "/v1/user/{userId}",
    responses={
        200: {"model": GetUser200Response, "description": "User details retrieved successfully."},
        401: {"model": Explanation401Response, "description": "Unauthorized"},
        404: {"description": "User not found."},
    },
    tags=["default"],
    summary="Retrieves a user&#39;s details",
    response_model_by_alias=True,
)
async def get_user(
    userId: str = Path(..., description="The unique identifier of the user to retrieve"),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> GetUser200Response:
    ...


@router.post(
    "/v1/document",
    responses={
        200: {"model": InsertDocument200Response, "description": "Document successfully inserted."},
        400: {"description": "Invalid request format."},
        401: {"model": Explanation401Response, "description": "Unauthorized"},
    },
    tags=["default"],
    summary="Inserts a document into the database and returns a document id.",
    response_model_by_alias=True,
)
async def insert_document(
    insert_document_request: InsertDocumentRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> InsertDocument200Response:
    ...


@router.post(
    "/v1/translation",
    responses={
        200: {"model": Translation200Response, "description": "OK"},
        401: {"model": Explanation401Response, "description": "Unauthorized"},
    },
    tags=["default"],
    summary="Translates text to a target language",
    response_model_by_alias=True,
)
async def translation(
    translation_request: TranslationRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> Translation200Response:
    ...


@router.get(
    "/v1/auth",
    responses={
        200: {"model": V1AuthGet200Response, "description": "Successfull"},
        403: {"model": V1AuthGet403Response, "description": "Forbidden"},
    },
    tags=["default"],
    summary="Obtain a valid access token",
    response_model_by_alias=True,
)
async def v1_auth_get(
) -> V1AuthGet200Response:
    """This endpoint provides a access token."""
    return BaseDefaultApi.subclasses[0]().v1_auth_get()


@router.post(
    "/v1/verify-explanation",
    responses={
        200: {"model": VerifyTokenAndFetchExplanation200Response, "description": "Token verification successful, explanation provided."},
        400: {"model": VerifyTokenAndFetchExplanation400Response, "description": "Bad Request"},
        401: {"model": VerifyTokenAndFetchExplanation401Response, "description": "Unauthorized"},
    },
    tags=["default"],
    summary="Verifies the access token&#39;s validity and returns an explanation of the provided Document on successful verification.",
    response_model_by_alias=True,
)
async def verify_token_and_fetch_explanation(
    verify_token_and_fetch_explanation_request: VerifyTokenAndFetchExplanationRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> VerifyTokenAndFetchExplanation200Response:
    ...
