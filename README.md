# News Aggregator

News Aggregator is a web application built with FastAPI that fetches and aggregates news articles from various sources using the NewsAPI. The application provides a RESTful API to search for news articles based on user queries.

## Features

- Fetches and aggregates news articles from multiple sources
- Provides a RESTful API to search for news articles
- Dockerized for easy deployment

## Requirements

- Python 3.11+
- FastAPI
- Uvicorn
- HTTPX
- Docker (for containerization)

## Installation

1. **Clone the repository:**

```sh
git clone https://github.com/al4an2/news_aggregator.git
cd news_aggregator

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root directory and add your NewsAPI key:

    ```env
    NEWS_API_KEY=your_newsapi_key
    ```

## Usage

1. **Run the application:**

    ```sh
    uvicorn app.main:app --reload
    ```

2. **Access the API documentation:**

    Visit `http://127.0.0.1:8000/docs` to view and interact with the API documentation provided by Swagger UI.

## Endpoints

- **GET /news**

  Fetch news articles based on a query.

  **Parameters:**
  - `query` (str): The search query for fetching news articles.

  **Response:**
  - `total_results` (int): The total number of results found.
  - `articles` (List[Article]): A list of articles containing the title, description, URL, and source.

  Example:

    ```sh
    curl "http://127.0.0.1:8000/news?query=python"
    ```
    
## Docker Deployment

1. **Build the Docker image:**

    ```sh
    docker build -t news-aggregator .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -d -p 8000:8000 --name news-aggregator-container --env-file .env news-aggregator
    ```

3. **Access the API:**

    Visit `http://127.0.0.1:8000/docs` to view the API documentation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
