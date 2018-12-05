from collections import defaultdict

def part1(unsorted_records):
    records = sorted(unsorted_records)
    records = parse_records(records)
    guards = {}
    for id, asleep, wakes in records:
        if id not in guards.keys():
            guards[id] = defaultdict(int)
        minutes = guards[id]
        for min in range(asleep, wakes):
            minutes[min] += 1

    best_sleep = 0
    best_id = 0
    for id, minutes in guards.items():
        sleep = sum(v for v in minutes.values())
        if sleep > best_sleep:
            best_sleep = sleep
            best_id = id

    best_count = 0
    best_minute = 0
    for min, count in guards[best_id].items():
        if count > best_count:
            best_count = count
            best_minute = min
    return best_minute * best_id

def parse_records(records):
    parsed = []
    for record in records:
        if 'Guard' in record:
           id = int(record.split('#')[1].split(' ')[0])
        else:
            secs = int(record.split(':')[1].split(']')[0])
            if 'asleep' in record:
                 asleep = secs
            else:
                wakes = secs
                parsed.append((id, asleep, wakes))
    return parsed
