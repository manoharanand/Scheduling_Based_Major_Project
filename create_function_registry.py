import json
import random

functions = 500
# to create a registry exactly like this
# function_registry = {
#     "function_id_1": {"package_imports": ["package_id_1", "package_id_2"]},
#     "function_id_2": {"package_imports": ["package_id_2", "package_id_3"]},
#     # Add more function registries as needed
# }
#
# {"package_id_1": {"package_size_in_MB": 107}, "package_id_2": {"package_size_in_MB": 59},
packages = open('packages.json')
packages_list = json.load(packages)
packages_list_length = len(packages_list)

functions_list = {}
for i in range(0, functions):
    #select list of packages from the list
    package_count = random.randint(1, 5)
    taken_packages = []
    while package_count:
        index = random.randint(1, packages_list_length)
        key = f"packages_id_{index}"
        taken_packages.append(key)
        package_count -= 1


    function_id = "func" + str(i+1)
    package_size = random.randint(10, 50) #package size required in MB
    functions_list[f"function_id_{i+1}"] = {"package_imports": taken_packages}


# dict_pkgs = {}
dict_funcs = {}
# dict_pkgs = packages_list
dict_funcs = functions_list


with open("C:/Users/1997m/OneDrive/Desktop/Scheduling_Based_Major_Project/function_registry/registry_of_functions.json", "w") as outfile:
    json.dump(dict_funcs, outfile)




