import re
import matplotlib.pyplot as plt

# Function to convert time string to seconds
def convert_time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def convert_time_to_seconds_shorter(time_str):
    m, s = map(int, time_str.split(':'))
    return m * 60 + s

# Lists to store points and times
points = []
times = []

# Read the file
with open('china_sample-9900781.out', 'r') as file:
    for line in file:
        match1 = re.search(r'\|\s+(\d+)/\d+\s+\[(\d{2}:\d{2})', line)
        if match1:
            points.append(int(match1.group(1)))
            times.append(convert_time_to_seconds_shorter(match1.group(2)))

        match2 = re.search(r'\|\s+(\d+)/\d+\s+\[(\d{1}:\d{2}:\d{2})', line)
        if match2:
            points.append(int(match2.group(1)))
            times.append(convert_time_to_seconds(match2.group(2)))

        match3 = re.search(r'\|\s+(\d+)/\d+\s+\[(\d{2}:\d{2}:\d{2})', line)
        if match3:
            points.append(int(match3.group(1)))
            times.append(convert_time_to_seconds(match3.group(2)))

# Plotting
plt.plot(times, points)
plt.xlabel('Time (seconds)')
plt.ylabel('Points')
plt.title('Points Over Time')
plt.show()