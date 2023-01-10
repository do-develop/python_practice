class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # two parties, radiant and dire
        radi, dire = deque(), deque()
        for i, v in enumerate(senate):
            if v == 'R':
                radi.append(i)
            else:
                dire.append(i)
        while radi and dire:
            if radi[0] < dire[0]:
                # the senate can keep 'alive' to the next round
                radi.append(radi.popleft() + len(senate))
                dire.popleft()
            else:
                dire.append(dire.popleft() + len(senate))
                radi.popleft()
        return "Radiant" if radi else "Dire"
