# Calmido Phone Number Lookup API

**The phone number lookup API for the Netherlands, Belgium and Luxembourg.** See who is calling and
whether a number is reported as spam: the community verdict, the number of reports, the most
reported scam or spam category and the registered business, for any Dutch (+31), Belgian (+32) or
Luxembourgish (+352) number.

| | |
|---|---|
| **Live** | MCP endpoint `https://www.calmido.com/api/mcp`: open, no account, no key |
| **In development** | REST endpoint `GET /api/v1/numbers/{number}` with a free key. Same numbers in, same fields out |
| **Docs** | [calmido.com/nl-en/developers](https://www.calmido.com/nl-en/developers) is the reference; this repository holds examples, the changelog and, from the REST launch on, the OpenAPI spec and the [API terms](terms/api-terms.md) |

## Quick start

The MCP endpoint speaks [Model Context Protocol](https://modelcontextprotocol.io) over Streamable
HTTP, stateless. One tool, `lookup_phone_number`. You can call it from any HTTP client:

```sh
curl -s https://www.calmido.com/api/mcp \
  -H 'content-type: application/json' \
  -H 'accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lookup_phone_number","arguments":{"number":"+31 183 554 004","language":"en"}}}'
```

Dependency-free examples in [examples/](examples/): [curl](examples/lookup.sh),
[Python](examples/lookup.py) (standard library only) and [Node.js](examples/lookup.mjs) (18 or later).

In an MCP client:

```sh
claude mcp add --transport http calmido https://www.calmido.com/api/mcp
```

```json
{ "mcpServers": { "calmido": { "url": "https://www.calmido.com/api/mcp" } } }
```

Adding Calmido to Claude or ChatGPT without code: [calmido.com/nl-en/ai-assistants](https://www.calmido.com/nl-en/ai-assistants).
Listed in the MCP Registry as `com.calmido/phone-number-lookup`.

## Input

| Argument | Required | |
|---|---|---|
| `number` | yes | International (`+31 20 123 4567`, `0031…`, `31201234567`) or national (`020 123 4567`). Spaces, dashes and brackets are ignored |
| `country` | no | ISO 3166-1 alpha-2 (`NL`, `BE`, `LU`) for a national number. Without it, NL, then BE, then LU are tried |
| `language` | no | `nl`, `en` or `fr`: the language of `summary` and of the page at `page_url`. Default `en` |

The number must be valid and dialable. An unallocated range is refused with an error that says so,
not guessed.

## Output

`structuredContent` of the tool result:

```json
{
  "number": {
    "e164": "+31183554004",
    "national": "0183 554 004",
    "international": "+31 183 554 004",
    "country": "NL"
  },
  "verdict": "suspicious",
  "report_count": 59,
  "top_category": null,
  "business": null,
  "restricted": false,
  "page_url": "https://www.calmido.com/nl-nl/directory/31183554004",
  "summary": "This number has been reported 59×. Based on user reports; no reports does not mean a number is safe. The reports themselves, their dates and the full picture are at https://www.calmido.com/nl-nl/directory/31183554004"
}
```

| Field | |
|---|---|
| `verdict` | One of the seven values below |
| `report_count` | Community reports on the number |
| `top_category` | The most reported category, in the requested language, or `null`: telemarketing, robocall, recruitment, phishing, spoofing, harassment, callback fraud, scam or silent call |
| `business` | `null`, or `{ "name", "sources": [{ "name", "url", "licence", "licence_url" }] }`: the registered business and where its name comes from |
| `restricted` | `true` when the identity behind the number was erased on request |
| `page_url` | The number's page, with the reports, their dates and the way to dispute them |
| `summary` | One sentence you may quote, with a link to `page_url` |

### Verdicts

A verdict describes the calls people reported from a number, not the person or business holding it.
Numbers are spoofed and reassigned.

| `verdict` | Meaning |
|---|---|
| `suspicious` | The reports place the number in an elevated or high threat band |
| `safe` | Reported, and even the cautious end of the estimate stays below the warning line |
| `neutral` | Reported, but not enough to say either way |
| `business` | No reports, and the number belongs to a registered business |
| `empty` | No reports and no business. **This does not mean the number is safe** |
| `restricted` | The identity was erased on request. Reports still count; no business name is returned |
| `unavailable` | The directory could not be read just now. Ask again later; this never means "no reports" |

## How the data may be used

These rules hold for every way in, and are part of the [API terms](terms/api-terms.md).

- **One number per lookup.** There is no bulk endpoint and no download of the directory.
- **Look up the numbers your users ask about or are called by.** Walking through number ranges is
  extraction, whatever the volume.
- **Wherever you show a verdict, name Calmido and link to `page_url`.** The page holds the evidence
  and the way to dispute it.
- **Keep an answer for at most 24 hours, and do not build a history from our answers.** A corrected or
  erased number must disappear from your product within a day.
- **Do not profile people** or screen anyone for credit, housing, employment or insurance, and do not
  resell the data.
- **No plan buys a different verdict**, a removed report or a hidden page.

## Limits

Anonymous use is throttled per address: a burst of at least 30 lookups, then 60 per minute. The
limit is counted per server, and there is more than one. Higher limits come with the free key and the
paid plans; until then, write to [support@calmido.com](mailto:support@calmido.com) with what you are
building.

## Data and privacy

- **What we store about you:** nothing. The looked-up number is not stored and no lookup record is
  written. Your address is held in memory for rate limiting only. A lookup through the API never
  moves a number up the directory's lists.
- **Where the data comes from:** community reports, as counts and categories, never as free text.
  Business names come from public sources such as Overture Maps, OpenStreetMap and the Belgian KBO
  register, and from businesses that claimed their number. Each answer names the source and licence
  of the business name.
- **Privacy statement:** [calmido.com/nl-en/privacy](https://www.calmido.com/nl-en/privacy).

## A number is wrong, or it is yours

**Never put a phone number in a GitHub issue here.** An issue is public, and a number in it is a
publication. Use the number's page instead:

- **The verdict is wrong:** the link under the verdict on the number's page.
- **The number is yours and you want it out:** write to [legal@calmido.com](mailto:legal@calmido.com).
- **Anything else about the API:** open an issue, without numbers, or write to
  [support@calmido.com](mailto:support@calmido.com).

## Licence

The examples and documentation in this repository are MIT-licensed. The data the API returns is not:
its use is governed by the rules above and by the [API terms](terms/api-terms.md).

---

Calmido B.V. · [calmido.com](https://www.calmido.com)
