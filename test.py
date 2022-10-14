a = [
     {'t1':
          [{'nt1':['url1', 'price1']},
           {'nt2':['url2', 'price2']}]
      },
     {'t2':
          [{'nt1':['url1', 'price1']},
           {'nt2':['url2', 'price2']}]
      }
     ]

insert = '''
insert into sales(t_name, p_name, url, price)
values (%s, %s, %s, %s)
'''

w = [
    ("https://www.bershka.com/by/%D0%B6%D0%B8%D0%BB%D0%B5%D1%82-%D0%B2-%D0%BA%D0%BB%D0%B5%D1%82%D0%BA%D1%83-c0p103214996.html?colorId=800", '49.99'),
    ("https://www.bershka.com/by/%D0%B6%D0%B0%D0%BA%D0%BA%D0%B0%D1%80%D0%B4%D0%BE%D0%B2%D1%8B%D0%B9-%D1%81%D0%B2%D0%B8%D1%82%D0%B5%D1%80-c0p103907519.html?colorId=800", '69.99')
]


b = []

for i in a:
    for c in i:
        for v in i[c]:
            for nt in v:
                b.append(
                    (
                        c, nt, v[nt][0], v[nt][1]
                     )
                )

from mysql.connector import connect, Error
try:
    with connect(
        host="localhost",
        user="root",
        password="",
        database="b_py"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.executemany(insert, b)
            connection.commit()
except Error as e:
    print(e)