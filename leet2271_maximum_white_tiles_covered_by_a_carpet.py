class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        N = len(tiles)
        tiles.sort(key=lambda x:x[0]) # sort by starting pos
        start_pos = [tile[0] for tile in tiles]
        tiles_sum = [0] * (N + 1)
        
        max_cover = 0
        for i in range(1, N + 1):
            tiles_sum[i] = tiles_sum[i - 1] + (tiles[i - 1][1] - tiles[i - 1][0] + 1)
        
        for i in range(N):
            s, e = tiles[i]
            if e >= s + carpetLen - 1:
                return carpetLen
            
            # binary search the index of the ending tile that the carpet can partially cover
            end_idx = bisect_right(start_pos, s + carpetLen - 1) - 1
            compensate = 0 # amount carpet cannot cover
            if tiles[end_idx][1] > s + carpetLen - 1:
                compensate = tiles[end_idx][1] - (s + carpetLen - 1)
            max_cover = max(max_cover, tiles_sum[end_idx + 1] - tiles_sum[i] - compensate)
        
        return max_cover
