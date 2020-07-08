import random

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '"', "'", ',','.', '?', '#', '$', '%'
           '&', '(', ')', '*', '+', '-', '/', ':', ';'
           '<', '=', '>', '@', '[', ']', '^', '_'
           '_', '`', '{', '|', '}', '~']

numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

def pass_gen(pw_length, special):
    length = int(pw_length)
    password = []
    alpha_req = int(special[0])
    number_req = int(special[1])
    symbol_req = int(special[2])
    #Meets character requirements
    while True:
        while alpha_req != 0:
            password.append(alpha[random.randrange(0,50)])
            alpha_req = alpha_req - 1
            length = length - 1
        while number_req != 0:
            password.append(numbers[random.randrange(0,9)])
            number_req = number_req - 1
            length = length - 1
        while symbol_req != 0:
            password.append(symbols[random.randrange(0,29)])
            symbol_req = symbol_req - 1
            length = length - 1
        break
    #Randomly fills the remainder
    while length != 0:
        x = random.randrange(1,4)
        if x == 1:
                password.append(alpha[random.randrange(0,50)])
                length = length - 1
        if x == 2:
            password.append(numbers[random.randrange(0,9)])
            length = length - 1
        if x == 3:
            password.append(symbols[random.randrange(0,29)])
            length = length - 1
    random.shuffle(password) 
    return ''.join(password) 

input1 = input('Password Length:')

input2 = input('Must Include:[letters][numbers][special characters]')

input3 = input('Password For:')

#Generate password and write to file

while True:
    password = pass_gen(input1, input2)
    print(pass_gen(input1, input2))
    final = input('Save or New Password?')
    if final == 'Save':
        file = open('Passwords.txt', 'a')
        file.write('{0} {1} {2}\n'.format(input3, ' = ', password))
        file.close
        break
    else:
        continue


