import random
import matplotlib.pyplot as plot


class LinearProbing:

    def __init__(self):
        self.comparisonOfLastFind = 0
        self.arraySize = 8
        self.usedCount = 0
        self.hashArray = [{'used': False} for _ in range(self.arraySize)]

    def insert(self, key, value):
        element, index = self._find(key)
        if element['used'] is False:
            self.usedCount += 1
            if 0.75 < self.usedCount / float(self.arraySize):
                self._resize()
        self.hashArray[index] = {'key': key, 'value': value, 'used': True}

    def delete(self, key):
        element, index = self._find(key)
        if element['used'] is True:
            self.usedCount -= 1
            self.hashArray[index]['used'] = False
            if 0.25 > self.usedCount / float(self.arraySize):
                self._resize()
        else:
            raise KeyError("No such key '{0}'!".format(key))

    def find(self, key):
        element, index = self._find(key)
        if element['used'] is False:
            raise KeyError("No such key '{0}'!".format(key))
        else:
            return element['key'], element['value']

    def _find(self, key):
        index = self._get_hash_index(key)
        self.comparisonOfLastFind = 0
        while self.hashArray[index]['used'] is True:
            self.comparisonOfLastFind += 1
            if self.hashArray[index]['key'] == key:
                return self.hashArray[index], index
            index = self._next_index(index)
        return self.hashArray[index], index

    def _get_hash_index(self, key):
        return hash(key) % self.arraySize

    def _next_index(self, index):
        return (index + 1) % self.arraySize

    def _resize(self):
        old_hash_array = self.hashArray
        self.arraySize = self.usedCount * 3
        self.usedCount = 0
        self.hashArray = [{'used': False} for _ in range(self.arraySize)]
        for element in old_hash_array:
            if element['used'] is True:
                self.insert(element['key'], element['value'])


class HashPlot:

    def __init__(self):
        self.listOfElementsCount = []
        self.listOfComparisonCount = []

    def add(self, elements_count, comparison_count):
        if elements_count < 0 or comparison_count < 0:
            return
        if len(self.listOfElementsCount) > 0 and self.listOfElementsCount[-1] == elements_count:
            return
        self.listOfElementsCount.append(elements_count)
        self.listOfComparisonCount.append(comparison_count)

    def show(self):
        plot.plot(self.listOfElementsCount, self.listOfComparisonCount)
        plot.show()


class HashTester:

    def __init__(self, number_of_draws, rand_max_range):
        self.numberOfDraws = number_of_draws
        self.randMaxRange = rand_max_range

    def start(self):
        my_hash = LinearProbing()
        my_plot = HashPlot()
        for _ in range(self.numberOfDraws):
            my_hash.insert(random.randint(1, self.randMaxRange), 5)
            my_plot.add(my_hash.usedCount, my_hash.comparisonOfLastFind)
        my_plot.show()


numberOfDraws = 100000
randMaxRange = 1000000000000000000
my_hash_tester = HashTester(numberOfDraws, randMaxRange)
my_hash_tester.start()
