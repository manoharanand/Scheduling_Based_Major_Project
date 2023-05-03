import json
import random
packages = 100
# packages_list = []
packages_dict = {}
for i in range(0, packages):
    # packages_list.append({f"package_id_{i+1}": {"package_size_in_MB": random.randint(50, 200)}})
    packages_dict[f"package_id_{i+1}"] = {"package_size_in_MB": random.randint(50, 200)}

with open("/home/pgcse/PycharmProjects/Scheduling_Based_Major_Project/packages.json", "w") as outfile:
    json.dump(packages_dict, outfile)

