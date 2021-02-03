class ArthOper:
    x = 5
    y = 3
    z = x % y
    def ArtOprFunc(self):
        print('testInside')

def main():
    print('testmain')
    testvar = ArthOper()
    testvar.ArtOprFunc()
if __name__ == '__main__': main()