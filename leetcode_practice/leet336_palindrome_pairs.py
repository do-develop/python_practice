"""
Given a list of unique words, return all the pairs of the distinct
indices (i, j) in the given list, so that the concatenation of the
two words words[i] + words[j] is a palindrome.

# Brute Force Approach
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i==j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])
        return output

# Using Trie data structure
class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.palindrome_word_ids = []
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, index, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            # check for any suffix palindrome
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results

"""

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(string):
            return string == string[::-1]

        # map with index
        words = {word: i for i, word in enumerate(words)}

        valid_pals = []
        for word, idx in words.items():
            for i in range(len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]

                if is_palindrome(prefix):
                    back = suffix[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], idx])

                if i != len(word) and is_palindrome(suffix):
                    back = prefix[::-1]
                    if back != word and back in words:
                        valid_pals.append([idx, words[back]])
        return valid_pals


# Test
words = ["abcd", "dcba", "lls", "s", "sssll"]
print(Solution().palindromePairs(words))
