class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = []

        for key in freq:
            heappush(max_heap, [-ord(key), key])
        
        output = []
        prev_char = ''

        while len(output) != len(s):
            greatest_char = heappop(max_heap)[1]
            if prev_char != greatest_char: # case 1 - need to use the greatest char
                repeated = 0
                while repeated < repeatLimit and freq[greatest_char] > 0:
                    output.append(greatest_char)
                    freq[greatest_char] -= 1
                    repeated += 1
                
                prev_char = greatest_char

                # any left over of the current char?
                if freq[greatest_char] > 0:
                    heappush(max_heap, [-ord(greatest_char), greatest_char])
            else: # case 2 - need to use the second greatest char
                # remove chars with 0 frequency
                while max_heap and freq[max_heap[0][1]] == 0:
                    heappop(max_heap)
                
                if not max_heap:
                    break

                second_greatest = heappop(max_heap)[1]
                output.append(second_greatest)
                prev_char = second_greatest
                freq[second_greatest] -= 1

                # any left over of the current char?
                if freq[second_greatest] > 0:
                    heappush(max_heap, [-ord(second_greatest), second_greatest])
                # put the greatest char back into the heap
                heappush(max_heap, [-ord(greatest_char), greatest_char])
        
        return "".join(output)
