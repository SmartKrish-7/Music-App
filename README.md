# 🎵 Music Player

A **simple and elegant** web-based music player built with **HTML, CSS, and vanilla JavaScript**, powered by a **FastAPI backend**.  
This project allows users to **search, play, and manage** a collection of songs with a **clean, modern interface**.

---

## ✨ Features

- 🔍 **Search Functionality** – Dynamic search bar with live suggestions for songs.
- 🎛 **Playback Controls** – Play, pause, forward, and backward buttons.
- 📊 **Progress Bar** – Interactive progress bar for tracking and scrubbing.
- 📱 **Responsive Design** – Optimized for desktop and mobile devices.
- ❤️ **Favorites** – Toggle songs as favorites.
- ⚡ **FastAPI Backend** – Handles song data, file serving, and API endpoints.

---

## 🛠 Technologies Used

### **Frontend**
- **HTML5** – Structure
- **CSS3** – Dark, modern theme styling
- **JavaScript (Vanilla)** – Playback logic, API calls, UI interactions
- **Font Awesome** – Icons

### **Backend**
- **FastAPI** – High-performance API framework
- **SQLAlchemy** – ORM for database operations
- **SQLite** – Default database for song data

---

## 🚀 Getting Started

### **Prerequisites**
Make sure you have:
- **Python 3.7+**
- **pip** (Python package installer)

---

### **1️⃣ Installation**

#### **Clone the repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

## **Set up the backend**

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

## Activate the environment:

-**Windows:**
```bash
venv\Scripts\activate
```

-**Mac/Linux:**
```bash
source venv/bin/activate
```

## **Install dependencies**
```bash
pip install -r requirements.txt
```
---

### **2️⃣ Run the Backend Server**
```bash
uvicorn main:app --reload
```

The server will run at:
📍 http://127.0.0.1:8000

---

### **3️⃣ Add Your Music Files**

1. Place your .mp3 files inside the static/songs/ folder.

2. Add album art images inside static/images/.

3. Insert song info into the database.

**Example SQL:**
```sql
INSERT INTO songs (name, artist, path, image) 
VALUES ("Song Name", "Artist Name", "songs/song_file.mp3", "images/album_art.png");
```

---

### **4️⃣ Open the Music Player**

Open index.html in your browser.
The frontend will automatically connect to the backend.

---


### **📂 Project Structure**
```structure
├── main.py                # FastAPI backend
├── requirements.txt       # Python dependencies
├── index.html             # Music player UI
├── style.css              # Player styling
├── static/
│   ├── songs/             # MP3 files
│   └── images/            # Album art
└── README.md              # Project documentation
```
