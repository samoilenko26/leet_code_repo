
def find_index(ranked: list[int], element: int) -> int:
    lo: int = 0
    hi: int = len(ranked) - 1

    while lo <= hi:
        mid: int = (lo + hi) // 2
        if ranked[mid] == element:
            return mid 
        elif ranked[mid] < element:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo 


def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
    ranked = list(set(ranked))
    ranked.sort(reverse=True)

    answer: list[int] = []
    for score in player:
        index: int = find_index(ranked, score)
        answer.append(index + 1)
    print(answer)
    return answer


if __name__ == '__main__':
    climbingLeaderboard([100, 90, 80, 75], [70, 79, 80, 105])
