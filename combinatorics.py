from typing import List, Any

# Random comment

# We get permutations as shuffling every possible position
def permutations(values: List[Any]) -> List[Any]:

    perms: List[Any] = []
    permutate(values, 0, len(values) - 1, perms)
    return perms


def permutate(values: List[Any],
            current: int,
            last: int,
            perms: List[Any]) -> None:

    if current == last:
        perms.append(values.copy())

    else:

        for i in range(current, last + 1):

            # Swap elements
            values[current], values[i] = values[i], values[current]

            # Calculate rest with fixed swapped values
            permutate(values, current + 1, last, perms)

            # Backtrack
            values[current], values[i] = values[i], values[current]



def all_subsets(values: List[Any]) -> List[Any]:

    res: List[Any] = []
    get_subsets(values, 0, [], res)
    return res


def get_subsets(values: List[Any],
                idx: int,
                have: List[Any],
                res: List[Any],
                k = 0) -> None:


    if idx == len(values) and k == 0:

        res.append(have.copy())

    elif k != 0 and len(have) == k:

        res.append(have.copy())

    elif idx < len(values):

        # In every subset we decide whether to involve eleme on idx or not

        # Involve
        have.append(values[idx])
        get_subsets(values, idx + 1, have, res, k)

        # Not involve
        have.pop()
        get_subsets(values, idx + 1, have, res, k)


# We get combinations as subset of k-elements
def combinations(values:List[Any], k: int) -> List[Any]:

    assert 0 <= k <= len(values)

    res: List[Any] = []
    get_subsets(values, 0, [], res, k)
    return res


# We get variations by permutating all combinations
def variations(values: List[Any], k: int) -> List[Any]:

    combs = combinations(values, k)
    res: List[Any] = []

    for comb in combs:
        res += permutations(comb)

    return res
