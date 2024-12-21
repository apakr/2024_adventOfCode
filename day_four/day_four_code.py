import re
import pandas as pd

text = open("day_four/day_four_data.txt",'r')

tot = 0
text = text.read()
# print(text)
text_as_list = list(text)
# print(text_as_list)

# left to right
for i in re.findall("XMAS", text):
    tot += 1

# written backwards
for i in re.findall("XMAS", ''.join(reversed(list(text)))):
    tot += 1
    
# vertical descending, only 1 in the
split_text = text.split("\n")
vert_text = ""
for i in range(0, len(split_text)):
    for j in split_text:
        vert_text += j[i]
    vert_text += '.' # represents a line break, so that ends of lines that together spell XMAS don't proc findall

for i in re.findall("XMAS", vert_text):
    tot += 1

# vertical ascending
for i in re.findall("XMAS", ''.join(reversed(list(vert_text)))):
    tot += 1



# diagonals

for i in range(0, len(split_text)): # splits text even further into a list of lists of chars
   split_text[i] = list(split_text[i])

def get_diagonals(grid, bltr = True):
    dim = len(grid)
    return_grid = [[] for _ in range(2 * len(grid) - 1)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if bltr: 
                return_grid[row + col].append(grid[col][row])
            else:    
                return_grid[col - row + (dim - 1)].append(grid[row][col])
    return return_grid


# diagonal bottom left to top right
diag_text = ""
diag_text = get_diagonals(split_text, True)
diag_bltr = []

# print(diag_text)
for i in diag_text:
    for j in i:
        diag_bltr += j
    diag_bltr += '.'
# print(diag_bltr)
for i in re.findall("XMAS", ''.join(diag_bltr)):
    tot += 1


# diagonal bottom left to top right reversed
for i in re.findall("XMAS", ''.join(reversed(diag_bltr))):
    tot += 1
    # for i in re.findall("XMAS", ''.join(reversed(list(vert_text)))):


# diagonal top left to bottom right
diag_text_nbltr = get_diagonals(split_text, False)

diag_nbltr = []

# print(diag_text_nbltr)
for i in diag_text_nbltr:
    for j in i:
        diag_nbltr += j
    diag_nbltr += '.'
for i in re.findall("XMAS", ''.join(diag_nbltr)):
    tot += 1


# diagonal top left to bottom right reversed
for i in re.findall("XMAS", ''.join(reversed(diag_nbltr))):
    tot += 1

# part 1 answer, correct
# print(tot)


# part 2:
print(text)
print(split_text)
dim = len(split_text[1])
# print(dim)

# x = re.search("A", text)
# print(re.search("A", text).start())
# print(text[re.search("A", text).start()+12])
# print(text[13])

copy_text = text
tot2 = 0
num_as =0
while re.search("A", copy_text) != None:
    # num_as += 1
    pos = re.search("A", copy_text).start()
    try:
        tl,tr,bl,br = copy_text[pos-12],copy_text[pos-10],copy_text[pos+10],copy_text[pos+12]
        corners = tl+tr+bl+br
        # print(f"corners at pos{pos}: {corners}")
        if all(substr not in corners for substr in ["X", "A", ".", "\n"]):
            print(f"corners at pos{pos}: {corners}")
            num_as += 1
        if (corners == "MMSS") or (corners == "MSMS") or (corners == "SMSM") or (corners == "SSMM") or (corners == "MSSM") or (corners == "SMMS"):
            tot2 += 1
            print(f"counted at pos {pos}")
        
    except IndexError:
        tot2 = tot2
    l = list(copy_text)
    l[int(pos)] = "."
    copy_text = ''.join(l)
    corners = ""
print(tot2)
print(num_as)