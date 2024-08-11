# Building a Flask API for Playlist Access and Management:
# Implement CRUD endpoints using Flask for managing playlists and songs.
# API endpoints:
# 1>Song Endpoints:
# Create Song
# Update Song
# Delete Song
# Search/Get a Song

# 2> Playlist Endpoints:
# Create Playlist
# Get Playlist
# Update Playlist
# Delete Playlist:

# 3> Additional Endpoints:
# Add song to Playlist
# Remove song from Playlist
# Sort songs in Playlist by song name, genre, and artist

from flask import Flask,request,jsonify

#www.127.0.0.1:5000/search_name?search_query=Exploring the Cosmos
app = Flask(__name__)

songs = [
    {"title": "Blinding Lights","artist": "The Weekend","genre": "Pop","album": "After Hours","release_year": 2019},
    {"title": "Bad Guy","artist": "Billie Eilish","genre": "Pop","album": "When We All Fall Asleep, Where Do We Go?","release_year": 2019},
    {"title": "Old Town Road","artist": "Lil Nas X ft. Billy Ray Cyrus","genre": "Country/Rap","album": "7","release_year": 2019},
    {"title": "Dear Friend","artist": "lean Nopes","genre": "Emotional","album": "3","release_year": 2019}
]

def search_song_title(song_list,title):
    song_sorted = sorted(song_list,key = lambda x : x['title'].lower())
    print(song_sorted)
    start = 0 
    end = len(song_sorted)-1

    while start <= end:
        mid = (start+end)//2

        if song_sorted[mid]['title'].lower() == title.lower():
            #return f"Song with title {title} is found at position {mid}"
            return mid
        elif title.lower() < song_sorted[mid]['title'].lower():
            end = mid-1
        else:
            start = mid+1

    # return f"Song with title {title} isnt found"
    return -1

#www.127.0.0.1:5000/search_songs?song=Old Town Road

@app.route('/search_songs',methods=['GET'])
def search_songs():
    song_search = request.args.get('song')
    if not song_search:
        return jsonify({"error":"Please provide song title to continue search!!"}),400
    
    song_idx = search_song_title(songs,song_search)

    if song_idx != -1:
        return jsonify({"title":song_search,"index":song_idx}),200
        #return jsonify('success'),200
    else:
        return jsonify({"message":"Song with above title isnt found"}),404

# One wayto create songs

# @app.route('/create_songs',methods=['POST'])
# def create_songs():
#     song_title = request.args.get('title')
#     song_artist = request.args.get('artist')
#     song_genre = request.args.get('genre')
#     song_album = request.args.get('album')
#     release_year = request.args.get('release')
#     if not song_title:
#         return jsonify({"error":"Please provide song title to create new song!!"}),400
    
#     song = {"title": song_title,"artist": song_artist,"genre": song_genre,"album": song_album,"release_year": release_year}
#     songs.append(song)
#     print(songs)

#     # return jsonify({'message':"Song list updated successully"}),200
#     return jsonify(song),201

# Another method

@app.route('/create_songs',methods=['POST'])
def create_songs():
    song_data = request.get_json()

    fields_mandatory = ["title","artist","genre","album","release_year"]

    if not all(field in song_data for field in fields_mandatory):
        return jsonify({"error":"Please provide all mandatory fields(title,artist,genre,album,release_year) to create new song!!"}),400
    
    song = {"title": song_data["title"],"artist": song_data["artist"],"genre": song_data["genre"],"album": song_data["album"],"release_year": song_data["release_year"]}
    songs.append(song)
    print(songs)

    # return jsonify({'message':"Song list updated successully"}),200
    return jsonify(song),201

# Update songs endpoint
@app.route('/update_songs/<string:title>',methods=['PUT'])
def update_songs(title):
    print('Title value',title)
    song_data = request.get_json()
    print(song_data)
    #print(song_data[''])
    for item in songs:
       print("Item:",item)
       if title == item['title']:
          for key,value in song_data.items(): # iterating the json content, for updating original list of dict
            if key in item and value:
                item[key] = value
          
          print(songs)
          return jsonify(songs),201
       
    return jsonify({"error":"Title of the song doesnt exist!!"}),400

