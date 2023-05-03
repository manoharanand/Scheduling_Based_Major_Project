import copy
import json

# def schedule_function_requests(worker_list, package_list, function_registry, function_requests):
#     scheduled_requests = []
#     current_time = 0
#
#     while function_requests:
#         request = function_requests.pop(0)
#         function_id = request["function_id"]
#
#         # Fetch the required packages from the package list based on the function ID
#         function_info = function_registry.get(function_id)
#         package_ids = function_info["package_imports"]
#         required_packages = [package_list.get(package_id) for package_id in package_ids]#list comprehension
#
#         # Check the availability of worker resources
#         available_worker = None
#         for worker in worker_list:
#             if worker["available_cpu"] >= request["cpu_requirement"] and \
#                worker["available_memory"] >= sum(package["package_size_in_MB"] for package in required_packages):
#                 available_worker = worker
#                 break
#
#         if available_worker is None:
#             # Add a new worker if no available worker can handle the request
#             new_worker = {"worker_id": len(worker_list) + 1, "available_cpu": 100, "available_memory": 1000}
#             worker_list.append(new_worker)
#             available_worker = new_worker
#
#         # Update the worker resources
#         available_worker["available_cpu"] -= request["cpu_requirement"]
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
#             "worker_id": available_worker["worker_id"]
#         }
#         scheduled_requests.append(scheduled_request)
#
#         # Update the current time
#         current_time = finish_time
#
#     return scheduled_requests

workers = open('workers.json')
# fn = json.load(func_file)
worker_list = json.load(workers)
packages = open('packages.json')
package_list = json.load(packages)
# function_reg = open('function_registry/functions.json')
# function_registry = json.load(function_reg)
function_req = open('function_requests/request100.json')
function_requests = json.load(function_req)
#temporary function registry

function_registry = {
    "function_id_1": {"package_imports": ["package_id_1", "package_id_2"]},
    "function_id_2": {"package_imports": ["package_id_2", "package_id_3"]},
    # Add more function registries as needed
}


def schedule_function_requests(worker_list, package_list, function_registry, function_requests):
    scheduled_requests = []
    current_time = 0

    while function_requests:
        request = function_requests.pop(0)
        function_id = request["function_id"]

        # Fetch the required packages from the package list based on the function ID
        function_info = function_registry.get(function_id)
        #change here to fetch the package size from the
        # package_ids = function_info["package_imports"]
        required_packages = [package_list.get(package_id) for package_id in package_ids]

        # Check the availability of worker resources
        available_worker = None
        best_finish_time = float('inf')

        for worker in worker_list:
            if worker["available_cpu"] >= request["cpu_requirement"] and \
               worker["available_memory"] >= sum(package["package_size_in_MB"] for package in required_packages):
                finish_time = max(current_time, request["arrival_time"]) + (request["deadline"] - current_time)
                if finish_time < best_finish_time:
                    best_finish_time = finish_time
                    available_worker = worker

        if available_worker is None:
            # Add a new worker if no available worker can handle the request
            new_worker = {"worker_id": len(worker_list) + 1, "available_cpu": 100, "available_memory": 1000}
            worker_list.append(new_worker)
            available_worker = new_worker

        # Update the worker resources
        available_worker["available_cpu"] -= request["cpu_requirement"]
        available_worker["available_memory"] -= sum(package["package_size_in_MB"] for package in required_packages)

        # Calculate the start and finish times of the request
        start_time = max(current_time, request["arrival_time"])
        finish_time = start_time + (request["deadline"] - start_time)

        # Add the scheduled request to the list
        scheduled_request = {
            "function_id": function_id,
            "start_time": start_time,
            "finish_time": finish_time,
            "worker_id": available_worker["worker_id"]
        }
        scheduled_requests.append(scheduled_request)

        # Update the current time
        current_time = finish_time
        # Remove finished requests from the worker
        # for worker in worker_list:
        #     worker["scheduled_requests"] = [req for req in worker.get("scheduled_requests", [])
        #                                     if req["finish_time"] > current_time]

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

current_time = 8

def print_assigned_requests(scheduled_requests, current_time):
    print(f"Assigned Requests at Time {current_time}:")
    for request in scheduled_requests:
        if request["start_time"] <= current_time < request["finish_time"]:
            print(f"Function ID: {request['function_id']}, Worker ID: {request['worker_id']}")


#memory in megabytes, available_cpu is in Mips, here 100 instruction per second
# Example usage
# worker_list = [
#     {"worker_id": 1, "available_cpu": 100, "available_memory": 1000},
#     {"worker_id": 2, "available_cpu": 100, "available_memory": 1000},
#     {"worker_id": 3, "available_cpu": 100, "available_memory": 1000},
#     {"worker_id": 4, "available_cpu": 100, "available_memory": 1000},
#     {"worker_id": 5, "available_cpu": 100, "available_memory": 1000}
# ]
#
# package_list = {
#     "package_id_1": {"package_size_in_MB": 200},
#     "package_id_2": {"package_size_in_MB": 150},
#     "package_id_3": {"package_size_in_MB": 300},
#     # Add more packages as needed
# }
#
# function_registry = {
#     "function_id_1": {"package_imports": ["package_id_1", "package_id_2"]},
#     "function_id_2": {"package_imports": ["package_id_2", "package_id_3"]},
#     # Add more function registries as needed
# }
#
# function_requests = [
#     {"function_id": "function_id_1", "cpu_requirement": 20, "arrival_time": 0, "deadline": 10},
#     {"function_id": "function_id_2", "cpu_requirement": 30, "arrival_time": 4, "deadline": 10},
#     {"function_id": "function_id_1", "cpu_requirement": 10, "arrival_time": 2, "deadline": 10},
#     {"function_id": "function_id_2", "cpu_requirement": 40, "arrival_time": 5, "deadline": 10},
#     {"function_id": "function_id_1", "cpu_requirement": 12, "arrival_time": 0, "deadline": 10},
#     {"function_id": "function_id_1", "cpu_requirement": 30, "arrival_time": 0, "deadline": 10},
#     {"function_id": "function_id_2", "cpu_requirement": 10, "arrival_time": 0, "deadline": 10},
#     {"function_id": "function_id_2", "cpu_requirement": 20, "arrival_time": 0, "deadline": 10}]


scheduled_requests = schedule_function_requests(worker_list, package_list, function_registry, function_requests)
# # current_time = 8  # Specify the desired time
print_worker_status(worker_list)
current_time = 10  # Specify the desired time
print_assigned_requests(scheduled_requests, current_time)

cpu_utilization, memory_utilization = calculate_utilization(worker_list)
print(f"CPU Utilization: {cpu_utilization}%, Memory Utilization: {memory_utilization}%")
