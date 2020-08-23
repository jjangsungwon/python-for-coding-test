from bisect import bisect_left, bisect_right


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


def solution(words, queries):
    # 단어의 길이에 따른 dictionary 구현
    word_length_dic = {}
    reverse_word_length_dic ={}
    for word in words:
        if len(word) in word_length_dic:
            word_length_dic[len(word)].append(word)
            reverse_word_length_dic[len(word)].append(word[::-1])
        else:
            word_length_dic[len(word)] = [word]
            reverse_word_length_dic[len(word)] = [word[::-1]]

    # 이진 탐색을 수행하기 위해서 정렬
    for key in word_length_dic.keys():
        word_length_dic[key].sort()
        reverse_word_length_dic[key].sort()

    # queries 하나씩 탐색
    result = []
    for search_word in queries:
        if len(search_word) in word_length_dic.keys():
            if search_word[0] == "?":
                result.append(count_by_range(reverse_word_length_dic[len(search_word)], search_word[::-1].replace("?", "a"), search_word[::-1].replace("?", "z")))
            else:
                result.append(count_by_range(word_length_dic[len(search_word)], search_word.replace("?", "a"), search_word.replace("?", "z")))
        else:
            result.append(0)
    return result


if __name__ == "__main__":
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
