# Python_PostgreSQL-DB

#PostgreSQL Project

This is a PostgreSQL-powered Python project that demonstrates full control over a local SQL database using `psycopg2`. The project includes:

- Creation of tables: `users`, `products`, `orders`, and `order_items`
- Inserting test data into each table using Python
- Foreign key relationships for safe, connected data
- Dynamic user ID selection to avoid foreign key errors

## Project Structure

- `init_db.py`: Initializes the database structure (tables and relationships)
- `insert_data.py`: Populates the tables with sample data, including one order and its related items

## How to Run

1. Make sure PostgreSQL is installed and running
2. Create your database and user using psql:
   ```bash
   CREATE USER example WITH PASSWORD 'example';
   CREATE DATABASE example OWNER example;
   GRANT ALL PRIVILEGES ON DATABASE example TO example;
   ```
3. Create a virtual environment and activate it:
   ```bash
   python3 -m venv postgresqlvenv
   source postgresqlvenv/bin/activate
   pip install psycopg2-binary
   ```
4. Run the database setup:
   ```bash
   python init_db.py
   ```
5. Insert the sample data:
   ```bash
   python insert_data_fixed.py
   ```

## Author
Lazyninjawithkatana
