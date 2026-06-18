---
source_url: https://developer.surecart.com/api-reference/errors
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/errors#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart uses conventional HTTP response codes to indicate the success or failure of an API request. In general: codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the 5xx range indicate an error with SureCart's servers (these are rare).

### [​](https://developer.surecart.com/api-reference/errors#http-status-codes) HTTP Status Codes

These are all of the status codes that the SureCart API will return.

| HTTP Status                | Description                                                             |
| -------------------------- | ----------------------------------------------------------------------- |
| `200` OK                   | Everything worked as expected                                           |
| `400` Bad Request          | The request was unacceptable, often due to missing a required parameter |
| `401`Unauthorized          | Invalid API token provided                                              |
| `404` Not Found            | The requested resource doesn't exist                                    |
| `422` Unprocessable Entity | The request failed validation or was not allowed for another reason     |
| `500` Server Error         | Something went wrong on SureCart's end                                  |

### [​](https://developer.surecart.com/api-reference/errors#error-responses) Error Responses

All error responses will be formatted like the example below, and they will have at least the following keys:

- `http_status` – The HTTP status code – matching the HTTP response status.
- `type` – The type of error – more specific than the http_status.
- `code` – The unique code for the error – this should be used for translations.
- `message` – The human readable error message.

```
{
  "http_status": "unprocessable_entity",
  "type": "not_found",
  "code": "product.not_found",
  "message": "Unable to find product with id='e0e92d34-aed9-4bb8-9107-89309370c4b'",
  "validation_errors": {}
}
```

### [​](https://developer.surecart.com/api-reference/errors#validation-errors) Validation Errors

If an error is due to object validation a validation_errors key will also be set within the error response. The validation errors response will be formatted like the example below, and each validation error will have the following keys:

- `attribute` – The attribute the validation error is associated with.
- `type` – The type of validation error.
- `code` – The unique code for the validation error – this should be used for translations.
- `options` – Any options that apply to this error – these can be used for translation interpolation. (For example, a numerical validation error might have options for min and max.)
- `message` – The human readable validation error message.

```
{
  "type": "unprocessable_entity",
  "code": "product.invalid",
  "message": "Failed to save product",
  "validation_errors": [\
    {\
      "attribute": "name",\
      "type": "blank",\
      "code": "product.name.blank",\
      "options": {},\
      "message": "can't be blank"\
    }\
  ]
}
```
