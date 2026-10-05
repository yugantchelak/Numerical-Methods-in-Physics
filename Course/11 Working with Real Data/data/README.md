# Data for Chapter 11

All files were downloaded on 5 October 2026 and are unmodified, apart from renaming the sunspot file.

| File | Contents | Source |
| :--- | :--- | :--- |
| `co2_mm_mlo.csv` | Monthly mean atmospheric CO2 at Mauna Loa Observatory, March 1958 onwards | NOAA Global Monitoring Laboratory, https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv |
| `SN_m_tot_V2.0.csv` | Monthly mean total sunspot number (version 2.0), 1749 onwards. Semicolon-separated: year; month; decimal date; sunspot number; std. dev.; number of observations; definitive flag | SILSO World Data Center, Royal Observatory of Belgium, https://www.sidc.be/SILSO/INFO/snmtotcsv.php |
| `H-H1_LOSC_4_V2-1126259446-32.txt.gz` | 32 s of LIGO Hanford strain around GW150914, 4096 Hz, starting GPS 1126259446 | Gravitational Wave Open Science Center, https://www.gwosc.org/s/events/GW150914/ |
| `L-L1_LOSC_4_V2-1126259446-32.txt.gz` | Same for LIGO Livingston | as above |

The CO2 and sunspot records are updated every month. To refresh them, download the files again from the URLs above. The notebook needs no other changes.

Please credit the data providers if you use these data elsewhere (see the acknowledgement at the end of section 11.5 of the notebook).
