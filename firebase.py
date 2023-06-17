import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Grab the credentials
cred = credentials.Certificate('serviceAccountKey.json')

# Log into the admin account
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cloudtest-bd14e-default-rtdb.firebaseio.com/'
})
# Grab refrence to the database
ref = db.reference()

# Create two related tables
users_ref = ref.child('customers')
users_ref.set({
    'user1': {
        'name': 'John Doe',
        'age': 30
    },
    'user2': {
        'name': 'Jane Doe',
        'age': 25
    },
    'user3': {
        'name': 'Jim Bean',
        'age': 11
    },
    'user4': {
        'name': 'Steve Smith',
        'age': 110
    },
    'user5': {
        'name': 'John Hank',
        'age': 21
    }
})

orders_ref = ref.child('orders')
orders_ref.set({
    'order1': {
        'user_id': 'user1',
        'item': 'Book',
        'quantity': 1
    },
    'order2': {
        'user_id': 'user2',
        'item': 'Pen',
        'quantity': 3
    },
    'order3': {
        'user_id': 'user3',
        'item': 'Knife',
        'quantity': 1
    },
    'order4': {
        'user_id': 'user4',
        'item': 'Cake',
        'quantity': 30
    },
    'order5': {
        'user_id': 'user5',
        'item': 'Pencil',
        'quantity': 14
    },
    'order6': {
        'user_id': 'user1',
        'item': 'Keyboard',
        'quantity': 2
    }
})

#Add new customer function
def addCust(users_ref,name,age):
    users_ref.push({
        'name': name,
        'age':age
    })
#Add new order function
def addOrder(orders_ref,user_id,item,quantity):
    orders_ref.push({
        'user_id': user_id,
        'item': item,
        'quantity': quantity
    })
#Get order by key
def getOrder(orders_ref,key):
    return orders_ref.child(key)
#Get customer by key
def getCustomer(users_ref,key):
    return users_ref.child(key)

# Insert data into the tables using the functions
addCust(users_ref,'Bob Smith', 33)
addOrder(orders_ref,"user4",'pen',8)

#Update data in the tables
users_ref.child('user1').update({
    'age': 33
})
orders_ref.child('order1').update({
    'quantity': 4
})

#Delete data from table
users_ref.child('user3').delete()
orders_ref.child('order3').delete()

#Dump all the user/order data
print(users_ref.get())
print(orders_ref.get())