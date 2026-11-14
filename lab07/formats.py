import json

def csv_to_records(text: str) -> list[dict]:
    records = []
    text = text.splitlines()
    if text != []:
        titles = text.pop(0).split(',')

    for line in text:
        record = {}

        for item in line.split(','):
            record[titles[line.split(',').index(item)].strip()] = item.strip()

        records.append(record)

    return records


# print(csv_to_records("id,город\n1,Азов\n2,Шахты"))
# # [{"id": "1", "город": "Азов"}, {"id": "2", "город": "Шахты"}]
def parse_type(value):
    if value.lower() == 'no' or value.lower() == 'false':
        value = False

    elif value.lower() == 'yes' or value.lower() == 'true':
        value = True

    else:
        if '.' in value or ',' in value:
            try:
                value = float(value.replace(',', '.'))

            except ValueError:
                value = value
        else:
            try:
                value = int(value)

            except ValueError:
                value = value

    return value

def parse_settings(lines: list[str]) -> dict:
    settings = {}
    for line in lines:
        line = line.split('#')[0].strip()
        if line == '' or line == '':
            settings[''] = ""

        elif len(line.split(':')) == 1 or line.split(':')[1].strip() == '':
            if not line.startswith('- '):
                key = line.replace(':', '').strip()
                settings[key] = []
            else:
                value = line.replace('- ', '')
                settings[key].append(parse_type(value))

        else:
            key, value = (line.split(':'))[0].strip(), (line.split(':')[1]).strip()
            settings[key] = parse_type(value)



    return settings

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    for row in rows:
        if key in row and row[key] in extra.keys():
            value = row[key]
            rows[rows.index(row)] = extra[value] | row

    return rows

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, sort_keys=True, indent=2, ensure_ascii=False)

print(parse_settings([""]))
