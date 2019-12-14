def find(text, pattern):
    comparison_count = 0
    text_length = len(text)
    pattern_length = len(pattern)
    for i in range(text_length - pattern_length + 1):
        pattern_match = True
        for j in range(len(pattern)):
            comparison_count += 1
            if text[i + j] != pattern[j]:
                pattern_match = False
                break
        if pattern_match:
            return i, comparison_count
    return -1, comparison_count
