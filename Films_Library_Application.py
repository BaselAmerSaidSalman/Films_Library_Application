import time
import re
import os
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

films_dic = {}
user_info_dic = {}
film_author_results = []
film_year_results = []

class Film:
  def __init__(self, type, name, author, year):
    self.type = type
    self.name = name
    self.author = author
    self.year = year

def add_film():
    film_type = input("Please enter your film type: ")
    film_name = input("Please enter your film name: ")
    film_author = input("Please enter your film author: ")
    film_year = input("Please enter the year that film was made: ")

    return Film(film_type, film_name, film_author, film_year)


class User:
   def __init__(self, name, email, password):
      self.name = name
      self.email = email
      self.password = password
    
def create_user():
    user_name = input("Please enter your name: ")
    user_email = input("Please enter your email: ")
    user_password = input("Please enter your password: ")

    return User(user_name, user_email, user_password)


def user_films():
    print("****************** Welcome to your films library! ******************\n")
    print("Choose an Action\n1. Create new film info\n2. See your films\n3. Search about film\n4. Exit\n")
    user_choice = input("Enter your choice (1,2,3 or 4): ")
    while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4":
       print("Sorry, invalid choice")
       user_choice = input("Enter your choice (1,2,3 or 4) only: ")
    if user_choice == "1":
        clear_screen()
        time.sleep(0.5)
        create_new_film = add_film()
        if films_dic:
            if create_new_film.type in films_dic:
                if create_new_film.name in films_dic[create_new_film.type]:
                    print("We had this film already!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films()
                else:
                    films_dic[create_new_film.type][create_new_film.name] = {"Author" : create_new_film.author, "Year" : create_new_film.year}
                    print("Film Added")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films()
            else:
                films_dic[create_new_film.type] = {create_new_film.name : {"Author" : create_new_film.author, "Year" : create_new_film.year}}
                print("Film Added")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                user_films()
        else:
            films_dic[create_new_film.type] = {create_new_film.name : {"Author" : create_new_film.author, "Year" : create_new_film.year}}
            print("Film Added")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            user_films()
    
    elif user_choice == "2":
        if films_dic:
            clear_screen()
            time.sleep(0.5)
            print("****************** Displaying all films ******************")
            for type in films_dic:
                print("---------------------------------")
                print(f"{type} => {films_dic[type]}")
            print("---------------------------------")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            user_films()
        else:
            print("We didn't have any films yet!")
            time.sleep(2)
            clear_screen()
            time.sleep(0.5)
            user_films()
        
    elif user_choice == "3":
        clear_screen()
        time.sleep(0.5)
        print("****************** Searching about film ******************")
        print("\nSearching by\n1. Film Type\n2. Film Name\n3. Film Author\n4. Film Year\n")
        search_way = input("Enter your choice (1,2,3 or 4): ")
        while search_way != "1" and search_way != "2" and search_way != "3" and search_way != "4":
            print("Sorry, invalid choice")
            search_way = input("Enter your choice (1,2,3 or 4) only: ")
        if search_way == "1":
            clear_screen()
            time.sleep(0.5)
            search_by_film_type = input("Please enter your film type: ")
            if films_dic:
                for type in films_dic:
                    if search_by_film_type == type:
                        clear_screen()
                        time.sleep(0.5)
                        print("****************** Your Search Results ******************")
                        print(f"{type} Films Information => {films_dic[type]}")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        user_films()
                else:
                    print("We didn't have this film yet!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films()
            else:
                print("We didn't have any films yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                user_films()

        elif search_way == "2":
            if films_dic:
                clear_screen()
                time.sleep(0.5)
                search_by_film_name = input("Please enter your film name: ")
                for type in films_dic:
                    for name in films_dic[type]:
                        if search_by_film_name == name:
                            clear_screen()
                            time.sleep(0.5)
                            print("****************** Your Search Results ******************")
                            print(f"{name} => Type : {type} => Information : {films_dic[type][name]}")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            user_films()
                        else:
                            print("We didn't have this film yet!")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            user_films()
            else:
                print("We didn't have any films yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                user_films()
        
        elif search_way == "3":
            if films_dic:
                clear_screen()
                time.sleep(0.5)
                search_by_film_author = input("Please enter your film author: ")
                for type in films_dic:
                    for name in films_dic[type]:
                        if search_by_film_author == films_dic[type][name]['Author']:
                            film_author_results.append(films_dic[type][name])
                        else:
                            continue

                if film_author_results:
                    for type in films_dic:
                        for name in films_dic[type]:
                            if films_dic[type][name] in film_author_results:
                                clear_screen()
                                time.sleep(0.5)
                                print("****************** Your Search Results ******************")
                                print(f"{name} Film  =>  Type : {type}  =>  Infomation : {films_dic[type][name]}")
                            else:
                                continue
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films()
                else:
                    print("We didn't have films that made by this author yet!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films()
            else:
                print("We didn't have any films yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                user_films()
        
        elif search_way == "4":
            if films_dic:
                clear_screen()
                time.sleep(0.5)
                search_by_film_year = int(input("Please enter the year that film made in it: "))
                for type in films_dic:
                    for name in films_dic[type]:
                        if str(search_by_film_year) == films_dic[type][name]['Year']:
                            film_year_results.append(films_dic[type][name])
                        else:
                            continue

                if film_year_results:
                    for type in films_dic:
                        for name in films_dic[type]:
                            if films_dic[type][name] in film_year_results:
                                clear_screen()
                                time.sleep(0.5)
                                print("****************** Your Search Results ******************")
                                print(f"{name} Film  =>  Type : {type}  =>  Infomation : {films_dic[type][name]}")
                            else:
                                continue
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films()
                else:
                    print("We didn't have films that made in this year yet!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films()
            else:
                print("We didn't have any films yet!")
                time.sleep(2)
                clear_screen()
                time.sleep(0.5)
                user_films()

    elif user_choice == "4":
        print("Thank you for using our films library application")
        print("Exiting.......")
        time.sleep(2)
        exit()







def films_application():
    
        clear_screen()
        time.sleep(0.5)
        print("****************** Welcome to the film library app! ******************\n")
        print("Choose an Action\n1. Sign up\n2. Login\n")
        user_sign = input("Enter your choice (1 or 2): ")
        while user_sign != "1" and user_sign != "2":
           print("Sorry, invalid choice")
           user_sign = input("Enter your choice (1 or 2) only: ")
        if user_sign == "1":
            clear_screen()
            time.sleep(0.5)
            create_new_user = create_user()
            is_email = re.findall(r"^[A-z0-9]+@[A-z0-9]+\.\w+$", create_new_user.email)
            while is_email == []:
                print("Invalid Email, Please try again")
                create_new_user = create_user()
                is_email = re.findall(r"^[A-z0-9]+@[A-z0-9]+\.\w+$", create_new_user.email)
            if is_email != []:
              if user_info_dic:
                for name in user_info_dic:
                    if create_new_user.name == name:
                        if create_new_user.email in user_info_dic[name]:
                            print("We had this email already, you should go to login choice")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            films_application()
                        else:
                            user_info_dic[create_new_user.name] = ({"Email" : create_new_user.email, "Password" : create_new_user.password})
                            print("User Added")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            user_films()
                    else:
                        user_info_dic.update({create_new_user.name : {"Email" : create_new_user.email, "Password" : create_new_user.password}})
                        print("User Added")
                        time.sleep(2)
                        clear_screen()
                        time.sleep(0.5)
                        user_films()
              else:
                    user_info_dic.update({create_new_user.name : {"Email" : create_new_user.email, "Password" : create_new_user.password}})
                    print("User Added")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    user_films() 


        elif user_sign == "2":
            clear_screen()
            time.sleep(0.5)
            create_new_user = create_user()
            is_email = re.findall(r"^[A-z0-9]+@[A-z0-9]+\.\w+$", create_new_user.email)
            while is_email == []:
                print("Invalid Email, Please try again")
                create_new_user = create_user()
            if is_email != []:
                if user_info_dic:
                    for name in user_info_dic:
                        if create_new_user.name == name:
                            if create_new_user.email in user_info_dic[name]:
                                print("Login......")
                                time.sleep(2)
                                clear_screen()
                                time.sleep(0.5)
                                user_films()
                            else:
                                print("We didn't have this user yet!")
                                time.sleep(2)
                                clear_screen()
                                time.sleep(0.5)
                                films_application()
                        else:
                            print("We didn't have this user yet!")
                            time.sleep(2)
                            clear_screen()
                            time.sleep(0.5)
                            films_application()
                else:
                    print("We didn't have any user info yet!")
                    time.sleep(2)
                    clear_screen()
                    time.sleep(0.5)
                    films_application()

        
    




films_application()