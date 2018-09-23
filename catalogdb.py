import psycopg2

DBNAME = "news"


def popular_articles():
    '''Prints most popular articles'''
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute('''select title, te.views from articles inner join (
    select path, count(*) as views from log group by path) te
    on concat('/article/', articles.slug) = te.path order by views desc limit 3;''')
    results1 = c.fetchall()
    for title, views in results1:
         print ("{} -- {}views".format(title, views))
    db.close()


def popular_author():
    '''Prints most popular author'''
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute('''select name, sum from authors join
    (select author, sum(views) from (select author, title, te.views from articles inner join (
    select path, count(*) as views from log group by path) te
    on concat('/article/', articles.slug) = te.path order by views) as auth group by author)
    as auth_name
    on authors.id = auth_name.author;''')
    results2 = c.fetchall()
    for name, sum in results2:
        print("{} -- {}views".format(name, sum))
    db.close()

def erros():
        '''Prints most popular author'''
        db = psycopg2.connect(dbname=DBNAME)
        c = db.cursor()
        c.execute('''select date_trunc('day', per.days), Percentage from
        (select days, (ERROR * 1.0 / TOTAL) * 100.0 Percentage from
         (select date_trunc('day', time) days,
          COUNT(case when status='404 NOT FOUND' then 1 ELSE NULL END) ERROR,
          COUNT(1) TOTAL
          from log
          group by date_trunc('day', time)) A) per
          where percentage > 1;''')
        results3 = c.fetchall()
        for day, Percentage in results3:
            print("""{} - {}% errors""".format(day, Percentage))
        db.close()

if __name__ == '__main__':
    print ("Most popular three articles of all time.")
    popular_articles()
    print("Most popular article authors of all time.")
    popular_author()
    print("Days where more than 1% of requests lead to errors.")
    erros()
