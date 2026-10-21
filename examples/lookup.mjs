// Look up a phone number through Calmido's MCP endpoint. Node.js 18 or later, no dependencies.
// Usage: node lookup.mjs "+31 183 554 004" [nl|en|fr]

const ENDPOINT = 'https://www.calmido.com/api/mcp';

export async function lookup(number, language = 'en', country) {
  const response = await fetch(ENDPOINT, {
    method: 'POST',
    headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream' },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 1,
      method: 'tools/call',
      params: { name: 'lookup_phone_number', arguments: { number, language, ...(country && { country }) } },
    }),
  });
  // The answer comes as one server-sent event: a line starting with "data: ".
  const line = (await response.text()).split('\n').find((l) => l.startsWith('data: '));
  const message = JSON.parse(line.slice(6));
  if (message.error) throw new Error(message.error.message);
  if (message.result.isError) throw new Error(message.result.content[0].text);
  return message.result.structuredContent;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [number, language = 'en'] = process.argv.slice(2);
  if (!number) {
    console.error('usage: node lookup.mjs NUMBER [nl|en|fr]');
    process.exit(1);
  }
  const answer = await lookup(number, language);
  console.log(`${answer.number.international}: ${answer.verdict}, ${answer.report_count} reports`);
  console.log(answer.summary);
}
