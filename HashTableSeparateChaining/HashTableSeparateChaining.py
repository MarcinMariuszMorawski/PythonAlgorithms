import random
import matplotlib.pyplot as plot


class Hash:

    def __init__(self, buckets_count=8, buckets_multiplier=2, increase_ratio=10):
        self.bucketsCount = buckets_count
        self.bucketsMultiplier = buckets_multiplier
        self.increaseRatio = increase_ratio
        self.elementsCount = 0
        self.comparisonOfLastFind = 0
        self.buckets = [[] for _ in range(self.bucketsCount)]

    def _calculate_hash_index(self, key):
        return hash(key) % self.bucketsCount

    def insert(self, key):
        index = self._calculate_hash_index(key)
        if self.find(key) is None:
            self.buckets[index].append(key)
            self.elementsCount += 1
            if (self.elementsCount / len(self.buckets)) > self.increaseRatio:
                self._resize()

    def delete(self, key):
        index = self._calculate_hash_index(key)
        if self.find(key) is key:
            self.buckets.remove(key)
            self.elementsCount -= 1

    def find(self, key):
        index = self._calculate_hash_index(key)
        self.comparisonOfLastFind = 0
        for element in self.buckets[index]:
            self.comparisonOfLastFind += 1
            if element == key:
                return key
        return None

    def show(self):
        print(self.buckets)

    def _resize(self):
        self.bucketsCount = int(self.bucketsCount * self.bucketsMultiplier)
        new_hash_table = [[] for _ in range(self.bucketsCount)]
        for a in self.buckets:
            for b in a:
                index = self._calculate_hash_index(b)
                if b not in new_hash_table[index]:
                    new_hash_table[index].append(b)
        self.buckets = new_hash_table

    def get_comparison_of_last_find(self):
        return self.comparisonOfLastFind

    def get_elements_count(self):
        return self.elementsCount


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

    def __init__(self, number_of_draws, rand_max_range, buckets_count, buckets_multiplier, increase_ratio):
        self.numberOfDraws = number_of_draws
        self.randMaxRange = rand_max_range
        self.bucketsCount = buckets_count
        self.bucketsMultiplier = buckets_multiplier
        self.increaseRatio = increase_ratio

    def start(self):
        my_hash = Hash(self.bucketsCount, self.bucketsMultiplier, self.increaseRatio)
        my_plot = HashPlot()
        for _ in range(self.numberOfDraws):
            my_hash.insert(random.randint(1, self.randMaxRange))
            my_plot.add(my_hash.elementsCount, my_hash.comparisonOfLastFind)
        my_plot.show()


numberOfDraws = 8820
randMaxRange = 80000
bucketsCount = 8
bucketsMultiplier = 2
increaseRatio = 10
my_hash_tester = HashTester(numberOfDraws, randMaxRange, bucketsCount, bucketsMultiplier, increaseRatio)
my_hash_tester.start()
