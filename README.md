# Spotify Music Discovery 🎵

Discover **music genres**, **listening patterns**, and **playlist suggestions** using Spotify audio features.

This interactive web app uses machine learning clustering to group songs based on their audio characteristics like danceability, energy, tempo, loudness, and mood (valence). Simply enter your song’s features and discover similar music patterns instantly.

---

## Live App 🚀

Try it here:  
**https://spotify-music-discovery.streamlit.app**

---

## What You Can Do

- Enter your song's **audio characteristics**
- Discover its **listening pattern**
- Explore **top genres** with similar sound profiles
- Get **playlist suggestions** from similar songs
- Understand typical **music mood and energy patterns**

---

## Features

### Input Audio Features
- **Danceability** → How suitable a track is for dancing
- **Energy** → Intensity and activity level
- **Valence** → Musical positivity or mood
- **Tempo** → Speed of the song (BPM)
- **Loudness** → Overall volume level

### Discover Insights
- Listening pattern classification
- Top genres in similar songs
- Typical audio characteristics of similar tracks
- Suggested songs from similar listening patterns

---

## How To Use

1. Open the live app  
2. Enter audio feature values using the sidebar  
3. View:
   - Listening pattern
   - Genre insights
   - Playlist suggestions

### Example

A song with high energy and high valence may match an **Energetic & Happy** listening pattern with genres like Pop or Dance along with similar recommended tracks.

---

## Real World Use Cases

- Music discovery
- Playlist generation
- Mood-based song exploration
- Audio pattern analysis
- Recommendation system prototype

---

## Tech Stack

- Python
- Scikit-learn (KMeans clustering)
- Streamlit
- Pandas
- NumPy
- Kaggle Spotify Dataset
  (https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
