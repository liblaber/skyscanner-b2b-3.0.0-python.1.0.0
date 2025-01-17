# SkyscannerB2B Python SDK 1.0.0

Welcome to the SkyscannerB2b SDK documentation. This guide will help you get started with integrating and using the SkyscannerB2b SDK in your project.

## Versions

- API version: `1.0.0`
- SDK version: `1.0.0`

## About the API

Our Travel APIs are provided to connect partners like yourself to all the data you need to build an innovative website or app using our Skyscanner travel content. We’ve made it easier than ever to develop your website using flexible price search options so you can build exciting tools that will expand your travel search options for your users.

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [API Key Authentication](#api-key-authentication)
- [Services](#services)
- [Models](#models)
- [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install skyscanner-b2b
```

## Authentication

### API Key Authentication

The SkyscannerB2b API uses API keys as a form of authentication. An API key is a unique identifier used to authenticate a user, developer, or a program that is calling the API.

#### Setting the API key

When you initialize the SDK, you can set the API key as follows:

```py
SkyscannerB2b(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER"
)
```

If you need to set or update the API key after initializing the SDK, you can use:

```py
sdk.set_api_key("YOUR_API_KEY", "YOUR_API_KEY_HEADER")
```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                                                       |
| :----------------------------------------------------------------------------------------- |
| [FlightsLivePricesService](documentation/services/FlightsLivePricesService.md)             |
| [FlightsIndicativePricesService](documentation/services/FlightsIndicativePricesService.md) |
| [CultureService](documentation/services/CultureService.md)                                 |
| [GeoService](documentation/services/GeoService.md)                                         |
| [AutosuggestService](documentation/services/AutosuggestService.md)                         |
| [CarriersService](documentation/services/CarriersService.md)                               |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                                                                     | Description |
| :--------------------------------------------------------------------------------------- | :---------- |
| [ItineraryrefreshCreateRequest](documentation/models/ItineraryrefreshCreateRequest.md)   |             |
| [HierarchyFlightsNearestRequest](documentation/models/HierarchyFlightsNearestRequest.md) |             |
| [AutosuggestFlightsRequest](documentation/models/AutosuggestFlightsRequest.md)           |             |
| [AutosuggestCarhireRequest](documentation/models/AutosuggestCarhireRequest.md)           |             |
| [AutosuggestHotelsRequest](documentation/models/AutosuggestHotelsRequest.md)             |             |
| [Locator](documentation/models/Locator.md)                                               |             |
| [AutosuggestFlightsRequestQuery](documentation/models/AutosuggestFlightsRequestQuery.md) |             |
| [AutosuggestCarhireRequestQuery](documentation/models/AutosuggestCarhireRequestQuery.md) |             |
| [AutosuggestHotelsRequestQuery](documentation/models/AutosuggestHotelsRequestQuery.md)   |             |

</details>

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->
