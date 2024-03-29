class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p:(-p[0], p[1]))
        new_q = []
        for p in people:
            new_q.insert(p[1], p)
        return new_q
        
