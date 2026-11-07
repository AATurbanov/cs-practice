def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Invalid string format")

    time = parts[0].strip()
    level = parts[1].strip()
    msg = parts[2].strip()

    if not all(('T' in time, '-' in time, ':' in time)):
        raise ValueError("Invalid time format")

    if not (level in ["DEBUG", "INFO", "WARNING", "ERROR"]):
        raise ValueError("Unknown level")

    if msg == '':
        raise ValueError("Empty message")

    return {'time': time, 'level': level, 'message': msg}


def count_levels(lines: list[str]) -> dict:
    counts = {}

    for line in lines:
        if line.strip() == '':
            continue
        try:
            event = parse_event(line)
            level = event['level']

        except ValueError:
            level = 'BROKEN'

        if level not in counts:
            counts[level] = 0

        counts[level] += 1

    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    errors = {}
    res = []

    for line in lines:
        if line.strip() == '':
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event['level'] == 'ERROR':
            msg = event['message']

            if msg not in errors:
                errors[msg] = 0
            errors[msg] += 1

    sorted_errors = sorted(errors.items(), key=lambda item: (-item[1], item[0]))
    for msg, count in sorted_errors[:n]:
        res.append([msg, count])

    return res


def format_report(counts: dict, errors: list[list]) -> str:
    report = 'Отчёт по журналу\n\n'
    for level in sorted(counts):
        report += f'{level}: {counts[level]}\n'

    report += '\nЧастые ошибки:\n'
    for error, count in errors:
        report += f'- {error.strip()} — {count}\n'

    return report


