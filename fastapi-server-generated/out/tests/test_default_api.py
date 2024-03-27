# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.add_user201_response import AddUser201Response  # noqa: F401
from openapi_server.models.add_user_request import AddUserRequest  # noqa: F401
from openapi_server.models.document_translation_request import DocumentTranslationRequest  # noqa: F401
from openapi_server.models.explanation200_response import Explanation200Response  # noqa: F401
from openapi_server.models.explanation401_response import Explanation401Response  # noqa: F401
from openapi_server.models.explanation_request import ExplanationRequest  # noqa: F401
from openapi_server.models.get_user200_response import GetUser200Response  # noqa: F401
from openapi_server.models.insert_document200_response import InsertDocument200Response  # noqa: F401
from openapi_server.models.insert_document_request import InsertDocumentRequest  # noqa: F401
from openapi_server.models.translation200_response import Translation200Response  # noqa: F401
from openapi_server.models.translation_request import TranslationRequest  # noqa: F401
from openapi_server.models.v1_auth_get200_response import V1AuthGet200Response  # noqa: F401
from openapi_server.models.v1_auth_get403_response import V1AuthGet403Response  # noqa: F401
from openapi_server.models.verify_token_and_fetch_explanation200_response import VerifyTokenAndFetchExplanation200Response  # noqa: F401
from openapi_server.models.verify_token_and_fetch_explanation400_response import VerifyTokenAndFetchExplanation400Response  # noqa: F401
from openapi_server.models.verify_token_and_fetch_explanation401_response import VerifyTokenAndFetchExplanation401Response  # noqa: F401
from openapi_server.models.verify_token_and_fetch_explanation_request import VerifyTokenAndFetchExplanationRequest  # noqa: F401


def test_add_user(client: TestClient):
    """Test case for add_user

    Adds a new user to the system
    """
    add_user_request = openapi_server.AddUserRequest()

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/user",
    #    headers=headers,
    #    json=add_user_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_translation(client: TestClient):
    """Test case for document_translation

    Translates a document to a target language
    """
    document_translation_request = openapi_server.DocumentTranslationRequest()

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/document-translation",
    #    headers=headers,
    #    json=document_translation_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_explanation(client: TestClient):
    """Test case for explanation

    Explains a given document in a specified output language and CEFR level
    """
    explanation_request = {"document":"SGVsbG8sIFdvcmxkIQ==","input_language":"auto","output_language":"en","output_language_level":"b1","session_id":"nldh884","history":null}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/explanation",
    #    headers=headers,
    #    json=explanation_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user(client: TestClient):
    """Test case for get_user

    Retrieves a user's details
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/user/{userId}".format(userId='user_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_insert_document(client: TestClient):
    """Test case for insert_document

    Inserts a document into the database and returns a document id.
    """
    insert_document_request = openapi_server.InsertDocumentRequest()

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/document",
    #    headers=headers,
    #    json=insert_document_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_translation(client: TestClient):
    """Test case for translation

    Translates text to a target language
    """
    translation_request = openapi_server.TranslationRequest()

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/translation",
    #    headers=headers,
    #    json=translation_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_auth_get(client: TestClient):
    """Test case for v1_auth_get

    Obtain a valid access token
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/auth",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_verify_token_and_fetch_explanation(client: TestClient):
    """Test case for verify_token_and_fetch_explanation

    Verifies the access token's validity and returns an explanation of the provided Document on successful verification.
    """
    verify_token_and_fetch_explanation_request = {"document":"SGVsbG8sIFdvcmxkIQ==","input_language":"auto","output_language":"en","output_language_level":"b1","history":null}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/verify-explanation",
    #    headers=headers,
    #    json=verify_token_and_fetch_explanation_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

