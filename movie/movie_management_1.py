# code for the movie management
import cowsay
import mysql.connector as myc

x = myc.connect(host="localhost",user="root",passwd="pin@53z1985",database="movie_management" )  # connecting py & MySql
mycursor = x.cursor() # creating cursor

think = 'y'
while think == 'y':
    print('** _______________________________ movie management _______________________________ **')
    print('chose the section to work with ')
    print('press [10] for MOVIE RECORDS MANIPULATION')
    print('press [20] for RECOMMENDATION SYSTEM')
    print()

    work = int(input('What do you wanna perform :'))
    if work == 10:
        Ans = 'y'
        while Ans == 'y':
            print('* _______________________________ *** movie records manipulation *** _______________________________ *')

            print('The operation to perform')
            print('press [1] to add record')
            print('press [2] to update record')
            print('press [3] to delete record')
            print('press [4] to view record')
            print('press [5] to search record')
            print()

            manipulation = int(input('Enter the desired operation to perform  :'))


                                                        # movie management

            def add_data(q, w, e, r, t, y, u, i):
                query = "insert into movies values({0},'{1}',{2},'{3}','{4}','{5}','{6}','{7}')".format(q, w, e, r, t, y, u, i)
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

                print('_________________________________________________________________________________________________________')
                print('total no of record found : ', rowc)
                for record in mydata:
                    print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


            def search(q):
                query = 'select * from movies where movie_id = {}'.format(q)
                mycursor.execute(query)
                record = mycursor.fetchone()
                print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


            if manipulation == 1:                  # this block is for adding record in the table movies
                ans = 'y'
                while ans == 'y':
                    print('_________________________________________________________________________________________________________')
                    movie_id = int(input('Enter the movie_id :'))
                    name = input('Enter the name of the movie :')
                    rating = float(input('Enter IMDB rating of the movie :'))
                    director = input('Enter name of the director of the movie :')
                    actor = input('Enter name of the actor of the movie :')
                    genre = input('Enter genre of the movie :')
                    release_year = input('Enter release year of the movie :')
                    duration = input('Enter duration of the movie :')

                    add_data(movie_id,name,rating,director,actor,genre,release_year,duration)

                    ans = input('do you wanna add more y/n :')

            elif manipulation == 2:                 # this block is for updating existing record in the table movies
                ans = 'y'
                while ans == 'y':
                    print('_________________________________________________________________________________________________________')
                    movie_id = int(input('Enter movie Id of the movie which you want to update :'))
                    new_imdb = float(input('Enter the new imdb rating of the movie :'))

                    update_data(movie_id, new_imdb)

                    ans = input('do you wanna update more y/n :')

            elif manipulation == 3:                  # this block is for deleting existing record in the table movies
                ans = 'y'
                while ans == 'y':
                    print('_________________________________________________________________________________________________________')
                    movie_id = int(input('Enter the movie Id to delete :'))

                    delete_data(movie_id)

                    ans = input('do you wanna delete more y/n :')

            elif manipulation == 4:                  # this block is for viewing record in the table movies
                print('_________________________________________________________________________________________________________')
                view_table()

            elif manipulation == 5:                  # this block is for searching existing record in the table movies
                ans = 'y'
                while ans == 'y':
                    print('_________________________________________________________________________________________________________')
                    movie_id = int(input('Enter movie_id of the movie which you wanna search :'))
                    search(movie_id)
                    ans = input('enter do you wanna search again y/n :')
            
            print('_________________________________________________________________________________________________________')
            print()
            Ans = input('do you want to use movie manipulation again (y/n): ')


    elif work == 20:
        Ans = 'y'
        while Ans == 'y':
            print('_______________________________ recommendation system _______________________________')
            print('the operation to perform')
            print('press [1] to get best movies of the director')
            print('press [2] to get best movies in the genre')
            print('press [3] to get top movies according to imdb rating ')
            print()

            recommendation = int(input('Enter the type of recommendation you want to get :'))


                                                    # recommendation system

            def DIRECTOR(x,y):
                query = "select * from movies where director = '{}' and IMdb_rating > {}".format(x, y)
                mycursor.execute(query)
                mydata = mycursor.fetchall()
                for record in mydata:
                    print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


            def IMDB(x):
                query = 'select * from movies where IMdb_rating > {}'.format(x)
                mycursor.execute(query)
                mydata = mycursor.fetchall()
                for record in mydata:
                    print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


            def GENRE(x, y):
                query = "select * from movies where genre = '{}' and IMdb_rating > {}".format(x, y)
                mycursor.execute(query)
                mydata = mycursor.fetchall()
                for record in mydata:
                    print(record[0],',',record[1],',',record[2],',',record[3],',',record[4],',',record[5],',',record[6],',',record[7])


            if recommendation == 1:
                ans = 'y'
                while ans == 'y':
                    director = input('enter the name of the director for his best movies :')
                    imdb = float(input('enter the desired value of imdb according to you :'))

                    DIRECTOR(director,imdb)
                    
                    ans = input('do you wanna get best movies of the director again(y/n): ').lower()
                    print()

            elif recommendation == 2:
                ans = 'y'
                while ans == 'y':
                    genre = input('enter the genre of which you want recommendation for the movie :')
                    imdb = float(input('enter the desired value of imdb according to you :'))

                    GENRE(genre,imdb)

                    ans = input('do you wanna get best movies in the genre again(y/n): ').lower()
                    print()

            elif recommendation == 3:
                ans = 'y'
                while ans == 'y':
                    imdb = float(input('enter the desired value of imdb according to you :'))
                    IMDB(imdb)

                    ans = input('do you wanna get top movies of imdb again(y/n): ').lower()
                    print()

            print('_________________________________________________________________________________________________________')
            print()
            Ans = input('do you want to use recommendation again (y/n): ').lower()

    print('_________________________________________________________________________________________________________')
    print()   
    think = input('do you wanna use ALL this from start again (y/n): ').lower()
    print()

cowsay.ghostbusters('Thanks For Using, SEE you next Time!')
x.close()
