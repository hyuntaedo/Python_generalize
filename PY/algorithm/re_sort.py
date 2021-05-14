data_number = input()
result = []
value =0

for x in data_number:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value !=0:
    result.append(str(value))

print("".join(result))


