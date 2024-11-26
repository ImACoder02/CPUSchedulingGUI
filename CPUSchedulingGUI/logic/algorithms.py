# logic/algorithms.py

def fcfs(processes):
    """
    FCFS Scheduling Algorithm
    :param processes: List of dictionaries with 'process', 'arrival_time', 'burst_time'
    :return: Process schedule with start and finish times
    """
    processes.sort(key=lambda x: x['arrival_time'])  # Sort by arrival time
    current_time = 0
    schedule = []

    for process in processes:
        start_time = max(current_time, process['arrival_time'])
        finish_time = start_time + process['burst_time']
        schedule.append({
            'process': process['process'],
            'start_time': start_time,
            'finish_time': finish_time,
            'waiting_time': start_time - process['arrival_time'],
            'turnaround_time': finish_time - process['arrival_time']
        })
        current_time = finish_time

    return schedule
