import tkinter as tk

window = tk.Tk()
window.title('calculator')
window.geometry('300x400')

for col in range(4):
    window.columnconfigure(col, weight=1, uniform="equal")

buttonLabels = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '00', 'CC', '/',
    '', '.', 'C', '=',     
]

outputText = tk.StringVar(value='0')
output = tk.Label(
    window, 
    textvariable=outputText, 
    font=('Arial', 12), 
    width=12, 
    anchor='e', 
    padx=15,
    height=2,
    relief='solid',
    borderwidth=2
)

output.grid(
    row=0, 
    column=0, 
    columnspan=4, 
    sticky="ew", 
    pady=15,
    padx=10
)

def createButtonRow(root):
    for index in range(len(buttonLabels)):
        text = buttonLabels[index]          
        row = (index // 4) + 1                           
        column = index % 4

        if text == '':
            continue

        if text == 'C':
            btn = tk.Button(root, text=text, font=('Arial', 12), command=onClearClick, width=5)
        elif text == '=':
            btn = tk.Button(root, text=text, font=('Arial', 12), command=prank, width=5)
        elif text == 'CC':
                    btn = tk.Button(root, text=text, font=('Arial', 12), command=onClearAllClick, width=5)
        else:                      
            btn = tk.Button(root, text=text, font=('Arial', 12), command=lambda t=text: onButtonClick(t), width=5)

        btn.grid(row=row, column=column)

def onButtonClick(buttonText):
    current = outputText.get()

    if current == '0':
        new_value = buttonText
    else:
         new_value = current + buttonText

    outputText.set(new_value)

def onClearClick():
    current = outputText.get()
    new_value = current[:-1]

    if new_value == '':
        new_value = '0'  

    outputText.set(new_value)

def onEqualClick():
    try:
        text = outputText.get()
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

        outputText.set(str(result))
    except:
        outputText.set('0')

def onClearAllClick():
    outputText.set('0')

def prank():
    outputText.set('Hello World!')

createButtonRow(window)
window.mainloop()