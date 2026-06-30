import machine
import inventary
import time
running = True
file_path = input('Enter the .csv file path you will be working on: ')
while running:

    print("""----------------Store Manager----------------  
Options available:
0 - View all current products
1 - Add a product
2 - Register a sale
3 - Update the price of a product
4 - Update the stock of a product
5 - Total sales
6 - Total stock
7 - Total stock value
8 - Total revenue
9 - Delete a product
10 - QUIT
----------------------------------------------""")
    option = input('Enter the option (0 - 10): ')
    print('----------------------------------------------')
    
    if option.isdigit() and int(option) >= 0 and int(option) <= 9:
        
        product = inventary.inventary(file_path)
        analytics = inventary.analytics(file_path)
        if option == '0':
            Table = machine.Table(file_path)
            rows = Table.readfile()
            header = Table.columns
            print(' | '.join(header))
            print('---------------------------------')
            for row in rows:
                print(f'{row['id']}  |  {row['name']}  |  {row['price']}  |  {row['stock']}  |  {row['sales']}\n')
            time.sleep(5)
        if option == '1':
            try:
                name = input("Enter the name of the new product: ")
                price = float(input('Enter the price of the product $(0.00): '))
                stock = int(input('Enter the stock of the product: '))
                product.add_product(name,price,stock)
                time.sleep(2)
            except ValueError:
                print("\nMust enter a valid price or stock!\n")
                time.sleep(2)

        if option == '2':
            try:  
                id = input('Enter the id of the product: ')
                quantity = int(input("Enter the quantity you sold: "))
                product.new_sale(id,quantity)
                time.sleep(2)
            except:
                print("\nMust enter a valid quantity!\n")
                time.sleep(2)

        if option == '3':
            try:
                id = input("Enter the id of the product: ")
                price = float(input('Enter the updated price of the product $(0.00): '))
                product.update_price(id,price)
                time.sleep(2)
            except:
                print("\nMust enter a valid price!\n")
                time.sleep(2)

        if option == '4':
            try:
                id = input("Enter the id of the product: ")
                new_stock = int(input("Enter the quantity to add for the current stock: "))
                product.update_stock(id,new_stock)
                time.sleep(2)
            except:
                print("\nMust enter a valid stock!\n")
                time.sleep(2)

        if option == '5':
            print(f'\nYour total of registred sales is: {analytics.total_sales()}\n')
            time.sleep(3)
        if option == '6':
            print(f'\nYour total stock is: {analytics.total_stock()}\n')
            time.sleep(3)
        if option == '7':
            print(f'\nThe total value of you stock is: ${analytics.total_stock_value()}\n')
            time.sleep(3)
        if option == '8':
            print(f'\nThe total revenue is: ${analytics.total_revenue()}\n')
            time.sleep(3)
        if option == '9':
            id = input('Enter the id of the product you want to delete: ')
            product.delete_product(id)
            time.sleep(2)

    elif option == '10':
            running = False

    else:
        print('\nPlease enter a valid option (0 - 10) !\n')
        time.sleep(2)
    
    
