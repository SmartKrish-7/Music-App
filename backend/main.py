from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with ["http://127.0.0.1:5500"] for stricter rules
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MySQL connection
DATABASE_URL = "mysql+pymysql://root:India%4011@localhost/musicapp"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# DB Model
class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    path = Column(String(255), nullable=False)

Base.metadata.create_all(bind=engine)

# Pydantic schema
class SongCreate(BaseModel):
    name: str
    path: str

class SongOut(BaseModel):
    id: int
    name: str
    path: str

    class Config:
        orm_mode = True

# Routes
@app.get("/songs/", response_model=List[SongOut])
def get_all_songs():
    db = SessionLocal()
    songs = db.query(Song).all()
    db.close()
    return songs

@app.post("/songs/", response_model=SongOut)
def add_song(song: SongCreate):
    db = SessionLocal()
    new_song = Song(name=song.name, path=song.path)
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    db.close()
    return new_song

@app.get("/songs/{song_id}", response_model=SongOut)
def get_song(song_name: str):
    db = SessionLocal()
    song = db.query(Song).filter(Song.name.ilike(f"%{song_name}%")).first()
    db.close()
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song
