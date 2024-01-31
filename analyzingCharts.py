# Billboard Top 100 Songs Chart
# April Nguyen
# October 10 2022
#
# Analyze a data file containing Billboard weekly ranked top 100 songs

print("Welcome to the Billboard top 100 app!")
print("\n")
print("PART 1")
print("======")

COLSONG = 2
COLRANK = 1
COLART = 3
COLRANKLW = 4
COLWEEKS = 6

# Initialize
tally_love = 0
tally_1or2 = 0
list_1or2 = []
list_artist_a = []
rank_adv = 0
weeks_sum = 0
songs_total = 0

# Open the file
file = open("charts.csv")

# Disregard the first line (titles)
file.readline()

# for loop
for line in file:
    l_list = line.split(",")
    song_name = l_list[COLSONG]
    song_name_cleaned = l_list[COLSONG].lower().split()
    rank = int(l_list[COLRANK])
    rank_lw = int(l_list[COLRANKLW])
    artist = l_list[COLART]
    first_char = artist[0]
# Count number of songs including the word "love" in the title (upper or lower case)
    if "love" in song_name_cleaned:
        tally_love += 1
# Count the songs names which were in rank 1 or 2 
    if rank == 1 or rank == 2:
        tally_1or2 += 1
        list_1or2.append(song_name)
# Count the artist's names whose names start in 'A'
    if first_char == "A":
        list_artist_a.append(artist)
# Count the number of songs which advanced in the ranks with respect to the previous week
# (Their current rank is greater than their last-week rank)
    if rank < rank_lw:
        rank_adv += 1
# Total weeks-on-board of every song
    weeks = int(l_list[COLWEEKS])
    weeks_sum += weeks
    songs_total += 1

# Print the statements
print("\n")
print("Number songs containg the word 'love':",tally_love)
print("\n")
print("Songs names in rank positions 1 or 2:",tally_1or2)
for song in list_1or2:
    print(song)
print("\n")
print("Artists names starting with 'A':")
for artist in list_artist_a:
    print(artist)
print("\n")
print("Songs advancing in rank wrt previous week:",rank_adv)

# Calculate the average of weeks-on-board (of all songs in the provided file)
avg_wob = weeks_sum/songs_total
avg_rounded = "Average weeks on board all songs: {:.2f}".format(avg_wob)
print("\n")
print(avg_rounded)

print("\n")
print("PART 2")
print("======")
print("First query: Individual artist songs")

# take input and turn all lowercase, remove leading and trailing spaces
# remove punctuation marks including .,?!
def clean(x):
    return x.lower().strip(" .,?!")

# Ask user to enter an artist name
artist_name = clean(input("Artist name (may be part of the name) --> "))

# Read from top of file
file.seek(0)

#Skip first line - headesrs
file.readline()

# Initialize 
COLDATE = 0
artist_found = 0
song_found = 0
wob = 0

# Print headers
print("{:25}""{:25}""{:12}""{:7}""{:15}".format("Artist","Song","Date","Rank","Previous rank"))

# For every line artist is in the file, print the song information
for line in file:
    l_list = line.split(",")
    artist = l_list[COLART].lower()
    if artist_name in artist:
        a = l_list[COLART]
        s = l_list[COLSONG]
        d = l_list[COLDATE]
        r = l_list[COLRANK]
        p = l_list[COLRANKLW]
        print("{:25}""{:25}""{:12}""{:>4}""{:>16}".format(a,s,d,r,p))
        artist_found += 1

# If artist is not in the file, print there is no such artist in the file

if artist_found == 0:
    print("\n")
    print("There is no such artist in the file")

print("\n")
print("Second query: Songs and weeks on board")

# Ask user to enter song title
song_title = clean(input("Song title (may be part of the title) --> "))

# Read from top of file
file.seek(0)

#Skip first line - headesrs
file.readline()

# Print headers
print("\n")
print("{:25}""{:12}""{:25}".format("Requested Song","Date","Weeks on board"))

# Once a song with song title is found, print song, date, weeks on board
# Only print the first song encountered
# Assume that the user types an existing song
# Assume that there exists at least one song with more weeks on board
for line in file:
    l_list = line.split(",")
    song = l_list[COLSONG].lower()
    if song_title in song:
        s = l_list[COLSONG]
        d = l_list[COLDATE]
        w = l_list[COLWEEKS]
        print("{:25}""{:24}""{:20}".format(s,d,w))
        wob = int(l_list[COLWEEKS])
        break
    
# Read from top of file
file.seek(0)

#Skip first line - headesrs
file.readline()

# Print all the songs (from the beginning of the file)
# Which were on board more weeks than the requested song
# Include song title, date, and the difference in number of weeks
# on the board between each song and the requested song

print("\n")
print("Songs with more weeks on board than the requested song")
print("\n")
print("{:25}""{:12}""{:25}".format("Song","Date","Extra weeks on board"))

for line  in file:
    l_list = line.split(",")
    if int(l_list[COLWEEKS]) > wob:
        s = l_list[COLSONG]
        d = l_list[COLDATE]
        e = int(l_list[COLWEEKS]) - wob
        print("{:25}""{:12}""{:20}".format(s,d,e))

# End of program
print("\n")
print("Bye! End of app!")    
