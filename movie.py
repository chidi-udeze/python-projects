"""
1. input: Movie name (string)
    Output: 
        1. When movie is present - "we are showing(movie name, time of showing)"
        2. When movie is not present =  "movie is not present at this time"
2. Highlight / Corner case / constraints: "user input!= present - "movie is not present at this time"
3. TC: Test cases
    1. When the movies is present
    2. When movie is not present
    3. When movie is present but the user types in a different Case
"""

movies = {"grinch": "11.00 am",
          "bruce lee": "01.00 am", "pirates": "04.00 pm", "blacklisted": "06.00 pm"}
print("Movie Name\t|\tTimings")
print('-'*30)
for key, value in movies.items():
    print(f"{key.title()}\t\t|{value}")
print('-'*30)
user_choice = input("which movie will you like to see?\n").lower()
print(user_choice)
if user_choice in movies:
    print(f"we are showing {user_choice}, at {movies[user_choice]}")
else:
    print(f"{user_choice} not present at this time")
