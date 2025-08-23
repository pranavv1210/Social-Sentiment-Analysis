import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

# =============================
# CONFIG (must be first Streamlit call)
# =============================
st.set_page_config(page_title="Airline Tweet Sentiment Dashboard", page_icon="✈️", layout="wide")

# =============================
# LOAD MODEL & DATA
# =============================
model = joblib.load("models/sentiment_model.pkl")

df = pd.read_csv("data/Tweets_clean.csv")

# =============================
# SIDEBAR
# =============================
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🔮 Predictions", "📊 Data Visuals"])

# =============================
# PAGE 1: PREDICTIONS
# =============================
if page == "🔮 Predictions":
    st.title("🔎 Tweet Sentiment Analyzer")

    user_input = st.text_area("✍️ Enter a Tweet to Analyze Sentiment", placeholder="Type a tweet here...")

    if st.button("Analyze"):
        if user_input.strip() != "":
            prediction = model.predict([user_input])[0]
            st.subheader("✅ Predicted Sentiment:")
            if prediction == "positive":
                st.success(f"🙂 Positive")
            elif prediction == "negative":
                st.error(f"😡 Negative")
            else:
                st.info(f"😐 Neutral")

# =============================
# PAGE 2: DATA VISUALS
# =============================
elif page == "📊 Data Visuals":
    st.title("📊 Sentiment Data Visualizations")

    # Sentiment Distribution
    st.subheader("🔹 Sentiment Distribution")
    fig, ax = plt.subplots()
    df["airline_sentiment"].value_counts().plot(kind="bar", ax=ax, color=["green", "red", "gray"])
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # Word Clouds
    st.subheader("🔹 Word Clouds by Sentiment")
    sentiments = df["airline_sentiment"].unique()
    for s in sentiments:
        text = " ".join(df[df["airline_sentiment"] == s]["text"].astype(str))
        wc = WordCloud(width=600, height=400, background_color="white").generate(text)
        fig, ax = plt.subplots()
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        st.write(f"**{s.capitalize()} Tweets Word Cloud**")
        st.pyplot(fig)

    # Correlation Heatmap (Optional)
    st.subheader("🔹 Feature Correlation Heatmap (TF-IDF)")
    try:
        vectorizer = model.named_steps['tfidf']
        X = vectorizer.transform(df["text"].astype(str))
        corr = pd.DataFrame(X.toarray()).corr()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(corr, ax=ax, cmap="coolwarm")
        st.pyplot(fig)
    except Exception as e:
        st.warning("Heatmap skipped due to memory constraints.")
