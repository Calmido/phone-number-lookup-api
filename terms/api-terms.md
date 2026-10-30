# Calmido API Terms

| | |
|---|---|
| **Version** | 1.0 |
| **Published** | 2026-10-30 |

## 1. Who we are

The Calmido API is provided by **Calmido B.V.**, a private limited company registered with the Dutch
Chamber of Commerce under number **96388455**, Amsterdam ("Calmido", "we", "us"). You ("you", "the customer")
are the party that uses the API.

## 2. What these terms cover

These terms apply to **all** access to the Calmido API: the REST endpoints under
`api.calmido.com/developer/v1/*` and the MCP endpoint at `www.calmido.com/api/mcp`, with or without a key, paid or
free. They do not apply to ordinary use of the website, which falls under our general terms. Our privacy
statement applies to both.

You accept these terms:

- **Without a key** (the MCP endpoint): by using it.
- **With a free key**: by requesting it. The form links to these terms, and the e-mail that delivers the key
  links to them again.
- **Trial and paid plans**: by putting the key into use. We send these terms with the key, before any
  invoice.

## 3. The plans

| Plan | Access | Limit | Attribution | SLA |
|---|---|---|---|---|
| **MCP, no key** | The MCP endpoint | Per address, as on the developer page | Link to the number page | No |
| **Free** | Lookup endpoint | Distinct numbers per day, on your key | Calmido and the number page link | No |
| **Trial** | As Pro, for 14 days | As Pro | As Free | No |
| **Pro** | Lookup endpoint | Higher distinct-number cap | Calmido and the number page link | No |
| **Business** | As Pro, plus higher limits | Highest distinct-number cap | Calmido and the number page link | Yes, art. 10 |
| **Monitoring** | Status, history and alerts for **your own verified numbers** | Per number | n/a | As Business |

Current prices and limits are on the developer page. Prices exclude VAT.

**Limits count distinct numbers per day**, not requests. Asking for the same number twice counts once.
We may adjust limits; we do not lower them for paying customers without the notice in art. 16.

## 4. Your key

- **Keep it secret.** Not in client-side code, a public repository or an app you ship to end users.
- **Traffic under your key is yours**, also if someone else uses it. Rotate it in your account if you
  suspect a leak.
- **We show a key once** and store only a hash.
- We may revoke a key under art. 12.

## 5. Trial

On request, 14 days of Pro, free, without payment details. It is for evaluation, not production. It ends by
itself and converts to a paid plan only if you explicitly agree. One trial per organisation. The deletion
duty in art. 7 applies when it ends.

## 6. What you may and may not do

While your plan runs, you get a **non-exclusive, non-transferable and revocable** right to request the data
and use it in your own product or service **for the purposes below**.

**Permitted purposes.** Warning a person about an incoming or missed call; showing who is calling, or which
business uses a number; deciding how to route or screen a call; answering a person who asks about a number.

**Not permitted:**

- **Extraction.** Looking up numbers no user of yours asked about or was called by: walking number ranges,
  enumerating, or rebuilding (part of) the directory, whatever the volume. One lookup is one number.
- **Profiling people.** Building a profile of a person, or combining our data with other data to identify or
  learn about the holder of a number.
- **Screening.** Using the data to assess anyone for credit, housing, employment, insurance or any comparable
  decision.
- **Decisions without a person.** Using a verdict as the sole basis for a decision that has legal effects
  for, or similarly significantly affects, a person. Screening a call is not such a decision; refusing someone
  a service is.
- **Resale.** Selling, licensing or offering the data as your own dataset, feed or API. A product that runs on
  the data is fine; the data itself is not for sale.
- **Circumventing limits.** Several keys or accounts, shared keys, or working around the caps.
- **Misrepresentation.** Presenting a verdict as a fact about a person, or as coming from or endorsed by an
  operator or authority. A verdict describes the calls people reported; numbers are spoofed and reassigned.
- Anything unlawful, or harmful to the service or its users.

**Attribution.** Wherever your users see a verdict, name Calmido as the source and link to the number's
Calmido page, using the `page_url` from the answer: it holds the evidence and the way to dispute it. Do not
rewrite it, shorten it or route it through your own domain or a link shortener. Linking to another language
version of the same page is fine. This applies on every plan. Business names from open
sources carry their source and licence in the answer; keep those with the name.

## 7. Caching, storage and deletion

- **Keep an answer for at most 24 hours.** Then ask again. A verdict that was corrected, suppressed or
  erased must leave your product within a day; the 24 hours is how it does.
- **Do not build a history** from our answers: no archive of verdicts or report counts per number, no
  dataset of what you looked up.
- **When your plan or trial ends**, delete everything you obtained through the API within 14 days, including
  caches, copies and exports, and confirm it in writing on request.

## 8. Personal data

Two kinds of personal data cross the API, in opposite directions, and the roles differ.

### 8.1 The number you send us

The numbers you look up are often your own users' call data. For those, **Calmido processes on your
behalf, as your processor** (GDPR art. 28), and this article is the processing agreement:

- **Purpose:** we use the number only to answer that request. We do not store it, we do not count it
  towards any verdict or list, and we do not use it for anything else.
