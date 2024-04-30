import matplotlib.pyplot as plt

# Data for performance comparison
scheduling_algorithms = ['FCFS', 'SJN', 'RR (Quantum = 10)', 'Priority']
average_waiting_times = [25, 15, 20, 12]
turnaround_times = [65, 55, 60, 50]
cpu_utilization = [60, 70, 65, 75]
response_times = [40, 30, 35, 25]
fairness_indices = [0.45, 0.35, 0.40, 0.50]

# Plotting the performance comparison graph
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Average Waiting Time
axes[0, 0].bar(scheduling_algorithms, average_waiting_times, color='skyblue')
axes[0, 0].set_title('Average Waiting Time (ms)')
axes[0, 0].set_ylabel('Time (ms)')

# Turnaround Time
axes[0, 1].bar(scheduling_algorithms, turnaround_times, color='lightgreen')
axes[0, 1].set_title('Turnaround Time (ms)')

# CPU Utilization
axes[1, 0].bar(scheduling_algorithms, cpu_utilization, color='orange')
axes[1, 0].set_title('CPU Utilization (%)')
axes[1, 0].set_ylabel('Utilization (%)')

# Response Time
axes[1, 1].bar(scheduling_algorithms, response_times, color='lightcoral')
axes[1, 1].set_title('Response Time (ms)')

# Adjusting layout
plt.tight_layout()
plt.show()
