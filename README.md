# GNews Flask Application

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Docker](#docker)
5. [Installation](#installation)
6. [Usage](#usage)
7. [How It Works](#how-it-works)
8. [API Information](#api-information)


## Project Overview
GNews Flask Application is a simple web application built using Flask that allows users to search for news articles based on their queries. It utilizes the GNews API to fetch the latest articles and presents them in a user-friendly format. The application demonstrates how to create a web interface for searching news and displaying results effectively.

## Features
- **Search Functionality**: Users can enter keywords to search for relevant news articles.
- **User-Friendly Interface**: A clean and modern interface built using HTML, CSS, and Flask.
- **Dynamic Results**: Fetches and displays news articles in real-time based on user queries.
- **Responsive Design**: Works seamlessly across different devices and screen sizes.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework for Python.
- **HTML/CSS**: For structuring and styling the web pages.
- **GNews API**: Provides access to a variety of news articles.
- **Docker**: For containerization of the application.
## Docker

I have pushed the application to Docker Hub. You can pull the Docker image using the following command:

docker push sannapavithra/flask-news-app

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/gnews-flask-app.git
   cd gnews-flask-app
   
## Usage
- Open the Application: Launch your web browser and go to http://127.0.0.1:5000.

- Search for News: Enter your search term in the input field and click the "Search" button. The application will display a list of relevant news articles.

- View Results: Click on any article title to read the full article. The results will show the title, description, and publication date.

## How It Works
The application is structured around the Flask framework. When a user submits a search query, the application makes a request to the GNews API to fetch the relevant articles. 
The API returns the articles in JSON format, which are then parsed and displayed on the results page. The application uses HTML templates to render the content dynamically.

## API Information
This application interacts with the GNews API to fetch news articles. 
You need to sign up at GNews.io to obtain your API key. Replace the placeholder in the .env file with your actual API key.
