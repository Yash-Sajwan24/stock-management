# STOCK MANAGEMENT

import os
import mysql.connector
import datetime
now = datetime.datetime.now()

def add_product():#------1.1
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           sql="INSERT INTO product(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
           code=int(input("\t\tEnter product code :"))
           search="SELECT count(*) FROM product WHERE pcode=%s;"
           val=(code,)
           mycursor.execute(search,val)
           for x in mycursor:
                      cnt=x[0]
           if cnt==0:
                      name=input("\t\tEnter product name :")
                      qty=int(input("\t\tEnter product quantity :"))
                      price=float(input("\t\tEnter product unit price :"))
                      cat=input("\t\tEnter Product category :")
                      val=(code,name,price,qty,cat)
                      mycursor.execute(sql,val)
                      mydb.commit()
           else:
                      print("\t\t Product already exist")
def list_product():#------1.2.1
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from product"
           mycursor.execute(sql)
           clrscr()
           print("PRODUCT DETAILS")
           print("-"*47)
           print("code,name,price,quantity,category")
           print("-"*47)
           for i in mycursor:
                      print(i[0],i[1],i[2],i[3],i[4])
           print("-"*47)
           


def list_prcode(code):#------1.2.2
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from product WHERE pcode=%s"
           val=(code,)
           mycursor.execute(sql,val)
           clrscr()
           print("PRODUCT DETAILS")
           print("-"*47)
           print("code,name,price,quantity,category")
           print("-"*47)
           for i in mycursor:
                      print(i[0],i[1],i[2],i[3],i[4])
           print("-"*47)


       
                              
def list_prcat(cat):#------1.2.3
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           print (cat)
           sql="SELECT * from product WHERE pcat =%s"
           val=(cat,)
           mycursor.execute(sql,val)
           clrscr()
           print("PRODUCT DETAILS")
           print("-"*47)
           print("code,name,price,quantity,category")
           print("-"*47)
           for i in mycursor:
                      print(i[0],i[1],i[2],i[3],i[4])
           print("-"*47)

def search_product():#------1.2
                    
           while True :
                      print(" 1. List all product")
                      print(" 2. List product code wise")
                      print(" 3. List product categoty wise")
                      print(" 4. Back (Main Menu)\n")
                     
                      s=int(input("Enter Your Choice :"))
                      if s==1 :
                                 list_product()
                      if s==2 :
                                  code=int(input(" Enter product code :"))
                                  list_prcode(code)
                                  
                      if s==3 :
                                  cat=input("Enter category :")
                                  list_prcat(cat)
                                 
                      if s== 4 :
                                 break
def update_product():#------1.3
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           code=int(input("Enter the product code :"))
           qty=int(input("Enter the quantity :"))
           sql="UPDATE product SET pqty=%s WHERE pcode=%s;"
           val=(qty,code)
           mycursor.execute(sql,val)
           mydb.commit()
           print("\t\t Product details updated")

def delete_product():#------1.4
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           code=int(input("Enter the product code :"))
           sql="DELETE FROM product WHERE pcode = %s;"
           val=(code,)
           mycursor.execute(sql,val)
           mydb.commit()
           print(mycursor.rowcount," record(s) deleted");

def product_mgmt( ):#------1
            while True :
                      print(" 1. Add New Product")
                      print(" 2. List Product")
                      print(" 3. Update Product")
                      print(" 4. Delete Product")
                      print(" 5. Back (Main Menu)\n")
                      p=int (input("Enter Your Choice :"))
        
                      if p==1:
                                 add_product()
                      if p==2:
                                 search_product()
                      if p==3:
                                 update_product()
                      if p==4:
                                 delete_product()
                      if p== 5 :
                                 break
def add_order():#------2.1
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           now = datetime.datetime.now()
           sql="INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat) values (%s,%s,%s,%s,%s,%s,%s)"
           code=int(input("Enter product code :"))
           oid=now.year+now.month+now.day+now.hour+now.minute+now.second
           qty=int(input("Enter product quantity : "))
           price=float(input("Enter Product unit price: "))
           cat=input("Enter product category: ")
           supplier=input("Enter Supplier details: ")           
           val=(oid,now,code,price,qty,supplier,cat)
           mycursor.execute(sql,val)
           mydb.commit()



