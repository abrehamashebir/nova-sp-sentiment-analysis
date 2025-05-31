from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

def analyze_headline_sentiment(news_df, text_column='headline', new_column='Sentiment'):
    """
    Adds a sentiment score column to a DataFrame using VADER sentiment analysis.

    Parameters:
    - news_df (pd.DataFrame): The input DataFrame containing a text column.
    - text_column (str): The name of the column containing text to analyze.
    - new_column (str): The name of the column to store the sentiment scores.

    Returns:
    - pd.DataFrame: The DataFrame with an added sentiment score column.
    """
    nltk.download('vader_lexicon', quiet=True)
    sid = SentimentIntensityAnalyzer()
    news_df[new_column] = news_df[text_column].apply(lambda x: sid.polarity_scores(x)['compound'])
    return news_df
