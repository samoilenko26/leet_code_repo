def is_ok(item, item_2):
    for ch in item_2:
        if ch not in item and item_2.count(ch) != item.count(ch):
            return False
    return True


def CountingAnagrams(input):
    result = []
    tmp = list(set(input.split()))
    origin = list(set(input.split()))
    for item in origin:
        tmp.remove(item)
        if item in tmp:
            continue
        for item_2 in tmp:
            if len(item_2) != len(item):
                continue
            if is_ok(item, item_2):
                result.append(item)

    print(result)
    return len(result)

print('Test 2 passed: {}'.format(CountingAnagrams('run urn urn') == 1))
print('Test 3 passed: {}'.format(CountingAnagrams('a b c d run urn urn') == 1))


