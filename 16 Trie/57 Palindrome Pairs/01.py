### Find every palindrome pairs using brute force
###
def palindrome_pairs(words):
    def is_palindrome(word):
        return word == word[::-1]

    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])
    return output


print(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(palindrome_pairs(["bat", "tab", "cat"]))