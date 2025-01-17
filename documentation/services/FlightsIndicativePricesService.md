# FlightsIndicativePricesService

A list of all methods in the `FlightsIndicativePricesService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description        |
| :-------------------------------------- | :----------------- |
| [indicative_search](#indicative_search) | /indicative/search |

## indicative_search

/indicative/search

- HTTP Method: `POST`
- Endpoint: `/apiservices/v3/flights/indicative/search`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | any  | ❌       | The request body. |
| x_api_key    | str  | ❌       |                   |

**Example Usage Code Snippet**

```python
from skyscanner_b2b import SkyscannerB2b, Environment
from skyscanner_b2b.models import any

sdk = SkyscannerB2b(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = ""

result = sdk.flights_indicative_prices.indicative_search(
    request_body=request_body,
    x_api_key="{{b2bapikey}}"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
