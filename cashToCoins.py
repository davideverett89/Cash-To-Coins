# piggyBank = {
#     "pennies": 0,
#     "nickels": 0,
#     "dimes": 0,
#     "quarters": 0
# }

def cash_to_coins(total):
    piggyBank = dict()
    piggyBank['quarters'] = round(total // .25)
    total = round(total % .25, 2)
    piggyBank['dimes'] = round(total // .10)
    total = round(total % .10, 2)
    piggyBank['nickels'] = round(total // .05)
    total = round(total % .05, 2)
    piggyBank['pennies'] = round(total // .01)
    total = round(total % .01, 2)
    print(piggyBank)

cash_to_coins(8.69)