- **Duration:** the time it takes to answer. Your daily limit needs us to recognise a number we have already
  counted today. For that we keep a fingerprint of the number, not the number: a keyed hash made with a
  random key that exists only in memory. The key and the fingerprints are dropped at midnight UTC, or
  earlier when the service restarts or your key has been idle for a while. Without the key, a fingerprint
  cannot be matched to a number. We do not cache answers.
- **Confidentiality and security:** only the systems that answer the request see the number; the measures
  are those in our privacy statement.
- **Sub-processors:** for the REST endpoints, only our hosting provider (Germany): `api.calmido.com` runs
  on our own servers, with no proxy or security service in front of it. For the MCP endpoint, also the
  security service in front of `www.calmido.com`. Both are named on our list of recipients. We tell you
  before we add one, and you may object.
- **Assistance:** we help you answer requests from people whose number you sent us, and with your own
  data protection impact assessment where it concerns this processing.
- **Breaches:** we tell you without undue delay after becoming aware of a breach affecting numbers you
  sent.
- **End:** there is nothing to return or delete, because nothing is kept. On request we confirm this in
  writing and give you the information you need to check it.

### 8.2 Our answer

For the directory, Calmido is the controller. For what you do with our answers, **you are an
independent controller** in your own right. For the answers there is no processing agreement between us.

**What you take on**, as the recipient of personal data:

- Use it only for the permitted purposes in art. 6, and have your own lawful basis for doing so.
- Tell your users in your own privacy notice that you use Calmido for caller information.
- Keep the attribution link: it is how a person whose number you show finds out where the verdict comes from
  and how to object.
- **Pass objections on.** If someone asks you to correct or remove a verdict, or objects to it, refer them
  to Calmido (the link on the number page, or support@calmido.com). We handle it, free, and the 24-hour cache
  carries the outcome to you.
- Secure what you hold, and tell us without delay if API data you hold is breached.

**Where you are.** A key is only for customers established in the **European Economic Area** (the EU plus
Iceland, Liechtenstein and Norway). We do not issue keys to customers established elsewhere.

**What we keep about you.** Your e-mail address, the site or repository you gave, your plan and limits, and
per day the count of distinct numbers your key looked up. **We do not record which numbers you looked up**
(art. 8.1).
Access logs are kept 30 days. See the privacy statement.

**What we e-mail you.** Only messages the service needs: your key, a limit reached, the end of a trial,
changes to the API or these terms, invoices and security notices. You receive these as long as you have a key.
We do not send marketing e-mail.

## 9. The data

The directory is built from community reports and public sources. Reports are counts and categories, never
free text. A verdict is a statistical reading of reported calls, with the uncertainty that comes with it; it
can be wrong, and numbers are spoofed and reassigned. The API is provided **as is**, without a warranty that
the data is accurate, complete or fit for your purpose. Build that into your product: show it as a report,
not a fact, and link to the evidence.

**No verdict is for sale.** No plan, paid or free, changes a verdict, removes a report or hides a page.
Disputing is free for everyone.

## 10. Availability, support and changes

- **Free, trial and Pro:** no availability guarantee.
- **Business:** 99.5% per calendar month, measured by our external monitoring. Missing it gives a pro rata
  credit on request, which is the only remedy.
- **Support:** support@calmido.com, working days 09:00–17:00 (Europe/Amsterdam), a first response within one
  working day. Live status: status.calmido.com.
- **Breaking changes** to a paid endpoint are announced at least **30 days** ahead by e-mail. New fields
  and better coverage roll out without notice.
- **Beta features** fall outside the SLA and the 30-day notice; you opt in per feature.

## 11. Prices, payment and cancellation

In euros, excluding VAT. Pro is billed monthly in advance, Business and Monitoring yearly in advance; payment
within 14 days. Cancel at the end of the current period; amounts paid are not refunded. We may suspend a key
after a reminder if an invoice stays unpaid. Price changes are announced 30 days ahead, and you may cancel
before they apply.

## 12. Suspension and termination

We may suspend or end access immediately if you breach these terms, art. 6 in particular, or endanger the
service; where reasonable, we warn first. Art. 7 applies afterwards. If we stop the API ourselves, paying
customers get at least **3 months'** notice.

## 13. Liability

Our liability is limited to what you paid for the API in the 12 months before the event. On the free plan
and during a trial it is excluded as far as the law allows. We are not liable for indirect damage, including
loss of profit, reputational damage, or damage to your customers from a verdict that was wrong, outdated or
unavailable. These limits do not apply to intent or deliberate recklessness.

## 14. Who may use which plan

- **The MCP endpoint and the free key** are open to anyone, including individuals who build something for
  themselves, such as spam filtering at home.
- **Trial, Pro, Business and Monitoring** are offered to businesses and professionals only. By requesting
  one you confirm you act in the course of a business or profession.

If you use the API as a consumer, the limits in art. 13 apply only as far as consumer law allows, and
nothing in these terms takes away rights the law gives you.

## 15. Your obligations towards us, if a verdict is challenged through you

If a person or authority contacts you about a verdict you showed, tell us, and give us what we need to
handle it. Do not settle it yourself by changing what the verdict says.

## 16. Changes to these terms

We may change these terms. Paying customers get **30 days'** notice by e-mail and may cancel before the
change applies. Without a key, the version on this page at the time of use applies.

## 17. Governing law

Dutch law. Disputes go to the competent court in Amsterdam, unless mandatory law says otherwise.
