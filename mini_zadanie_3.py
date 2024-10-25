from pathlib import Path
import argparse
import os
import csv
import random


def file_processing():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--create",
                        action="store_true",
                        help="Podaj tryb: tworzenie -> -c, czytanie -> DEFAULT")
    parser.add_argument("-m", "--months",
                        type=str,
                        nargs="+",
                        help="Podaj miesięce w formacie: miesiac1 miesiac2 ...")
    parser.add_argument("-d", "--days",
                        type=str,
                        nargs="+",
                        help="Podaj dni w formacie: d11-d12-... d21... #krotek = #miesiecy")
    parser.add_argument("-t", "--times",
                        type=str,
                        nargs="+",
                        help="Podaj pory dnia w formacie: p1 p2 ... DEFAULT: rano")

    args = parser.parse_args()

    if len(args.months) != len(args.days):
        print("Błędne dane wejściowe.")
        return

    month_list = args.months
    month_dictionary = {}
    for i, month in enumerate(args.months):
        day_group = args.days[i]
        days = [day.strip() for day in day_group.split('-')]
        month_dictionary[month] = days
    time_list = args.times
    time_len = len(time_list)
    curr_dir = os.getcwd()
    k = 0  # Zlicza ścieżki, kiedy przekroczy time_len pobieramy default.

    if args.create:
        print("Creating files...")

        for month, days in month_dictionary.items():
            for day in days:
                if k < time_len:
                    time = time_list[k]
                    k += 1
                else:
                    time = "rano"

                path = os.path.join(curr_dir, month, day, time)

                os.makedirs(path, exist_ok=True)
                filename = os.path.join(path, "Dane.csv")
                with open(filename, "w", newline="") as my_file:
                    writer = csv.writer(my_file, delimiter=";")
                    writer.writerow(["Model", "Wynik", "Czas"])
                    model = random.choice(['A', 'B', 'C'])
                    wynik = random.randint(0, 1000)
                    czas = str(random.randint(0, 1000)) + "s"
                    writer.writerow([model, wynik, czas])

        print("All files have been successfully created.")

    else:
        print("Reading files...")


if __name__ == "__main__":
    file_processing()
