"""Look up a phone number through Calmido's REST endpoint with your free key. Standard library only.

Usage: CALMIDO_API_KEY=cal_… python3 rest-lookup.py "+31 183 554 004" [nl|en|fr]
"""

import json
import os
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://api.calmido.com/developer/v1/lookup"


def lookup(number, language="en", country=None, key=None):
    body = {"number": number, "language": language}
    if country:
        body["country"] = country
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode(),
        headers={"content-type": "application/json", "x-api-key": key or os.environ["CALMIDO_API_KEY"]},
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        # 400 invalid_number, 401 missing_key or invalid_key, 429 rate_limited (see Retry-After).
        retry = error.headers.get("Retry-After")
        raise RuntimeError(f"{error.code} {json.load(error)['error']}" + (f", retry in {retry}s" if retry else "")) from None


if __name__ == "__main__":
    if len(sys.argv) < 2 or "CALMIDO_API_KEY" not in os.environ:
        sys.exit(__doc__)
    answer = lookup(sys.argv[1], *(sys.argv[2:3] or ["en"]))
    print(f"{answer['number']['international']}: {answer['verdict']}, {answer['report_count']} reports")
    print(answer["summary"])
