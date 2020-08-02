from controller.domain.gcode import GCommand

class G0Command(GCommand):
    def __init__(self,x:float, y:float, z:float, e:float, f:float):
        self.x = x
        self.y = y
        self.z = z
        self.e = e    
        self.f = f
    
class G1Command(GCommand):
    def __init__(self,x:float, y:float, z:float, e:float, f:float):
        self.x = x
        self.y = y
        self.z = z
        self.e = e    
        self.f = f
