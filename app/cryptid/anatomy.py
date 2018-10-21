from app.cryptid.assets import DEFAULT_TORSO, DEFAULT_LEG

class Anatomy:
    def __init__(self, torso=DEFAULT_TORSO, port1=DEFAULT_LEG, port2, port3, port4, port5, port6=DEFAULT_LEG):
        self.torso = torso
        self.port1 = port1
        self.port2 = port2
        self.port3 = port3
        self.port4 = port4
        self.port5 = port5
        self.port6 = port6
