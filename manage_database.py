import sqlite3
import ast

conn = sqlite3.connect('database.db')
c = conn.cursor()

# c.execute("""CREATE TABLE count_names(
#             id int,
#             politician_name text,
#             date_mentioned text,
#             article_title text,
#             article_author text,
#             article_link text,
#             XML int
#             )""")


#
# def check_if_added(name):
#     # 0 = DOES NOT EXIST; 1 = EXISTS; RETURN TRUE = EXISTS
#     c.execute('SELECT EXISTS(SELECT 1 FROM count_names WHERE politician_name=(:politician_name))',{'politician_name': name})
#     if c.fetchone()[0]:
#          return True
#
#
# def insert_politician(name, date):
#     if check_if_added(name):
#         # print("already exists")
#         pass
#     else:
#         arr = str([date])
#         with conn:
#             c.execute("INSERT INTO count_names VALUES (:politician_name, :mentioned_date)", {'politician_name': name, 'mentioned_date': arr})
#
#
# def get_politician_dates(name):
#     with conn:
#         c.execute("SELECT * FROM count_names WHERE politician_name=:politician_name", {'politician_name':name})
#         print(c.fetchone())
#         return c.fetchone()[1]
#
#
#
# def update_date_mentioned(name, date):
#     old_arr = ast.literal_eval(get_politician_dates(name))
#     print(old_arr[0])
#     new_arr = old_arr.append(date)
#     print(new_arr)
#     # with conn:
#         # c.execute("""UPDATE count_names SET dates_mentioned=:dates_mentioned WHERE politician_name=:politician_name""",{"dates_mentioned":new_arr, "politician_name":name})
#
#
# update_date_mentioned("Lee Hsien Loong", "30 jan 2021")


def insert_name_instance(name, date, article_title, article_author, article_link, xml):
    with conn:
        c.execute("SELECT * FROM count_names ORDER BY id DESC LIMIT 1")
        new_id = c.fetchone()[0] + 1

    c.execute("INSERT INTO count_names VALUES (:id, :politician_name, :date_mentioned, :article_title, :article_author, :article_link, :XML)",
            {'id': new_id, 'politician_name': name, 'date_mentioned': date, 'article_title': article_title, 'article_author': article_author, 'article_link':article_link, 'XML':xml})
    conn.commit()
    print("NOTE: Added "+name+" to database")


def get_database_values(name, xml):
    if not xml[0]:
        with conn:
            c.execute("SELECT * FROM count_names WHERE politician_name=:politician_name",{"politician_name":name})
            return c.fetchall()
    else:
        xml = xml[1]
        with conn:
            c.execute("SELECT * FROM count_names WHERE politician_name=:politician_name AND XML=:xml",{"politician_name":name, "xml":xml})
            return c.fetchall()

# insert_name_instance("J S Mill", "20 aug 2022", "test", "test", "test")


# def delete_rows(id):
#     with conn:
#         try:
#             c.execute("DELETE from count_names where id = :id", {"id":id})
#             conn.commit()
#         except:
#             print("id "+str(id)+" already deleted")
#
# #range (x,y) includes x but doesn't include y
# for x in range(2,220):
#     delete_rows(x)


# conn.close()


#2-219;219-490