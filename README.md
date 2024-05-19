# Tokenizacja za pomocą białych znaków oraz wyrażen regularnych

Wybrałem tokenizacje za pomocą użycia metody białych znaków oraz wyrażeń regularnych. Tokenizacja oparta na białych znakach jest prostym sposobem podziału tekstu na poszczególne tokeny, co sprawia, że jest szybka i łatwa w implementacji. Z kolei tokenizacja oparta na wyrażeniach regularnych pozwala na dokładniejsze dopasowanie, co jest przydatne w przypadku bardziej złożonych danych wejściowych.

# Implementacja

1. Tokenizer oparty na białych znakach (whiteSpaceTokenizer):
Ta funkcja to sposób na tokenizację, która dzieli tekst na tokeny, na podstawie tak zwanych białych znaków (spacje, tabulatory, nowe linie). Jest to szybki i prosty sposób podziału tekstu na części.

2. Tokenizer oparty na wyrażeniach regularnych (regexTokenizer):
Ta funkcja używa wyrażeń regularnych do znajdowania różnych typów tokenów, takich jak daty, liczby, słowa, znaki interpunkcyjne. Jest to bardziej precyzyjny sposób tokenizacji, który uwzględnia różne wzorce w tekście.

# Wybór Metod:

- Tokenizacja oparta na białych znakach jest szybka i jedną z najprostszych w użyciu, co czyni ją odpowiednią do prostych zastosowań, gdzie tekst jest dzielony spacjami lub innymi białymi znakami.

- Tokenizacja oparta na wyrażeniach regularnych jest preferowana w przypadku bardziej złożonych danych wejściowych. Na przykład w przypadku analizy tekstu zawierającego daty, liczby, skomplikowane słowa lub znaki interpunkcyjne.

# Wyzwania i Rozwiązania:

1. Tokenizacja dla białych znaków (Whitespace):

2. Tokenizacja dla wyrażeń regularnych:

- Wyższe Obciążenie Obliczeniowe: Tokenizacja oparta na wyrażeniach regularnych może pobierać więcej mocy obliczeniowej w porównaniu z prostszymi metodami (tymbardziej z długimi i bardziej skomplikowanymi danymi wejściowymi).

- Ryzyko Przechwytywania Nieprawidłowych Tokenów: Niewłaściwie zdefiniowane wzorce wyrażeń regularnych mogą doprowadzić do przechwytywania nieprawidłowych tokenów lub pominięcia części tekstu, co może prowadzić do błędów w analizie tekstu. 

Na przykład: 
Tekst: we]soly 
Tokenizer: 'we', 'soly'







 


