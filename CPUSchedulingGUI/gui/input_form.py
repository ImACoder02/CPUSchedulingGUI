# gui/input_form.py

import tkinter as tk

class InputForm(tk.Frame):
    def __init__(self, parent, submit_callback):
        super().__init__(parent)
        self.submit_callback = submit_callback

        tk.Label(self, text="Process").grid(row=0, column=0)
        tk.Label(self, text="Arrival Time").grid(row=0, column=1)
        tk.Label(self, text="Burst Time").grid(row=0, column=2)

        self.entries = []
        for i in range(5):  # Limit to 5 processes for simplicity
            process = tk.Entry(self, width=10)
            arrival = tk.Entry(self, width=10)
            burst = tk.Entry(self, width=10)
            process.grid(row=i + 1, column=0)
            arrival.grid(row=i + 1, column=1)
            burst.grid(row=i + 1, column=2)
            self.entries.append({'process': process, 'arrival_time': arrival, 'burst_time': burst})

        tk.Button(self, text="Submit", command=self.submit).grid(row=6, column=1, pady=10)

    def submit(self):
        data = []
        for entry in self.entries:
            process = entry['process'].get()
            arrival_time = entry['arrival_time'].get()
            burst_time = entry['burst_time'].get()

            if process and arrival_time.isdigit() and burst_time.isdigit():
                data.append({
                    'process': process,
                    'arrival_time': int(arrival_time),
                    'burst_time': int(burst_time)
                })

        self.submit_callback(data)
