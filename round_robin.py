# round_robin.py
def round_robin(processes, time_quantum):
    gantt_chart = []
    queue = processes[:]
    current_time = 0
    completion_times = {pid: None for _, _, pid, _ in processes} 
    
    while queue:
        process = queue.pop(0)
        burst_time, arrival_time, pid, _ = process
        if burst_time > time_quantum:
            queue.append((burst_time - time_quantum, arrival_time, pid, _))
            gantt_chart.append((pid, current_time, current_time + time_quantum))
            current_time += time_quantum
        else:
            gantt_chart.append((pid, current_time, current_time + burst_time))
            current_time += burst_time
            completion_times[pid] = current_time  # Update the completion time

    return gantt_chart, completion_times
