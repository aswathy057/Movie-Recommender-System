Movie Recommender System 🎬
A content-based movie recommendation engine built with Python and Machine Learning. This application suggests 5 similar movies based on a user's selection using text analysis and mathematical similarity.
**> FEATURES
Interactive Web App: Built using Streamlit.
Visuals: Fetches real-time posters via the TMDB API.
Smart Search: Search through a dataset of 5,000 movies.
**> HOW IT WORKS
Data Processing: I combined movie tags (genres, keywords, cast) into a single string.
Vectorization: Used CountVectorizer to turn text into vectors.
Similarity: Applied Cosine Similarity to find the closest movies in a 5,000-dimensional space.
**> TECH STACK
Language: Python
Libraries: Pandas, Scikit-Learn, Streamlit, Requests
Model: Cosine Similarity
**> MISSING MODEL FILES
Due to GitHub's file size limits, the similarity.pkl file is hosted externally.
Download similarity.pkl here
(https://drive.google.com/file/d/1wcpkPlfl_jD4OR6R1gZxGAutHTXcaOQz/view?usp=sharing)
