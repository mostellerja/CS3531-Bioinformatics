import math

def convertToMax(coinList):
    max_val = 1
    for max_c1 in coinList:
        max_val = max_val*(max_c1+1)

    # max_val = max_val - 1
    return max_val


def convertDigits(maxCoinsAmount, p):
    digitArray = []
    coinsCopy = maxCoinsAmount.copy()
    coinsCopy.reverse()
    max_val = p
    for c1 in coinsCopy:
        coin = max_val % (c1+1)
        max_val = int(max_val / (c1+1))
        digitArray.append(coin)
        if max_val == 0:
            break
    while len(digitArray) < len(maxCoinsAmount):
        digitArray.append(0)
    digitArray.reverse()
    return digitArray


def bruteforce_change(amount, coins):
    # amount = 40

    # c1 = 25
    # c2 = 20
    # c3 = 10
    # c4 = 5
    # c5 = 1
    # coins = [c1, c2, c3, c4, c5]
    maxCoinArr = []
    for coin in coins:
        max_coin = int(amount / coin)
        maxCoinArr.append(max_coin)

    best_change = []
    min_num_of_coins = float("inf")

    # for c1_count in range(max_c1 + 1):
    #     for c2_count in range(max_c2 + 1):
    #         for c3_count in range(max_c3 + 1):
    #             for c4_count in range(max_c4 + 1):
    #                 for c5_count in range(max_c5 + 1):
    #                     value_of_combination = c1_count * c1 + c2_count * c2 + c3_count * c3 + c4_count * c4 + c5_count * c5
    #                     if value_of_combination == amount:
    #                         num_of_coins = c1_count + c2_count + c3_count + c4_count + c5_count
    #
    #                         if num_of_coins < min_num_of_coins:
    #                             min_num_of_coins = num_of_coins
    #                             best_change = (c1_count, c2_count, c3_count, c4_count, c5_count)
    max_val = convertToMax(maxCoinArr)

    for p in range(max_val):
        digits = convertDigits(maxCoinArr, p)
        # print(digits)
        valueofcombination = 0
        for i in range(len(digits)):
            valueofcombination = valueofcombination + (digits[i] * coins[i])
        if valueofcombination == amount:
            valueNum = 0
            for coin in digits:
                valueNum = valueNum + coin
            if valueNum < min_num_of_coins:
                min_num_of_coins = valueNum
                best_change = digits
    print("Number of coins: " + str(min_num_of_coins))
    print(best_change)
    # print(max_val)
    # print(maxCoinArr)
    # print(coins)


amountInput = int(input("Enter amount: "))
coinInput = input("Enter coins: ")
coinInput = coinInput.split()
for i in range(len(coinInput)):
    coinInput[i] = int(coinInput[i])
bruteforce_change(amountInput, coinInput)
