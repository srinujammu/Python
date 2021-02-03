class forloopcls:
    animals = ('bear', 'bunny', 'dog','cat','velociraptor')
    def forloopfunc(self):
        for pet in self.animals:
            print(pet)

def main():
    forloopvar = forloopcls()
    forloopvar.forloopfunc()

if __name__ == '__main__': main()