while True:
    answer = input("Do you like the winter? ")

    y_list = ['y', 'yes', 'sure', 'yea']
    n_list = ['n', 'no', 'nope', 'nada']

    answer = answer.lower()

    if answer in y_list:
        print("Yes fucking amazing fuck.")
        break
    elif answer in n_list:
        print('fuck off')
        break
    else:
        print("what did you say")


