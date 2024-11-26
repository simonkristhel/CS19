import tkinter as tk
from tkinter import messagebox, ttk
from fcfs import fcfs
from sjf import sjf
from priority import priority_scheduling
from round_robin import round_robin
from srtf import srtf
from utils import calculate_metrics, display_gantt_chart


def run_algorithm():
    try:
        num_processes = int(entry_num_processes.get())
        processes = []

        # Collect process details
        for i in range(num_processes):
            burst_time = int(entries_burst_time[i].get())
            arrival_time = int(entries_arrival_time[i].get())
            priority = (
                int(entries_priority[i].get()) if var_algorithm.get() == "Priority" else 0
            )
            processes.append([burst_time, arrival_time, i + 1, priority])

        # Run the selected algorithm
        if var_algorithm.get() == "FCFS":
            gantt_chart, completion_times = fcfs(processes)
        elif var_algorithm.get() == "SJF":
            gantt_chart, completion_times = sjf(processes)
        elif var_algorithm.get() == "Priority":
            gantt_chart, completion_times = priority_scheduling(processes)
        elif var_algorithm.get() == "Round Robin":
            time_quantum = int(entry_time_quantum.get())
            gantt_chart, completion_times = round_robin(processes, time_quantum)
        elif var_algorithm.get() == "SRTF":
            gantt_chart, completion_times = srtf(processes)

        # Calculate metrics
        tat, wt, avg_tat, avg_wt = calculate_metrics(processes, gantt_chart, completion_times)

        # Display the results
        result_text.set(f"Process-wise metrics:\n")
        for i in range(num_processes):
            result_text.set(
                result_text.get() + f"P{i + 1}: TAT = {tat[i]}, WT = {wt[i]}\n"
            )

        result_text.set(result_text.get() + f"\nAverage TAT: {avg_tat:.2f}\n")
        result_text.set(result_text.get() + f"Average WT: {avg_wt:.2f}")

        # Display Gantt Chart
        display_gantt_chart(gantt_chart)

    except Exception as e:
        messagebox.showerror("Input Error", f"Error: {e}")


def update_ui_for_algorithm():

    if var_algorithm.get() == "Priority":
        for priority_field in entries_priority:
            priority_field.grid() 
        for label in labels_priority:
            label.grid()  
    else:
        # Hide priority fields and label
        for priority_field in entries_priority:
            priority_field.grid_remove()
        for label in labels_priority:
            label.grid_remove()  

    # Show/hide time quantum field for Round Robin
    if var_algorithm.get() == "Round Robin":
        label_time_quantum.grid(row=2, column=0, padx=10, pady=5)
        entry_time_quantum.grid(row=2, column=1, padx=10, pady=5)
    else:
        label_time_quantum.grid_forget()
        entry_time_quantum.grid_forget()


def add_process_inputs():

    num_processes = int(entry_num_processes.get())

    # Clear previous input fields
    for widget in frame_process_inputs.winfo_children():
        widget.destroy()

    global entries_burst_time, entries_arrival_time, entries_priority, labels_priority
    entries_burst_time = []
    entries_arrival_time = []
    entries_priority = []
    labels_priority = []

    for i in range(num_processes):
        # Burst Time
        label_burst_time = tk.Label(frame_process_inputs, text=f"P{i + 1} Burst Time:")
        label_burst_time.grid(row=i, column=0, padx=5, pady=5)
        entry_burst_time = tk.Entry(frame_process_inputs, width=10)
        entry_burst_time.grid(row=i, column=1, padx=5, pady=5)
        entries_burst_time.append(entry_burst_time)

        # Arrival Time
        label_arrival_time = tk.Label(frame_process_inputs, text=f"P{i + 1} Arrival Time:")
        label_arrival_time.grid(row=i, column=2, padx=5, pady=5)
        entry_arrival_time = tk.Entry(frame_process_inputs, width=10)
        entry_arrival_time.grid(row=i, column=3, padx=5, pady=5)
        entries_arrival_time.append(entry_arrival_time)

        # Priority 
        label_priority = tk.Label(frame_process_inputs, text=f"P{i + 1} Priority:")
        label_priority.grid(row=i, column=4, padx=5, pady=5)
        entry_priority = tk.Entry(frame_process_inputs, width=10)
        entry_priority.grid(row=i, column=5, padx=5, pady=5)
        labels_priority.append(label_priority)
        entries_priority.append(entry_priority)

    
    update_ui_for_algorithm()


# Main window
root = tk.Tk()
root.title("CPU Scheduling Simulation")
root.geometry("800x600")  


title_label = tk.Label(
    root, text="CPU Scheduling Simulation", font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

label_algorithm = tk.Label(frame_top, text="Select Algorithm:", font=("Arial", 12))
label_algorithm.grid(row=0, column=0, padx=10, pady=5)

var_algorithm = tk.StringVar()
algorithm_options = ["FCFS", "SJF", "Priority", "Round Robin", "SRTF"]
dropdown_algorithm = ttk.Combobox(
    frame_top, textvariable=var_algorithm, values=algorithm_options, state="readonly"
)
dropdown_algorithm.grid(row=0, column=1, padx=10, pady=5)
dropdown_algorithm.set("FCFS") 
dropdown_algorithm.bind("<<ComboboxSelected>>", lambda event: update_ui_for_algorithm())

label_num_processes = tk.Label(frame_top, text="Number of Processes:", font=("Arial", 12))
label_num_processes.grid(row=1, column=0, padx=10, pady=5)

entry_num_processes = tk.Entry(frame_top, width=10)
entry_num_processes.grid(row=1, column=1, padx=10, pady=5)

button_add_process_inputs = tk.Button(
    frame_top, text="Add Processes", command=add_process_inputs
)
button_add_process_inputs.grid(row=1, column=2, padx=10, pady=5)

label_time_quantum = tk.Label(frame_top, text="Time Quantum (RR Only):", font=("Arial", 12))
entry_time_quantum = tk.Entry(frame_top, width=10)

frame_process_inputs = tk.Frame(root)
frame_process_inputs.pack(pady=10)

frame_results = tk.Frame(root)
frame_results.pack(pady=20)

result_text = tk.StringVar()
label_results = tk.Label(frame_results, text="Results:", font=("Arial", 12, "bold"))
label_results.pack(anchor="w")
label_output = tk.Label(
    frame_results, textvariable=result_text, justify="left", font=("Arial", 10)
)
label_output.pack(anchor="w")

button_run_algorithm = tk.Button(root, text="Run Algorithm", command=run_algorithm)
button_run_algorithm.pack(pady=10)

root.mainloop()
