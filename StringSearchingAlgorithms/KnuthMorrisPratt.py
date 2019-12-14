def transform_pattern(pattern):
    pattern_length = len(pattern) + 1
    kmp_array = [0] * pattern_length
    pos = kmp_array[0] = -1

    for i in range(1, pattern_length):
        while pos > -1 and pattern[pos] != pattern[i - 1]:
            pos = kmp_array[pos]
        pos += 1
        if i == pattern_length - 1 or pattern[i] != pattern[pos]:
            kmp_array[i] = pos
        else:
            kmp_array[i] = kmp_array[pos]

    return kmp_array


def find(text, pattern):
    comparison_count = 0
    kmp_array = transform_pattern(pattern)
    b = 0
    for i, char in enumerate(text):
        comparison_count+=1
        while b > -1 and pattern[b] != char:
            b = kmp_array[b]
        b += 1
        if b == len(pattern):
            return i - len(pattern) + 1, comparison_count
    return -1, comparison_count
