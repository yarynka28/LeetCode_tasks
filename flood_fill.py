class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or image[sr][sc] == color:
            return image
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        start_color = image[sr][sc]
        queue = [(sr, sc)]
        visited = set(queue)
        while queue:
            r, c = queue.pop(0)
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == start_color and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return image      
            