def list_order():#------2.2
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from orders"
           mycursor.execute(sql)
           clrscr()
           print(" ORDER DETAILS")
           print("-"*85)
           print("orderid,Date,Product code,price,quantity,Supplier,Category")
           print("-"*85)
           for i in mycursor:
                      print(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
           print("-"*85)
                
def purchase_mgmt( ):#------2
           while True :
                print(" 1. Add Order")
                print(" 2. List Order")
                print(" 3. Back (Main Menu)\n")
                o=int (input("Enter Your Choice :"))
                if o==1 :
                            add_order()
                if o==2 :
                            list_order()
                if o== 3 :
                            break
def sale_product():#------3.1
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           pcode=input("Enter product code: ")
           sql="SELECT count(*) from product WHERE pcode=%s;"
           val=(pcode,)
           mycursor.execute(sql,val)
           for x in mycursor:
                      cnt=x[0]
           if cnt!=0 :
                      sql="SELECT * from product WHERE pcode=%s;"
                      val=(pcode,)
                      mycursor.execute(sql,val)
                      for x in mycursor:
                                 print(x)
                                 price=int(x[2])
                                 pqty=int(x[3])
                      qty=int(input("Enter no of quantity sold:"))
                      if qty <= pqty:
                                 total=qty*price;
                                 print ("Collect  Rs. ", total)
                                 sno=int(input("enter the sales id: "))
                                 sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
                                 val=(sno,datetime.datetime.now(),pcode,price,qty,total) 
                                 mycursor.execute(sql,val)
                                 sql="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
                                 print("Your record have been added\n")
                                 val=(qty,pcode)
                                 mycursor.execute(sql,val)
                                 mydb.commit()
                      else:
                                 print(" Quantity not Available")
           else:
                      print(" Product is not avalaible")

def list_sale():#------3.2
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * FROM sales"
           mycursor.execute(sql)
           print(" SALES DETAILS")
           print("-"*80)
           print("Sales id,Date,Product Code,Price,Quantity,Total")
           print("-"*80)
           for x in mycursor:
                      print(x[0],x[1],x[2],x[3],x[4],x[5])
           print("-"*80)
                          
def sales_mgmt( ):#------3
           while True :
                      print(" 1. Sale Items")
                      print(" 2. List Sales")
                      print(" 3. Back (Main Menu)\n")
                      s=int (input("Enter Your Choice :"))
                      if s== 1 :
                                 sale_product()
                      if s== 2 :
                                 list_sale()
                      if s== 3 :
                                 break
def add_user():#------4.1
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           uid=input("Enter emaid id :")
           name=input(" Enter Name :")
           paswd=input("Enter Password :")
           sql="INSERT INTO user values (%s,%s,%s);"
           val=(uid,name,paswd)
           mycursor.execute(sql,val)
           mydb.commit()
           print(mycursor.rowcount, " user created")


def list_user():#------4.2
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT uid,uname from user"
           mycursor.execute(sql)
           clrscr()
           print(" USER DETAILS")
           print("-"*27)
           print(" UID,name")
           print("-"*27)
           for i in mycursor:
                      print(i[0],i[1])
           print("-"*27)
def user_mgmt( ):#------4
           while True :
                      print(" 1. Add user")
                      print(" 2. List user")
                      print(" 3. Back (Main Menu)\n")
                      u=int (input("Enter Your Choice :"))
                      if u==1:
                                 add_user()
                      if u==2:
                                 list_user()
                      if u==3:
                                 break

def create_database():#------5.1
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")
           mycursor=mydb.cursor()
           print(" Creating PRODUCT table")
           sql = "CREATE TABLE if not exists product (\
                  pcode int(4) PRIMARY KEY,\
                  pname char(30) NOT NULL,\
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  pcat char(30));"
           mycursor.execute(sql)
           print(" Creating ORDER table")
           sql = "CREATE TABLE if not exists orders (\
                  orderid int(4)PRIMARY KEY ,\
                  orderdate DATE ,\
                  pcode char(30) NOT NULL , \
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  supplier char(50),\
                  pcat char(30));"
           mycursor.execute(sql)
           print(" ORDER table created")

           print(" Creating SALES table")
           sql = "CREATE TABLE if not exists sales (\
                  salesid int(4) PRIMARY KEY ,\
                  salesdate DATE ,\
                  pcode char(30) references product(pcode), \
                  pprice float ,\
                  pqty int(4) ,\
                  Total float\
                  );"
           mycursor.execute(sql)
           print(" SALES table created")
           sql = "CREATE TABLE if not exists user (\
                  uid char(6) PRIMARY KEY,\
                  uname char(30) NOT NULL,\
                  upwd char(30));"
           mycursor.execute(sql)
           print(" USER table created")

def list_database():#------5.2
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="aabha",database="stock")   
        mycursor=mydb.cursor()
        sql="show tables;"
        mycursor.execute(sql)
        for i in mycursor:
                   print(i)



def db_mgmt( ):#------5
           while True :
                      print("\t\t\t 1. Database creation")
                      print("\t\t\t 2. List Database")
                      print("\t\t\t 3. Back (Main Menu)")
                      p=int (input("\t\tEnter Your Choice :"))
                      if p==1 :
                                 create_database()
                      if p==2 :
                                 list_database()
                      if p== 3 :
                                 break





def clrscr():
            print("\n"*5)


while True:
           clrscr()
           print(" ****************")
           print(" STOCK MANAGEMENT")
           print(" ****************\n")
           print(" 1. PRODUCT MANAGEMENT")
           print(" 2. PURCHASE MANAGEMENT")
           print(" 3. SALES MANAGEMENT")
           print(" 4. USER MANAGEMENT")
           print(" 5. DATABASE SETUP")
           print(" 6. EXIT\n")
           n=int(input("Enter your choice :"))
           print("")
           if n== 1:
                      product_mgmt()
           if n== 2:
                      os.system('cls')
                      purchase_mgmt()
           if n== 3:
                      sales_mgmt()
           if n== 4:
                      user_mgmt()
           if n==5 :
                      db_mgmt()
           if n== 6:
                      break
