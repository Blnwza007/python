text = "12+7*3/3+ 100"
operatorPositions = []  

for index, char in enumerate(text):
    if char in "+-*/":
        operatorPositions.append(index)

starts = [0] + [index + 1 for index in operatorPositions]
ends = operatorPositions + [len(text)]

numbers = []
operator = []

for i in range(len(operatorPositions)):
    operator.append(text[operatorPositions[i]])

for start, end in zip(starts, ends):
    piece = text[start:end]
    numbers.append(piece)

tokens = []
for num, op in zip(numbers, operator):
    tokens.append(num)
    tokens.append(op)

tokens.append(numbers[-1])
print(tokens)

i = 0
while i < len(tokens):
    if tokens[i] == '*' or tokens[i] == '/':
        num1 = float(tokens[i-1])
        num2 = float(tokens[i+1])
        
        if tokens[i] == '*':
            result = num1 * num2
        else:
            result = num1 / num2
        
        tokens[i-1:i+2] = [str(result)]  
    else:
        i += 1   

print(tokens)

result = float(tokens[0])   

i = 1
while i < len(tokens):
    op = tokens[i]
    num = float(tokens[i+1])
    
    if op == '+':
        result = result + num
    else:  
        result = result - num

    i += 2  

print(result)

