# app.py
import streamlit as st
import random
from recommend import df, recommend_songs

# ────────────────────────────────────────────────────────────────────────────────
# 🎛 Page config
st.set_page_config(
    page_title="LyricMind - Music Recommender 🎵",
    page_icon="🎧",
    layout="centered"
)

# ────────────────────────────────────────────────────────────────────────────────
# 🧠 Project Introduction
st.markdown("""
# 🎼 **LyricMind**
### *Lyrics-based Music Recommendation System*

Discover songs that *sound like your vibe* — not based on genre or popularity, but **pure lyrical similarity**.

This tool uses **Natural Language Processing (NLP)**, **TF-IDF**, and **Cosine Similarity** to find songs with similar meaning and content.

---
""")

# ────────────────────────────────────────────────────────────────────────────────
# 🔍 Song selector
song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox("🎵 Select a song:", song_list)

# 🎯 Recommend button
if st.button("🚀 Recommend Similar Songs"):
    with st.spinner("Finding similar songs..."):
        recommendations = recommend_songs(selected_song)
        if recommendations is None:
            st.warning("Sorry, song not found.")
        else:
            st.success("Top similar songs:")
            st.table(recommendations)

# 🎲 Random surprise button
if st.button("🎲 Surprise Me! Recommend from a random song"):
    random_song = random.choice(song_list)
    st.info(f"Randomly selected: **{random_song}**")
    recommendations = recommend_songs(random_song)
    if recommendations is not None:
        st.success("Top similar songs:")
        st.table(recommendations)

# ────────────────────────────────────────────────────────────────────────────────
# 👤 Footer
st.markdown("""
---
👨‍💻 *Project by* **Aswin Roshan Rajendran**  
🎓 Master’s in Data Science & Analytics, EPITA Paris, France  
📅 *July 2025*  
🔗 [GitHub](https://github.com/aswinroshanrajendran) | [LinkedIn](https://www.linkedin.com/in/aswinroshan-rajendran/)
""")
