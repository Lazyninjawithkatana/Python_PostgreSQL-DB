import psycopg2

connect = psycopg2.connect(
    host='example',
    database='example',
    user='example',
    password='example'
)

cur = connect.cursor()

#USERS TABLE
cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username TEXT,
    email TEXT        
)
''')

#PRODUCTS TABLE
cur.execute('''
CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC(10, 2),
    stock INTEGER
)
''')

#ORDERS TABLE
cur.execute('''
CREATE TABLE IF NOT EXISTS orders(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

#ORDERED ITEMS
cur.execute('''
CREATE TABLE IF NOT EXISTS order_items(
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER
)
''')

connect.commit()
cur.close()
connect.close()

print('[*] DataBase added successfully')
