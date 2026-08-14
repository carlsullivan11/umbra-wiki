# NVD CVE attribution

- Source: NIST National Vulnerability Database (NVD), API 2.0
- URL: https://services.nvd.nist.gov/rest/json/cves/2.0
- Imported pages: `17` (see imports/nvd-cve/manifest.json)
- Import mode: **incremental** — CVEs modified in the last 7 day(s),
  capped at 40 per run. The full catalogue (~377k CVEs) is
  deliberately never dumped.
- CVEs already covered by another importer (e.g. CISA KEV) are skipped so one
  CVE has exactly one page.
- Terms: NVD data is public domain (U.S. government work); NVD requests
  attribution and does not endorse derived products.
- Last importer run date: 2026-08-14
