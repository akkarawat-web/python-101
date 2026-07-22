keep_going = "y"
while keep_going == "y":
    sales = float(input('enter the amount of sales:'))
    comm_rate = float(input('enter the commission rate :'))
    commission =sales * comm_rate
    print(f'the commission is ${commission :.2f}')
    keep_going = input ('Do you want to claculate another' + \
        'commission (Enter u for yes):')