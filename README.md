# Social Sentiment Analysis

A machine learning project and interactive dashboard for analyzing and visualizing sentiment in airline tweets. Built with Streamlit, this app allows users to predict tweet sentiment, explore data visualizations, and understand public opinion about airlines.

## Features
- **Sentiment Prediction**: Instantly predict the sentiment (positive, negative, neutral) of any tweet using a trained ML model.
- **Interactive Visualizations**: Explore sentiment distributions, word clouds, and feature correlations.
- **Data Exploration**: Browse and analyze real-world airline tweet data.
- **User-Friendly Interface**: Simple, modern UI powered by Streamlit.

## Project Structure
```
├── app/           # Streamlit app source code
│   └── app.py
├── data/          # Raw and processed datasets
│   ├── Tweets.csv
│   ├── Tweets_clean.csv
│   └── sentiment_tweets.csv
├── models/        # Trained ML model and vectorizers
│   ├── sentiment_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── vectorizer.pkl
├── notebooks/     # Jupyter notebooks for each project stage
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_sentiment_analysis.ipynb
│   ├── 04_eda_visualization.ipynb
│   └── 05_model_training.ipynb
├── scripts/       # Optional data preparation helpers
│   └── prepare_tweetclaw_export.py
├── examples/      # Small sample exports for helper validation
│   └── tweetclaw_export.jsonl
├── requirements.txt
├── README.md
└── reports/       # (Optional) Generated reports
```

## Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/pranavv1210/Social-Sentiment-Analysis.git
   cd Social-Sentiment-Analysis
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Streamlit app**
   ```sh
   streamlit run app/app.py
   ```
2. **Interact**: Open the provided local URL in your browser to use the dashboard.

## Prepare TweetClaw Exports
Use `scripts/prepare_tweetclaw_export.py` to convert [TweetClaw](https://github.com/Xquik-dev/tweetclaw) JSON, JSONL, or CSV exports into a CSV that matches this dashboard's tweet columns.

```sh
python scripts/prepare_tweetclaw_export.py examples/tweetclaw_export.jsonl --output data/tweetclaw_tweets.csv
```

The helper writes `airline_sentiment`, `airline`, `text`, `tweet_created`, and `clean_text` columns, plus source metadata for review. Exported TweetClaw rows default to `unlabeled` sentiment so they stay separate from the training labels.

## Data
- **Tweets.csv**: Raw tweets with sentiment labels and metadata.
- **Tweets_clean.csv**: Cleaned version of the tweets for modeling.
- **sentiment_tweets.csv**: Final dataset with all features used for training and analysis.

## Model
- Trained using scikit-learn and NLP techniques (TF-IDF, etc.).
- Model and vectorizers are saved in the `models/` directory as `.pkl` files.

## Notebooks
- `01_data_collection.ipynb`: Scraping and collecting tweet data.
- `02_data_cleaning.ipynb`: Data cleaning and preprocessing.
- `03_sentiment_analysis.ipynb`: Sentiment analysis and feature engineering.
- `04_eda_visualization.ipynb`: Exploratory data analysis and visualizations.
- `05_model_training.ipynb`: Model training, evaluation, and export.

## Requirements
See `requirements.txt` for all dependencies, including:
- pandas, scikit-learn, nltk, transformers, torch, matplotlib, seaborn, wordcloud, streamlit, plotly, joblib, snscrape

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.

## Credits
- Developed by [pranavv1210](https://github.com/pranavv1210)
- Data: [Kaggle Airline Sentiment Dataset](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)

---

*Feel free to add screenshots or a demo GIF below to showcase the app!*
