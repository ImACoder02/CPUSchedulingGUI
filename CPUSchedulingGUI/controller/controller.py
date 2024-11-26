# controller/controller.py

from logic.algorithms import fcfs
from logic.scheduler import calculate_avg_times

def run_fcfs(process_data):
    schedule = fcfs(process_data)
    avg_times = calculate_avg_times(schedule)
    return schedule, avg_times
