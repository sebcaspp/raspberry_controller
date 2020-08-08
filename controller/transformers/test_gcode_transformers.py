import unittest

from .gcode_transformers import *


class TestGCodeTransformers(unittest.TestCase):

    def test_clear_comments(self):
        gcode = """G0 X12               ; move to 12mm on the X axis"""
        gcode_without_comments = "G0 X12 "
        result = clear_comments(gcode)

        self.assertEqual(gcode_without_comments, result, "clear_comments should delete the commentes into gcode")

    def test_is_gxcode(self):
        GCode="G0 X12"
        result:bool=is_gxcode(GCode)
        self.assertTrue(result,"is_gxcode deberia de debolver un True")
        GCode="g0 X12"
        result=is_gxcode(GCode)
        self.assertTrue(result,"is_gxcode con g minuscala debe de debolver true")
        GCode="G X12"
        result=is_gxcode(GCode)
        self.assertFalse(result,"is_gxcode sin numero debe de debolver falce")
    
    def test_transform_string_to_g0_code(self):
        GCode="G0 X12 Y13 Z14 E15 f1500"
        resultComandosRespuesta="G0Command(x:12.0 y:13.0 z:14.0 e:15.0 f:1500.0)"
        string_a_g0=transform_string_to_g0_code(GCode)
        result=string_a_g0.gcode_to_string()
        self.assertEqual(resultComandosRespuesta,result,"transform_string_to_g0_code deberia de debolver un string ")
        
        GCode="g0 X12 Y13 Z14 E15 f1500"
        string_a_g0=transform_string_to_g0_code(GCode)
        result=string_a_g0.gcode_to_string()
        self.assertEqual(resultComandosRespuesta,result,"transform_string_to_g0_code deberia de debolver un string aun que tenga una g minuscula")
        
        GCode="g0  Y13 Z14 E15 f1500"
        string_a_g0=transform_string_to_g0_code(GCode)
        result=string_a_g0.gcode_to_string()
        self.assertNotEqual(resultComandosRespuesta,result,"transform_string_to_g0_code deberia de debolver un daño por que falta un comando ")

        resultComandosRespuesta="G0Command(x:0.0 y:13.0 z:14.0 e:15.0 f:1500.0)"
        GCode="g0 Y13 Z14 E15 f1500"
        string_a_g0=transform_string_to_g0_code(GCode)
        result=string_a_g0.gcode_to_string()
        self.assertEqual(resultComandosRespuesta,result,"transform_string_to_g0_code deberia de debolver un string aunq que falte un comando ")

    def test_transform_string_to_gxcode(self):
        GCode="G0 X12 Y13 Z14 E15 f1500"
        comandosGcode=transform_string_to_gxcode(GCode)
        respuesta:bool=isinstance(comandosGcode,G0Command)
        self.assertTrue(respuesta,"transform_string_to_gxcode deberia de debolber un G0command")

        GCode="1 12 13 14 15 1500"
        comandosGcode=transform_string_to_gxcode(GCode)
        respuesta:bool=isinstance(comandosGcode,G0Command)
        self.assertFalse(respuesta,"transform_string_to_gxcode no deberia de deboler un g0Comand debido a que le faltan los comandos")


    def test_transform_string_to_gcode(self):
        GCode="G0 X12 Y13 Z14 E15 f1500"
        comandosGcode=transform_string_to_gcode(GCode)
        respuesta:bool=isinstance(comandosGcode,G0Command)
        self.assertTrue(respuesta,"transform_string_to_gcode deberia debolber GXcommand")

        GCode="asdasdad g0 "
        comandosGcode=transform_string_to_gcode(GCode)
        respuesta:bool=isinstance(comandosGcode,G0Command)
        self.assertFalse(respuesta,"transform_string_to_gcode deberia debolber gCode vasio ya que no tiene cordenadas")
        
        GCode="G0  Y13 Z14 E15 f1500 "
        comandosGcode=transform_string_to_gcode(GCode)
        respuesta:bool=isinstance(comandosGcode,G0Command)
        self.assertTrue(respuesta,"transform_string_to_gcode deberia debolber un  GXcommand aunque le falte una de las cordenadas")
        