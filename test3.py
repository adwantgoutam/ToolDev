__author__ = 'adwant'

import argparse

def Main():
    parser = argparse.ArgumentParser(description="To the find the fibonacci number of the give number")
    arg1 = parser.add_argument("-l", "--location", dest="location",action="store_true", help="Test3: location of the person running this test")
    arg2 = parser.add_argument("-d", "--distance",help="Test3: distance of the person",action="store_true", dest="distance")
    arg3 = parser.add_argument("-o", "--ocuppation", help="Test3: ocuppation of the person",action="store_true", dest="ocuppation")

    parser.add_argument("-pf", "--permfile", help="increase output verbosity",action="store_true")
    args = parser.parse_args()

    if args.permfile:

            for x in range(1,len(vars(args))):
                value = locals()["arg"+str(x)]
                print(value.dest+ " "+ value.help)

    if args.location:
        print("Test 3 : location of the person")

    if args.distance:
        print("Test 3 : distance of the person")

    if args.ocuppation:
        print("Test 3 : ocuppation of the person")


if __name__ == '__main__':
    Main()



##result = fibo(args.num)
    ##print("The "+str(args.num)+"th fibonacci number is "+str(result))