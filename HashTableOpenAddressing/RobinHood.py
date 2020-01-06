import random
import matplotlib.pyplot as plot


class KeyValuePair:
    def __init__(self, key, value, psl=0):
        self.key = key
        self.value = value
        self.psl = psl

    def __str__(self):
        return str(self.key) + " " + str(self.value) + " " + str(self.psl)

    def __repr__(self):
        return str(self.key) + " " + str(self.value) + " " + str(self.psl)


class RobinHood:
    def __init__(self):
        self.comparisonOfLastInsert = 0
        self.arraySize = 2
        self.usedCount = 0
        self.hashArray = [None for _ in range(self.arraySize)]

    def _insert(self, key_value_pair):
        self.comparisonOfLastInsert = 0
        key_value_pair.psl = 0
        index = self._get_index_of_key(key_value_pair.key)
        while True:
            index = index % self.arraySize
            self.comparisonOfLastInsert += 1
            found_key_value_pair = self.hashArray[index]
            if found_key_value_pair is None:
                self.hashArray[index] = key_value_pair
                self.usedCount += 1
                break
            self.comparisonOfLastInsert += 1
            if found_key_value_pair.psl < key_value_pair.psl:
                self.hashArray[index] = key_value_pair
                self._insert(found_key_value_pair)
                break
            key_value_pair.psl += 1
            index += 1
        if 0.90 < self.usedCount / float(self.arraySize):
            self._resize()

    def _delete(self, key):
        index, element = self._find(key)
        if element is None:
            raise KeyError("No such key '{0}'!".format(key))
        while True:
            self.hashArray[index] = None
            next_index = (index + 1) % self.arraySize
            if self.hashArray[next_index] and self.hashArray[next_index].psl == 0:
                break
            self.hashArray[index] = self.hashArray[next_index]
            if self.hashArray[next_index] is None:
                break
            self.hashArray[index].psl -= 1
            index = next_index
        self.usedCount -= 1
        if 0.10 > self.usedCount / float(self.arraySize):
            self._resize()

    def _find(self, key_value_pair):
        index = self._get_index_of_key(key_value_pair.key)
        while True:
            if self.hashArray[index] is None:
                return None, index
            if self.hashArray[index].key == key_value_pair.key:
                return self.hashArray[index], index
            index = (index + 1) % self.arraySize

    def _resize(self):
        print("Array size: " + str(self.arraySize))
        old_hash_array = self.hashArray
        self.arraySize = self.usedCount * 2
        self.usedCount = 0
        self.hashArray = [None for _ in range(self.arraySize)]
        for element in old_hash_array:
            if element is not None:
                self._insert(element)

    def _get_index_of_key(self, key):
        return hash(key) % self.arraySize

    def insert(self, key, value):
        self._insert(KeyValuePair(key, value))

    def delete(self, key):
        self._delete(KeyValuePair(key, None))

    def find(self, key):
        element, index = self._find(KeyValuePair(key, None))
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
        plot.title("Robin Hood")
        plot.plot(self.listOfElementsCount, self.listOfComparisonCount)
        plot.show()


class HashTester:

    def __init__(self, number_of_draws, rand_max_range):
        self.numberOfDraws = number_of_draws
        self.randMaxRange = rand_max_range

    def start(self):
        my_hash = RobinHood()
        my_plot = HashPlot()
        for _ in range(self.numberOfDraws):
            my_hash.insert(random.randint(1, self.randMaxRange), 1)
            # print(my_hash.hashArray)
            my_plot.add(my_hash.usedCount, my_hash.comparisonOfLastInsert)
        my_plot.show()


numberOfDraws = 1000
randMaxRange = 1000000000000000000
my_hash_tester = HashTester(numberOfDraws, randMaxRange)
my_hash_tester.start()
