class booltype:
    x = True
    y = None
    def boolfun(self):
        print('x is {}'.format(self.x))
    def boolfunNone(self):
        print('y is {}'.format(self.y))


boolvar = booltype()
boolvar.boolfun()
boolvar.boolfunNone()