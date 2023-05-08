
from main import *
from leastLoaded import *
from worseFit import *
result = []

for i in range(10):
    resource_utilization = main()
    result.append(resource_utilization['cpu_utilization'])
print(result)
#print(schedule_function_requests_ll(worker_list, package_list, function_registry, function_requests))
#print(schedule_function_requests_wr(worker_list, package_list, function_registry, function_requests))