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

functions_list = {}
for i in range(0,functions):
    function_id = "func" + str(i+1)
    package_size = random.randint(10,50) #package size required in MB
    functions_list.append({"function_id": function_id, "package_id": package_size})


# dict_pkgs = {}
dict_funcs = {}
# dict_pkgs = packages_list
dict_funcs = functions_list


with open("/home/pgcse/PycharmProjects/Scheduling_Based_Major_Project/function_registry/functions.json", "w") as outfile:
    json.dump(dict_funcs, outfile)




