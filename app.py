from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os 
app = Flask(__name__)

#unix_socket = '/cloudsql/{}'.format("celtic-beacon-387519:europe-central2:main-instance")

# Connect to the database
conn = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST'),
    database=os.environ.get('POSTGRES_DATABASE'),
    user=os.environ.get('POSTGRES_USERNAME'),
    password=os.environ.get('POSTGRES_PASSWORD')
    )
  
# create a cursor
cur = conn.cursor()
  
# if you already have any table or not id doesnt matter this 
# will create a products table for you.
cur.execute(
   '''CREATE TABLE IF NOT EXISTS products (id serial \
    PRIMARY KEY, name varchar(100), price float);''')
  
# Insert some data into the table
cur.execute(
   '''INSERT INTO products (name, price) VALUES \
  ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''')
  
# commit the changes
conn.commit()
  
# close the cursor and connection
cur.close()
conn.close()
  
  
@app.route('/')
def index():
    # Connect to the database
    conn = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST'),
    database=os.environ.get('POSTGRES_DATABASE'),
    user=os.environ.get('POSTGRES_USERNAME'),
    password=os.environ.get('POSTGRES_PASSWORD')
    )
  
    # create a cursor
    cur = conn.cursor()
  
    # Select all products from the table
    cur.execute('''SELECT * FROM products''')
  
    # Fetch the data
    data = cur.fetchall()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return render_template('index.html', data=data)
  
  
@app.route('/create', methods=['POST'])
def create():
    conn = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST'),
    database=os.environ.get('POSTGRES_DATABASE'),
    user=os.environ.get('POSTGRES_USERNAME'),
    password=os.environ.get('POSTGRES_PASSWORD')
    )
  
    cur = conn.cursor()
  
    # Get the data from the form
    name = request.form['name']
    price = request.form['price']
  
    # Insert the data into the table
    cur.execute(
        '''INSERT INTO products \
        (name, price) VALUES (%s, %s)''',
        (name, price))
  
    # commit the changes
    conn.commit()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return redirect(url_for('index'))
  
  
@app.route('/update', methods=['POST'])
def update():
    conn = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST'),
    database=os.environ.get('POSTGRES_DATABASE'),
    user=os.environ.get('POSTGRES_USERNAME'),
    password=os.environ.get('POSTGRES_PASSWORD')
    )
  
    cur = conn.cursor()
  
    # Get the data from the form
    name = request.form['name']
    price = request.form['price']
    id = request.form['id']
  
    # Update the data in the table
    cur.execute(
        '''UPDATE products SET name=%s,\
        price=%s WHERE id=%s''', (name, price, id))
  
    # commit the changes
    conn.commit()
    return redirect(url_for('index'))
  
  
@app.route('/delete', methods=['POST'])
def delete():
    conn = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST'),
    database=os.environ.get('POSTGRES_DATABASE'),
    user=os.environ.get('POSTGRES_USERNAME'),
    password=os.environ.get('POSTGRES_PASSWORD')
    )

    cur = conn.cursor()
  
    # Get the data from the form
    id = request.form['id']
  
    # Delete the data from the table
    cur.execute('''DELETE FROM products WHERE id=%s''', (id,))
  
    # commit the changes
    conn.commit()
  
    # close the cursor and connection
    cur.close()
    conn.close()
  
    return redirect(url_for('index'))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return f'path /{path}'
  
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0',  port=45612)
   #from waitress import serve
   #serve(app, port=45612)
