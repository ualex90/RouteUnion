from pathlib import Path


def add_data(file_name: str, data: set) -> None:
    # Добавление данных
    shared_set = data
    for i in data_list:
        shared_set = shared_set & i
    data_list.append(data)
    statistic_file["files"].update({file_name: len(data)})
    statistic_file["shared"] = len(shared_set)


def lower_text(list_string: list) -> list:
    # Установка всех символов в нижний регистр
    result = list()
    for i in list_string:
        result.append("".join([s.lower() for s in i]))
    return result


def print_statistic() -> None:
    # Вывод на экран статистики
    max_k = max(map(len, statistic_file["files"].keys()))
    max_v = max(map(lambda x: len(str(x)), statistic_file["files"].values()))
    for k, v in statistic_file["files"].items():
        print(f'{k}{"":{"."}>{max_k - len(k) + 3}}{v}')
    print(f'{"":{"-"}>{max_k + 3 + max_v}}')
    print(f'Общих маршрутов{"":{"."}>{max_k - 12}}{statistic_file["shared"]}')
    print(
        f'{RESULT_FILE.stem}{"":{"."}>{max_k - len(RESULT_FILE.stem) + 3}}{len(result)}'
    )


# settings
BASE_DIR = Path(__file__).resolve().parent
FILES_DIR = Path(BASE_DIR, "files")
RESULT_FILE = Path(BASE_DIR, "result", "my_list.bat")

# get file list
files = FILES_DIR.glob("*.bat")

# main code
data_list = list()
statistic_file = {"files": {}, "shared": 0}
result = set()
for file in files:
    with open(file, encoding="UTF-8") as file_in:
        data = set(file_in.read().split("\n"))
    add_data(file.stem, data)
    text = lower_text(data)
    result = result | data

with open(RESULT_FILE, "w", encoding="UTF-8") as file_out:
    file_out.write("\n".join(sorted(list(result))))

print_statistic()
