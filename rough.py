# from datetime import datetime
# import time
#
# # current datetime
# now = datetime.now()
# current_time = now.time()
# time.sleep(3)
# end_time = now.time()
# print('Time', end_time - current_time)
# # print(type(current_time))
import copy

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
#         required_packages = [package_list.get(package_id) for package_id in package_ids]
#
#         # Check the availability of worker resources
#         available_worker = None
#         best_finish_time = float('inf')
#
#         for worker in worker_list:
#             if worker["available_cpu"] >= request["cpu_requirement"] and \
#                worker["available_memory"] >= sum(package["package_size_in_MB"] for package in required_packages):
#                 finish_time = max(current_time, request["arrival_time"]) + (request["deadline"] - current_time)
#                 if finish_time < best_finish_time:
#                     best_finish_time = finish_time
#                     available_worker = worker
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
#         # Remove finished requests from the worker
#         for worker in worker_list:
#             worker["scheduled_requests"] = [req for req in worker.get("scheduled_requests", [])
#                                             if req["finish_time"] > current_time]
#
#     return scheduled_requests
import math

def schedule_function_requests(worker_list, package_list, function_registry, function_requests):
    scheduled_requests = []
    current_time = 0

    # Sort function requests based on their CPU requirements in descending order
    sorted_requests = sorted(function_requests, key=lambda x: x["cpu_requirement"], reverse=True)

    for request in sorted_requests:
        function_id = request["function_id"]

        # Fetch the required packages from the package list based on the function ID
        function_info = function_registry.get(function_id)
        package_ids = function_info["package_imports"]
        required_packages = [package_list.get(package_id) for package_id in package_ids]

        # Check the availability of worker resources
        best_fit_worker = None
        best_fit_gap = math.inf

        for worker in worker_list:
            if worker["available_cpu"] >= request["cpu_requirement"] and \
               worker["available_memory"] >= sum(package["package_size_in_MB"] for package in required_packages):
                cpu_gap = worker["available_cpu"] - request["cpu_requirement"]
                if cpu_gap < best_fit_gap:
                    best_fit_gap = cpu_gap
                    best_fit_worker = worker

        if best_fit_worker is None:
            # If no available worker can handle the request, skip scheduling it
            continue

        # Update the worker resources
        best_fit_worker["available_cpu"] -= request["cpu_requirement"]
        best_fit_worker["available_memory"] -= sum(package["package_size_in_MB"] for package in required_packages)

        # Calculate the start and finish times of the request
        start_time = max(current_time, request["arrival_time"])
        finish_time = start_time + (request["deadline"] - start_time)

        # Add the scheduled request to the list
        scheduled_request = {
            "function_id": function_id,
            "start_time": start_time,
            "finish_time": finish_time,
            "worker_id": best_fit_worker["worker_id"]
        }
        scheduled_requests.append(scheduled_request)

    # Check for completed tasks and free up worker resources
    for worker in worker_list:
        completed_requests = [req for req in scheduled_requests if req["finish_time"] <= current_time and
                              req["worker_id"] == worker["worker_id"]]
        for request in completed_requests:
            function_id = request["function_id"]
            function_info = function_registry.get(function_id)
            package_ids = function_info["package_imports"]
            required_packages = [package_list.get(package_id) for package_id in package_ids]
            worker["available_cpu"] += request["cpu_requirement"]
            worker["available_memory"] += sum(package["package_size_in_MB"] for package in required_packages)
            scheduled_requests.remove(request)

    return scheduled_requests
