# srtf.py
def srtf(processes):
    processes.sort(key=lambda x: x[1]) 
    gantt_chart = []
    current_time = 0
    remaining_burst_times = {process[2]: process[0] for process in processes}
    completion_times = {}  
    processes_left = processes[:]  

    while processes_left:
        ready_queue = [p for p in processes_left if p[1] <= current_time]
        
        if ready_queue:
            # Find the process with the shortest remaining burst time
            shortest_process = min(ready_queue, key=lambda x: remaining_burst_times[x[2]])
            gantt_chart.append((shortest_process[2], current_time, current_time + 1))
            current_time += 1

            # Reduce the remaining burst time for the chosen process
            remaining_burst_times[shortest_process[2]] -= 1

            # If the process has finished, remove it and record its completion time
            if remaining_burst_times[shortest_process[2]] == 0:
                processes_left.remove(shortest_process) 
                completion_times[shortest_process[2]] = current_time  # Store completion time
        else:
            # If no process is ready, increment time
            current_time += 1

    return gantt_chart, completion_times
