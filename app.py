import streamlit as st
import pandas as pd
import pickle
import numpy as np

# --- Load model artifacts ---
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

cluster_data = pd.read_csv('spotify_sample.csv')  # has cluster, genre, danceability, energy, valence, loudness, track_name, artist_name, popularity

st.title("🎵 Spotify Music Genre & Listening Pattern Discovery")
st.write("""
Discover music genres, listening patterns, and playlist suggestions based on your song's audio features!
""")

# --- User Inputs ---
st.sidebar.header("Enter Audio Features of Your Song")
danceability = st.sidebar.slider("Danceability (0 to 1)", 0.0, 1.0, 0.5)
energy = st.sidebar.slider("Energy (0 to 1)", 0.0, 1.0, 0.5)
valence = st.sidebar.slider("Valence (0 to 1, mood/happiness)", 0.0, 1.0, 0.5)
tempo = st.sidebar.number_input("Tempo (BPM)", min_value=50, max_value=200, value=120)
loudness = st.sidebar.number_input("Loudness (dB, usually negative)", min_value=-60.0, max_value=0.0, value=-10.0)

# --- Predict cluster ---
user_features = np.array([[danceability, energy, tempo, loudness, valence]])
user_features_scaled = scaler.transform(user_features)
cluster_label = kmeans.predict(user_features_scaled)[0]

# --- Get cluster data ---
cluster_info = cluster_data[cluster_data['cluster'] == cluster_label]

# --- Generate descriptive cluster name ---
avg_valence = cluster_info['valence'].mean()
avg_energy = cluster_info['energy'].mean()
avg_danceability = cluster_info['danceability'].mean()

name = ""
if avg_energy > 0.6:
    name += "Energetic "
else:
    name += "Calm "

if avg_valence > 0.6:
    name += "& Happy"
elif avg_valence < 0.4:
    name += "& Sad"
else:
    name += "& Neutral"

# --- Display results ---
st.subheader(f"🎯 Your Song Fits the Listening Pattern: {name}")

# --- Genres in this cluster ---
st.write("### Top Genres in this Listening Pattern:")
top_genres = cluster_info['genre'].value_counts().head(5)
st.write(top_genres)

# --- Average Audio Features as Listening Pattern ---
st.write("### Typical Listening Pattern of This Cluster:")
pattern_df = cluster_info[['danceability','energy','valence','loudness','tempo']].mean().reset_index()
pattern_df.columns = ["Audio Feature","Average Value"]
pattern_df.index = [
    "How suitable for dancing",
    "Intensity level",
    "Positivity/Mood",
    "Volume level",
    "Speed BPM"
]
st.dataframe(pattern_df)

# --- Playlist suggestions ---
st.write("### 🎧 Playlist Suggestions from This Cluster:")
top_songs = cluster_info.sort_values('popularity', ascending=False).head(5)
for idx, row in top_songs.iterrows():

    st.write(f"**{row['track_name']}** by *{row['artist_name']}*")

st.write("### Listening Pattern Insight")

if avg_energy > 0.65:
    st.write("⚡ Songs here are typically high-energy and suitable for workouts or parties.")
if avg_valence > 0.6:
    st.write("😊 Songs here generally have a positive and happy mood.")
if avg_danceability > 0.65:
    st.write("💃 Songs here are very danceable.")





