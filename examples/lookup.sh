#!/bin/sh
# Look up a phone number through Calmido's MCP endpoint with curl.
# Usage: ./lookup.sh "+31 183 554 004" [nl|en|fr]
set -eu

number=${1:?usage: $0 NUMBER [LANGUAGE]}
language=${2:-en}

curl -sS https://www.calmido.com/api/mcp \
  -H 'content-type: application/json' \
  -H 'accept: application/json, text/event-stream' \
  -d "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"lookup_phone_number\",\"arguments\":{\"number\":\"$number\",\"language\":\"$language\"}}}" |
  sed -n 's/^data: //p'
