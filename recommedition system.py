import pandas as pd
import numpy as np

# Sample data: A list of books with their titles and genres
data = {
    'Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Genre': ['Fiction', 'Drama', 'Dystopian', 'Romance', 'Fiction']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to calculate cosine similarity between two strings
def cosine_similarity(str1, str2):
    # Convert strings to lowercase
    str1, str2 = str1.lower(), str2.lower()
    
    # Create a set of words for each string
    words1, words2 = set(str1.split()), set(str2.split())
    
    # Calculate intersection and union of words
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    
    # Cosine similarity = intersection / union
    return intersection / union if union != 0 else 0

# Function to recommend books based on user input
def recommend_books(user_input, df):
    print(f"Your input genre: {user_input}")
    
    # Create a list to store similarity scores
    sim_scores = []
    
    # Compare user input with each book's genre
    for index, row in df.iterrows():
        genre = row['Genre']
        score = cosine_similarity(user_input, genre)
        sim_scores.append((index, score))
    
    # Sort by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 3 most similar books
    recommended_indices = [score[0] for score in sim_scores[1:4]]  # Exclude the input genre itself
    
    # Print out the recommended book titles
    print("\nBooks recommended for you:")
    for idx in recommended_indices:
        print(df['Title'][idx])

# Get user input for genre preference
user_input = input("Enter your preferred genre (e.g., 'Fiction', 'Romance'): ")

# Call the recommendation function
recommend_books(user_input, df)
