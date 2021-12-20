import re
from collections import defaultdict, Counter


def main():
    insertion_pairs = defaultdict(list)
    polymer_template = []
    insertion_regex = "([A-Z])([A-Z]) -> ([A-Z])"
    with open('input.txt', 'r') as infile:
        for line in infile:
            is_insertion = re.search(insertion_regex, line.strip())
            if is_insertion is not None:
                insertion_pairs[is_insertion.group(1) + is_insertion.group(2)] = [
                    is_insertion.group(1) + is_insertion.group(3), is_insertion.group(3) + is_insertion.group(2),
                    is_insertion.group(3)]
            else:
                polymer_template.extend(list(line.strip()))

    polymer = []
    for index in range(len(polymer_template) - 1):
        polymer.append(polymer_template[index] + polymer_template[index + 1])
    main_counter = Counter(polymer)

    insertion_keys = insertion_pairs.keys()
    steps = 0

    while steps < 40:
        step_counter = Counter()
        for key in insertion_keys:
            current_count = main_counter[key]
            if current_count > 0:
                pair_1, pair_2, insert = insertion_pairs[key]
                step_counter[pair_1] += 1 * current_count
                step_counter[pair_2] += 1 * current_count
                main_counter[key] -= 1 * current_count
        main_counter += step_counter
        steps += 1

    element_count = defaultdict(int)
    for key in insertion_keys:
        current_count = main_counter[key]
        element, *_ = re.findall("[A-Z]", key)
        element_count[element] += current_count
    # increment the count of the last element
    element_count[polymer_template[-1]] += 1
    count_values = element_count.values()
    return max(count_values) - min(count_values)


if __name__ == '__main__':
    print(main())
