from typing import List


class Solution:
    """
    Accepted
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.paint(image, sr, sc, image[sr][sc], newColor)
        return image

    def paint(self, image, sr, sc, oldColor, newColor):
        # out of bounds check
        if sr == len(image) or sr < 0 or sc == len(image[0]) or sc < 0:
            return

        # check if connected pixel should be the same color and not be already painted
        if image[sr][sc] != oldColor or image[sr][sc] == newColor:
            return

        # paint
        image[sr][sc] = newColor

        # look for neighbouring pixels
        for new_sr, new_sc in ((sr + 1, sc), (sr - 1, sc), (sr, sc + 1), (sr, sc - 1)):
            self.paint(image, new_sr, new_sc, oldColor, newColor)