import unittest
from polybot.img_proc import Img
import os

img_path = 'polybot/test/beatles.jpeg' if '/polybot/test' not in os.getcwd() else 'beatles.jpeg'


class TestImgConcat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.img = Img(img_path)
        cls.other_img = Img(img_path)
        cls.img.concat(cls.other_img)

    def test_concat_result_dimension(self):
        actual_height = len(self.img.data)
        actual_width = len(self.img.data[0])

        expected_height = len(self.other_img.data)
        expected_width = 2 * len(self.other_img.data[0])

        self.assertEqual(actual_height, expected_height)
        self.assertEqual(actual_width, expected_width)

    def test_concat_similarity_using_mse(self):
        actual_width = len(self.img.data[0])

        small_image_width = actual_width // 2

        # Check if the image width is divisible by 2
        self.assertEqual(actual_width % 2, 0)

        left_half = [row[:small_image_width] for row in self.img.data]
        right_half = [row[small_image_width:] for row in self.img.data]

        self.assertEqual(left_half, right_half)


if __name__ == '__main__':
    unittest.main()
