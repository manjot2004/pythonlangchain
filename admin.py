movies=[
    { "name": "Forrest Gump", 
     "year": 1994, 
     "duration": 142,
     "genres": ["Drama", "Romance"]},
    
    
    { "name": "Avengers: Endgame",
     "year": 2019,
     "duration": 181,
     "genres": ["Action","Adventure", "Drama"] },
    
    
    { "name": "Back to the Future",
     "year": 1985,
     "duration": 114,
      "genres": ["Adventure", "Comedy", "Sci-Fi"] }
    
]


def input_int(prompt):
    while True:
        value=int(input(prompt))
        if value>=1:
            return value
        else:
            print("invalid input")
            
            
def input_something(prompt):
    while True:
        value=input(prompt).strip()
        if value:
            return value
        else:
            print("enter valid input")
        
        
print("welcome to movie manager")

while True:
    print("\nchoose [a]add, [l]list, [s]search, [v]view, [d]delete, [q]quit")
    choice=input("enter choice")
    
    if choice=="a":
        name=input_something("enter movie name:")
        year=input_int("enter release year:")
        duration=input_int("enter duration in minutes")
        generes=input_something("enetr generes").split(",")
        movie={"name":name,"year":year,"duration":duration,"genres":generes}
        movies.append(movie)
        print("movies added successfully")
        
    elif choice=="l":
        if not movies:
            print("no movies added")
        else:
             print("\nmovies list")
             for index,movie in enumerate(movies,start=1):
                print(f"{index}) {movie['name']} ({movie['year']})")
            
    elif choice=="s":
        if len(movies)==0:
            print("no movies added")
        else:
            search=input_something("enter search term").lower()
            for index,movie in enumerate(movies,start=1):
                if search in movie['name'].lower():
                    print(f"{index}) {movie['name']} ({movie['year']})")
                    
    elif choice=="v":
        if len(movies)==0:
            print("no movies added")
        else:
            index=input_int("enter index number")
            if index<0:
                print("invalid index number")
            else:
                movie=movies[index-1]
                print(f"{index}) {movie['name']} ({movie['year']}) ({movie['duration']}) ({movie['genres']})")
                
    elif choice=="d":
         if len(movies)==0:
            print("no movies added")
         else:
             indexx=input_int("enter the index number")
             if index<0:
                print("invalid index number")
             else:
                 delete=movies.pop(indexx-1)
                 print(f"{delete['name']} deleted successfully")
                 
    elif choice=="q":
        print("goodbye")
        break
    
    else:
        print("invalid choice")             
            
                
        
    