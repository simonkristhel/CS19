Overview

This program simulates CPU scheduling algorithms to help users understand and visualize different scheduling techniques. It supports both non-preemptive and preemptive scheduling, with user-friendly input and output features.

How to Run the Program

Prerequisites:
Python installed on your system (version 3.8 or higher).
Required Python libraries: matplotlib, numpy, and tkinter (pre-installed with Python).

Use the command below to install additional libraries if needed:

pip install matplotlib numpy

Running the Program:
Open a terminal or command prompt.
Navigate to the directory containing the program files.

Run the program using:

python main.py

User Interface:
1. Select the scheduling algorithm from the dropdown menu.
2. Enter the number of processes.
3. Provide the required input for each process:
4. Burst Time and Arrival Time for all algorithms. 
   Priority (only for Priority Scheduling).
   Time Quantum (only for Round Robin).
5. Click the Run button to execute the algorithm.
View the Gantt chart in a separate window and detailed metrics in the main window.


Files in the Project
main.py: The entry point for the program, managing the user interface.
fcfs.py: Implements the First-Come-First-Serve algorithm.
sjf.py: Implements the Shortest Job First algorithm.
priority.py: Implements the Priority Scheduling algorithm.
round_robin.py: Implements the Round Robin algorithm.
srtf.py: Implements the Shortest Remaining Time First algorithm.
utils.py: Helper functions for calculations and data validation.