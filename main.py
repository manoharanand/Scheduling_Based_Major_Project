import copy
import json
from Global import *
from collections import defaultdict
from create_function_request import *
import math

#import testcases
workers = open('workers.json')
worker_list = json.load(workers)

packages = open('packages.json')
package_list = json.load(packages)

function_reg = open('function_registry/registry_of_functions.json')
function_registry = json.load(function_reg)

success_ratio_without_auto_scaling = []
resource_utilization = defaultdict(list)#to store the result

# print(requests) # request is a list in create_funciton_request.py
for x in requests:
    function_req = open(f'function_requests/request{x}.json')
    function_requests = json.load(function_req)


    # def schedule_function_requests_bin_packing(worker_list, package_list, function_registry, function_requests):
    #     scheduled_requests = []
    #     current_time = 0
    #
    #     # Sort function requests based on their CPU requirements in descending order
    #     # sorted_requests = sorted(function_requests, key=lambda x: x["required_cpu"], reverse=True)
    #
    #     for request in function_requests:
    #         function_id = request["function_id"]
    #
    #         # Fetch the required packages from the package list based on the function ID
    #         function_info = function_registry.get(function_id)
    #         package_ids = function_info["package_imports"]
    #         required_packages = [package_list.get(package_id) for package_id in package_ids]
    #
    #         # Check the availability of worker resources
    #         best_fit_worker = None
    #         best_fit_gap = math.inf
    #
    #         for worker in worker_list:
    #             if worker["available_cpu"] >= request["required_cpu"] and  worker["available_memory"] >= sum(package["package_size_in_MB"] for package in required_packages):
    #                 cpu_gap = worker["available_cpu"] - request["required_cpu"]
    #                 if cpu_gap < best_fit_gap:
    #                     best_fit_gap = cpu_gap
    #                     best_fit_worker = worker
    #
    #         if best_fit_worker is None:
    #             # If no available worker can handle the request, skip scheduling it
    #             continue
    #
    #         # Update the worker resources
    #         best_fit_worker["available_cpu"] -= request["required_cpu"]
    #         best_fit_worker["available_memory"] -= sum(package["package_size_in_MB"] for package in required_packages)
    #
    #         # Calculate the start and finish times of the request
    #         start_time = max(current_time, request["arrival_time"])
    #         finish_time = start_time + (request["deadline"] - start_time)
    #
    #         # Add the scheduled request to the list
    #         scheduled_request = {
    #             "function_id": function_id,
    #             "start_time": start_time,
    #             "finish_time": finish_time,
    #             # "worker_id": available_worker["worker_id"],
    #             "cpu_required": request["cpu_required"]
    #         }
    #         scheduled_requests.append(scheduled_request)
    #
    #     # Check for completed tasks and free up worker resources
    #     for worker in worker_list:
    #         completed_requests = [req for req in scheduled_requests if req["finish_time"] <= current_time and
    #                               req["worker_id"] == worker["worker_id"]]
    #         for request in completed_requests:
    #             function_id = request["function_id"]
    #             function_info = function_registry.get(function_id)
    #             package_ids = function_info["package_imports"]
    #             required_packages = [package_list.get(package_id) for package_id in package_ids]
    #             worker["available_cpu"] += request["required_cpu"]
    #             worker["available_memory"] += sum(package["package_size_in_MB"] for package in required_packages)
    #             scheduled_requests.remove(request)
    #
    #     return scheduled_requests

    # def schedule_function_requests_with_success_ratio(worker_list, package_list, function_registry, function_requests):
    #     scheduled_requests = []
    #     current_time = 0
    #     function_scheduled = 0
    #
    #     while function_requests:
    #         request = function_requests.pop(0)
    #         function_id = request["function_id"]
    #         # Fetch the required packages from the package list based on the function ID
    #         function_info = function_registry.get(function_id)
    #         #change here to fetch the package size from the
    #         package_ids = function_info["package_imports"]
    #         required_packages = [package_list.get(package_id) for package_id in package_ids]
    #         # Check the availability of worker resources
    #         available_worker = None
    #         best_finish_time = float('inf')
    #
    #         flag = False
    #         for req in scheduled_requests:
    #             if req["function_id"] == function_id:
    #                 flag = True
    #                 req["finish_time"] += request["deadline"]
    #                 break
    #         #logic for warm start
    #         if flag:
    #             print("fid found and it's a warm start", function_id)
    #             continue
    #         #cold start
    #         for worker in worker_list:
    #             if worker["available_cpu"] >= request["cpu_required"] and worker["available_memory"] >= sum(package["package_size_in_MB"] for package in required_packages):
    #                 finish_time = max(current_time, request["arrival_time"]) + (request["deadline"] - current_time)
    #                 if finish_time < best_finish_time:
    #                     best_finish_time = finish_time
    #                     available_worker = worker
    #
    #         #logic for auto-scaling
    #         if available_worker is None:
    #             # Add a new worker if no available worker can handle the request
    #             # new_worker = {"worker_id": len(worker_list) + 1, "available_cpu": 100, "available_memory": 1000}
    #             # worker_list.append(new_worker)
    #             # available_worker = new_worker
    #             #without auto-scaling
    #             continue
    #
    #         # Update the worker resources after scheduling the function request
    #         available_worker["available_cpu"] -= request["cpu_required"]
    #         available_worker["available_memory"] -= sum(package["package_size_in_MB"] for package in required_packages)
    #
    #         # Calculate the start and finish times of the request
    #         start_time = max(current_time, request["arrival_time"])
    #         finish_time = start_time + (request["deadline"] - start_time)
    #
    #         # Add the scheduled request to the list
    #         scheduled_request = {
    #             "function_id": function_id,
    #             "start_time": start_time,
    #             "finish_time": finish_time,
    #             "worker_id": available_worker["worker_id"],
    #             "cpu_required": request["cpu_required"]
    #         }
    #         scheduled_requests.append(scheduled_request)
    #         function_scheduled += 1
    #
    #         # Update the current time
    #         current_time = finish_time
    #         # Remove finished requests from the worker
    #         # for worker in worker_list:
    #         #     worker["scheduled_requests"] = [req for req in worker.get("scheduled_requests", [])
    #         #                                     if req["finish_time"] > current_time]
    #         #resource deallocation from worker's for every request
    #         for worker in worker_list:
    #             completed_requests = [req for req in scheduled_requests if req["finish_time"] < start_time and
    #                                   req["worker_id"] == worker["worker_id"]]
    #
    #             for request in completed_requests:
    #                 function_id = request["function_id"]
    #                 function_info = function_registry.get(function_id)
    #                 package_ids = function_info["package_imports"]
    #                 required_packages = [package_list.get(package_id) for package_id in package_ids]
    #                 worker["available_cpu"] += request["cpu_required"]
    #                 worker["available_memory"] += sum(package["package_size_in_MB"] for package in required_packages)
    #                 scheduled_requests.remove(request)
    #         # scheduled_requests.append(function_scheduled//request_size)
    #     print(f"success ratio for {request_size} is: ", function_scheduled // request_size)
    #     return scheduled_requests
    def schedule_function_requests(worker_list, package_list, function_registry, function_requests):
        scheduled_requests = []
        current_time = 0
        request_size = len(function_requests)
        request_scheduled = 0


        while function_requests:
            request = function_requests.pop(0)
            function_id = request["function_id"]
            # Fetch the required packages from the package list based on the function ID
            function_info = function_registry.get(function_id)
            #change here to fetch the package size from the
            package_ids = function_info["package_imports"]
            required_packages = [package_list.get(package_id) for package_id in package_ids]
            # Check the availability of worker resources
            available_worker = None
            best_finish_time = float('inf')

            flag = False
            for req in scheduled_requests:
                if req["function_id"] == function_id:
                    flag = True
                    req["finish_time"] += request["deadline"]
                    break
            #logic for warm start
            if flag:
                print("fid found and it's a warm start", function_id)
                continue
            #cold start
            for worker in worker_list:
                if worker["available_cpu"] >= request["cpu_required"] and worker["available_memory"] >= sum(package["package_size_in_MB"] for package in required_packages):
                    finish_time = max(current_time, request["arrival_time"]) + (request["deadline"] - current_time)
                    if finish_time < best_finish_time:
                        best_finish_time = finish_time
                        available_worker = worker

            #logic for auto-scaling
            if available_worker is None:
                # Add a new worker if no available worker can handle the request
                # new_worker = {"worker_id": len(worker_list) + 1, "available_cpu": 100, "available_memory": 1000}
                # worker_list.append(new_worker)
                # available_worker = new_worker
                #without auto-scaling
                continue

            # Update the worker resources after scheduling the function request
            available_worker["available_cpu"] -= request["cpu_required"]
            available_worker["available_memory"] -= sum(package["package_size_in_MB"] for package in required_packages)

            # Calculate the start and finish times of the request
            start_time = max(current_time, request["arrival_time"])
            finish_time = start_time + (request["deadline"] - start_time)

            # Add the scheduled request to the list
            scheduled_request = {
                "function_id": function_id,
                "start_time": start_time,
                "finish_time": finish_time,
                "worker_id": available_worker["worker_id"],
                "cpu_required": request["cpu_required"]
            }
            request_scheduled += 1
            scheduled_requests.append(scheduled_request)

            # Update the current time
            current_time = finish_time
            # Remove finished requests from the worker
            # for worker in worker_list:
            #     worker["scheduled_requests"] = [req for req in worker.get("scheduled_requests", [])
            #                                     if req["finish_time"] > current_time]
            #resource deallocation from worker's for every request
            for worker in worker_list:
                completed_requests = [req for req in scheduled_requests if req["finish_time"] < start_time and
                                      req["worker_id"] == worker["worker_id"]]

                for request in completed_requests:
                    function_id = request["function_id"]
                    function_info = function_registry.get(function_id)
                    package_ids = function_info["package_imports"]
                    required_packages = [package_list.get(package_id) for package_id in package_ids]
                    worker["available_cpu"] += request["cpu_required"]
                    worker["available_memory"] += sum(package["package_size_in_MB"] for package in required_packages)
                    scheduled_requests.remove(request)
        success_ratio_without_auto_scaling.append(request_scheduled/request_size)
        return scheduled_requests

    def calculate_utilization(worker_list):
        total_cpu = 100 * len(worker_list)
        total_memory = 1000 * len(worker_list)
        used_cpu = total_cpu - sum(worker["available_cpu"] for worker in worker_list)
        used_memory = total_memory - sum(worker["available_memory"] for worker in worker_list)
        cpu_utilization = (used_cpu / total_cpu) * 100
        memory_utilization = (used_memory / total_memory) * 100
        return cpu_utilization, memory_utilization

    def print_worker_status(worker_list):
        for worker in worker_list:
            print(f"Worker {worker['worker_id']} - CPU: {worker['available_cpu']} units, Memory: {worker['available_memory']}MB")

    # current_time = 8

    def print_assigned_requests(scheduled_requests, current_time):
        print(f"Assigned Requests at Time {current_time}:")
        for request in scheduled_requests:
            if request["start_time"] <= current_time < request["finish_time"]:
                print(f"Function ID: {request['function_id']}, Worker ID: {request['worker_id']}")


    scheduled_requests = schedule_function_requests(worker_list, package_list, function_registry, function_requests)
    # # current_time = 8  # Specify the desired time
    print_worker_status(worker_list)
    # current_time = 10  # Specify the desired time
    # print_assigned_requests(scheduled_requests, current_time)

    cpu_utilization, memory_utilization = calculate_utilization(worker_list)
    resource_utilization["cpu_utilization"].append(cpu_utilization)
    resource_utilization["memory_utilization"].append(memory_utilization)

    print(f"CPU Utilization: {cpu_utilization}%, Memory Utilization: {memory_utilization}%")

print(resource_utilization)
print("success_ratio_without_auto_scaling", success_ratio_without_auto_scaling)
