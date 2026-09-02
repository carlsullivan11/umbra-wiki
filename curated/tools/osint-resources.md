---
slug: tool/osint-resources
title: Public OSINT resource directory
page_type: tool
tags: [osint, maps, aviation, maritime, land, rf, imagery, archives, lawful-use]
related:
  - tool/dns-blocklist
  - concept/email-authentication
  - concept/mitre-attack
provenance: curated
updated_at: 2026-09-01
summary: "Lawful public OSINT portals by type: land and mining claims, flight and ship trackers, imagery, RF, filings, archives. Portals to query, not scrapes."
sources:
  - name: BLM Mineral & Land Records System (MLRS)
    url: https://www.blm.gov/services/land-records
  - name: USGS EarthExplorer
    url: https://earthexplorer.usgs.gov/
  - name: OpenSky Network
    url: https://opensky-network.org/
  - name: NOAA Marine Cadastre AIS
    url: https://marinecadastre.gov/ais/
  - name: FCC Universal Licensing System
    url: https://www.fcc.gov/wireless/universal-licensing-system
  - name: CourtListener / Free Law Project
    url: https://www.courtlistener.com/
  - name: SEC EDGAR
    url: https://www.sec.gov/edgar
  - name: CISA Known Exploited Vulnerabilities
    url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
---

# Public OSINT resource directory

A working directory of **public, lawful** sources investigators actually open. Organized by *what you are looking at*, not by vendor brand.

This is **not** a people-finder, not a scrape cookbook, and not a substitute for Umbra collectors. Use these when you need a map, a tracker, a filing, or an archive that Umbra does not (and should not) bulk-ingest.

**Rules**

- Prefer the **official portal**. Paid assessors, PACER full-text, and login walls stay out of Umbra collectors; you can still *visit* them in a browser when your authorization basis allows.
- A hit on a map or tracker is **an observation**, not identity, ownership, or guilt.
- Do not scrape JS map UIs (WiGLE, Deflock, NSOPW, MarineTraffic). Query, screenshot, or export what the site offers you.
- Lawful use only. See Umbra `docs/ETHICS.md`.

Umbra already wraps some of this (DNSBL, CT, OFAC, CourtListener name search, OSM cameras). Those rows say **in Umbra**.

## Land, minerals, cadastral (US)

