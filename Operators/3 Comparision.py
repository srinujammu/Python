class cmpocls:

    def compfun(self):
        x = 42
        y = 20
        if x <= y:
            print('comparision is true')
        else:
            print('comparision is false')

def main():
    compvar = cmpocls()
    compvar.compfun()

if __name__ == '__main__': main()