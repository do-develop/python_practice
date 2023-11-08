class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # find who can't communicate each other
        # find the most popular language among them
        # teach that language to the minority who can't speak it
        languages = [set(l) for l in languages]
        cantspeak = set()
        for u, v in friendships:
            u, v = u - 1, v - 1 # 0-index
            if languages[u] & languages[v]: # can communicate
                continue
            cantspeak.add(u)
            cantspeak.add(v)

        langcount = Counter()
        for i in cantspeak:
            for j in languages[i]:
                langcount[j] += 1

        return 0 if not cantspeak else len(cantspeak) - max(list(langcount.values()))
