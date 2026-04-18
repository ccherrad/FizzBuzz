from typing import List


def generate_fizzbuzz(
    int1: int, int2: int, limit: int, str1: str, str2: str
) -> List[str]:
    result = []
    for i in range(1, limit + 1):
        acc = ""
        if i % int1 == 0:
            acc += str1
        if i % int2 == 0:
            acc += str2
        if not acc:
            acc = str(i)
        result.append(acc)
    return result
