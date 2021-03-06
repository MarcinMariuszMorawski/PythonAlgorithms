def find(text, pattern):
    found_at_array = []
    text_length = len(text)
    pattern_length = len(pattern)
    comparison_count = 0
    shift = [-1] * 256
    p = 0

    for index in range(pattern_length):
        ascii_code = ord(pattern[index])
        shift[ascii_code] = index

    while p <= (text_length - pattern_length):
        pattern_match = True

        for index in range(pattern_length):
            comparison_count += 1
            if pattern[index] != text[p + index]:
                pattern_match = False
                break

        if pattern_match:
            found_at_array.append(p)

        p += pattern_length

        if p < text_length:
            ascii_code = ord(text[p])
            p = p - shift[ascii_code]

    return -1, comparison_count
