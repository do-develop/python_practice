class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # store user active minutes (uam)
        minutes = defaultdict(set)
        for user, minute in logs:
            minutes[user].add(minute)
        
        # store count of UAM
        result = [0] * k
        for user_min in minutes.values():
            uam = len(user_min)
            result[uam - 1] += 1 
        return result
