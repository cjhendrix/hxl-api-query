from hdxapi import get_datasets_with_active_datastores

url = "https://data.hdx.rwlabs.org/api/3/action/package_search?rows=10"
temp = [{"package_title": "Really cool data","package_name": "really-cool-data","resource_name": "cool.csv"}]




items = temp#get_datasets_with_active_datastores(url)
print items
print len(items)