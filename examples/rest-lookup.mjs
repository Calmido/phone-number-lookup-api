// Look up a phone number through Calmido's REST endpoint with your free key. Node.js 18 or later, no dependencies.
// Usage: CALMIDO_API_KEY=cal_… node rest-lookup.mjs "+31 183 554 004" [nl|en|fr]

const ENDPOINT = 'https://www.calmido.com/api/v1/lookup';

export async function lookup(number, language = 'en', country, key = process.env.CALMIDO_API_KEY) {
  const response = await fetch(ENDPOINT, {
    method: 'POST',
    headers: { 'content-type': 'application/json', 'x-api-key': key },
    body: JSON.stringify({ number, language, ...(country && { country }) }),
  });
  const body = await response.json();
  // 400 invalid_number, 401 missing_key or invalid_key, 429 rate_limited (see Retry-After).
  if (!response.ok) {
    const retry = response.headers.get('retry-after');
    throw new Error(`${response.status} ${body.error}${retry ? `, retry in ${retry}s` : ''}`);
  }
  return body;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const [number, language = 'en'] = process.argv.slice(2);
  if (!number || !process.env.CALMIDO_API_KEY) {
    console.error('usage: CALMIDO_API_KEY=cal_… node rest-lookup.mjs NUMBER [nl|en|fr]');
    process.exit(1);
  }
  const answer = await lookup(number, language);
  console.log(`${answer.number.international}: ${answer.verdict}, ${answer.report_count} reports`);
  console.log(answer.summary);
}
