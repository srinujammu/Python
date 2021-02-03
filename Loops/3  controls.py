class controlexp1:
    secret = 'swordfish'
    pw = ''
    count = 0
    Auth = False
    maxattempts = 5
    def controlexp1fun(self):
        pw = ''
        while pw != self.secret:
            pw = ''
            self.count +=1
            if self.count > self.maxattempts : break
            pw= input(f"{self.count}:What is the secrete work")
        else:
            self.Auth = True

        print("Authorized" if self.Auth else "Calling the FBI ...")
class controlexp2:
    animals = ('bear', 'bunny','dog','cat','velociraptor')
    def controlexp2fun(self):
        for pet in self.animals:
            print(pet)
        else:
            print('that is all of the animals')

def main():
    controlexp1var = controlexp1()
    controlexp1var.controlexp1fun()
    controlexp2var = controlexp2()
    controlexp2var.controlexp2fun()

if __name__ == '__main__': main()