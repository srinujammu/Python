class booleancls:
    a = True
    b = False
    x = ('bear', 'bunny', 'true', 'sky', 'rain')
    y = 'bear'
    def booleanfun(self):
                if self.y in self.x:
                    print('Expression is true ({})'.format(self.y))
                else:
                    print('Expression is false ')

def main():
    booleanvar = booleancls()
    booleanvar.booleanfun()

if __name__ == '__main__': main()