# Update songs endpoint
@app.route('/delete_songs/<string:title>',methods=['DELETE'])
def delete_songs(title):
    print('Title value',title)
    song_data = request.get_json()
    print(song_data)
   
    # using remove function

    # for item in songs:
    #    print("Item:",item)
    #    if title == item['title']:
    #          songs.remove(item)
    #          return jsonify(songs),201
    #    print(songs)
    # return jsonify({"error":"Title of the song doesnt exist!!"}),400

    # using delete function

    for idx,song_item in enumerate(songs):
        if song_item["title"] == title:
            del songs[idx]
            return jsonify(songs),201
        print(songs)
    return jsonify({"error":"Title of the song doesnt exist!!"}),400 


###################### playlist and its api routes ##########################################

playlists = [
    {
        "name": "Morning Vibes",
        "description": "Uplifting tracks to start your day right",
        "creator": "DJMorning",
        "creation_date": "2024-08-10",
        "songs": [
            {"title": "Sunshine", "artist": "Katrina and The Waves", "genre": "Rock", "album": "Walking on Sunshine", "release_year": 1983},
            {"title": "Happy", "artist": "Pharrell Williams", "genre": "Pop", "album": "G I R L", "release_year": 2014},
        ]
    },
    {
        "name": "Workout Energy",
        "description": "High-energy hits to boost your workout session",
        "creator": "FitFanatic",
        "creation_date": "2024-08-11",
        "songs": [
            {"title": "Stronger", "artist": "Kanye West", "genre": "Hip-Hop", "album": "Graduation", "release_year": 2007},
            {"title": "Eye of the Tiger", "artist": "Survivor", "genre": "Rock", "album": "Eye of the Tiger", "release_year": 1982},
        ]
    },
    {
        "name": "Evening Chill",
        "description": "Relaxing tunes for a peaceful evening",
        "creator": "CalmCollector",
        "creation_date": "2024-08-12",
        "songs": [
            {"title": "Fix You", "artist": "Coldplay", "genre": "Rock", "album": "X&Y", "release_year": 2005},
            {"title": "Chasing Cars", "artist": "Snow Patrol", "genre": "Alternative Rock", "album": "Eyes Open", "release_year": 2006},
        ]
    }
]

playlist_new=[
    {
        "name": "Morning Vibes",
        "description": "Uplifting tracks to start your day right",
        "creator": "DJMorning",
        "creation_date": "2024-08-10",
        "song_title":"Eye of the Tiger"
    },
    {
        "name": "Workout Energy",
        "description": "High-energy hits to boost your workout session",
        "creator": "FitFanatic",
        "creation_date": "2024-08-11",
        "song_title": "Stronger"
    },
    {
        "name": "Evening Chill",
        "description": "Relaxing tunes for a peaceful evening",
        "creator": "CalmCollector",
        "creation_date": "2024-08-12",
        "song_title":"Fix You"
    }
]


# with song details
# Additional endpoints

# Add song to Playlist

@app.route('/create_songs_playlist',methods=['POST'])
def create_playlist_song():
    playlist_info = request.get_json()
    print("Playlist info", playlist_info)

    mandatory_fields = ["name","description","creator","creation_date","title","artist","genre"]

    if not all(fields in playlist_info for fields in mandatory_fields):
        return jsonify({"error":"Please provide all mandatory fields(name,description,creator,creation_date,and for song(title,artist,genre))"})
    
    playlist = {"name": playlist_info["name"], "description": playlist_info["description"],"creator": playlist_info["creator"],"creation_date":playlist_info["creation_date"],
                "songs" : [{"title":playlist_info["title"],"artist":playlist_info["artist"],"genre":playlist_info["genre"]}]}
    playlists.append(playlist)
    print(playlists)
    return jsonify(playlist),201

# @app.route('/update_playlist/<string:updated_name>',methods=['PUT'])
# def update_playlist(updated_name):
#     playlist_info = request.get_json()
#     print("Playlist info", playlist_info)
    
