# logic/scheduler.py

def calculate_avg_times(schedule):
    total_waiting_time = sum(p['waiting_time'] for p in schedule)
    total_turnaround_time = sum(p['turnaround_time'] for p in schedule)
    n = len(schedule)

    return {
        'avg_waiting_time': total_waiting_time / n,
        'avg_turnaround_time': total_turnaround_time / n
    }
