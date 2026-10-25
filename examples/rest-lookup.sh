#!/bin/sh
# Look up a phone number through Calmido's REST endpoint with curl and your free key.
# Usage: CALMIDO_API_KEY=cal_… ./rest-lookup.sh "+31 183 554 004" [nl|en|fr]
set -eu

: "${CALMIDO_API_KEY:?set CALMIDO_API_KEY to your key}"
number=${1:?usage: $0 NUMBER [LANGUAGE]}
language=${2:-en}

curl -sS https://www.calmido.com/api/v1/lookup \
  -H "x-api-key: $CALMIDO_API_KEY" \
  -H 'content-type: application/json' \
  -d "{\"number\":\"$number\",\"language\":\"$language\"}"
echo
