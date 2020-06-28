class Agreement:
    def __init__(self, n = 2):
        self.cnt = n

    def printhelloworld(self):
        i = 1
        while i <= self.cnt:
            print(" hello world")
            i += 1


# create an object of the class
obj = Agreement(10)

# call the method
obj.printhelloworld()

