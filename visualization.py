import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- DATA LOADING --------------------
def load_and_clean(path):
    df = pd.read_csv(path)
    df.drop_duplicates(inplace=True)

    # Date processing
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year

    # Fill NaN
    fill_cols = ['country', 'title', 'rating', 'description', 'cast', 'listed_in']
    for col in fill_cols:
        df[col] = df[col].fillna("Unknown")

    return df

# -------------------- VISUALIZATIONS --------------------
def plot_content_per_year(df):
    yearly_counts = df['year_added'].value_counts().sort_index()
    plt.figure(figsize=(10,5))
    sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o')
    plt.title("Content Added per Year", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")
    plt.grid(True)
    plt.show()

def plot_top_countries(df):
    country_counts = df['country'].value_counts().head(10)
    plt.figure(figsize=(10,5))
    sns.barplot(x=country_counts.values, y=country_counts.index, palette="viridis")
    plt.title("Top 10 Countries by Content", fontsize=14)
    plt.xlabel("Number of Titles")
    plt.ylabel("Country")
    plt.show()

def plot_rating_distribution(df):
    rating_counts = df['rating'].value_counts()
    plt.figure(figsize=(8,8))
    plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title("Rating Distribution", fontsize=14)
    plt.show()

def plot_top_genres(df):
    genre_counts = df['listed_in'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="coolwarm")
    plt.title("Top 10 Genres", fontsize=14)
    plt.xlabel("Number of Titles")
    plt.ylabel("Genre")
    plt.show()

# -------------------- MAIN --------------------
def main():
    df = load_and_clean("netflix_titles.csv")
    plot_content_per_year(df)
    plot_top_countries(df)
    plot_rating_distribution(df)
    plot_top_genres(df)

if __name__ == "__main__":
    main()
