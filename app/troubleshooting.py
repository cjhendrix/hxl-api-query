from hdxapi import get_datasets_with_active_datastores

url = "https://data.hdx.rwlabs.org/api/3/action/package_search?q=ebola&rows=100"

items = get_datasets_with_active_datastores(url)
print items
print len(items)