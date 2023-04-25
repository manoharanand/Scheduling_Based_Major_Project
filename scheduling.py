# First fit
import random
import time
from datetime import datetime, date


# Function - F_id,Arrival_time,No_Instruction,Exec_Time
# Worker - W_id, Threshold_Instruction

def main(req_no, func_no, worker_no):
    print(f"\t\t{datetime.now().time()}\t Auto_Fit completed\n")

    req = req_no

    req_details = dict()

    fn = func_no
    fn_details = dict()

    worker = worker_no
    worker_details = dict()

    instruction_running_time = 1
    # preparing workers
    for w in range(worker):
        worker_details[w] = random.randint(20, 20)

    for f in range(fn):
        fn_details[f] = random.randint(1, 20)

    for r in range(req):
        req_details[r] = list()
        _f = random.randint(0, fn - 1)
        _at = random.randint(1, 20)
        req_details[r].append((_f, _at))
        # _f = random.randint(1, fn)
        # _at = random.randint(1, 20)
        # req_details[r].append((_f, _at))

    # print(req_details)
    # print(fn_details)
    # print(worker_details)

    req_func = dict()

    for key, value in req_details.items():
        for val in value:
            req_func[(key, val[0])] = val[1]

    sorted_req_func = sorted(req_func.items(), key=lambda kv: (kv[1]), reverse=False)

    # print(sorted_req_func)

    # Mapping Started

    mapping_RF_to_worker = dict()
    mapping_worker_to_RF = dict()

    waiting_time = dict()

    wt_time = []

    start_time = datetime.now().time()

    print(req_func)

    print(sorted_req_func[0])

    assigned_function = 0
    i = 0

    #for key, value in sorted_req_func:
    while i < len(sorted_req_func):
        key, value = sorted_req_func[i]
        _instruction_count = fn_details[key[1]]

        eligible_workers = []

        _to_unallocate = []
        for mapped_RF, mapped_worker in mapping_RF_to_worker.items():
            if req_func[mapped_RF] + fn_details[mapped_RF[1]] * instruction_running_time <= value:
                worker_details[mapped_worker] += fn_details[mapped_RF[1]]
                _to_unallocate.append(mapped_RF)

        for unallocate in _to_unallocate:
            mapping_RF_to_worker.pop(unallocate)

        # time.sleep(_instruction_count * instruction_running_time / 1000)

        for w, ic in worker_details.items():
            if ic >= _instruction_count:
                eligible_workers.append([w, ic - _instruction_count])

        # print(eligible_workers)
        eligible_workers.sort(key=lambda x: x[1])
        # print(eligible_workers)

        if len(eligible_workers) == 0:
            sorted_req_func.append((key, value))
            i += 1
            print([i,len(sorted_req_func)])
            continue
        i += 1
        print([i, len(sorted_req_func)])
        mapping_RF_to_worker[key] = eligible_workers[0][0]
        worker_details[eligible_workers[0][0]] -= _instruction_count
        assigned_function += 1
        end_time = datetime.now().time()
        # print(end_time)
        duration = datetime.combine(date.min, end_time) - datetime.combine(date.min, start_time)
        # print(duration.microseconds / 1000)
        # waiting_time[key] = (duration.microseconds / 1000) + _instruction_count * instruction_running_time
        waiting_time[key] = (duration.microseconds / 1000)
        wt_time.append(waiting_time[key])
        # print(waiting_time[key])
    # print(mapping_RF_to_worker)

    # logging.info(f"\t\tThe revenue to cost ratio is {(revenue / tot_cost) * 100:.4f}%")
    # logging.info(f"\t\tTotal number of requests embedded is {accepted} out of {len(vne_list)}")
    # logging.shutdown()
    output_dict = {
        "total_request": req_no,
        "total_worker": worker_no,
        "total_function": func_no,
        "avg_waiting_time": sum(wt_time) / req_no,
        "assigned_function": assigned_function,
        # "wt_assigned_ratio": assigned_function / (sum(wt_time) / req_no)
    }
    print(f"\t\t{datetime.now().time()}\t Auto_Fit completed\n")
    return output_dict
