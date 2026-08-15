# IEEE OUI / MAC prefix attribution

- Source: IEEE Registration Authority public listings (MA-L, MA-M, MA-S)
- URLs:
  - https://standards-oui.ieee.org/oui/oui.csv
  - https://standards-oui.ieee.org/oui28/mam.csv
  - https://standards-oui.ieee.org/oui36/oui36.csv
- Entries: `53622` (MA-L 39944, MA-M 6548, MA-S 7133)
- `2` prefix(es) are registered to more than one organisation in IEEE's
  own listings (e.g. the legacy `080030` shared by Network Research Corp, RMIT
  and CERN). Those rows list every claimant separated by ` | ` rather than
  silently keeping one.
- Stored as a single CSV lookup table, **not** as wiki pages — ~53k
  registrations would bury the readable corpus.
- **Lookup rule:** longest prefix wins (36 → 28 → 24 bits). MA-M/MA-S blocks are
  carved out of MA-L space, and on the live data 7,132/7,133 MA-S and
  6,420/6,548 MA-M prefixes have a different vendor than their 24-bit parent
  (usually the umbrella "IEEE Registration Authority"). A 24-bit-only lookup is
  therefore wrong for ~13,500 prefixes.
- Terms: IEEE publishes these listings publicly for identification purposes.
  Attribute IEEE; do not imply IEEE endorsement.
- Last importer run date: 2026-08-14
