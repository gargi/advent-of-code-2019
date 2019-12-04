f = open("day2_input.txt")
input = [int(i) for i in f.read().split(",")]
for i in range(0, len(input)-3, 4):
    pos_1 = input[i+1]
    pos_2 = input[i+2]
    pos_3 = input[i+3]
    if input[i] == 1:
        input[pos_3] = input[pos_1] + input[pos_2]
    if input[i] == 2:
        input[pos_3] = input[pos_1] * input[pos_2]
    if input[i] == 99:
        break
print(input)
