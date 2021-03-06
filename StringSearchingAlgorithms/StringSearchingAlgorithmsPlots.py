from Naive import find as naive
from Sunday import find as sunday
from matplotlib import pyplot as plot
import string
import random

# TEXT LENGTH ---------------------------------------------------------------
naive_comparison_count_array = []
sunday_comparison_count_array = []
text_length_array = []
for iteration in range(1, 100):
    pattern = "".join([random.choice(string.letters) for _ in range(10)])
    text = "".join([random.choice(string.letters) for _ in range(10 + iteration)])
    naive_comparison_count_array.append(naive(text, pattern)[1])
    sunday_comparison_count_array.append(sunday(text, pattern)[1])
    text_length_array.append(len(text))

plot.plot(text_length_array, naive_comparison_count_array, color="blue")
plot.plot(text_length_array, sunday_comparison_count_array, color="orange")
plot.xlabel('Dlugosc tekstu')
plot.ylabel('Liczba porownan')
plot.title('Zaleznosc od dlugosci tesktu')
plot.gca().legend(('Algorytm naiwny', 'Algorytm Sundaya'))
plot.show()

# PATTERN LENGTH ---------------------------------------------------------------
naive_comparison_count_array = []
sunday_comparison_count_array = []
kmp_comparison_count_array = []
pattern_length_array = []

for iteration in range(1, 100):
    pattern = "".join([random.choice(string.letters) for _ in range(iteration)])
    text = "".join([random.choice(string.letters) for _ in range(500)])
    naive_comparison_count_array.append(naive(text, pattern)[1])
    sunday_comparison_count_array.append(sunday(text, pattern)[1])
    pattern_length_array.append(len(pattern))

plot.clf()
plot.plot(pattern_length_array, naive_comparison_count_array, color="blue")
plot.plot(pattern_length_array, sunday_comparison_count_array, color="orange")
plot.xlabel('Dlugosc wzorca')
plot.ylabel('Liczba porownan')
plot.title('Zaleznosc od dlugosci wzorca')
plot.gca().legend(('Algorytm naiwny', 'Algorytm Sundaya'))
plot.show()

# ALPHABET LENGTH ---------------------------------------------------------------
naive_comparison_count_array = []
sunday_comparison_count_array = []
alphabet_length_array = []
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for iteration in range(1, len(letters)):
    pattern = "".join([random.choice(letters[0:iteration]) for _ in range(10)])
    text = "".join([random.choice(letters[0:iteration]) for _ in range(100)]) + pattern
    naive_comparison_count_array.append(naive(text, pattern)[1])
    sunday_comparison_count_array.append(sunday(text, pattern)[1])
    alphabet_length_array.append(iteration)

plot.clf()
plot.plot(alphabet_length_array, naive_comparison_count_array, color="blue")
plot.plot(alphabet_length_array, sunday_comparison_count_array, color="orange")
plot.xlabel('Dlugosc alfabetu')
plot.ylabel('Liczba porownan')
plot.title('Zaleznosc od dlugosci alfabetu')
plot.gca().legend(('Algorytm naiwny', 'Algorytm Sundaya'))
plot.show()
