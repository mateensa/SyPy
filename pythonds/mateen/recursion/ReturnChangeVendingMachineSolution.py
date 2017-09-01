def recMC(coinValueList, change):
    if change == 1:
        print(1);
        exit(1);
    else:
        for i in [c for c in coinValueList if c <= change]:
            if change == 1:
                break
            else:
                print(change)
                numCoins = 1 + recMC(coinValueList, (change - i))
    return numCoins;

print(recMC([25, 10, 5, 1], 63))