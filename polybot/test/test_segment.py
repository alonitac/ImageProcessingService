import unittest
import random
from polybot.img_proc import Img
import os

img_path = 'polybot/test/beatles.jpeg' if '/polybot/test' not in os.getcwd() else 'beatles.jpeg'


class TestImgConcat(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.img = Img(img_path)
        cls.original_img = Img(img_path)

        cls.img.segment()

    def test_rotation_dimension(self):
        actual_dimension = (len(self.img.data), len(self.img.data[0]))
        expected_dimension = (len(self.original_img.data), len(self.original_img.data[0]))
        self.assertEqual(expected_dimension, actual_dimension)

    def test_black_white(self):
        bw_sum = all(pixel in [0, 255] for row in self.img.data for pixel in row)
        self.assertTrue(bw_sum)

    def test_segmentation_in_random_pixels(self):
        for i in range(50):
            y = random.randint(0, len(self.img.data) - 1)
            x = random.randint(0, len(self.img.data[0]) - 1)

            if 90 < self.original_img.data[y][x] < 110:
                continue

            self.assertEqual(self.img.data[y][x], 0 if self.img.data[y][x] < 100 else 255)


if __name__ == '__main__':
    unittest.main()
