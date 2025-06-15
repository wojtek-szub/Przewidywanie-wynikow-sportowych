# Przewidywanie Wyników Meczów Piłkarskich

Projekt oparty na uczeniu maszynowym, którego celem jest przewidywanie wyniku meczu piłkarskiego: **wygrana, remis lub porażka**. Model oparty jest na algorytmie **CatBoostClassifier**, a dane wejściowe pochodzą z historycznych wyników spotkań najpopularniejszych lig europejskich.
Wszystkie dane pochodzą ze strony `https://www.football-data.co.uk`
## Budowa programu
### 1. Tworzymy dwa DataFrame'y
---
#### 1.1 DataFrame Elo
Tworzymy DataFrame z historycznych wynikow lig angielskiej, hiszpańskiej, francuskiej, niemieckiej oraz włoskiej z lat 2007/2008 do 2012/2013
#### 1.1 DataFrame Data
Tworzymy DataFrame z historycznych wynikow lig angielskiej, hiszpańskiej, francuskiej, niemieckiej oraz włoskiej z lat 2013/2014 do 2024/2025
### 2. Czyścimy dane
---
- Sortujemy rosnąco względm daty
- Usuwamy puste wiersze
- Resetujemy indeksy
- Wybieramy tylko potrzebne kolumny (data, nazwy druzyn, liczba goli strzelonych przez dana druzyne, wynik meczu)
### 3. Ranking Elo
---
Kazdej druzynie przypisujemy 1500 punktów na start oraz przechodząc po kazdym meczu zmieniamy ranking wedle wzoru elo, `https://pl.wikipedia.org/wiki/Ranking_Elo_(piłka_nożna)`.
Po tej operacji w dataframie otrzymujemy odpowiedni ranking druzyn, który ma kluczowe znaczenie w przewidywaniu meczy, by rozrozniac klase zespołów.

### 4. Tworzenie parametrów
---
Chcemy dać modelowi jak najwięcej parametrów by jak najskuteczniej mógł przewidzieć wyniki.
Tworzymy parametry takie jak:
- Ranking Elo,
- Średnia liczba goli strzelonych przez druzynę gospodarzy, gdy grali jako gospodarze w ostatnich 20 oraz 3 meczach,
- Średnia liczba goli straconych przez druzynę gospodarzy, gdy grali jako gospodarze w ostatnich 20 oraz 3 meczach,
- Procent przegranych spotkań przez druzynę gospodarzy, gdy grali jako gospodarze w ostatnich 20 oraz 3 meczach,

Analogicznie gdy druzyna gospodarzy grała jako goście, oraz analogicznie dla druzyny gości. Do tworzenia parametrów wykorzystujemy funkcje Dataframeu oraz prostą analizę oraz zliczanie odpowiednich wartości dla trudniejszych parametrów.

### 5. Podział danych na treningowe oraz testowe
---
Dane dzielimy na testowe oraz treningowe. Wybieramy ostatnie dwa sezony do jako zbiory testowe co daje nam ponad 3400 meczy.
Treningowe zostają zboiry z sezonów 2013/2014 do 2022/2023. Wyrozniamy `y_train/y_test` oraz `X_train/X_test` z naszego Dataframu bez odpowiednich kolumn. W `y_train/y_test` zostają tylko wynniki spotkań, a w `X_train/X_test` zostają wszystkie parametry oraz nazwy druzyn.

### 6. Nauka Modelu
---
Wybieramy klasyfikator **CatBoost** poniewaz wykazywal najwyzszą skuteczność. Wykorzystujemy funkcje **GridSearchCV** do osiągnięcia najlepszych parametrów dostosowanych do naszego modelu.

### 7. Prezentacja wyników
---
Model osiąga skuteczność wysokości 68%. Najlpiej radzi sobie z przewidywaniem wygranej gospodarzy gdzie precyzja wynosi 77%, a najcięzej z remisem gdzie osiąga 53%. Wygraną gości przewiduje z precyzją 60%.

Dokładny kod z budową tego programu znajduje się w pliku pod nazwą `build_predictor.ipynb`
## Użyte technologie

- `CatBoost`
- `scikit-learn` (w tym `GridSearchCV`)
- `pandas`, `numpy`
- `matplotlib`
- `pickle`

##  Jak uruchomić?

1. Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki:

```bash
pip install -r requirements.txt
```

2. Otrzów plik `main.py`
3. Upewnij się, ze program odpowiednio importuje potrzebną funkcję do predykcji pod nazwą `predykcja`
```bash
from predictor import predykcja
```
4. Wpisz nazwy druzyn, których spotkanie chcesz przewidzieć, upewniając się, ze nazwy są tak samo wpisane jak w `rating.csv`
```bash
predykcja("Paris SG", "Tottenham")
```
5. Otrzymasz wykres przedstawiający prawdopodobieństwo wyniku spotkania.


![Referance Image](/projektPSI/PSGvT.png)


## Autorzy
Projekt stworzony przez Michała Podmokłego oraz Wojciech Szubę.