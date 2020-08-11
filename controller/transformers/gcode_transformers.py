from controller.domain.gxcode import *
from controller.domain.gcode import *

import re 

def clear_comments(string_code:str) -> str:    
    string_code:str=re.split(";",string_code)[0]
    while re.search("  ",string_code):
        string_code=re.sub("  "," ",string_code)
    return string_code

def transform_string_to_g0_code(string_code:str) -> G0Command:
    comandosX:float=None
    comandosY:float=None
    comandosZ:float=None
    comandosE:float=None
    comandosF:float=None
    motores=['X','Y','Z','E','F']
    for i in motores:
        if re.search(i+"\d*|"+i.lower()+"\d*",string_code):
            GComando=re.findall(i+"[0-9]*\W*[0-9]*|"+i.lower()+"[0-9]*\W*[<0-9]",string_code)
            GComando=re.sub("[a-z]|[A-Z]","",str(GComando))
            GComando=re.sub("(?![\.])\W","",GComando)
            if i=='X':comandosX=float(GComando)
            if i=='Y': comandosY=float(GComando)
            if i=='Z': comandosZ=float(GComando)
            if i=='E': comandosE=float(GComando)
            if i=="F": comandosF=float(GComando)
    return G0Command(comandosX,comandosY,comandosZ,comandosE,comandosF)
    
def transform_string_to_g1_code(string_code:str) -> G1Command:
    comandosX:float=None
    comandosY:float=None
    comandosZ:float=None
    comandosE:float=None
    comandosF:float=None
    motores=['X','Y','Z','E','F']
    for i in motores:
        if re.search(i+"\d*|"+i.lower()+"\d*",string_code):
            GComando=re.findall(i+"[0-9]*\W*[0-9]*|"+i.lower()+"[0-9]*\W*[<0-9]",string_code)
            GComando=re.sub("[a-z]|[A-Z]","",str(GComando))
            GComando=re.sub("(?![\.])\W","",GComando)
            if i=='X':comandosX=float(GComando)
            if i=='Y': comandosY=float(GComando)
            if i=='Z': comandosZ=float(GComando)
            if i=='E': comandosE=float(GComando)
            if i=="F": comandosF=float(GComando)
    return G1Command(comandosX,comandosY,comandosZ,comandosE,comandosF)

""" "G1 X90.6 Y13.8 E22.4" -> Gcode() """
def transform_string_to_gxcode(string_code:str) -> GCommand:
    code=re.findall(r"\bG\d* |\bg\d* ",string_code)
    code =re.sub(r"[A-Z]*","",str(code))
    code=re.sub("(?![\.])\W","",code)
    if code=="0":
        return transform_string_to_g0_code(string_code)
    elif code=="1":
        return transform_string_to_g1_code(string_code)
    else: 
        return None

def transform_string_to_mxcode(string_code:str) -> MCommand:
    return GCode    

def is_gxcode(string_code:str) -> bool:
    if re.search(r"\bG[0-9]+ |\bg[0-9]+ ",string_code):
        return True
    else:
        return False


def is_mxcode(string_code:str) -> bool:
    if re.search(r"\bM\d* |\bm\d* ",string_code):
        return True
    else:
        return False
    
def transform_string_to_gcode(string_code:str) -> GCode:
    gCode:str=clear_comments(string_code)
        
    if is_mxcode(gCode):
        return transform_string_to_mxcode(gCode)    
    elif is_gxcode(gCode):
        return transform_string_to_gxcode(gCode)
    else:
        return None

