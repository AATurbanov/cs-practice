def csv_to_records(text: str) -> list[dict]:
    records = []
    text = text.splitlines()
    titles = text.pop(0).split(',')

    for line in text:
        record = {}

        for item in line.split(','):
            record[titles[line.split(',').index(item)]] = item

        records.append(record)

    return records


# print(csv_to_records("id,город\n1,Азов\n2,Шахты"))
# # [{"id": "1", "город": "Азов"}, {"id": "2", "город": "Шахты"}]

def parse_settings(lines: list[str]) -> dict:
    settings = {}
    for line in lines:
        line = line.split('#')[0].strip()
        if line == '' or line == '':
            continue

        if len(line.split(':')) == 1 or line.split(':')[1].strip() == '':
            if not line.startswith('- '):
                key = line
                settings[key] = []
            else:
                value = line.replace('- ', '')
                settings[key].append(value)

        else:
            key, value = (line.split(':'))[0].strip(), (line.split(':')[1]).strip()

            if value.lower() == 'no' or value.lower() == 'false':
                settings[key] = False

            elif value.lower() == 'yes' or value.lower() == 'true':
                settings[key] = True

            else:
                if '.' in value or ',' in value:
                    try:
                        settings[key] = float(value.replace(',', '.'))

                    except ValueError:
                        settings[key] = value
                else:
                    try:
                        settings[key] = int(value)

                    except ValueError:
                        settings[key] = value

    return settings

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    for row in rows:
        if key in row:
            value = row[key]
            rows[rows.index(row)] = extra[value] | row

    return rows

def records_to_json(records: list[dict]) -> str:
    json_str = ''
    for record in records:
        json_str += str(dict(sorted(record.items())))[1:-1] + '  '

    return json_str
