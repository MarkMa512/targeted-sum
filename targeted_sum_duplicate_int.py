from typing import List

def find_combinations(candidates: List[int], target: int, start: int, path: List[int], res: List[List[int]]) -> None:
    if target == 0:
        res.append(path)
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        find_combinations(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)

def sum_combinations(x: List[int], y: List[int]) -> List[List[int]]:
    x.sort()
    results = []
    for target in y:
        res = []
        find_combinations(x, target, 0, [], res)
        results.extend(res)
    return results

def unique_combinations(x: List[int], combinations: List[List[int]]) -> List[List[int]]:
    used_numbers = set()
    unique_combinations = []

    for combination in combinations:
        if not any(num in used_numbers for num in combination):
            unique_combinations.append(combination)
            used_numbers.update(combination)

    return unique_combinations

# Example usage
x = [1, 2, 2, 3, 4, 5]
y = [8, 9]
combinations = sum_combinations(x, y)
filtered_combinations = unique_combinations(x, combinations)
print(filtered_combinations)
