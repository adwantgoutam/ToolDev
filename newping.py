__author__ = 'adwant'

import argparse

def Main():
    parser = argparse.ArgumentParser(description="To the find the fibonacci number of the give number")

    arg1 = parser.add_argument("-p", "--password", dest="password",action="store_true", help="current appliance password. Between 8 and 15 characters")
    arg2 = parser.add_argument("-i", "--ignore",help="ignore the args",action="store_true", dest="ignore")
    arg3 = parser.add_argument("-c", "--check", help="performance metrics",action="store_true", dest="check")
    arg4 = parser.add_argument("-m", "--node/model",dest="Node_Model",help="Type of the Model",action="store_true")
    parser.add_argument("-pf", "--permfile", help="increase output verbosity",action="store_true")
    args = parser.parse_args()

    if args.permfile:

            for x in range(1,len(vars(args))):
                value = locals()["arg"+str(x)]
                print(value.dest+ " "+ value.help)

    if args.password:
        print("Command Executes: The password entered is valid")

    if args.ignore:
        print("This command executes to ignore few parameters within the domain testing")

    if args.check:
        print("Executes few commands: This is to check the performance of the server")


if __name__ == '__main__':
    Main()



##result = fibo(args.num)
    ##print("The "+str(args.num)+"th fibonacci number is "+str(result))