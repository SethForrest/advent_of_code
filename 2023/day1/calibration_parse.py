output = 0

with open("input.txt",'r') as f:
    for line in f:
        # because there can be overlapping letters I keep the first and last letter of each number
        # (i.e. eightwothree == 823, even though eight and two share a 't')
        line = line.replace("one",'o1e')
        line = line.replace("two",'t2o')
        line = line.replace('three','t3e')
        line = line.replace('four','f4r')
        line = line.replace('five','f5e')
        line = line.replace('six','s6x')
        line = line.replace('seven','s7n')
        line = line.replace('eight','e8t')
        line = line.replace('nine','n9e')

        number = []
        for char in line:
            if char.isdigit():
                number.append(char)
                break

        # the [::-1] is a way of reversing a list in python
        for char in line[::-1]:
            if char.isdigit():
                number.append(char)
                break
        number = int(''.join(number))
        print(f"{line.strip()}: {number}")
        output += number
print(output)

