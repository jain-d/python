def power_set(s: list[int]) -> list[list[int]]:
    if len(s) == 0:
        return [[]]
    else:
        all_subsets = [[]]
        for element in s:
            new_subset = []
            for subset in all_subsets:
                subset_copy = subset.copy()
                subset_copy.append(element)
                new_subset.append(subset_copy)
            all_subsets.extend(new_subset)

        return all_subsets

print(power_set([1, 2, 3]))
