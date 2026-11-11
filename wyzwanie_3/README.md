Moja hipoteza do sprawdzenia:
W notatce z poprzedniego wyzwania zastanawiałam się nad wpływem fazy względnej na stan kubitu. 
Zatem moja hipotez brzmi:
Encoding wykorzystujący Ry i Rz będzie osiągał wyższe accuracy od encodingu tylko przez Ry, ponieważ dzięki temu
jedna cecha będzie reprezentowana na dwa sposoby. Wydaj mi się, że taki encoding może pozwolić na lepszą 
klasyfikację szczególnie trudniejszych zależności nieliniowych, ponieważ faza może pomóc w rozpoznawaniu 
różnych zależności między cechami.

WNIOSKI:
Moja hipoteza niestety została niepotwierdzona. Początkowo wyniki wyszły tragicznie dla encodingu z Ry i Rz, bo aż o ok. 20
punktów procentowych. Zaczełam się jednak zastanawiać skąd aż tak duża różnica i za pomocą odpowiednich wykresów odkryłam,
że wynika to w dużej mierze z progu = 0 dla obu modeli.

Więc zadałam sobie pytanie: co by było, gdyby przesunąć próg dla Ry i Rz? Może jednak ten encoding da lepsze wyniki tylko dla innego progu?

Tak jak model Ry przy tym progu radził sobie fantastycznie, tak model Ry i Rz bardzo słabo.
Znalazłam próg, który najlepiej pasuje do kategoryzacji danych przez model Ry i Rz i wynosi on ok. 0.2. (Dla modelu Ry wynosi 0.055) Dla nowych progów 
wyniki Ry i Rz znacząco się poprawiły, (aż o ponad 20 punktów procentowych) osiągając wynik zbliżony, ale nadal niższy od modelu z encodingiem Ry :(
Ostatecznie encoding wykorzystujący Ry i Rz nie pomógł w lepszej klasyfikacji. Nie wiem do końca czemu. Może obwód nie potrafił dobrze
wykorzystać tej informacji lub dodatkowe kodowanie utrudniło trening modelu.

Wyniki ze zbioru testowego:
RY: 0.8740740740740741
RY + RZ: 0.8592592592592593