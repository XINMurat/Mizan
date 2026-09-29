# Instructions

Be a rigorous, skeptical reviewer. For each claim, check what evidence supports it, whether there is a baseline or control, who judged the result, and whether the conclusion goes further than the evidence allows. Name each problem specifically, and say which claims are adequately supported.

# Task

Review this incident postmortem before it is published internally. Which conclusions are supported?

---
**Postmortem — checkout outage, 2026-09-18**

1. The on-call engineer was paged at 14:05.
2. The outage lasted 47 minutes, from 14:03 to 14:52.
3. Error rate peaked at 38% of requests (load balancer logs).
4. Root cause: the cache eviction change shipped in release 8.2. We rolled 8.2 back at 14:50 and errors stopped shortly after.
5. No customer data was affected: we checked the three services we suspected might have written partial orders.
6. The upstream DNS provider's status page records an incident on their side, resolved at 14:49.
7. We added an alert that fires when the error rate exceeds 5% for 2 minutes; replayed against this incident's logs, it fires at 14:06.
8. This will not happen again.
9. The team held a retrospective on Friday.
