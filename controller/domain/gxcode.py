from controller.domain.gcode import GCommand

class G0Command(GCommand):
    def __init__(self,x:float, y:float, z:float, e:float, f:float):
        self.x = x
        self.y = y
        self.z = z
        self.e = e    
        self.f = f

    def gcode_to_string(self):
        stringGcode= "G0Command(x:"+str(self.x)+" "+"y:"+str(self.y)+" "+"z:"+str(self.z)+" "+"e:"+str(self.e)+" "+"f:"+str(self.f)+")"
        print(stringGcode)
        return stringGcode


class G1Command(GCommand):
    def __init__(self,x:float, y:float, z:float, e:float, f:float):
        self.x = x
        self.y = y
        self.z = z
        self.e = e    
        self.f = f
