from urllib2 import urlopen
import json
from sys import stdout
import dateutil.parser
import datetime
'''
Ideas:  
Lookup by ckan id paste in an id, get a link to the thing
'''

# MAIN FUNCTIONS
def get_datasets_with_active_datastores(url):  #2nd version main 
    dataset_list = []
    parsed_json = get_json_from_ckan(url)
    results = parsed_json.get("result").get("results")
    for package in results:
        if package.get("num_resources") > 0:
            resources = package.get("resources")
            for resource in resources:
                resource_id = resource.get("id")
                resource_dict = check_datastore_active(resource_id)
                if resource_dict == False:
                    continue
                else: 
                    resource_dict["package_title"] = package.get("title")
                    resource_dict["package_name"] = package.get("name")
                    resource_dict["revision_timestamp"] = \
                    dateutil.parser.parse(package.get(
                        "revision_timestamp")).strftime('%Y-%m-%d %H:%M')
                    dataset_list.append(resource_dict)
    return dataset_list

#HELPER FUNCTIONS       
def check_datastore_active(resource_id):
    call = "https://data.hdx.rwlabs.org/api/3/action/resource_show?id=" + resource_id
    resource_dict = {}
    response = urlopen(call)
    jsonstring = response.read()
    data = json.loads(jsonstring)
    if data.get("result").get("datastore_active") == True:
        resource_dict = {}
        resource_dict["resource_name"] = data.get("result").get("name")
    if len(resource_dict) > 0:
        return resource_dict
    else:
        return False

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
'''
def humanize_resources(resource_list):
    for res in resource_list:
        call = "https://data.hdx.rwlabs.org/api/3/action/resource_show?id=" + resource_id
        response = urlopen(call)
        jsonstring = response.read()
        data = json.loads(jsonstring)
        return data.get("result").get("datastore_active")
'''
 
