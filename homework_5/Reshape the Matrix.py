# 566. Reshape the Matrix
from typing import List


def matrixReshape(nums: List[List[int]], row: int, col: int) -> List[List[int]]:
    # if is given right row and column numbers
    if row * col == len(nums) * len(nums[0]):

        # data is flattened nums list
        data = [item for sublist in nums for item in sublist]

        return [
            [
                data[col * i + j] for j in range(col)
                # constructs column values for a given row

            ] for i in range(len(data) // col)  # defines and iterates rows
        ]
    else:
        return nums


mat = [[1, 2], [3, 4], [5, 6]]
r, c = 2, 3
print(matrixReshape(nums=mat, row=r, col=c))

