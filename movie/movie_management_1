# code for the movie management

import mysql.connector as myc

x = myc.connect(host="localhost",user="root",passwd="pin@53z1985",database="movie_management" )  # connecting py & MySql
mycursor = x.cursor()

print('** =============================== movie management =============================== **')
print('chose the section to work with ')
print('press [10] for MOVIE RECORDS MANIPULATION')
print('press [20] for RECOMMENDATION SYSTEM')

m = int(input('What do you wanna perform :'))
if m == 10:
    print('* =============================== *** movie records manipulation *** =============================== *')

    print('The operation to perform')
    print('press [1] to add record')
    print('press [2] to update record')
    print('press [3] to delete record')
    print('press [4] to view record')
    print('press [5] to search record')

    y = int(input('Enter the desired operation to perform  :'))


                                                 # movie management

    def add_data(q, w, e, r, t, y, u, i):
        query = 'insert into movies values({0},{1},{2},{3},{4},{5},{6},{7})'.format(q, w, e, r, t, y, u, i)
        mycursor.execute(query)
        x.commit()
        print('## record saved ##')


    def update_data(q, s):
        query = 'update movies set IMdb_rating = {0} where movie_id = {1}'.format(q, s)
        mycursor.execute(query)
        x.commit()
        print('## record updated ##')


    def delete_data(q):
        query = 'delete from movies where movie_id = {}'.format(q)
        mycursor.execute(query)
        x.commit()
        print('## record deleted ##')


    def view_table():
        query = 'select * from movies '
        mycursor.execute(query)
        mydata = mycursor.fetchall()
        rowc = mycursor.rowcount

        print('=========================================================================================================')
        print('total no of record found : ', rowc)
        for record in mydata:
            print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


    def search(q):
        query = 'select * from movies where movie_id = {}'.format(q)
        mycursor.execute(query)
        mydata = mycursor.fetchone()
        print(mydata)


    if y == 1:                  # this block is for adding record in the table movies
        ans = 'y'
        while ans == 'y':
            print('=========================================================================================================')
            a = int(input('Enter the movie_id :'))
            s = input('Enter the name of the movie :')
            d = float(input('Enter IMDB rating of the movie :'))
            f = input('Enter name of the director of the movie :')
            g = input('Enter name of the actor of the movie :')
            h = input('Enter genre of the movie :')
            j = input('Enter release year of the movie :')
            k = input('Enter duration of the movie :')

            add_data(a,s,d,f,g,h,j,k)

            ans = input('do you wanna add more y/n :')

    elif y == 2:                 # this block is for updating existing record in the table movies
        ans = 'y'
        while ans == 'y':
            print('=========================================================================================================')
            a = int(input('Enter movie Id of the movie which you want to update :'))
            s = float(input('Enter the new imdb rating of the movie :'))

            update_data(s, a)

            ans = input('do you wanna update more y/n :')

    elif y == 3:                  # this block is for deleting existing record in the table movies
        ans = 'y'
        while ans == 'y':
            print('=========================================================================================================')
            a = int(input('Enter the movie Id to delete :'))

            delete_data(a)

            ans = input('do you wanna delete more y/n :')

    elif y == 4:                  # this block is for viewing record in the table movies
        print('=========================================================================================================')
        view_table()

    elif y == 5:                  # this block is for searching existing record in the table movies
        ans = 'y'
        while ans == 'y':
            print('=========================================================================================================')
            a = int(input('Enter movie_id of the movie which you wanna search :'))
            search(a)
            ans = input('enter do you wanna search again y/n :')


elif m == 20:
    print('=============================== recommendation system ===============================')
    print('the operation to perform')
    print('press [1] to get best movies of the director')
    print('press [2] to get best movies in the genre')
    print('press [3] to get top movies according to imdb rating ')

    l = int(input('Enter the type of recommendation you want to get :'))


                                            # recommendation system

    def director(x,y):
        query = 'select * from movies where director = {} and IMdb_rating > {}'.format(x, y)
        mycursor.execute(query)
        mydata = mycursor.fetchall()
        for record in mydata:
            print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


    def Imdb(x):
        query = 'select * from movies where IMdb_rating > {}'.format(x)
        mycursor.execute(query)
        mydata = mycursor.fetchall()
        for record in mydata:
            print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


    def genre(x, y):
        query = 'select * from movies where genre = {} and IMdb_rating > {}'.format(x, y)
        mycursor.execute(query)
        mydata = mycursor.fetchall()
        for record in mydata:
            print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


    if l == 1:
        p = input('enter the name of the director for his best movies :')
        o = float(input('enter the desired value of imdb according to you :'))

        director(p,o)

    elif l == 2:
        p = input('enter the genre of which you want recommendation for the movie :')
        o = float(input('enter the desired value of imdb according to you :'))

        genre(p,o)

    elif l == 3:
        p = float(input('enter the desired value of imdb according to you :'))
        Imdb(p)

