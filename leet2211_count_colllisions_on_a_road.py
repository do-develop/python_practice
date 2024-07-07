class Solution:
    def countCollisions(self, directions: str) -> int:
        # two loops in each directions
        # count collision if there is a block on the opposite direction
        count = 0
        left_block, right_block = 0, 0

        # loop left to right
        for c in directions:
            if c == 'L':
                count += left_block
            else:
                left_block = 1 # it is either stationary or moving toward right

        # loop right to left
        for c in directions[::-1]:
            if c == 'R':
                count += right_block
            else:
                right_block = 1
        
        return count
