import random
import matplotlib.pyplot as plot


class KeyValuePair:
    def __init__(self, key, value, psl=0):
        self.key = key
        self.value = value
        self.psl = psl


class RobinHood:
    def __init__(self):
        self.comparisonOfLastInsert = 0
        self.arraySize = 2
        self.usedCount = 0
        self.hashArray = [None for _ in range(self.arraySize)]

    def insert(self, key_value_pair):
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
            if found_key_value_pair.psl < key_value_pair.psl:
                self.hashArray[index] = key_value_pair
                self.insert(found_key_value_pair)
                break
            key_value_pair.psl += 1
            index += 1
        self._resize()

    def _resize(self):
        if 0.90 < self.usedCount / float(self.arraySize):
            old_hash_array = self.hashArray
            print("Array size: " + str(self.arraySize))
            self.arraySize = self.usedCount * 2
            self.usedCount = 0
            self.hashArray = [None for _ in range(self.arraySize)]
            for element in old_hash_array:
                if element is not None:
                    self.insert(element)

    def _get_index_of_key(self, key):
        return hash(key) % self.arraySize


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
            my_hash.insert(KeyValuePair(random.randint(1, self.randMaxRange), 1))
            my_plot.add(my_hash.usedCount, my_hash.comparisonOfLastInsert)
        my_plot.show()


numberOfDraws = 100000
randMaxRange = 1000000000000000000
my_hash_tester = HashTester(numberOfDraws, randMaxRange)
my_hash_tester.start()
