def main():
    data = []
    sleep_count = {}
    on_duty = 0
    """ LOAD DATA FROM FILE """
    with open('input.txt') as file:
        for line in file:
            line = line.split(']')
            time = dict()
            time['time'] = int(line[0][6:8] + line[0][9:11] + line[0][12:14] + line[0][15:17])
            time['event'] = line[1].strip()
            data.append(time)
        data.sort(key=lambda x: x['time'])
    file.close()
    """ FIND GUARD THAT SLEEPS THE LONGEST """
    for entry in data:
        if entry['event'] == "falls asleep":
            sleep_count[on_duty] = [sleep_count[on_duty][0], entry['time']]
        elif entry['event'] == "wakes up":
            sleep_count[on_duty] = [sleep_count[on_duty][0] + entry['time']-sleep_count[on_duty][1]]
        elif 'Guard #' in entry['event']:
            on_duty = int(entry['event'][7:11])
            if on_duty in sleep_count:
                sleep_count[on_duty] = [sleep_count[on_duty][0]]
            else:
                sleep_count[on_duty] = [0]
                
    max_sleep = 0
    max_sleep_guard = None
    for guard in sleep_count:
        if sleep_count[guard][0] > max_sleep:
            max_sleep = sleep_count[guard][0]
            max_sleep_guard = guard

    minutes = {}
    asleep_minute = 0
    sleepy_guard_on_duty = False
    for entry in data:
        if str(max_sleep_guard) in entry['event']:
            sleepy_guard_on_duty = True
        elif '#' in entry['event']:
            sleepy_guard_on_duty = False
        if sleepy_guard_on_duty and entry['event'] == 'falls asleep':
            asleep_minute = entry['time'] % 100
        if sleepy_guard_on_duty and entry['event'] == 'wakes up':
            wake_time = entry['time'] % 100
            for i in range(asleep_minute, wake_time):
                if i in minutes:
                    minutes[i] += 1
                else:
                    minutes[i] = 1
    print(sleepiest_guard_and_time(minutes, max_sleep_guard))


def sleepiest_guard_and_time(minutes, guard):
    max_min = 0
    max_sleep = 0
    for minute in minutes:
        if minutes[minute] > max_sleep:
            max_min = minute
            max_sleep = minutes[minute]
    return guard * max_min


main()
