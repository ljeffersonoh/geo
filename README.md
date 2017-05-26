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
