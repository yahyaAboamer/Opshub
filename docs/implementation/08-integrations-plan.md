# Integrations

Concrete read HTTP drivers are T0309 Shopify, T0406 Bosta and T0915 Meta, tested through mock endpoints locally. Their actual account qualifications consume those accepted runtime drivers and the deployed release, rather than a separate test-only client.

M3/M4 deliver fake-backed Shopify commerce/catalog and Bosta shipment journeys before actual account qualification. T0301 freezes read/action/reconciliation ports and encrypted versioned credentials. The web encrypts; only the worker decrypts and verifies merchant/connection/version. Inbound authentication keys have a separate ingress boundary.

T0302 owns safe-read rate budgets, connection locks, atomic page/checkpoint commits and independently known acquisition closure. Successful pagination is not complete source population. T0305 and T0402 distinguish receipt identity, logical event/native revision, account binding and authenticated read corroboration. Unknown callback guarantees cannot be invented.

Shopify identity/item/catalog/confirmation observations preserve separate business/payment/fulfillment/courier dimensions. Bosta native delivery versus display tracking, purpose/finality, reported counters and individually evidenced attempts stay distinct. Available fee data is context, not a mandatory ledger; missing fee is not zero.

T0306/T0307/T0403 provide list/detail/navigation/trust/limited-state/fallback experiences. T0308/T0405 are actual authorized read qualifications; T0914 covers Meta. They consume staging credentials only after T1201–T1204, never make production the first integrated environment and do not prove mutations.

Core supported read/action/result connections remain MVP. Temporary unavailable/unsupported/incomplete-onboarding fallback preserves exact reason and later rejoins identity. Meta is read-only; no broad provider marketplace, campaign writes or guessed SKU attribution.
