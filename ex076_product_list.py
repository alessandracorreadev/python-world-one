products = ('Gel Pen Set', 12.99,
            'Sticky Note Pack', 5.25,
            'Minimalist Notebook', 8.50,
            'Pastel Highlighters', 7.80,
            'Acrylic Pencil Holder', 11.00,
            'Desk Organizer Tray', 19.99,
            'Sketchbook', 14.60,
            'Brush Pen', 7.95)

print('-'*50)
print('PRODUCT PRICE LIST'.center(50))
print('-'*50)

for item in range(0, len(products), 2):
    print(f"{products[item]}".ljust(41, '.'), end='$')
    print(f"{products[item + 1]:.2f}".rjust(7))

print('-'*50)
print('END OF THE LIST'.center(50))
print('-'*50)