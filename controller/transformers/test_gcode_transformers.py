import unittest

from .gcode_transformers import *


class TestGCodeTransformers(unittest.TestCase):

    def test_clear_comments(self):
        gcode = """G0 X12               ; move to 12mm on the X axis"""
        gcode_without_comments = "G0 X12"
        result = clear_comments(gcode)

        self.assertEqual(gcode_without_comments, result, "clear_comments should delete the commentes into gcode")



        