
balance = 0
while balance < 50:
        try:
            coin = int(input("Enter a coin: "))
            if coin in [25, 10,5]:
                   balance += coin
                   print(f"Amount due: {50 - balance} ")
            else:
               continue
        except ValueError:
              continue
if balance == 50:
        print("Amount due: 0 ")
        print("Change owed: 0 ")
else:
    print(f"Change owed: {balance - 50} ")
