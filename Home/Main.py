from InaSystemCall import MainIna

class EngSystemCall():
    def execute(self):
        print("Hello universe")

class EspSystemCall():
    def execute(self):
        print("Hello country")

def Main():
    print("(Choose Language)")
    print("1. Indonesian")
    print("2. English")
    print("3. Spanish")
    lgInput = input("Answer: ")

    try:
        lgInput = int(lgInput)
    except ValueError:
        lgInput = None

    if lgInput == 1:
        MainIna()
    elif lgInput == 2:
        command = EngSystemCall()
        command.execute()
    elif lgInput == 3:
        command = EspSystemCall()
        command.execute()

Main()
