from datetime import datetime
import time

# # current datetime
# now = datetime.now()
# current_time = now.time()
# time.sleep(3)
# end_time = now.time()
# print('Time', end_time - current_time)
# # print(type(current_time))

# import time
requests = [100, 200, 300, 400, 500]
import random
import json
# curr_time = time.ctime()
# print(curr_time)
timestamplim = 10
for total_request in requests:
    functions_list = []
    for i in range(0, total_request):
        fid = "func" + str(random.randint(1, 500))
        cpu_required = random.randint(10,25)
        arrival_time = random.randint(1, timestamplim)
        deadline = arrival_time + random.randint(10, 25)
        functions_list.append({"fid": fid, "cpu_required": cpu_required, "arrival_time": arrival_time, "deadline": deadline})

    with open(f"/home/pgcse/PycharmProjects/Scheduling_Based_Major_Project/function_requests/request{total_request}.json", "w") as outfile:json.dump(functions_list, outfile)

#
# functions_list.sort(key=lambda x: x["timestamp"])
# dict = {}
# dict["workers"] = workers_list
# dict["functions"] = functions_list
# with open("/home/pgcse/Downloads/CHR/fs_major_least_loaded/requests/request1.json", "w") as outfile:
#     json.dump(dict, outfile)
#
# # with open("C:/Users/student/Desktop/CHR/CHR/least_loaded/test/2.json", "w") as outfile:
# #     json.dump(dict, outfile)
# #
# # with open("C:/Users/student/Desktop/CHR/CHR/improvedPaSch/test/2.json", "w") as outfile:
# #     json.dump(dict, outfile)