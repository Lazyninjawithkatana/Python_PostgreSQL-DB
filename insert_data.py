import psycopg2

connect = psycopg2.connect(
    host='example',
    database='example',
    user='example',
    password='example'
)

cur = connect.cursor()

# ADD USERS
users = [
    ('example', 'example'),
    ('example', 'example')
]

for user in users:
    cur.execute('INSERT INTO users (username, email) VALUES (%s, %s)', user)

# ADD PRODUCTS
products = [
    ('example', 99.99, 10),
    ('Cexample', 49.90, 30),
    ('example', 150.00, 5)
]

for product in products:
    cur.execute('INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)', product)

# ADD ORDER

# GET user_id dynamically
cur.execute("SELECT id FROM users WHERE username = %s", ('example',))
user_id = cur.fetchone()[0]

cur.execute('INSERT INTO orders (user_id) VALUES (%s) RETURNING id', (user_id,))

order_id = cur.fetchone()[0]

order_items = [
    (order_id, 1, 2),
    (order_id, 3, 1)
]

for item in order_items:
    cur.execute('INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)', item)

connect.commit()
cur.close()
connect.close()

print('[*] Insert Data uploaded successfully')
