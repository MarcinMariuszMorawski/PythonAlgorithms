def longest_common_subsequence_array(str1, str2):
    array = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for index_row, item_row in enumerate(str1):
        for index_column, item_column in enumerate(str2):
            if item_row == item_column:
                array[index_row + 1][index_column + 1] = array[index_row][index_column] + 1
            else:
                array[index_row + 1][index_column + 1] = max(array[index_row + 1][index_column],
                                                             array[index_row][index_column + 1])
    return array


def longest_common_subsequence_string(str1, str2, array):
    str1_index = len(str1) - 1
    str2_index = len(str2) - 1
    result = ''

    while str1_index >= 0 and str2_index >= 0:
        if str1[str1_index] == str2[str2_index]:
            result += str1[str1_index]
            str1_index -= 1
            str2_index -= 1
        elif array[str1_index][str2_index + 1] > array[str1_index + 1][str2_index]:
            str1_index -= 1
        else:
            str2_index -= 1

    return result[::-1]


file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

text1 = file1.readline()
text2 = file2.readline()

file1.close()
file2.close()

longestCommonSubsequenceArray = longest_common_subsequence_array(text1, text2)
longestCommonSubsequenceAsString = longest_common_subsequence_string(text1, text2, longestCommonSubsequenceArray)

print('Longest common subsequence length:', longestCommonSubsequenceArray[-1][-1])
print('Longest common subsequence:', longestCommonSubsequenceAsString)
