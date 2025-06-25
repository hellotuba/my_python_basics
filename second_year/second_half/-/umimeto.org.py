def compute_tax(money_list):
    tax = 0
    for money in money_list:
        if 200 <= money:
            tax = 20
        elif 100 <= money:
            tax = 10
        else:
            tax = 0
    return tax