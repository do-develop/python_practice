class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            move_pos = len(row) - 1
            for pos in range(len(row) - 1, -1, -1):
                if row[pos] == '*': # obstacle
                    move_pos = pos - 1 # canno move stoens behind obstacle
                elif row[pos] == '#':
                    row[move_pos], row[pos] = row[pos], row[move_pos]
                    move_pos -= 1
        # return zip(*box[::-1])
        rotated = []
        for y in range(len(box[0])):
            rotated.append([])
            for x in range(len(box)-1, -1, -1):
                rotated[y].append(box[x][y])
        return rotated
