"""
A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""
import collections
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        result = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei_word in nei[pattern]:
                        if nei_word not in visited:
                            visited.add(nei_word)
                            q.append(nei_word)
            result += 1
        return 0



# TEST
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))
"""
Expected Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
                                    -> "dog" -> cog", which is 5 words long.
"""
