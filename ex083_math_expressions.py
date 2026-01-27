expression = input('Enter the math expression: ').strip()
open_p = []

print(expression)

for element in expression:
    if element == '(':
        open_p.append(element)
    if element == ')':
        if len(open_p) == 0:
            break
        else:
            open_p.pop()


if len(open_p) == 0:
    print("Expressao válida")
else:
    print("Expressao invalida")