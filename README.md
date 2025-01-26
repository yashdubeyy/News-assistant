News Summarizer Assistant
A Streamlit-based web application that fetches and summarizes the latest news articles using the NewsAPI. This application allows users to search for news by topic, displays articles with images, and saves chat history to an SQLite database.

📝 Features
Search News by Topic: Fetches the latest news articles using NewsAPI.

Image Support: Displays article images when available.

Chat History: Saves and displays search history using SQLite.

Streamlit Integration: Clean and interactive UI for user interaction.

🚀 Getting Started
Prerequisites
Before running the project, ensure the following dependencies are installed:

Python 3.7 or later
pip
A valid NewsAPI key

🔧 Installation Steps
Clone the Repository:


git clone https://github.com/your-repo/news-summarizer-assistant.git
cd news-summarizer-assistant
Install Dependencies:


pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the project root directory.

Add your NewsAPI key:


NEWS_API_KEY=your_news_api_key_here
Run the Application:


streamlit run file1.py
📂 Project Structure
.
├── file1.py          # Main Python file containing the app code
├── requirements.txt  # Requirements file for dependencies
├── chat_history.db   # SQLite database for storing chat history (created at runtime)
├── .env              # Environment variables file (not included in version control)

📦 Dependencies
The project uses the following Python libraries:

python-dotenv: Manage environment variables.

openai (placeholder, not currently used in the code).

requests: For making API calls.

streamlit: Framework for creating web apps.


🏗️ How It Works
Users enter a topic to search for news articles.

The app fetches news articles from the NewsAPI based on the topic.

Articles are displayed with:

Title, author, and source details.

Description and a link to the full article.

Images (if available).

Chat history (search queries) is saved in a local SQLite database and displayed in the sidebar.


✨ Future Improvements
Authentication: Add user login and authentication for personalized chat history.

Advanced Search: Enable filters for news categories, date ranges, and regions.

AI Integration: Summarize articles using OpenAI's GPT model.

Deployment: Deploy the app to a cloud platform like Heroku or AWS.


📚 Resources
NewsAPI Documentation

Streamlit Documentation

📄 License
This project is licensed under the MIT License.
