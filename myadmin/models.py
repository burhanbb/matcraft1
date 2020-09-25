import MySQLdb

db=MySQLdb.connect('localhost','root','root','matcraft')

cursor=db.cursor()

print('connection done....')

