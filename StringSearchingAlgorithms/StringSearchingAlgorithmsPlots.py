from Naive import find as naive
from SundayQuickSearch import find as sunday
from KnuthMorrisPratt import find as kmp
from matplotlib import pyplot as plot

text = "taxkikdiaadasdczdatasedtaxqweasdwewaetakxi"
pattern = "taxi"

print(naive(text, pattern))
print(sunday(text, pattern))
print(kmp(text, pattern))

text = "AAAAAAAAABB"
pattern = "BB"

a = []
b = []
c = []
x = []
for _ in range(50):
    a.append(naive(text, pattern)[1])
    b.append(sunday(text, pattern)[1])
    c.append(kmp(text, pattern)[1])
    x.append(len(text))
    plot.plot(x, a, color="blue")
    plot.plot(x, b, color="orange")
    plot.plot(x, c, color="lightblue")
    text = 10 * "A" + text
plot.title('Zaleznosc od dlugosci tesktu')
plot.gca().legend(('Algorytm naiwny', 'Algorytm Sundaya', 'Algorytm KMP'))
plot.show()

# **********************************************************************************************************************
# **********************************************************************************************************************

# wykres - dl wzroca

text = 400 * "A" + 200 * "B"
pattern = 10 * "B"
a = []
b = []
c = []
x = []

for _ in range(10):
    a.append(naive(text, pattern)[1])
    b.append(sunday(text, pattern)[1])
    c.append(kmp(text, pattern)[1])
    x.append(len(pattern))
    plot.plot(x, a, color="blue")
    plot.plot(x, b, color="orange")
    plot.plot(x, c, color="lightblue")
    pattern = pattern + 10 * "B"
plot.title('Zaleznoxc od dlugosci wzorca')
plot.gca().legend(('Algorytm naiwny', 'Algorytm Sundaya', 'Algorytm KMP'))
plot.show()

# **********************************************************************************************************************
# **********************************************************************************************************************

# wykres ci alfabetu
text = "A" + 2 * "B"
pattern = "BB"
a = []
b = []
d = []
x = []

asciStart = 67
alphabetSize = 1
for c in range(1, 26):
    a.append(naive(text, pattern)[1])
    b.append(sunday(text, pattern)[1])
    d.append(kmp(text, pattern)[1])
    x.append(alphabetSize)

    plot.plot(x, a, color="blue")
    plot.plot(x, b, color="orange")
    plot.plot(x, d, color="lightblue")
    text = chr(asciStart) + text
    asciStart += 1
    alphabetSize += 1
plot.title('Zaleznosc od dlugosci alfabetu')
plot.gca().legend(('Algorytm naiwny', 'Algorytm Sundaya', 'Algorytm KMP'))
plot.show()
