def main():
    data = []
    minutes = {}
    for i in range(60):
        minutes[i] = {}

   """ LOAD DATA FROM FILE """
   with open('input.txt') as file:
        for line in file:
            time = line.split(']')
            time = [int(time[0][6:8] + time[0][9:11] +
                        time[0][12:14] + time[0][15:17]), time[1].strip()]
            data.append(time)
        data.sort(key=lambda x: x[0])
    file.close()
    
    """ FIND GUARD AND MINUTE SUCH THAT THE GUARD IS MOST LIKELY ASLEEP """
    for entry in data:
        if '#' in entry[1]:
            sleeping_guard = int(entry[1][7:11])
        if entry[1] == 'falls asleep':
            asleep_time = entry[0] % 100
        if entry[1] == 'wakes up':
            wake_time = entry[0] % 100
            for i in range(asleep_time, wake_time):
                if sleeping_guard in minutes[i]:
                    minutes[i][sleeping_guard] += 1
                else:
                    minutes[i][sleeping_guard] = 1

    print(sleepiest_guard_and_time(minutes))


def sleepiest_guard_and_time(minutes):
    max_freq = 0
    max_min = 0
    max_guard = None
    for minute in minutes:
        for guard in minutes[minute]:
            if minutes[minute][guard] > max_freq:
                max_freq = minutes[minute][guard]
                max_min = minute
                max_guard = guard
    return max_guard * max_min


main()
