<h2>Music Player</h2>h2>
A simple and elegant web-based music player built with HTML, CSS, and vanilla JavaScript, powered by a FastAPI backend. This project allows users to search, play, and manage a collection of songs with a clean, modern interface.

Features
Search Functionality: Find songs by name using a dynamic search bar with live suggestions.

Playback Controls: Standard play, pause, forward, and backward controls.

Progress Bar: Interactive progress bar to track and scrub through the song.

Responsive Design: A clean, mobile-friendly interface.

Favorites: A simple toggle to mark songs as favorites.

FastAPI Backend: A robust backend handles song data, file serving, and a RESTful API.

Technologies Used
Frontend:

HTML5: For the player's structure.

CSS3: Custom styling for a dark, modern theme.

JavaScript (Vanilla): For all the core playback logic, API calls, and UI interactions.

Font Awesome: For icons.

Backend:

FastAPI: A high-performance Python web framework for the API.

SQLAlchemy: An Object-Relational Mapper (ORM) for database interactions.

SQLite: The default database used for storing song information.

Getting Started
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.7+

pip (Python package installer)

Installation
Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Set up the backend:
Create a Python virtual environment (optional but recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required Python packages:

Bash

pip install -r requirements.txt
Note: If you don't have a requirements.txt file, you can generate one using pip freeze > requirements.txt after installing your dependencies.

Run the backend server:
Start the FastAPI server. This will also create the songs table in the database if it doesn't exist.

Bash

uvicorn main:app --reload
The server will run on http://127.0.0.1:8000.

Add your music files:
Place your .mp3 files in a directory (e.g., a songs/ folder in the project root).
Then, you need to populate the database with song information. You can use a tool like SQL Workbench or use a simple script to insert records into the songs table. Each song entry should have a name, artist, path (the local file path), and image (the path to the album art).

Example SQL INSERT statement:

SQL

INSERT INTO songs (name, artist, path, image) VALUES ("Song Name", "Artist Name", "songs/song_file.mp3", "images/album_art.png");
Open the music player:
Open the index.html file in your web browser. The frontend will automatically connect to the running backend.

Project Structure
├── main.py                # FastAPI backend code
├── requirements.txt       # Python dependencies
├── index.html             # The music player's HTML file
├── style.css              # The CSS for styling the player
├── static/
│   ├── songs/             # Directory for music files
│   └── images/            # Directory for album art
└── README.md              # This file
API Endpoints
GET /songs/: Retrieve a list of all songs.

GET /songs/{song_name}: Search for a specific song by name.

POST /songs/: Add a new song to the database.

Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
