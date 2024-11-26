# utils.py
import matplotlib.pyplot as plt
from tabulate import tabulate

def calculate_metrics(processes, gantt_chart, completion_times):
    tat = []
    wt = []
    total_tat = 0
    total_wt = 0

    # For each process, calculate TAT and WT
    for process in processes:
        process_id = process[2] 
        arrival_time = process[1]
        burst_time = process[0]

        # Get the completion time of the process
        finish_time = completion_times[process_id]  
        
        # Calculate TAT (Turnaround Time) and WT (Waiting Time)
        tat_i = finish_time - arrival_time  
        wt_i = tat_i - burst_time  

        tat.append(tat_i)
        wt.append(wt_i)
        total_tat += tat_i
        total_wt += wt_i

    avg_tat = total_tat / len(processes)
    avg_wt = total_wt / len(processes)

    return tat, wt, avg_tat, avg_wt


def display_gantt_chart(gantt_chart):
    fig, ax = plt.subplots(figsize=(10, 6))

    for i, (pid, start, finish) in enumerate(gantt_chart):
        ax.barh(0, finish - start, left=start, height=0.5, align='center')
        ax.text((start + finish) / 2, 0, f'P{pid}', va='center', ha='center', color='white')

    ax.set_xlabel('Time')
    ax.set_yticks([])
    ax.set_title('Gantt Chart')
    plt.show()
