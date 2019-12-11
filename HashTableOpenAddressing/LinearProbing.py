import random
import matplotlib.pyplot as plot


class KeyValuePair:
    def __init__(self, key, value, used=True):
        self.key = key
        self.value = value
        self.used = used

    def __str__(self):
        return str(self.key) + " " + str(self.value) + " " + str(self.used)

    def __repr__(self):
        return str(self.key) + " " + str(self.value) + " " + str(self.used)


class LinearProbing:
    def __init__(self):
        self.comparisonOfLastFind = 0
        self.arraySize = 2
        self.usedCount = 0
        self.hashArray = [None for _ in range(self.arraySize)]

    def _insert(self, key_value_pair):
        element, index = self._find_insert(key_value_pair.key)
        if element is None or element.used is False:
            self.usedCount += 1
        self.hashArray[index] = key_value_pair
        if 0.90 < self.usedCount / float(self.arraySize):
            self._resize()

    def _delete(self, key):
        element, index = self._find_basic(key)
        if element is None:
            raise KeyError("No such key '{0}'!".format(key))
        self.usedCount -= 1
        self.hashArray[index].used = False
        if 0.10 > self.usedCount / float(self.arraySize):
            self._resize()

    def _find_insert(self, key):
        index = self._get_index_of_key(key)
        self.comparisonOfLastFind = 0
        while True:
            self.comparisonOfLastFind += 2
            if self.hashArray[index] is None or self.hashArray[index].used is False:
                return self.hashArray[index], index
            index = (index + 1) % self.arraySize

    def _find_basic(self, key):
        index = self._get_index_of_key(key)
        while True:
            if self.hashArray[index] is None:
                return None, index
            if self.hashArray[index].used is True and self.hashArray[index].key == key:
                return self.hashArray[index]
            index = (index + 1) % self.arraySize

    def _get_index_of_key(self, key):
        return hash(key) % self.arraySize

    def _resize(self):
        print("Array size: " + str(self.arraySize))
        old_hash_array = self.hashArray
        self.arraySize = self.usedCount * 2
        self.usedCount = 0
        self.hashArray = [None for _ in range(self.arraySize)]
        for element in old_hash_array:
            if element is not None and element.used is True:
                self._insert(element)

    def insert(self, key, value):
        self._insert(KeyValuePair(key, value))

    def delete(self, key):
        self._delete(key)

    def find(self, key):
        element, index = self._find_basic(key)
        if element is None:
            raise KeyError("No such key '{0}'!".format(key))
        return element.key, element.value


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
        plot.title("Linear Probing")
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
            # print(my_hash.hashArray)
            my_plot.add(my_hash.usedCount, my_hash.comparisonOfLastFind)
        my_plot.show()


numberOfDraws = 100000
randMaxRange = 1000000000000000000
my_hash_tester = HashTester(numberOfDraws, randMaxRange)
my_hash_tester.start()
