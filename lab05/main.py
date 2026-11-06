from logstats import *
def main():
    file_name = input('Enter file name: ').strip()

    total = 0
    count_error = 0
    count_broken = 0

    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == '':
                continue

            total += 1

            try:
                event = parse_event(line)
                if event['level'] == 'ERROR':
                    count_error += 1

            except ValueError:
                count_broken += 1

    print(total)
    print(count_error)
    print(count_broken)

    with open(file_name, "r", encoding="utf-8") as log:
        counts = count_levels(log)

    with open(file_name, "r", encoding="utf-8") as log:
        errors = top_errors(log, 3)

    report = format_report(counts, errors)

    with open('report.txt', 'w', encoding='utf-8') as rep:
        rep.write(report)


if __name__ == '__main__':
    main()