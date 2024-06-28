class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # populate the grid matrix and assign unique artifact number
        marker = [[-1] * n for _ in range(n)] # 2D marker to track excavated status
        artifact_id = 0

        # traverse dig array and set grid[r][c] -= 1 to denote dug up
        for r1, c1, r2, c2 in artifacts:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    marker[r][c] = artifact_id
            artifact_id += 1
       
        # traverse grid matrix and check any remaining artifact
        for r, c in dig:
            if marker[r][c] >= 0:
                marker[r][c] = -1 # set to dug up value (-1)
                
        # fully excavated artifacts = total - still remaining
        remaining_artifact_id = set()
        for r in range(n):
            for c in range(n):
                if marker[r][c] >= 0:
                    remaining_artifact_id.add(marker[r][c])
        
        return artifact_id - len(remaining_artifact_id)
