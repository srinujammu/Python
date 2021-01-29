# Example 1
x = 'Seven'
print('x is {}'.format(x))
print(type(x))

class stringVar:
    y ='ten'
    def uppercase(self):
        print(self.y.upper())
def main():
    sample = stringVar()
    sample.uppercase()

if __name__ == '__main__': main()

# Example 2

z = 'Nine {1} {0}'.format(8,9)
print(z)

# Example Adding spaces trailing and heading.

class 