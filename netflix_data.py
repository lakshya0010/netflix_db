import pandas as pd
import numpy as np

def load_data(path):
    return pd.read_csv(path)

def basic_info(df):
    print("Shape of the dataset:", df.shape)
    print("\nColumns in the dataset:", df.columns)
    print("\nBasic Info:")
    df.info()

def clean_data(df):
    df.drop_duplicates(inplace=True)
    df['date_added'] = pd.to_datetime(df["date_added"], errors = "coerce")
    df['year_added'] = df["date_added"].dt.year
    df['country'] = df['country'].fillna("Unknown")
    df['title'] = df['title'].fillna("Unknown")
    df['rating'] = df['rating'].fillna("Unknown")
    df['description'] = df['description'].fillna("Unknown")
    

def types(df):
    print("types of content are\n")
    print(df['type'].value_counts())

def top_countries(df):
    print("Top 10 countries are")
    print(df['country'].value_counts().head(10))

def content_per_year(df):
    print("content per year: ")
    print(df['year_added'].value_counts().sort_index())

def top_generes(df):
    print("top generes: ")
    print(df['listed_in'].value_counts().head(10))

def most_featured_cast(df):
    df['cast_list']= df['cast'].str.split(",")
    df_exploded = df.explode("cast_list")
    print(df_exploded['cast_list'].value_counts())

def most_common_ratings(df):
    print(df['rating'].value_counts())




net = load_data('netflix_titles.csv')
clean_data(net)
most_common_ratings(net)


