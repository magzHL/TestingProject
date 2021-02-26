def addTwoNumbers(a, b):
    return a+b


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
    run_flag = True
    while(run_flag):
        print('Enter two numbers to add! Format: a <space> b. To quit, enter <q!>.')
        numbers_as_string = input()
        if numbers_as_string == 'q!':
            break
        str_list = numbers_as_string.split()
        int_list = [int(i) for i in str_list]
        print('The addition result is : '+addTwoNumbers(int_list[0], int_list[1]).__str__()+'.')
    print('Programm failed successfully!')