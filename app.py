from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import subprocess

app = Flask(__name__)

import subprocess

def get_public_ip():
    # Run the Terraform command to get the public IP address
    cmd = "terraform output -raw db_public_ip"
    public_ip = subprocess.check_output(cmd, shell=True, text=True).strip()
    return public_ip

#if __name__ == "__main__":
#    public_ip = get_public_ip()
#    print(f"The public IP address is: {public_ip}")
    # Now you can use the 'public_ip' variable in your Python code as needed.




# Connect to the database
conn = psycopg2.connect(
    database="my-database",
    user="me",
    password="changeme", 
    host=get_public_ip())
  
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

from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import subprocess

app = Flask(__name__)

import subprocess

def get_public_ip():
    # Run the Terraform command to get the public IP address
    cmd = "terraform output -raw db_public_ip"
    public_ip = subprocess.check_output(cmd, shell=True, text=True).strip()
    return public_ip

#if __name__ == "__main__":
#    public_ip = get_public_ip()
#    print(f"The public IP address is: {public_ip}")
    # Now you can use the 'public_ip' variable in your Python code as needed.




# Connect to the database
conn = psycopg2.connect(
    database="my-database",
    user="me",
    password="changeme", 
    host=get_public_ip())
  
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
    database="postgres",
    user="postgres",
    password="1234",
    host="34.116.216.64")
  
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
    database="postgres",
    user="postgres",
    password="1234",
    host="34.116.216.64")
  
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

@app.route('/create', methods=['POST'])
def create():
    conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="1234",
    host="34.116.216.64")
  
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

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0',  port=45612)
   #from waitress import serve
   #serve(app, port=45612)
  
  
