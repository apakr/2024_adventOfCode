def mul(x,y):
    return x * y

def get_num_x(file): # if returns "break" then break
    num = ""
    while 1:
        next_char = file.read(1)
        num += next_char
        # print(num + " num outside")
        # print(next_char)
        # if next_char == ')':
        #     print(num + " inside ) statement")
        #     return int(num[0:(len(num)-1)])
        if next_char == 'm':
            return 0
        if next_char != ',':
            try:
                int(num)
            except ValueError:
                group = file.read(4)
                return 0
        # elif next_char == ')':
        #     print(num + " inside ) statement")
        #     return int(num[0:(len(num)-1)])
        else:
            return int(num[0:(len(num)-1)])
    print("hit outside return")
    return

def get_num_y(file): # if returns "break" then break
    num = ""
    while 1:
        next_char = file.read(1)
        num += next_char
        print(num + " num outside")
        print(next_char)
        # if next_char == ')':
        #     print(num + " inside ) statement")
        #     return int(num[0:(len(num)-1)])
        if next_char == 'm':
            print("hits m return")
            return 0
        if next_char == ')':
            print("hits normal return")
            print(int(num[0:(len(num)-1)]))
            return int(num[0:(len(num)-1)])
        else:
            try:
                int(num)
            except ValueError:
                group = file.read(4)
                print("hits value error return")
                return 0
        # if next_char != ')':
        #     try:
        #         int(num)
        #     except ValueError:
        #         group = file.read(4)
        #         return
        # else:
        #     return int(num[0:(len(num)-1)])
    print("hit outside return")
    return

file = open("day_three\day_three_data.txt", 'r')

group = file.read(4)
tot = 0
while 1: # loop to find inital "mul("
    if group != "mul(":
        group = group[1:4] + file.read(1)
    else:
        x,y = 0,0
        x = get_num_x(file)
        print(f"{x} is x")
        if x == 0:
            group = file.read(4)
        y = get_num_y(file)
        print(f"{y} is y")
        if y == 0:
            group = file.read(4)
        # closing_parenthesis = file.read(1)
        # print(f"x:{x}, y:{y}")
        if (x != 0) & (y != 0):
            # print("runs tot add")
            tot += mul(x,y)
            group = file.read(4)
        else:
            # print("runs skip")
            group = file.read(4)
    if group == '':
        break
print(tot)


