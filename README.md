# geo
geography

[Iraq Political Risk demo](https://github.com/terramundi/geo/blob/master/notebooks/0.2-iraq-pol_risk.ipynb)


Given a Point(lon, lat), the function returns the details about the region in JSON format:

E.g.: `POINT (42.451171875 35.82672127366604)`

```json
{
  "ISO3166-2": "IQ-NI",
  "admin_level": "4",
  "alt_name": "Nīnawā",
  "alt_name:syc": "Nīnwē",
  "boundary": "administrative",
  "name": "نینوى",
  "name:ar": "نینوى",
  "name:de": "Ninawa",
  "name:en": "Nineveh",
  "name:ja": "ニーナワー",
  "name:ku": "Neynewa",
  "name:pl": "Niniwa",
  "name:ru": "Найнава",
  "name:syc": "ܢܝܢܘܐ",
  "name:uk": "Найнава",
  "source": "Wikimedia Commons",
  "wikidata": "Q189352",
  "wikipedia": "en:Nineveh Province"
}
```

The Jupyter notebook iterates through a list of (lat, lon) data points and aggregates the political risk scores by administrative region in Iraq.

Results:

```json
s = {
  "polriskevents-count": {
    "Al Anbar": 43,
    "Al-Qadisiyah": 32,
    "Babil": 58,
    "Baghdad": 66,
    "Diyala": 78,
    "Dohuk": 47,
    "Erbil": 59,
    "Halabja": 19,
    "Karbala": 7,
    "Kirkuk": 30,
    "Maysan": 29,
    "Muthanna": 20,
    "Najaf": 15,
    "Nineveh": 103,
    "Not found": 103,
    "Saladin": 68,
    "Sulaymaniyah": 51,
    "Wasit": 28
  },
  "polriskevents-max": {
    "Al Anbar": 20729,
    "Al-Qadisiyah": 23,
    "Babil": 859,
    "Baghdad": 7762,
    "Diyala": 583,
    "Dohuk": 106,
    "Erbil": 933,
    "Halabja": 85,
    "Karbala": 201,
    "Kirkuk": 1201,
    "Maysan": 142,
    "Muthanna": 104,
    "Najaf": 122,
    "Nineveh": 680,
    "Not found": 1052,
    "Saladin": 825,
    "Sulaymaniyah": 146,
    "Wasit": 120
  },
  "polriskevents-mean": {
    "Al Anbar": 531.90697674418607,
    "Al-Qadisiyah": 3.125,
    "Babil": 17.637931034482758,
    "Baghdad": 126.87878787878788,
    "Diyala": 12.435897435897436,
    "Dohuk": 4.4255319148936172,
    "Erbil": 23.338983050847457,
    "Halabja": 7.3157894736842106,
    "Karbala": 31.714285714285715,
    "Kirkuk": 48.200000000000003,
    "Maysan": 8.1724137931034484,
    "Muthanna": 12.699999999999999,
    "Najaf": 11.533333333333333,
    "Nineveh": 41.932038834951456,
    "Not found": 15.660194174757281,
    "Saladin": 24.220588235294116,
    "Sulaymaniyah": 4.882352941176471,
    "Wasit": 6.9285714285714288
  },
  "polriskevents-median": {
    "Al Anbar": 3.0,
    "Al-Qadisiyah": 1.0,
    "Babil": 1.0,
    "Baghdad": 2.0,
    "Diyala": 1.0,
    "Dohuk": 1.0,
    "Erbil": 1.0,
    "Halabja": 1.0,
    "Karbala": 3.0,
    "Kirkuk": 2.0,
    "Maysan": 0.0,
    "Muthanna": 2.0,
    "Najaf": 3.0,
    "Nineveh": 2.0,
    "Not found": 2.0,
    "Saladin": 1.5,
    "Sulaymaniyah": 1.0,
    "Wasit": 0.0
  },
  "polriskevents-min": {
    "Al Anbar": 0,
    "Al-Qadisiyah": 0,
    "Babil": 0,
    "Baghdad": 0,
    "Diyala": 0,
    "Dohuk": 0,
    "Erbil": 0,
    "Halabja": 0,
    "Karbala": 0,
    "Kirkuk": 0,
    "Maysan": 0,
    "Muthanna": 0,
    "Najaf": 0,
    "Nineveh": 0,
    "Not found": 0,
    "Saladin": 0,
    "Sulaymaniyah": 0,
    "Wasit": 0
  },
  "polriskevents-std": {
    "Al Anbar": 3157.2805493543206,
    "Al-Qadisiyah": 5.5401758444201734,
    "Babil": 112.55668330689114,
    "Baghdad": 954.42358786944544,
    "Diyala": 66.620965021177682,
    "Dohuk": 15.549003436332816,
    "Erbil": 125.05869107239644,
    "Halabja": 19.48518705632263,
    "Karbala": 74.738910628298299,
    "Kirkuk": 218.71732662392628,
    "Maysan": 28.180627800871147,
    "Muthanna": 26.399960127561599,
    "Najaf": 30.856503520713577,
    "Nineveh": 117.75200444869188,
    "Not found": 103.51011633785198,
    "Saladin": 106.12873702974802,
    "Sulaymaniyah": 20.447637573884691,
    "Wasit": 23.063404668882583
  },
  "polriskevents-sum": {
    "Al Anbar": 22872,
    "Al-Qadisiyah": 100,
    "Babil": 1023,
    "Baghdad": 8374,
    "Diyala": 970,
    "Dohuk": 208,
    "Erbil": 1377,
    "Halabja": 139,
    "Karbala": 222,
    "Kirkuk": 1446,
    "Maysan": 237,
    "Muthanna": 254,
    "Najaf": 173,
    "Nineveh": 4319,
    "Not found": 1613,
    "Saladin": 1647,
    "Sulaymaniyah": 249,
    "Wasit": 194
  }
}
```