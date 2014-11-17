from urllib2 import urlopen
import json
from sys import stdout
#TODO  Make this into a class(es) that can be used externally passing only query terms and limits

def find_active_datastores(url):
    datastore_active_resources = []
    parsed_json = get_json_from_ckan(url)
    dataset_list = get_all_dataset_ids(parsed_json)
    resource_list = get_all_resource_ids(parsed_json)
    datastore_active_resources = check_datastore_active(resource_list)
    return datastore_active_resources

def get_json_from_ckan(url):
    try:
        response = urlopen(url)
        jsonstring = response.read()
        data = json.loads(jsonstring)
    except Exception, e:
        print e
        return
    if data.get("success") == True:
        return data
    else:
        return False  ##TODO raise a custom exception
 
def get_all_dataset_ids(parsed_json):
        dataset_list = []
        results = parsed_json.get("result").get("results")
        for package in results:
                dataset_list.append(package.get("id"))
        return dataset_list
 
def get_all_resource_ids(parsed_json):
    resource_list = []
    results = parsed_json.get("result").get("results")
    for package in results:
                if package.get("num_resources") > 0:
                        resources = package.get("resources")
                        for resource in resources:
                                resource_id = resource.get("id")
                                resource_list.append(resource_id)
    return resource_list
 
def check_datastore_active(resource_list):
    ds_active_list = []
    for item in resource_list:
        call = "https://data.hdx.rwlabs.org/api/3/action/resource_show?id=" + item
        response = urlopen(call)
        jsonstring = response.read()
        data = json.loads(jsonstring)
        if data.get("result").get("datastore_active") == True:
            dict = {}
            dict["datastore_active"] = True
            dict["name"] = data.get("result").get("name")
            ds_active_list.append(dict)
    return ds_active_list
 
def humanize_resources(resource_list):
    for res in resource_list:
        call = "https://data.hdx.rwlabs.org/api/3/action/resource_show?id=" + resource_id
        response = urlopen(call)
        jsonstring = response.read()
        data = json.loads(jsonstring)
        return data.get("result").get("datastore_active")

 
