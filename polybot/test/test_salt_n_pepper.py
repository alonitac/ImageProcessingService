import unittest
from polybot.img_proc import Img
import os

img_path = 'polybot/test/beatles.jpeg' if '/polybot/test' not in os.getcwd() else 'beatles.jpeg'


class TestImgConcat(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.img = Img(img_path)
        cls.original_img = Img(img_path)

        cls.img.salt_n_pepper()

    def test_rotation_dimension(self):
        actual_dimension = (len(self.img.data), len(self.img.data[0]))
        expected_dimension = (len(self.original_img.data), len(self.original_img.data[0]))
        self.assertEqual(expected_dimension, actual_dimension)

    def test_percentage_salt_pixels(self):
        total_pixels = len(self.img.data) * len(self.img.data[0])
        white_pixels = sum(row.count(255) for row in self.img.data)
        white_pixel_percentage = (white_pixels / total_pixels) * 100
        self.assertGreaterEqual(white_pixel_percentage, 0.15)

    def test_percentage_pepper_pixels(self):
        total_pixels = len(self.img.data) * len(self.img.data[0])
        white_pixels = sum(row.count(0) for row in self.img.data)
        white_pixel_percentage = (white_pixels / total_pixels) * 100
        self.assertGreaterEqual(white_pixel_percentage, 0.15)

    def test_percentage_untouched_pixels(self):
        squared_diff_sum = sum(pixel1 == pixel2 for row1, row2 in zip(self.original_img.data, self.img.data) for pixel1, pixel2 in zip(row1, row2))
        untouched_pixel_percentage = (squared_diff_sum / (len(self.original_img.data) * len(self.original_img.data[0]))) * 100
        self.assertGreaterEqual(untouched_pixel_percentage, 0.70)


if __name__ == '__main__':
    unittest.main()
