# gui/output_view.py

import tkinter as tk

class OutputView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.result_label = tk.Label(self, text="", justify="left", anchor="w")
        self.result_label.pack()

    def display_results(self, schedule, avg_times):
        result_text = "Schedule:\n"
        for p in schedule:
            result_text += f"Process {p['process']}: Start {p['start_time']}, Finish {p['finish_time']}, Waiting {p['waiting_time']}, Turnaround {p['turnaround_time']}\n"

        result_text += f"\nAverage Waiting Time: {avg_times['avg_waiting_time']:.2f}"
        result_text += f"\nAverage Turnaround Time: {avg_times['avg_turnaround_time']:.2f}"

        self.result_label.config(text=result_text)
