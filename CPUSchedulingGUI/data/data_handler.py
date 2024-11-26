import csv

def read_process_data(file_path):
    """
    Reads process data from a CSV file and returns it as a list of dictionaries.
    Each dictionary contains the process information like process ID, arrival time, burst time, and priority.
    """
    processes = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert values to appropriate types (e.g., integers for arrival_time and burst_time)
                process = {
                    'process': int(row['process']),
                    'arrival_time': int(row['arrival_time']),
                    'burst_time': int(row['burst_time']),
                    'priority': int(row['priority']) if 'priority' in row else None,
                }
                processes.append(process)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error reading the file: {e}")
    
    return processes


def validate_process_data(process_data):
    """
    Validates the process data to ensure that all necessary fields are present and valid.
    """
    for process in process_data:
        if 'process' not in process or 'arrival_time' not in process or 'burst_time' not in process:
            print("Error: Missing essential fields in process data.")
            return False
        
        if not isinstance(process['process'], int) or not isinstance(process['arrival_time'], int) or not isinstance(process['burst_time'], int):
            print("Error: Invalid data types in process data.")
            return False

        # If priority is given, ensure it's an integer
        if process.get('priority') is not None and not isinstance(process['priority'], int):
            print("Error: Invalid priority data.")
            return False
    
    return True


def transform_process_data(process_data):
    """
    Transforms the process data into the correct format for the scheduling algorithms.
    """
    transformed_data = []
    for process in process_data:
        transformed_process = {
            'process': process['process'],
            'arrival_time': process['arrival_time'],
            'burst_time': process['burst_time'],
            'priority': process.get('priority', None),  # priority is optional
            'original_burst_time': process['burst_time'],  # Used for calculating waiting and turnaround times
        }
        transformed_data.append(transformed_process)
    
    return transformed_data


def save_schedule_to_file(schedule, file_path):
    """
    Saves the scheduling results (processes, start time, finish time, waiting time, turnaround time)
    to a CSV file.
    """
    try:
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ['process', 'start_time', 'finish_time', 'waiting_time', 'turnaround_time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for entry in schedule:
                writer.writerow({
                    'process': entry['process'],
                    'start_time': entry['start_time'],
                    'finish_time': entry['finish_time'],
                    'waiting_time': entry['waiting_time'],
                    'turnaround_time': entry['turnaround_time'],
                })
        print(f"Schedule has been saved to {file_path}")
    except Exception as e:
        print(f"Error saving schedule to file: {e}")


def print_schedule(schedule):
    """
    Prints the scheduling results in a readable format.
    """
    print("Process | Start Time | Finish Time | Waiting Time | Turnaround Time")
    for entry in schedule:
        print(f"{entry['process']}       | {entry['start_time']}        | {entry['finish_time']}       | {entry['waiting_time']}         | {entry['turnaround_time']}")
