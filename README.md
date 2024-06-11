# AplikacjaZDanymiOZanieczyszczeniuPowietrza
Pod dołączonym adresem znajduje się opis API serwującego dane o zanieczyszczeniu powietrza na świecie. Należy skonstruować klienta do tego API, który będzie w stanie pobrać dane dla jednej dowolnej stacji w Warszawie, a następnie przesłać je do aplikacji back-endowej. Następnie należy napisać aplikację backendową, która będzie przyjmowała pojedynczy odczyt dla danego timestampu o pogodzie i zanieczyszczeniu na podstawie danych historycznych, wykona walidację tych danych i umieści je w persystencji (całkowicie akceptowalnym rozwiązaniem jest lista/słownik w pamięci). Aplikacja powinna posiadać również endpoint, który będzie potrafił zwrócić posiadany odczyt pogody lub zanieczyszczenia najbliższy podanej dacie i godzinie.

WSKAZÓWKI:
1. nazwy zmiennych, pól powinny coś oznaczać, proszę nie przepisywać biernie skrótów ze źródłowego API;
2. nie każde pole w modelu musi zostać zwalidowane, ale proszę wykonać przynajmnie 3 walidację dla danych pogodowych (zgodnie ze swoją wiedzą na temat temperatury, ciśnienia itp.);
3. konstruując endpointy w aplikacji, proszę zastosować widoki oparte o klasy, wstrzykiwanie zależności, architekturę trójwarstwową.

KRYTERIA OCENIANIA:
5 ptk. - prawidłowa, zgodna z założeniami konstrukcja klienta, wraz z możliwością skonfigurowania stacji, którą się wybiera za pomocą np. zmiennych środowiskowych lub argumentów przekazywanych przy wywoływaniu klienta.
10 ptk. - prawidłowa konstrukcja aplikacji backendowej:
- 2 ptk. za brak wstrzykiwania zależności;
- 2 ptk. za brak endpointów opartych na klasach;
- 2 ptk. za brak walidacji;
- 1 ptk. za nieczytelne nazwy pól, brak typowania;
- 1 ptk. za pracę bez gita;
- 2 ptk. za brak architektury trójwarstwowej.
