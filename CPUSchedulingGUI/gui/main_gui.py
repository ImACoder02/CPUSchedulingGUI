# gui/main_gui.py

import tkinter as tk
from gui.input_form import InputForm
from gui.output_view import OutputView
from controller.controller import run_fcfs

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FCFS Scheduling Algorithm")

        self.input_form = InputForm(self, self.handle_submit)
        self.input_form.pack()

        self.output_view = OutputView(self)
        self.output_view.pack()

    def handle_submit(self, process_data):
        if not process_data:
            return

        schedule, avg_times = run_fcfs(process_data)
        self.output_view.display_results(schedule, avg_times)
