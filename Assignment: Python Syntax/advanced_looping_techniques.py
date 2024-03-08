#10. Advanced Looping Techniques
    #Task 1: The Selective DJ
# Selective playlist slice
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slic
for genre in selected_genres:
    print("Selective play: " + genre)

    #Task 2: The One-Liner Band with List Comprehensions
# List comprehension to append "Music" to each genre
music_genres = [genre + " Music" for genre in genres]
print(music_genres)

    #Task 3: Numerical Beats with range
# Countdown with range
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")