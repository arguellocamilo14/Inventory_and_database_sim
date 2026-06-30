'''Machine Module
Read, Write and Structure the .CSV files'''
import csv

class Table:
    def __init__(self,filename,columns = ['id','name','price','stock','sales']):
        self.file = filename
        self.columns = columns

    def readfile(self):
        try:
            with open(self.file,'r', newline = '') as f:
                self.reader = csv.DictReader(f)
                return [x for x in self.reader]
        
        except FileNotFoundError:
            with open(self.file,'w', newline = '') as cf:
                cf.write(','.join(self.columns) + '\n')
            return self.readfile()
        
    def append_row(self,dictionary):
        try:
            with open(self.file,"+a", newline = '\n') as f:
                writer = csv.DictWriter(f, fieldnames= self.columns)
                writer.writerow(dictionary)
        except IOError as e:
            print(f"Something happened: {e}")

    
    def update_row(self, row_id, updated_fields):
        rows = self.readfile()
        found = False

        for row in rows:
            if (row['id']) == (row_id):
                row.update(updated_fields)  
                found = True
                break

        if not found:
            print(f"No row with id {row_id}")

        with open(self.file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.columns)
            writer.writeheader()
            writer.writerows(rows)
    
    def delete_row(self,id):
            rows = self.readfile()
            rows = [row for row in rows if row['id'] != id]
            for row in rows:
                if int(row['id']) > int(id):
                    row.update({'id': int(row['id']) - 1}) 

            with open(self.file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.columns)
                writer.writeheader()
                writer.writerows(rows)



        



