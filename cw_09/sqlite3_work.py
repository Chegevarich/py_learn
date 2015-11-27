#coding:utf-8
import sqlite3
conn = sqlite3.connect('example.db')

#create table

conn.execute('''
	create table if not exists cusomer
	(id integer primary key autoincrement, name text, age integer )
	''')

conn.execute('''
	create table if not exists products
	(id integer primary key autoincrement, name text, price integer )
	''')

conn.execute('''
	create table if not exists sales
	( id integer primary key autoincrement, product_id integer, customer_id integer, count integer)
	''')


#conn.execute('insert into cusomer (name, age) values ("customer_0", 30)')
#conn.execute('insert into cusomer (name, age) values ("customer_1", 31)')
#conn.execute('insert into cusomer (name, age) values ("customer_2", 32)')


#conn.execute('''insert into products (name, price) values 
#		("product_0", 107),
#		("product_1", 106),
#		("product_2", 105),
#		("product_3", 1004),
#		("product_4", 103),
#		("product_5", 102),
#		("product_6", 101)
#		''')

#conn.execute('''
#insert into sales (product_id, customer_id, count) values 
#	(1, 1, 12),
#	(2, 1, 12),
#	(3, 1, 12),
#	(4, 1, 12),
#	(5, 1, 12),
#	(6, 1, 12),
#	(7, 1, 12)
#''')


conn.commit()

print(conn.execute('select * from products').fetchall())

cur = conn.execute('select * from cusomer')

lj = conn.execute('''
select c.name, p.name, s.count, p.price
	from sales s
	left join products p on p.id = s.product_id
	left join cusomer c on c.id = s.customer_id
'''
	)

print(lj.fetchall())

print(cur.fetchone())
print(cur.fetchone())

print(cur.fetchmany(2))
print(cur.fetchmany(2))

for row in cur:
	print(row)
	print(type(row))

print(cur.fetchone())
print(cur.fetchone())

conn.close()