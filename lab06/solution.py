from traceback import print_tb


def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}

    for path in paths:
        if '.' not in path:
            ext = ''
        else:
            ext = path.split('.')[-1].lower()

        if ext not in counts:
            counts[ext] = 0
        counts[ext] += 1

    return counts

def deepest_path(paths: list[str]) -> str:
    max_len = 0
    deepest = ''
    for path in paths:
        if path.count('/') > max_len:
            max_len = path.count('/')
            deepest = path

    return deepest

def human_size(n_bytes: int) -> str:
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    size = float(n_bytes)
    i = 0

    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1

    if i == 0:
        res = f'{int(size)} Б'
    else:
        res = f'{size:.1f} {units[i]}'

    return res
