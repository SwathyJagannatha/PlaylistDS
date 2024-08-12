# Playlist Management API

## Project Overview

The Playlist Management API is a Flask-based project that allows users to manage their music playlists and songs. The API supports CRUD (Create, Read, Update, Delete) operations on both songs and playlists, along with additional functionalities like adding and removing songs from playlists, and sorting songs within a playlist based on various attributes.

## Problem Statement

Our goal is to develop a system that enables users to:
- Create and manage songs.
- Create and manage playlists.
- Add and remove songs from playlists.
- Efficiently search for songs or playlists and sort songs within playlists by attributes such as name, artist, or genre.

## Project Requirements

### Data Organization

- **Songs** and **Playlists** are managed using Python's `lists` and `dictionaries`.
- Operations are provided to create, update, delete, and search songs and playlists.

### Search and Sort Algorithms

- **Binary Search** is implemented for efficient song and playlist retrieval, ensuring a time complexity of `O(log n)` for searches.
- **Merge Sort** is utilized to sort songs within a playlist by name, artist, or genre, providing efficient sorting with a time complexity of `O(n log n)`.

### API Endpoints

The API provides the following endpoints:

#### Song Endpoints

- **Create a Song**: `POST /create_songs`
- **Update a Song**: `PUT /update_songs/<string:title>`
- **Delete a Song**: `DELETE /delete_songs/<string:title>`
- **Search/Get a Song**: `GET /search_songs?song=<string:title>`

#### Playlist Endpoints

- **Create a Playlist**: `POST /create_playlist`
- **Get a Playlist**: `GET /search_playlist?search_query=<string:name>`
- **Update a Playlist**: `PUT /update_songs_playlist/<string:updated_name>`
- **Delete a Playlist**: `DELETE /delete_songs_playlist/<string:playlist_name>/<string:song_title>`

#### Additional Endpoints

- **Add a Song to Playlist**: `POST /create_songs_playlist`
- **Remove a Song from Playlist**: `DELETE /delete_songs_playlist/<string:playlist_name>/<string:song_title>`
- **Sort Songs in Playlist**: `GET /sort_songs_playlist/<string:playlist_name>/<string:sort_attr>`

### Efficient Data Handling

- **Merge Sort** is used for sorting songs, which handles large datasets effectively.
- **Binary Search** ensures quick retrieval of songs and playlists.
- Consideration of **stacks**, **queues**, and **linked lists** for handling song insertion and deletion in playlists efficiently.

## Setup and Installation

1. **Clone the Repository**: 
    
    git clone <repository-url>
    cd playlist-management-api
  

2. **Install Dependencies**:
 
    pip install flask
  

3. **Run the Application**:
    
    python app.py

4. **Access the API**:
    - The API will be available at `http://127.0.0.1:5000`.


## Conclusion

This project demonstrates the implementation of a basic playlist management system using Flask, with a focus on efficient data management through search and sort algorithms. The system is designed to handle a large number of songs and playlists efficiently, ensuring quick and reliable access to music data.
