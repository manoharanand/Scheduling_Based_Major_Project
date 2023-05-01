from scheduling import main as auto_fit

import copy
import os
from time import sleep
import pandas as pd
import time
import logging
import pickle


def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    # formatter = logging.Formatter('%(asctime)s %(levelname)s  : %(message)s')
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)


output_dict = {
    "algorithm": [],
    "total_request": [],
    "total_worker": [],
    "total_function": [],
    "avg_waiting_time": [],
    "assigned_function": [],
    # "wt_assigned_ratio": []
}


def exec_auto_fit(req_no, func_no, worker_no):
    #calling main() function of scheduling.py
    autofit_out = auto_fit(req_no, func_no, worker_no)

    printToExcel(
        algorithm='AUTOFIT',
        total_request=autofit_out['total_request'],
        total_worker=autofit_out['total_worker'],
        total_function=autofit_out['total_function'],
        avg_waiting_time=autofit_out['avg_waiting_time'],
        assigned_function=autofit_out['assigned_function'],
        # wt_assigned_ratio=autofit_out['wt_assigned_ratio']

    )


def printToExcel(algorithm='', total_request='', total_worker='', total_function='', avg_waiting_time='',
                 assigned_function='', wt_assigned_ratio=''):
    output_dict["algorithm"].append(algorithm)
    output_dict["total_request"].append(total_request)
    output_dict["total_worker"].append(total_worker)
    output_dict["total_function"].append(total_function)
    output_dict["avg_waiting_time"].append(avg_waiting_time),
    output_dict["assigned_function"].append(assigned_function),
    # output_dict["wt_assigned_ratio"].append(wt_assigned_ratio)
    addToExcel()


def addToExcel():
    geeky_file = open('geekyfile.pickle', 'wb')
    pickle.dump(output_dict, geeky_file)
    geeky_file.close()


def main():
    tot = 0
    requests = [25,50,100]
    for req_no in requests:
        tot += 1
        print(f"\n\treq_no: {req_no}\n")

        func_no = [100]
        worker_no = [10]

        for fn in func_no:
            for wk in worker_no:
                exec_auto_fit(req_no, fn, wk)  # Runs Autofit algorithm
                printToExcel()


        #     exec_auto_fit(req_no, func_no, worker_no)  # Runs Autofit algorithm
        #     printToExcel()



if __name__ == "__main__":
    main()
    excel = pd.DataFrame(output_dict)
    excel.to_excel("Results.xlsx")
