### Grouping string array in anagram unit.
import collections

def group_anagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # add to dictionary after sorting
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()


input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

print(group_anagrams(input))