# package_list = {
#     "package_id_1": {"package_size_in_MB": 200},
#     "package_id_2": {"package_size_in_MB": 150},
#     "package_id_3": {"package_size_in_MB": 300},
#     # Add more packages as needed
# }

import json
import random

packages = 100
# packages_list = []
packages_dict = {}
for i in range(0, packages):
    # packages_list.append({f"package_id_{i+1}": {"package_size_in_MB": random.randint(50, 200)}})
    packages_dict[f"packages_id_{i+1}"] = {"package_size_in_MB": random.randint(50, 200)}

with open("C:/Users/1997m/OneDrive/Desktop/Scheduling_Based_Major_Project/packages.json", "w") as outfile:
    json.dump(packages_dict, outfile)

