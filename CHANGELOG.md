# Changelog

Changes to the Calmido Phone Number Lookup API that you can see from the outside. Newest first.

## Unreleased

- Every REST error carries a `message` next to its `error` code: a sentence for the developer, which may
  be reworded. A body that is not a JSON object is now `invalid_request` (400) instead of
  `invalid_number`. A 429 says whether the per-minute limit or the daily cap refused.
- The answer carries `last_reported_on`: the day of the newest community report in UTC, or `null`. This
  is a new field, which per the API terms (art. 9) needs no notice, and it is also in the MCP result.
- OpenAPI `info.version` 1.1.0.

## 2026-11-27

- REST endpoint `POST https://api.calmido.com/developer/v1/lookup` with a free key from
  [calmido.com/nl-en/developers](https://www.calmido.com/nl-en/developers), and
  `GET /developer/v1/partner/usage`. Contract in [openapi.yaml](openapi.yaml); examples in
  [examples/](examples/).

## 2026-11-25

- [API terms](terms/api-terms.md) version 1.0 published, in force on 25 November 2026. Art. 5 states that a business name is shown only with its source information.

## 2026-10-16

- `page_url` follows the requested `language` where the number's market has a page in it (`nl-en`,
  `be-fr`, …); otherwise the market's main language.
- Listed in the Claude connectors directory.

## 2026-10-15

- Listed in the MCP Registry as `com.calmido/phone-number-lookup`.
- [calmido.com/nl-en/developers](https://www.calmido.com/nl-en/developers) became the developer hub,
  with the accepted number formats, an example answer and the meaning of each verdict.

## 2026-09-17

- Listed in the ChatGPT apps directory.

## 2026-09-08

- `lookup_phone_number` 1.0.0 on the MCP endpoint `https://www.calmido.com/api/mcp`.
