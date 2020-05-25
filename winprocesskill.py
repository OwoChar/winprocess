#windows process list, find, kill

import psutil
from datetime import datetime
import pandas as pd
import time
import os

def processinfo():
    # the list the contain all process dictionaries
    processes = []
    for proc in psutil.process_iter():
        try:
                process = psutil.Process(proc.pid)
                pid = process.pid
                name = process.name()
        except:
                continue
        if pid == 0:
                continue

        try:
            create_time = datetime.fromtimestamp(process.create_time())
        except OSError:
            # system processes, using boot time instead
            create_time = datetime.fromtimestamp(psutil.boot_time())

        try:
            # get the number of CPU cores that can execute this process
            cores = len(process.cpu_affinity())
        except psutil.AccessDenied:
            cores = 0

        # get the CPU usage percentage
        cpu_usage = process.cpu_percent()
        # get the status of the process (running, idle, etc.)
        status = process.status()

        try:
            # get the process priority (a lower value means a more prioritized process)
            nice = int(process.nice())
        except psutil.AccessDenied:
            nice = 0

        try:
            # get the memory usage in bytes
            memory_usage = process.memory_full_info().uss
        except psutil.AccessDenied:
            memory_usage = 0

        # total process read and written bytes
        io_counters = process.io_counters()
        read_bytes = io_counters.read_bytes
        write_bytes = io_counters.write_bytes
        # get the number of total threads spawned by this process
        n_threads = process.num_threads()

        try:
            username = process.username()
        except psutil.AccessDenied:
            username = "N/A"

        processes.append({
            'pid': pid, 'name': name, 'create_time': create_time,
            'cores': cores, 'cpu_usage': cpu_usage, 'status': status, 'nice': nice,
            'memory_usage': memory_usage, 'read_bytes': read_bytes, 'write_bytes': write_bytes,
            'n_threads': n_threads, 'username': username,
        })
    return processes

def winprocessinfo():
    processes = processinfo()
    #return processes
    memorylist = []
    for processinfo0 in processes:
        if processinfo0['memory_usage'] > 0:
                memorylist.append(processinfo0['memory_usage'])
        else:
                continue

    print ('-----------Background Processes------------')
    for processinfo1 in processes:
        if processinfo1['memory_usage'] == 0:
                print(processinfo1['pid'], processinfo1['name'], processinfo1['memory_usage'], processinfo1['status'])
        else:
                continue

    print ('-----------Foreground Processes------------')

    for memory in sorted(memorylist):
        for processinfo2 in processes:
                if memory == processinfo2['memory_usage']:
                        print(processinfo2['pid'], processinfo2['name'], processinfo2['memory_usage'],processinfo2['status'])
                else:
                        continue

def winkillid(processid):
        processes = processinfo()
        for processkillid in processes:
                if processid == processkillid['pid']:
                        killprocessid = psutil.Process(processkillid['pid'])
                        killprocessid.kill()
                        winprocessinfo()
                else:
                        continue
def winkill(name):
        processes = processinfo()
        for processkill in processes:
                if name in processkill['name']:
                        killprocess = psutil.Process(processkill['pid'])
                        killprocess.kill()
                        winprocessinfo()
                else:
                        continue

def winfind(name):
        processes = processinfo()
        for process in processes:
                if name in process['name']:
                    print(name)
                else:
                    continue
