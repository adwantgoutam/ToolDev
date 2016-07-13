__author__ = 'adwant'

import argparse

def Main():
    parser = argparse.ArgumentParser(description="To the find the fibonacci number of the give number")
    arg1 = parser.add_argument("-n", "--name", dest="name",action="store_true", help="Test2: Name of the person running this test")
    arg2 = parser.add_argument("-a", "--age",help="Test2: age of the person",action="store_true", dest="age")
    arg3 = parser.add_argument("-d", "--place", help="Test2: destination of the person",action="store_true", dest="place")

    parser.add_argument("-pf", "--permfile", help="increase output verbosity",action="store_true")
    args = parser.parse_args()

    if args.permfile:

            for x in range(1,len(vars(args))):
                value = locals()["arg"+str(x)]
                print(value.dest+ " "+ value.help)

    if args.name:
        print("Test 2 : Name of the person")

    if args.age:
        print("Test 2 : Age of the person")

    if args.place:
        print("Test 2 : Place of the person")


if __name__ == '__main__':
    Main()



##result = fibo(args.num)
    ##print("The "+str(args.num)+"th fibonacci number is "+str(result))