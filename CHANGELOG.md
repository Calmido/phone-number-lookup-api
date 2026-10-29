# Changelog

Changes to the Calmido Phone Number Lookup API that you can see from the outside. Newest first.

## Unreleased

- REST endpoint `POST https://api.calmido.com/developer/v1/lookup` with a free key from
  [calmido.com/nl-en/developers](https://www.calmido.com/nl-en/developers), and
  `GET /developer/v1/partner/usage`. Contract in [openapi.yaml](openapi.yaml); examples in
  [examples/](examples/).

## 2026-10-16

- `page_url` follows the requested `language` where the number's market has a page in it (`nl-en`,
  `be-fr`, …); otherwise the market's main language. *Rolling out with the next website release.*
- Listed in the Claude connectors directory.

## 2026-10-15

- Listed in the MCP Registry as `com.calmido/phone-number-lookup`.
- [calmido.com/nl-en/developers](https://www.calmido.com/nl-en/developers) became the developer hub,
  with the accepted number formats, an example answer and the meaning of each verdict.

## 2026-09-17

- Listed in the ChatGPT apps directory.

## 2026-09-08

- `lookup_phone_number` 1.0.0 on the MCP endpoint `https://www.calmido.com/api/mcp`.
