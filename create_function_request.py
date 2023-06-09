

# import time
import random
import json


requests = []
for i in range(1,10):
    requests.append(i*100)

# curr_time = time.ctime()
# print(curr_time)
timestamplim = 10
initial = 1
m = -1
for total_request in requests:
    functions_list = []
    for i in range(0, total_request):
        fid = "function_id_" + str(random.randint(1, 500))
        cpu_required = random.randint(10,60)
        arrival_time = random.randint(initial, timestamplim)
        m = max(m,arrival_time)
        deadline = arrival_time + random.randint(10, 25)
        functions_list.append({"function_id": fid, "cpu_required": cpu_required, "arrival_time": arrival_time, "deadline": deadline})
    functions_list.sort(key=lambda x: x["arrival_time"])
    with open(f"/home/pgcse/PycharmProjects/Scheduling_Based_Major_Project/function_requests/request{total_request}.json", "w") as outfile:
        json.dump(functions_list, outfile)
    initial = m
    timestamplim += m

