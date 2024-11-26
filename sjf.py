# sjf.py
def sjf(processes):
    processes.sort(key=lambda x: (x[1], x[0]))  
    gantt_chart = []
    current_time = 0
    completion_times = {} 

    for process in processes:
        start_time = max(current_time, process[1]) 
        finish_time = start_time + process[0] 
        gantt_chart.append((process[2], start_time, finish_time))  
        completion_times[process[2]] = finish_time  # Store the finish time for each process
        current_time = finish_time  # Update the current time to the finish time of this process

    return gantt_chart, completion_times  