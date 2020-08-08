import re
def clear_comments(string_code:str) -> str:    
    string_code:str=re.split(";",string_code)[0]
    while re.search("  ",string_code):
        string_code=re.sub("  "," ",string_code)
    return string_code
def is_gxcode(string_code:str) -> bool:
    if re.search(r"\bG[0-9]+ |\bg[0-9]+ ",string_code):
        print(re.search(r"\bG[0-9]+ |\bg[0-9]+ ",string_code).group())
        return True
    else:
        return False
class G0Command:
    def __init__(self,x:float, y:float, z:float, e:float, f:float):
        self.x = x
        self.y = y
        self.z = z
        self.e = e    
        self.f = f
    
    def gcode_to_string(self):
        stringGcode="G0Command(x:"+str(self.x)+" "+"y:"+str(self.y)+" "+"z:"+str(self.z)+" "+"e:"+str(self.e)+" "+"f:"+str(self.f)+")"
        print(stringGcode)
        return stringGcode



""" "G1 X90.6 Y13.8 E22.4" -> Gcode() """
def transform_string_to_gxcode(string_code:str) :    
    code=re.findall(r"\bG\d* |\bg\d* ",string_code)
    code =re.sub(r"[A-Z]*","",str(code))
    code=re.sub("(?![\.])\W","",code)
    print(code)
    if code=="0":
        return transform_string_to_g0_code(string_code)

def transform_string_to_gcode(string_code:str) :
    gCode=clear_comments(string_code)
    validarContenidoGcode=False
    comandosGcode=G0Command
    
    if re.search("x|X",gCode): 
        validarContenidoGcode=True      
    else:
        if(re.search("y|Y",gCode)):
            validarContenidoGcode=True
        else:
            if(re.search("z|Z",gCode)):
                validarContenidoGcode=True    
            else:
                if (re.search("e|E",gCode)):
                    validarContenidoGcode=True

    if validarContenidoGcode==True:
        gxCode=is_gxcode(gCode)
        print(gCode,gxCode)
        if gxCode==True:
            comandosGcode=transform_string_to_gxcode(gCode)
            print("hola",comandosGcode.gcode_to_string())
    else:
        pass


def transform_string_to_g0_code(string_code:str)->G0Command:
    comandosX:float=0.0
    comandosY:float=0.0
    comandosZ:float=0.0
    comandosE:float=0.0
    comandosF:float=0.0
    motores=['X','Y','Z','E','F']
    for i in motores:
        if re.search(i+"\d*|"+i.lower()+"\d*",string_code):
            GComando=re.findall(i+"[0-9]*\W*[0-9]*|"+i.lower()+"[0-9]*\W*[0-9]",string_code)
            GComando=re.sub("[a-z]|[A-Z]","",str(GComando))
            GComando=re.sub("(?![\.])\W","",GComando)
            if i=='X':comandosX=float(GComando)
            if i=='Y': comandosY=float(GComando)
            if i=='Z': comandosZ=float(GComando)
            if i=='E': comandosE=float(GComando)
            if i=="F": comandosF=float(GComando)
    movimiento=G0Command(comandosX,comandosY,comandosZ,comandosE,comandosF)
    return movimiento
"""dd=transform_string_to_g0_code("G1 X90.666 Y13.8 Z777 E22.4 f1800")
ddd=dd.gcode_to_string()
transform_string_to_gxcode("  as G1  X90.666 Y13.8 Z777 E22.4 f1800")
gcodoGX=is_gxcode("G1241 X90.666 Y13.8")
transform_string_to_gcode("G0  Y13.8 Z777 E22.4 f1800")
gcodoGX=is_gxcode("G0  Y13.8 Z777 E22.4 f1800")
transform_string_to_gcode("G0  Y13.8 Z777 E22.4 f1800")
"""
dd=clear_comments("G0 Y13.8 Z777 E22.4 f1800")
print(dd)