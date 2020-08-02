from controller.domain.gxcode import *
from controller.domain.gcode import *


def clear_comments(string_code:str) -> str:
    pass

def transform_string_to_g0_code(string_code:str) -> G0Command:
    pass

def transform_string_to_g1_code(string_code:str) -> G1Command:
    pass

""" "G1 X90.6 Y13.8 E22.4" -> Gcode() """
def transform_string_to_gxcode(string_code:str) -> GCommand:
    pass    

def transform_string_to_mxcode(string_code:str) -> MCommand:
    pass    


def is_gxcode(string_code:str) -> bool:
    pass

def is_mxcode(string_code:str) -> bool:
    pass

def transform_string_to_gcode(string_code:str) -> GCode:
    pass