#     for playlist_each in playlists:
#         if updated_name == playlist_each["name"]:
#             print("Found matching playlist:", playlist_each["name"])

#             # Print each key-value pair in the received playlist_info
#             for key, value in playlist_info.items():
#                 if key in playlist_each and value:
#                     #playlist_each[key] = value
#                      if key == "songs":
                       
#                        all_songs = [playlist["songs"] for playlist in playlists]
#                        # Flatten the list of lists into a single list of songs
#                        flattened_songs = [song for songs in all_songs for song in songs]
#                        print("Foundsongs key")
#                        print(flattened_songs)

#                        for song in flattened_songs:
#                            print(song)
#                            for key,value in song.items():
#                                print(f"{key} - {value}")
#                      else:
#                        playlist_each[key] = value
#             # print("Updated playlist:", playlists)
#             return jsonify(playlists), 200

#     # If no matching playlist found
#     print("Playlist with the specified name does not exist.")
#     return jsonify({"error": "Playlist with that name doesn't exist!"}), 404

### needs some work here

# update playlist with information

@app.route('/update_songs_playlist/<string:updated_name>',methods=['PUT'])
def update_playlist_song(updated_name):
    playlist_info = request.get_json()
    print("Playlist info", playlist_info)
    
    for playlist_each in playlists:
        if updated_name == playlist_each["name"]:

            # Print each key-value pair in the received playlist_info
            for key, value in playlist_info.items():
                if key in playlist_each and value:
                     if key == "songs":  # if song is mentioned in the json
                       songs = playlist_info.get("songs", [])
                       # Iterating through each song in the songs list
                       for song_json in songs:
                            print("Song Details:")
                            for key, value in song_json.items():
                                  print(f"{key}: {value}")

                       all_songs = [playlist["songs"] for playlist in playlists]
                       # Flatten the list of lists into a single list of songs
                       flattened_songs = [song for songs in all_songs for song in songs]
                       print("Foundsongs key")
                       print(flattened_songs)

                       for song in flattened_songs:
                           print(song)
                           for key,value in song.items():
                               print(f"{key} - {value}")
                     
                     else:
                       playlist_each[key] = value

            print("Updated playlist:", playlists)
            return jsonify(playlists), 200

    # If no matching playlist found
    print("Playlist with the specified name does not exist.")
    return jsonify({"error": "Playlist with that name doesn't exist!"}), 404

# delete songs from playlist

@app.route('/delete_songs_playlist/<string:playlist_name>/<string:song_title>',methods=['DELETE'])
def delete_songs_playlist(playlist_name,song_title):
    print('Title value',song_title)
    print('Playlist value',playlist_name)
    playlist_data = request.get_json()
   
    for playlist_item in playlists: # get each playlist
        if playlist_name == playlist_item["name"]:
                for song in playlist_item["songs"]:
                    if song["title"] == song_title:
                        playlist_item["songs"].remove(song)
                print("Updated playlist:", playlists)
                return jsonify(playlists), 200

    # If no matching playlist found
    print("Playlist with the specified name does not exist.")
    return jsonify({"error": "Playlist with that name doesn't exist!"}), 404

#Sort songs in Playlist by song name, genre, and artist

# Sort songs endpoint
@app.route('/sort_songs_playlist/<string:playlist_name>/<string:sort_attr>',methods=['GET'])
def sort_songs_playlist(playlist_name,sort_attr):

    if not playlist_name:
        return jsonify({"message":"Playlist is not found!!"}),404
    if not sort_attr:
        return jsonify({"message":"Sort attribute is required for sorting the playlist!!"}),404
    
    for playlist_item in playlists:
        if playlist_item["name"] == playlist_name:
            playlist_found = playlist_item

    sorted_songs = merge_sort(playlist_found["songs"],sort_attr) 
    if sorted_songs:
        playlist_found["songs"] = sorted_songs 
        print(playlists)
        return jsonify(playlists),201
    
    return jsonify({"message":"Playlist was not sorted"}),404

