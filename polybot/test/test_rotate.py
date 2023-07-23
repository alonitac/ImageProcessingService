import unittest
from polybot.img_proc import Img
import os

img_path = 'polybot/test/beatles.jpeg' if '/polybot/test' not in os.getcwd() else 'beatles.jpeg'


class TestImgConcat(unittest.TestCase):

    def setUp(self):
        self.img = Img(img_path)
        self.original_dimension = (len(self.img.data), len(self.img.data[0]))

    def test_rotation_dimension(self):
        self.img.rotate()
        actual_dimension = (len(self.img.data), len(self.img.data[0]))
        self.assertEqual(self.original_dimension, actual_dimension[::-1])

    def test_360_rotation(self):
        self.img.rotate()
        self.img.rotate()

        rotated_image = [row[::-1] for row in self.img.data]
        expected_img = [row[::-1] for row in rotated_image]

        self.assertEqual(expected_img, self.img.data)


if __name__ == '__main__':
    unittest.main()
