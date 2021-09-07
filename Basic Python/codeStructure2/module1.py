import module2

def welcomeModule1():
    print("Welcome from module1 - welcomeModule1 function")

def main():
    print("-----This is module 1-----")

    welcomeModule1()
    module2.welcomeModule2()

    print(__name__)

    print("-----This is the end of the module 1-----")



if __name__ == '__main__':
    main()
