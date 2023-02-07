class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        count = 0
        
        for a in answers:
            if a == 0:
                count += 1
            else:
                # check if answer (a) is present in the frequency dict
                # also if the frequency of a is and the value of a is the same
                # it needs to be separated into different groups
                if a not in freq or a == freq[a]:
                    freq[a] = 0 # reset for next group
                    count += (1 + a)
                else:
                    freq[a] += 1
        
        return count
