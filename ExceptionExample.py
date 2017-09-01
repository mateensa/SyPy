# anumber = int(input("Please enter an a integer "))

import math;


strbnumber = input("Please enter an integer ");
catch = False;
try:
    bnumber = int(strbnumber);
    if bnumber <1:
        catch = True;
        raise RuntimeError("invalid number")

except:
    if catch :
        print("Invalid number : cannot be lt 0");
    else:
        print("Bad Value for square root")

