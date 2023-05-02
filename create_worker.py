import json
import random


workers = 5


workers_list = []
# threshold = random.randint(int(instructions/workers)*2+10 , int(instructions/workers)*4 + 20 )
available_cpu = 100
available_memory = 1000 # in MB
for i in range(0, workers):
    workers_list.append({"worker_id": i+1, "available_cpu": available_cpu, "available_memory": available_memory})

# dict = {}
# dict["workers"] = workers_list
# # dict["functions"] = functions_list
# with open("/home/pgcse/PycharmProjects/Scheduling_Based_Major_Project/workers.json, "w") as outfile:
#     json.dump(dict, outfile)


with open("/home/pgcse/PycharmProjects/Scheduling_Based_Major_Project/workers.json", "w") as outfile:
    json.dump(workers_list, outfile)

