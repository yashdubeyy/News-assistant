import requests
import json
from dotenv import find_dotenv, load_dotenv
import streamlit as st
import os
import sqlite3

load_dotenv()

# Get the news API key from environment variables
news_api_key = os.environ.get("NEWS_API_KEY")

# Define the get_news function
def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apikey={news_api_key}&pageSize=10&language=en&sortBy=publishedAt"  # Sort by publishedAt in descending order

    try:
        response = requests.get(url)
        if response.status_code == 200:
            news_json = response.json()
            articles = news_json.get("articles", [])

            final_news = []
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description = article["description"]
                url = article["url"]
                image_url = article["urlToImage"]  # Added image URL

                title_description = f"""
                    Title: {title}
                    Author: {author}
                    Source: {source_name}
                    Description: {description}
                    URL: {url}
                """
                final_news.append((title_description, image_url))  # Appended image URL along with other details

            return final_news
        else:
            return []
    except requests.exceptions.RequestException as e:
        print("Error occurred during API request:", e)

# Create or connect to SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return conn

# Save chat history to SQLite database
def save_chat_history(conn, message):
    sql = ''' INSERT INTO chat_history(message)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (message,))
    conn.commit()
    return cur.lastrowid

# Streamlit app
def main():
    # Create or connect to SQLite database
    conn = create_connection("chat_history.db")
    if conn is not None:
        # Create chat history table if not exists
        create_table_sql = """ CREATE TABLE IF NOT EXISTS chat_history (
                                        id integer PRIMARY KEY,
                                        message text NOT NULL
                                    ); """
        with conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)

    st.title("News Summarizer Assistant")
    
    # Sidebar for chat history
    st.sidebar.title("Chat History")
    chat_history = st.sidebar.empty()
    
    topic_to_search = st.text_input("Enter a topic to search for news:")
    if st.button("Get News"):
        news_results = get_news(topic_to_search)
        if news_results:
            for news_item, image_url in news_results:
                st.write(news_item)
                if image_url:
                    st.image(image_url, caption='Image', width=200)  # Resizing image
                st.markdown("---")  # Adding a separator
                # Save news item to chat history
                if conn is not None:
                 chat_history.text(news_item)  # Updating chat history
        else:
            st.write("No news articles found for the given topic!")

if __name__ == "__main__":
    main()
