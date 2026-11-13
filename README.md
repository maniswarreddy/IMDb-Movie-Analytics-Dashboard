
# 🎬 IMDb Movie Analytics Dashboard

## 📌 Introduction
The IMDb Movie Analytics Dashboard is a web-based application developed using Python and Streamlit. It helps users explore and analyze the Top 250 IMDb Movies dataset through interactive charts, metrics, and filters.

## 🎯 Objectives
- Analyze IMDb movie data.
- Display movie ratings and votes.
- Explore different movie genres.
- Identify top 10 movies based on worldwide gross.
- Search and filter movies interactively.

## 🚀 Features

### 1. Dataset Loading and Preparation
- Load CSV dataset using Pandas.
- Display first 10 records.
- Display total rows and columns.
- Display column names and data types.
- Check missing values.

### 2. KPI Metrics
- Total Number of Movies.
- Average IMDb Rating.
- Highest IMDb Rating.
- Total Number of Votes.

### 3. Data Visualization
- Bar Chart – Movies by Genre.
- Histogram – IMDb Rating Distribution.
- Scatter Plot – IMDb Rating vs Number of Votes.
- Bar Chart – Top 10 Movies by Worldwide Gross.

### 4. Interactive Movie Explorer
- Selectbox for movie genres.
- Multiselect for countries.
- Slider for IMDb ratings.
- Number input for minimum votes.
- Text input for movie title search.
- Radio buttons for sorting.
- Display filtered movie records.
- Reset filters button.

### 5. Session State and Form Handling
- Maintain selected movie using Session State.
- Movie search form.
- Select preferred genre.
- Set minimum IMDb rating.
- Display selected movie details.
- Show success and information messages.

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- Plotly

## 📂 Project Structure

IMDb-Movie-Analytics-Dashboard/
│
├── app.py
├── movies.csv
├── requirements.txt
└── README.md

## ⚙️ Installation

### Step 1: Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

### Step 2: Install Required Libraries

pip install -r requirements.txt

### Step 3: Run the Application

streamlit run app.py

## 📊 Dataset Information

Dataset Name: Top 250 Movies on IMDb in 2026

Dataset Format: CSV

The dataset contains movie details such as title, genre, country, IMDb rating, number of votes, and worldwide gross collection.

## 👨‍💻 Project Details

Project Title: IMDb Movie Analytics Dashboard

Developed Using: Python and Streamlit

## 📝 Conclusion

This project provides an interactive platform to explore IMDb movie information. It uses data analysis and visualization techniques to present useful insights about movies, ratings, genres, votes, and worldwide gross collections.
