class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # find largest element in array
        # make the current largest at the head
        # reverse the whole array to make it bottom
        # repeat until all sorted

        flip = []
        value_to_sort = len(arr)
        while value_to_sort:
            idx = arr.index(value_to_sort)
            if idx != value_to_sort - 1: # not sorted yet
                if idx != 0: # if not potisioned to head
                    flip.append(idx + 1)
                    arr[:idx + 1] = arr[:idx + 1][::-1]
                flip.append(value_to_sort)
                arr[:value_to_sort] = arr[:value_to_sort][::-1]
            value_to_sort -= 1
        return flip
