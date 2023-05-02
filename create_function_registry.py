import json
import random

functions = 500



functions_list = []
for i in range(0,functions):
    function_id = "func" + str(i+1)
    package_size = random.randint(10,50) #package size required in MB
    functions_list.append({"function_id": function_id, "package_id": package_size})


# dict_pkgs = {}
dict_funcs = {}
# dict_pkgs = packages_list
dict_funcs = functions_list


with open("/home/pgcse/PycharmProjects/Scheduling_Based_Major_Project/fucntion_registry/functions.json", "w") as outfile:
    json.dump(dict_funcs, outfile)




