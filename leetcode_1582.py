class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        x, y = len(mat), len(mat[0])
        count = 0

        for i in range(y):
            special = None

            for j in range(x):
                if mat[j][i] == 1:
                    if special is not None:
                        special = None
                        break
                    special = j

            if special is not None:
                if 1 not in mat[special][:i] + mat[special][i + 1 :]:
                    count += 1

        return count
