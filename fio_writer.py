import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Запись ФИО и даты в файл")
parser.add_argument("fio", nargs="+", help="Фамилия Имя Отчество")
parser.add_argument("--file", help="Имя файла для записи результата")
args = parser.parse_args()

fio = " ".join(args.fio)
line = f"{fio} - {datetime.now():%d.%m.%Y %H:%M:%S}"

if args.file:
    with open(args.file, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print("Записано в файл", args.file)
else:
    print(line)
