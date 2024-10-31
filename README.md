# OpenAPI Specification for the Totoy API

This repository contains an [OpenAPI](https://www.openapis.org/) specification for the [Totoy API](https://developer.totoy.ai).

## Useful commands

```bash
# Bundle multi-file spec into one openapi.yaml file:
redocly bundle src/openapi.yaml --output openapi.yaml
```

```bash
# Lint openapi.yaml with Redocly
redocly lint openapi.yaml
```

```bash
# Lint openapi.yaml with Speakeasy (SDK Generator)
speakeasy validate openapi -s openapi.yaml
```

## Naming Conventions for Spec Developers

### Schema Object Names

Use PascalCase for schema object names, as this will be reflected in class names, e.g., `KnowledgeBase`. In `schemas.yaml`, name the schema `KnowledgeBase` and the file `KnowledgeBase.yaml`.

For POST and PATCH requests, unlike GET and DELETE, a `requestBody` is required. Both request and response schemas are created for these requests.

#### POST Requests

There are two types of POST Requests:

1. Creating a new resource (e.g., `POST /sources` creates a new `Source` with a `source_id`).
2. Not creating a new resource (e.g., `POST /explanation` returns a response but does not create a new resource).

Naming conventions:

1. `CreateSourceRequest` (request schema includes `Create` and `Request`) -> `Source` (response schema is the new resource without `Response` in the name).
2. `ExplanationRequest` (request schema includes `Request` but not an operation name) -> `ExplanationResponse` (response schema includes `Response` in the name).

When different media types are possible for a request, multiple schemas may be needed, e.g.:

- `CreateDocumentSourceRequest`/`CreateTextSourceRequest` -> `Source`.

#### PATCH Requests

Only used for existing resources. Naming convention:
`ModifySourceRequest` (request schema includes `Modify` and `Request`) -> `Source` (returns the modified resource).

### Example Object Names

Use kebab-case, start with the schema name and end with `-example`, e.g., `knowledge-base-example`. In `examples.yaml`, name the example `knowledge-base-example` and the file `knowledge-base-example.yaml`. For multiple examples:

- `explanation-request-example-1`
- `explanation-request-example-2`

### Paths Item Object Names

Use kebab-case, e.g., `/knowledge-base`. The file name should also be `knowledge-base.yaml`.

### Parameter Object Names

Use camelCase ending with `Param`, e.g., `knowledgeBaseIdParam`. The file name should be `knowledgeBaseIdParam.yaml` and in `parameters.yaml`, the name should be `knowledgeBaseIdParam`.

### Response Objects

Use camelCase ending with `Response`, e.g., `general4XXResponse`. The file name should be `general4XXResponse.yaml` and in `responses.yaml`, it should be named `general4XXResponse`.

### Properties in Schema Objects

Use snake_case, e.g., `knowledge_base_id` (matching the keys in the final JSON).
