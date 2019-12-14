from Naive import find as naive
from SundayQuickSearch import find as sunday
from KnuthMorrisPratt import find as kmp

text = "aadasdczdasedqweasdwewaetaxi"
pattern = "taxi"

print(naive(text, pattern))
print(sunday(text, pattern))
print(kmp(text, pattern))
