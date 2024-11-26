# priority.py
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[3])) 
    gantt_chart = []
    current_time = 0
    completion_times = {}  

    for process in processes:
        start_time = max(current_time, process[1]) 
        finish_time = start_time + process[0] 
        gantt_chart.append((process[2], start_time, finish_time))
        current_time = finish_time  
        # Store the completion time for the process
        completion_times[process[2]] = finish_time

    return gantt_chart, completion_times
