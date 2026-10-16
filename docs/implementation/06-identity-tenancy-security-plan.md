# Identity tenancy and security

T0111 owns the concrete Resend runtime delivery transport. T1203 qualifies its controlled predeployment context; T1211 separately verifies the distinct production issuer/client/callback/current-grant and controlled account-invitation context after T1210. Neither a fake mail port nor staging configuration proves production onboarding.

M1 is a signed-in merchant-context slice with independent application and database denial proofs. User/issuer-subject identity is shared; Membership and scoped Platform Assignment are independent. T0110 explicitly owns Merchant Admin member list/role/suspension commands and last-Admin protection. T0108 exposes the usable sign-in/invitation/context/member journey.

T0102 establishes transaction-local tenant context, composite relations, forced RLS and nonowner/non-BYPASSRLS runtime roles before business modules. Separate queue, worker, control-plane and migration grants remain distinct. Every later tenant table/view/file/projection joins the grant/RLS inventory.

OpsHub owns hashed opaque server sessions, current authorization, CSRF/Origin checks and cookie rotation. Auth0 supplies OIDC login/account recovery. No IdP organization/claim or platform assignment supplies merchant business authority. Local OIDC/mail stubs are replaced only by separately qualified T1203.

T0106 introduces verified initial-Admin/source-owner readiness and commercial primitives early. TEST-POLICY enables local verification flows; actual representative/recovery/session/step-up/suspended-access policy remains OP02/OP11/OP12/A04/MD09. Platform cannot self-grant or browse contacts.

T0109 proves foundation guards/RLS independently; T1205 repeats full TI/AU surface inventory after all modules exist. Restore uses an external epoch and current verified grants/privacy before reads/export, separately from action/contact egress. RLS is defense in depth, not a claim to contain a fully compromised runtime SQL credential.
