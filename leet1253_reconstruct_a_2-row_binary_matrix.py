class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        cols = len(colsum)
        upper_list = [0 for _ in range(cols)]
        lower_list = [0 for _ in range(cols)]

        for i, v in enumerate(colsum):
            if v == 1:
                if upper > lower:
                    upper -= 1
                    upper_list[i] = 1
                else:
                    lower -= 1
                    lower_list[i] = 1
            elif v == 2:
                upper_list[i] = lower_list[i] = 1
                upper -= 1
                lower -= 1
        
        return [upper_list, lower_list] if upper == lower == 0 else []
