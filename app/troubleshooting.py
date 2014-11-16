from hdxapi import find_active_datastores

url = "https://data.hdx.rwlabs.org/api/3/action/package_search?q=ebola&rows=100"

items = find_active_datastores(url)
print items
print len(items)