| Resource | What you get | Notes |
|----------|----------------|-------|
| [BLM MLRS](https://mlrs.blm.gov/s/) | Mining claims, mineral patents, land status on federal surface/minerals | Replaced LR2000. Serial numbers, claimants, township/range. Account may be required for some reports. |
| [BLM GLO Records](https://glorecords.blm.gov/) | Historic land patents, surveys, homesteads | Best for *original* federal conveyance, not current ownership. |
| [BLM GeoHub / GIS](https://gbp-blm-egis.hub.arcgis.com/) | Surface management, grazing, wildfire, PLSS layers | Downloadable ArcGIS layers. PLSS is how western parcels are described. |
| [The National Map](https://apps.nationalmap.gov/viewer/) | USGS topo, hydro, structures, geographic names | Authoritative US basemap. Pair with GNIS names. |
| [USGS EarthExplorer](https://earthexplorer.usgs.gov/) | Landsat, Sentinel (via USGS), aerial, DEMs | Free after a USGS login. Scene IDs are citable. |
| [USGS Mineral Resources / USMIN](https://www.usgs.gov/centers/national-minerals-information-center) | Deposit locations, commodity stats | Geology, not claim validity. |
| [BOEM](https://www.boem.gov/) | Offshore leases, oil/gas, wind | Outer Continental Shelf, not onshore BLM. |
| [PAD-US](https://www.usgs.gov/programs/gap-analysis-project/science/pad-us-data-overview) | Protected areas inventory | Who manages the polygon (NPS, USFS, state, easement). |
| [FEMA MSC](https://msc.fema.gov/portal/home) | Flood maps (FIRM) | Insurance/floodplain, not a title search. |
| [USFS MVUM](https://www.fs.usda.gov/visit/maps) | Motor Vehicle Use Maps | Roads that exist on the ground vs GIS fantasy. |
| County GIS / assessor | Situs, APN, owner-of-record *as published* | Varies by county. Name on an assessor page ≠ identity. Umbra `county_records` only GET allowlisted portals. |

**Canada / other:** [NRCAN geospatial](https://natural-resources.canada.ca/maps-tools-and-publications/maps) (topo, claims by province — e.g. British Columbia Mineral Titles Online). Do not assume BLM-like coverage worldwide.

## Imagery and maps

| Resource | What you get | Notes |
|----------|----------------|-------|
| [OpenStreetMap](https://www.openstreetmap.org/) | Crowdsourced map + Overpass | Umbra RF cameras use Overpass (`man_made=surveillance`). `out body`, not `out tags`. |
| [Overpass Turbo](https://overpass-turbo.eu/) | Ad-hoc OSM queries | Keep bounding boxes small. World dumps OOMs the VPS. |
| [Copernicus Browser](https://browser.dataspace.copernicus.eu/) | Sentinel-1/2/3, recent EU imagery | Free. Cloud cover and revisit matter. |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) | Near-real-time fire detections | MODIS/VIIRS thermal, not a “wildfire perimeter” product. |
| [NOAA GOES](https://www.star.nesdis.noaa.gov/goes/) | Geostationary weather/imagery | Americas. Good for event timelines. |
| [Mapillary](https://www.mapillary.com/) | Street-level photos (OSM-friendly) | Better ToS than scraping Google Street View. |
| [OpenAerialMap](https://openaerialmap.org/) | Open ortho imagery | Disaster and NGO collections. |
| [ESRI Wayback](https://livingatlas.arcgis.com/wayback/) | Dated World Imagery | When “that building wasn’t there in 2018” matters. |
| Google Earth Pro | Historical imagery slider | Free desktop. Export is on you; do not bulk-scrape. |

## Aviation

| Resource | What you get | Notes |
|----------|----------------|-------|
| [OpenSky Network](https://opensky-network.org/) | ADS-B / Mode S research data | Academic ToS. Historical API is the grown-up source. |
| [ADS-B Exchange](https://globe.adsbexchange.com/) | Unfiltered ADS-B globe | Fewer blocked military/privacy airframes than some commercial globes. Still not “secret flights.” |
| [FlightAware](https://www.flightaware.com/) | Flight status, routes, FAA SWIM-derived | Free tier is thin; ident and tail still useful. |
| [Flightradar24](https://www.flightradar24.com/) | Consumer tracker | Same caveat: blocked tracks, MLAT estimates. |
| [FAA aircraft registry](https://registry.faa.gov/aircraftinquiry/) | N-number, owner, airworthiness | US civil only. Trust but verify addresses. |
| [OurAirports](https://ourairports.com/) | Airport/runway database | Good join key with ICAO/IATA. |
| [AirNav](https://www.airnav.com/) | US airport facilities, frequencies | Pilot-facing, still public. |

Live tracks are **last-seen radio**, not a passenger list. Do not treat a hex code as a person.

## Maritime

| Resource | What you get | Notes |
|----------|----------------|-------|
| [NOAA Marine Cadastre AIS](https://marinecadastre.gov/ais/) | US AIS archives | The lawful bulk source. Prefer this over scraping commercial globes. |
| [MarineTraffic](https://www.marinetraffic.com/) | Live AIS globe | Portal only. |
| [VesselFinder](https://www.vesselfinder.com/) | Live AIS, particulars | Portal only. |
| [Equasis](https://www.equasis.org/) | IMO ship particulars, management, inspections | Free account. Quality above globes for *who manages the ship*. |
| [USCG PSIX](https://cgmix.uscg.mil/psix/) | US vessel inspections, deficiencies | Flag-state view. |
| [IMO GISIS](https://gisis.imo.org/) | IMO numbers, company, casualties | Some modules need registration. |
| [Marine Cadastre National Viewer](https://marinecadastre.gov/nationalviewer/) | Offshore planning, AIS density | BOEM/NOAA. |

AIS can be spoofed or dark. Absence of a track is not “the ship vanished.”

## Radio, towers, spectrum

| Resource | What you get | Notes |
|----------|----------------|-------|
| [FCC ULS](https://www.fcc.gov/wireless/universal-licensing-system) | US wireless licenses, coordinates, callsigns | Land mobile, microwave, amateur, cellular licenses — not live RF. |
| [FCC ASR](https://wireless2.fcc.gov/UlsApp/AsrSearch/asrRegistrationSearch.jsp) | Antenna structure registration | Towers, lighting, height. |
| [FCC Geographic Search / LMS](https://www.fcc.gov/media/radio/fm-query) | Broadcast FM/AM/TV | Facility IDs. |
| [RadioReference](https://www.radioreference.com/) | Trunked system wikis, frequencies | Crowdsourced. Good lead, cite the FCC record when it matters. |
| [KiwiSDR map](http://rx.kiwisdr.com/) | Web SDRs | Listen; do not treat a waterfall as geolocation of a *target phone*. |
| [APRS.fi](https://aprs.fi/) | Amateur radio positions | Opt-in beacons. |
| [OpenCelliD](https://opencellid.org/) | Cell tower crowdsource | MCC/MNC/LAC/CID. Messy in dense cities. |
| [WiGLE](https://wigle.net/) | Wi-Fi / Bluetooth maps | Umbra: portal + optional **one BSSID** API. No world dump, no map scrape. |

Umbra `wifi_maps` + `umbra rf sync` cover OSM cameras near packed cities. Last-seen Wi-Fi ≠ residence.

## Weather, hazards, environment

| Resource | What you get | Notes |
|----------|----------------|-------|
| [NWS](https://www.weather.gov/) | Forecasts, warnings, radar | Event timelines. |
| [USGS earthquakes](https://earthquake.usgs.gov/) | Quake catalog | Magnitude, depth, felt reports. |
| [NIFC / InciWeb](https://inciweb.wildfire.gov/) | Incident status | Wildfire ops, not FIRMS pixels. |
| [AirNow](https://www.airnow.gov/) | AQI | Smoke/plume context. |
| [EPA ECHO](https://echo.epa.gov/) | Facility enforcement/compliance | US environmental records. |
| [Envirofacts](https://www.epa.gov/enviro) | Superfund, TRI, water | Facility IDs join to orgs. |

## Companies, filings, money

| Resource | What you get | Notes |
|----------|----------------|-------|
| [SEC EDGAR](https://www.sec.gov/edgar/search/) | US public company filings | Umbra `edgar_search`. 10-K, 8-K, beneficial ownership. |
| [SAM.gov](https://sam.gov/) | US federal awards, exclusions | Entity registration. |
| [FEC](https://www.fec.gov/) | Campaign finance | Umbra hits FEC name API in county/person packs (`DEMO_KEY` limits). |
| [OpenCorporates](https://opencorporates.com/) | Company register aggregator | Often captcha. Prefer jurisdiction primary (Companies House, Sunbiz, …). |
| [UK Companies House](https://find-and-update.company-information.service.gov.uk/) | UK officers, PSCs, accounts | Gold standard among company portals. |
| [OpenSecrets](https://www.opensecrets.org/) | US lobbying / donor context | Derived, not the FEC raw file. |
| [OpenSanctions](https://www.opensanctions.org/) | Sanctions/PEP datasets | Joins OFAC and others. Umbra crypto screen uses an **owned OFAC lake**. |
| [OFAC SDN](https://sanctionssearch.ofac.treas.gov/) | US sanctions search | Names and vessels. Miss ≠ clean. |

## Courts and public records

| Resource | What you get | Notes |
|----------|----------------|-------|
| [CourtListener](https://www.courtlistener.com/) | Opinions, RECAP dockets | Umbra `court_records`. Candidates, `identity_confirmed: False`. |
| [RECAP](https://free.law/recap/) | PACER documents people already paid for | Do not scrape PACER. |
| PACER | Federal docket PDFs | Paid. Out of Umbra collectors. |
| State e-courts / SOS | Business filings, UCC, courts | Umbra L1 = 50-state SOS/courts/SOR homepages. |
| FOIA.gov / agency reading rooms | Released records | Slow. Search existing reading rooms before filing. |

A docket hit on a common name is a **lead**. Acquittals and homonyms exist.

## Archives and web history

| Resource | What you get | Notes |
|----------|----------------|-------|
| [Wayback Machine](https://web.archive.org/) | Archived pages | Umbra `wayback_cdx` (CDX). Capture ≠ the live site. |
| [archive.today](https://archive.today/) | On-demand snapshot | Different crawler than IA. |
| [Library of Congress](https://www.loc.gov/) | Newspapers, maps, photos | Rights vary by item. |
| [Chronicling America](https://chroniclingamerica.loc.gov/) | Historic US newspapers | OCR errors. |
| Wikidata / Wikipedia | Structured claims, bios | Umbra `wikidata`. Cite the claim id. |

## Domain, IP, certificates, routing

| Resource | What you get | Notes |
|----------|----------------|-------|
| [crt.sh](https://crt.sh/) | Certificate Transparency | Umbra `crtsh` + owned `ct_lake`. crt.sh is flaky; lake first. |
| [RIPE Stat](https://stat.ripe.net/) | Prefix, ASN, abuse contacts | Routing, not geolocation of a person. |
| [Hurricane Electric BGP](https://bgp.he.net/) | ASN, prefixes, whois | Fast triage. |
| [PeeringDB](https://www.peeringdb.com/) | IX and network interconnection | Infra, not users. |
| [RDAP](https://about.rdap.org/) | Registration data | Umbra `rdap_domain` / `rdap_ip`. |
| [SSL Labs](https://www.ssllabs.com/ssltest/) | TLS config of *a host you may test* | Same authorization as a probe. |
| [urlscan.io](https://urlscan.io/) | Public URL scans | Other people’s submissions. |
| [MXToolbox](https://mxtoolbox.com/) | MX, SPF, blacklist views | Complementary to Umbra DNSBL (Unbound-only). |
| Censys / Shodan search | Banner indexes | Accounts/quotas. Do not confuse with Umbra `http_probe` on an authorized host. |

Umbra `/reputation` is the first-party check for domain/IP/phone. Wiki blocklists: [tool/dns-blocklist](https://umbra-osint.com/wiki/p/tool/dns-blocklist).

## Space and orbital

| Resource | What you get | Notes |
|----------|----------------|-------|
| [CelesTrak](https://celestrak.org/) | TLEs, satcat | Public TLEs. |
| [N2YO](https://www.n2yo.com/) | Pass predictions | Derived from TLEs. |
| [space-track.org](https://www.space-track.org/) | Official SATCAT (US) | Free account, ToS. |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) | (also imagery) | Thermal, listed above. |

## Leak and journalism databases (public)

| Resource | What you get | Notes |
|----------|----------------|-------|
| [ICIJ Offshore Leaks](https://offshoreleaks.icij.org/) | Published leak graphs | Already in the news. Not a stolen-data marketplace. |
| [OCCRP Aleph](https://aleph.occrp.org/) | Investigative collections | Access rules per dataset. |
| [LittleSis](https://littlesis.org/) | US power mapping | Crowdsourced edges. |

Never buy stolen dumps. Never run crimeware-primary tools. If a “source” is a forum selling access, it is out.

## How to add a source here

Official or clearly licensed public portal, citable URL, one-line honesty about limits. No people-search vendors, no PACER scrapers, no map-UI harvest. Open a PR on `umbra-wiki` under `curated/tools/`.
