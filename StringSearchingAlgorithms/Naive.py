def find(text, pattern):
    comparison_count = 0
    found_at_array = []
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
            found_at_array.append(i)
    return found_at_array, comparison_count
