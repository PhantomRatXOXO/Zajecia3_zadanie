# Zajecia3_zadanie
Python Minizadanie, tydzień 3. (grupowe)
Hubert Krupniewski, Marta Muskus

Skrypt wywoływany jest poleceniem formatu:
python skrypt.py (-c) -m month_1 month_2 ... month_n -d day_11-day_12-...day_1n ... -day_mn -t time_1 ... time_n

Liczba miesięcy powinna być równa liczbie krotek dni.
Domyślny tryb, bez opcji -c to czytanie, z opcją -c, tworzenie.
Domyślna pora: ranek.
Jeśli plik o podanej ścieżce już istnieje to nie jest tworzony na nowo.

W przypadku odczytu istniejących plików wypisywana jest suma czasów zapisanych w komórce 'Czas' dla plików zawierających 'A' w komórce 'Model'.
Poprawny format pliku do odczytu:
Model;Wynik;Czas
A/B/C;(int);(int)s
