
import streamlit as st
import pandas as pd

# Page title
st.title("IMDb Movie Analytics Dashboard")

# Load dataset
df = pd.read_csv("ToP 250 movies on imdb in 2026.csv")

# Display first 10 records
st.header("Dataset Preview")
st.dataframe(df.head(10))

# Dataset information
st.header("Dataset Information")

st.write("Total Rows:", df.shape[0])
st.write("Total Columns:", df.shape[1])

st.write("Column Names:")
st.write(df.columns.tolist())

st.write("Data Types:")
st.write(df.dtypes)

# Missing values
st.header("Missing Values")
st.write(df.isnull().sum())

# Success message
st.success("Dataset loaded successfully!")

# Question 2: Dashboard KPI Metrics

st.divider()

st.header("Movie Analytics Dashboard")

# Calculate metrics
total_movies = len(df)
average_rating = df["averageRating"].mean()
highest_rating = df["averageRating"].max()
total_votes = df["numVotes"].sum()

# Display metrics in 4 columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Movies", total_movies)

with col2:
    st.metric("Average IMDb Rating", round(average_rating, 2))

with col3:
    st.metric("Highest Rating", highest_rating)

with col4:
    st.metric("Total Votes", f"{total_votes:,}")


# Question 3 and 4: Charts with Tabs

st.divider()
st.header("Movie Data Analysis")

tab1, tab2, tab3 = st.tabs([
    "Genre Analysis",
    "Rating Analysis",
    "Gross Collection"
])

# Tab 1: Genre Analysis
with tab1:
    st.subheader("Movies by Genre")

    genre_data = df["genres"].dropna().str.split(",").explode()
    genre_count = genre_data.value_counts()

    st.bar_chart(genre_count)

# Tab 2: Rating Analysis
with tab2:
    st.subheader("IMDb Rating Distribution")

    st.bar_chart(
        df["averageRating"].value_counts().sort_index()
    )

    st.subheader("Rating vs Number of Votes")

    st.scatter_chart(
        df,
        x="averageRating",
        y="numVotes"
    )

# Tab 3: Gross Collection
with tab3:
    st.subheader("Top 10 Movies by Worldwide Gross")

    top_movies = df.sort_values(
        by="grossWorldwide",
        ascending=False
    ).head(10)

    st.bar_chart(
        top_movies,
        x="primaryTitle",
        y="grossWorldwide"
    )

# Dataset Information Expander
with st.expander("Dataset Information"):
    st.write("Total Records:", df.shape[0])
    st.write("Total Columns:", df.shape[1])
    st.write("Available Columns:", df.columns.tolist())

st.success("Movie dashboard loaded successfully!")

# Question 5: Interactive Movie Explorer

st.divider()
st.header("Interactive Movie Explorer")

# Get genre options
import ast

def clean_values(value):
    try:
        result = ast.literal_eval(str(value))
        if isinstance(result, list):
            return [str(x).strip() for x in result]
    except:
        pass

    return [x.strip(" []'\"") for x in str(value).split(",")]

genre_list = sorted(set(
    item
    for value in df["genres"].dropna()
    for item in clean_values(value)
))

# Get country options
country_col = "countriesOfOrigin"

country_list = sorted(set(
    item
    for value in df[country_col].dropna()
    for item in clean_values(value)
)) if country_col in df.columns else []

# Reset button
if st.button("Reset Filters"):
    for key in ["genre", "countries", "rating", "votes", "title", "sorting"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# Filters
col1, col2 = st.columns(2)

with col1:
    selected_genre = st.selectbox(
        "Select Genre",
        ["All"] + genre_list,
        key="genre"
    )

    selected_countries = st.multiselect(
        "Select Countries",
        country_list,
        key="countries"
    )

    rating = st.slider(
        "IMDb Rating",
        0.0, 10.0, (0.0, 10.0),
        key="rating"
    )

with col2:
    votes = st.number_input(
        "Minimum Votes",
        min_value=0,
        value=0,
        key="votes"
    )

    title = st.text_input(
        "Search Movie Title",
        key="title"
    )

    sorting = st.radio(
        "Sort Order",
        ["Ascending", "Descending"],
        key="sorting"
    )

# Apply filters
filtered_df = df.copy()

if selected_genre != "All":
    filtered_df = filtered_df[
        filtered_df["genres"].apply(
            lambda x: selected_genre in clean_values(x)
        )
    ]

if selected_countries and country_col in df.columns:
    filtered_df = filtered_df[
        filtered_df[country_col].apply(
            lambda x: any(
                c in clean_values(x)
                for c in selected_countries
            )
        )
    ]

filtered_df = filtered_df[
    (filtered_df["averageRating"] >= rating[0]) &
    (filtered_df["averageRating"] <= rating[1])
]

filtered_df = filtered_df[
    filtered_df["numVotes"] >= votes
]

if title:
    filtered_df = filtered_df[
        filtered_df["primaryTitle"].str.contains(
            title, case=False, na=False
        )
    ]

# Sorting
filtered_df = filtered_df.sort_values(
    by="averageRating",
    ascending=(sorting == "Ascending")
)

# Display results
st.subheader("Filtered Movies")

st.write("Total Movies Found:", len(filtered_df))

st.dataframe(filtered_df, use_container_width=True)

# Question 6: Session State and Form Handling

st.divider()
st.header("Movie Search (Session State)")

# Initialize session state
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# Create search form
with st.form("movie_search_form"):

    movie_title = st.text_input("Enter Movie Title")

    preferred_genre = st.selectbox(
        "Preferred Genre",
        ["All"] + genre_list
    )

    minimum_rating = st.slider(
        "Minimum IMDb Rating",
        0.0, 10.0, 7.0
    )

    submitted = st.form_submit_button("Search Movie")

# Process form after submission
if submitted:

    search_df = df.copy()

    if movie_title:
        search_df = search_df[
            search_df["primaryTitle"].str.contains(
                movie_title, case=False, na=False
            )
        ]

    if preferred_genre != "All":
        search_df = search_df[
            search_df["genres"].apply(
                lambda x: preferred_genre in clean_values(x)
            )
        ]

    search_df = search_df[
        search_df["averageRating"] >= minimum_rating
    ]

    if len(search_df) > 0:
        st.session_state.selected_movie = search_df.iloc[0].to_dict()
        st.success("Movie found successfully!")
    else:
        st.session_state.selected_movie = None
        st.info("No matching movie found.")

# Display selected movie
if st.session_state.selected_movie is not None:

    movie = st.session_state.selected_movie

    st.subheader("Selected Movie Details")

    st.write("Movie Title:", movie["primaryTitle"])
    st.write("Genre:", movie["genres"])
    st.write("IMDb Rating:", movie["averageRating"])
    st.write("Number of Votes:", movie["numVotes"])
