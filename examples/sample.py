# This file was generated by liblab | https://liblab.com/

from skyscanner_b2b import SkyscannerB2b, Environment

sdk = SkyscannerB2b(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
)

result = sdk.culture.locales(x_api_key="{{b2bapikey}}")

print(result)