def merge_sort(list,sort_attr):
    if len(list)>1:
        mid = len(list) // 2
        left_side = list[:mid]
        right_side = list[mid:]

        merge_sort(left_side,sort_attr)
        merge_sort(right_side,sort_attr)

        i = 0 # main
        j = 0 # left half
        k = 0 # right

        while j < len(left_side) and k < len(right_side):
            if left_side[j][sort_attr] < right_side[k][sort_attr]:
                print('Value is' , left_side[j][sort_attr])
                
                list[i] = left_side[j]
                i += 1
                j += 1
            else:
                list[i] = right_side[k]
                i += 1
                k += 1
        
        while j < len(left_side):
            list[i] = left_side[j]
            i += 1
            j += 1

        while k < len(right_side):
            list[i] = right_side[k]
            i += 1
            k += 1
        print(f'MERGED {list}')
        return list
    else:
        print('BASE CASE')
##################################################################################################################################################

# create playlist without song details , just song name

@app.route('/create_playlist',methods=['POST'])
def create_playlist_only():
    playlist_info = request.get_json()
    print("Playlist info", playlist_info)

    mandatory_fields = ["name","description","creator","creation_date","title"]

    if not all(fields in playlist_info for fields in mandatory_fields):
        return jsonify({"error":"Please provide all mandatory fields(name,description,creator,creation_date,and for song(title)"})
    
    playlist = {"name": playlist_info["name"], "description": playlist_info["description"],"creator": playlist_info["creator"],"creation_date":playlist_info["creation_date"],
                "song_title" : playlist_info["title"]}
    playlist_new.append(playlist)
    print(playlist_new)
    return jsonify(playlist_new),201

## search / get a playlist
#www.127.0.0.1:5000/search_playlist?search_query="Morning Vibes"

## search algorithm for search playlist or get playlist

@app.route('/search_playlist', methods=['GET'])
def search_playlist():
    playlist_search = request.args.get('search_query')
    
    if not playlist_search:
        return jsonify({"error":"Please provide playlist name to continue search!!"})
    
    playlist_idx = search_playlist_binary(playlist_new,playlist_search)

    if playlist_idx != -1:
        return jsonify({"title":playlist_search,"index":playlist_idx}),200
    else:
        return jsonify({"message":"Playlist with above name isnt found"}),404
    
@app.route('/delete_playlist/<string:name>', methods=['DELETE'])
def delete_playlist(name):

    playlist_info = request.get_json()
    print("Playlist initially:")
    print(playlist_new)

    for item in playlist_new:
        for key,value in item.items():
            if item["name"] == name:
              playlist_new.remove(item)
              print("Updated playlist:", playlist_new)
              return jsonify(playlist_new), 200    

    print("Playlist with the specified name does not exist.")   
    return jsonify({"message":"Playlist with above name isnt found"}),404

def search_playlist_binary(playlists_new,target_name):
    # need to sort items before applying binary search!!
    playlist_sorted = sorted(playlists_new,key = lambda x : x["name"])
    low = 0
    high = len(playlist_sorted)-1

    while low <= high:
        mid = (low+high)//2

        if target_name.lower() == playlist_sorted[mid]["name"].lower():
            return mid
        elif target_name.lower() < playlist_sorted[mid]["name"].lower():
            high = mid - 1
        else:
            low = mid + 1
    return -1

####### update playlist #########################################

@app.route('/update_playlist/<string:playlist_name>',methods=['PUT'])
def update_playlist(playlist_name):
    print(playlist_name)
    playlist_data = request.get_json()
    print(playlist_data)
    
    if not playlist_data:
        return jsonify({"error":"Please provide playlist data to perform update operation!!"})
    
    for playlist_item in playlist_new:
        if playlist_item["name"] == playlist_name:
             for key,value in playlist_data.items():
                 if key in playlist_item and value:
                     playlist_item[key]=value
             
             print(playlist_new)
             return jsonify(playlist_new),201
                 
    return jsonify({"message":"Playlist with above name isnt found"}),404
    
if __name__ == '__main__':
    app.run(debug=True)