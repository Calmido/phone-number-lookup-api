"""Look up a phone number through Calmido's MCP endpoint. Standard library only.

Usage: python3 lookup.py "+31 183 554 004" [nl|en|fr]
"""

import json
import sys
import urllib.request

ENDPOINT = "https://www.calmido.com/api/mcp"


def lookup(number, language="en", country=None):
    arguments = {"number": number, "language": language}
    if country:
        arguments["country"] = country
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": "lookup_phone_number", "arguments": arguments},
        }
    ).encode()
    request = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={"content-type": "application/json", "accept": "application/json, text/event-stream"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        text = response.read().decode()
    # The answer comes as one server-sent event: a line starting with "data: ".
    message = json.loads(next(line[6:] for line in text.splitlines() if line.startswith("data: ")))
    if "error" in message:
        raise RuntimeError(message["error"]["message"])
    result = message["result"]
    if result.get("isError"):
        raise RuntimeError(result["content"][0]["text"])
    return result["structuredContent"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    answer = lookup(sys.argv[1], *(sys.argv[2:3] or ["en"]))
    print(f"{answer['number']['international']}: {answer['verdict']}, {answer['report_count']} reports")
    print(answer["summary"])
