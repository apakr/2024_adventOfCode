import re

def mul(x,y):
    return x * y

file = open("day_three/day_three_data.txt", 'r')

text = file.read()

# text = re.findall("mul[(].\d+,.\d+[)]", text)

# text = re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", text)



# nums = []
# for i in text:
#     nums.append(re.findall(".\d+",i))
# text = re.findall(".\d+",text)

tot = 0

# for i in text:
#     mul()


# print(text)
# print(nums)

# for i in text:
#     tot += eval(i)

for i in re.findall("mul[(]\d+,\d+[)]", text):
    tot += eval(i)
# for i in text:
#     tot += mul(int(i[1]), int(i[2]))
# gives 178856918

# print(re.findall("mul\(.\d+,.\d+\)", text))

tot2 = 0
def part2_funct(text, tot2):
    do = True
    # for i, j, k in re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data):
    for i, j, k, l in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", text):
                            # "(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
        print(i)
        print(j)
        print(k)
        print(l)
        if k == "do()":
            do = True
            continue
        if l == "don't()":
            do = False
        if do:
            tot2 += int(i)*int(j)
    return(tot2)

print(f"Part 1: {tot}")
print(f"Part 2: {part2_funct(text,tot2)}")
