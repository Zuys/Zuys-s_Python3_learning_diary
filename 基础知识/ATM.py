
def input_coin():
    money = 0
    while True:
        input_money = input("Please input your money: ('q' to enter shop)")
        if input_money == 'q':
            if input_money == 0:
                print('ERROR, Please input your money\n')
            else:
                print('Now entering the shopping menu...\n')
                break
        else:
            input_money = int(input_money)
            money = input_money + money
            print('You have input ',input_money,' \nYou have ',money)
    return money

list_product ={
    "cola":3,
    "juice":5,
    "coffee":10,
    "tea":6,
    "spirit":3,
}

def buy1(money_tota):
    i = 0
    money = money_tota
    print("Please input product: ")
    for p in list_product:
        i = i+1
        print("No.",i,'  ',p,'\t\tcost:',list_product[p])

    while True:
        buy_number = input("Please input the num you want:('q' to quit) ")
        if buy_number == 'q':
            break
        else:
            buy_number = int(buy_number)
        if(buy_number > 0) and (buy_number <= len(list_product)):
                for x in list_product:
                    if x == buy_number-1:
                        if money >= list_product[x]:
                            money = money - list_product[x]
                            print("You've brought ",x)
                        else:
                            print("You dont have enough money! ")
        else:
            print("Wrong number ")

    if money > 0:
        print("return ",moeny)
    else:
        print("Thanks")


money_total = input_coin()
buy1(money_total)
