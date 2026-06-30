'''Inventary Module
Translate Data to the Machine Module,
add and register products'''
import machine
class product:
    def __init__(self,id,name,price,stock,sales=0):       
        self.id = id
        self.name = name
        self.price = str(price)
        self.stock = str(stock)
        self.sales = str(sales) 

    def to_dict(self):
        return {'id':self.id,'name':self.name,'price':self.price,'stock':self.stock,'sales':self.sales}
    
class inventary:
    def __init__(self,machine_instance):
        self.machine_instance = machine.Table(machine_instance)

    def create_new_id(self):
        self.get_id = self.machine_instance.readfile()
        if len(self.get_id) == 0:
            return 0
        else:
            return int(self.get_id[-1]['id']) +1
        
    def add_product(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
        if price <= 0 or stock <= 0:
            print("\nPrice and Stock must be positive numbers!\n")
            return
        item = product(self.create_new_id(),self.name,self.price,self.stock)
        self.machine_instance.append_row(item.to_dict())
        print('\nNew product added correctly!\n')

    def new_sale(self, id, quantity):
        quantity = int(quantity)
        rows = self.machine_instance.readfile()
        if quantity > 0:
            for item in rows:
                if item['id'] == id:
                    if int(item['stock']) >= quantity:
                        self.machine_instance.update_row(id, {
                            'stock': int(item['stock']) - quantity,
                            'sales': int(item['sales']) + quantity
                        })
                        print("\nSale registered correctly!\n")
                        return
                    else:
                        print("\nNot enough stock available!\n")
                        return
            print(f"\nProduct with id {id} not found!\n")
        else:
            print(f"\nYou must enter a positive number!\n")

    def update_price(self,id,price):
        price = float(price)
        rows = self.machine_instance.readfile()
        if price > 0:
            for item in rows:
                if item['id'] == id:
                    self.machine_instance.update_row(id,{'price': price})
                    print('\nPrice updated correctly!\n')
                    return
            print(f"\nProduct with id {id} not found\n")
        else:
            print('\nYou must enter a positive number!\n')

    def update_stock(self,id,new_stock):
        stock = int(new_stock)
        rows = self.machine_instance.readfile()
        if new_stock > 0:       
            for item in rows:
                if item['id'] == id:
                    self.machine_instance.update_row(id,{'stock': int(item['stock']) + stock})
                    print("\nStock updated correctly!\n")
                    return
            print(f"\nProduct with id {id} not found\n")
        else:
            print('\nYou must enter a positive number!\n')
            
    def delete_product(self,id):
        rows = self.machine_instance.readfile()
        for row in rows:
            if row['id'] == id:
                self.machine_instance.delete_row(id)
                print("\nProduct deleted correctly!\n")
                return
        print(f"\nProduct with id {id} not found!\n")
        

class analytics:
    def __init__(self,machine_instance):
        self.machine_instance = machine.Table(machine_instance)

    def total_sales(self):
        rows = self.machine_instance.readfile()
        return sum(int(item['sales']) for item in rows)
    
    def total_stock(self):
        rows = self.machine_instance.readfile()
        return sum(int(item['stock']) for item in rows)
    
    def total_stock_value(self):
        rows = self.machine_instance.readfile()
        return sum(float(item['price']) * int(item['stock']) for item in rows)
    
    def total_revenue(self):
        rows = self.machine_instance.readfile()
        return sum(int(item['sales']) * float(item['price']) for item in rows)
    





    



