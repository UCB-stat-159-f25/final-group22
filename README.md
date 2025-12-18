# Spotify Data Analysis

In this project, we study whether a track’s quantitative audio features from Spotify (e.g., danceability, energy, loudness, acousticness, valence) can predict a song's popularity score (0–100). Our Spotify dataset is obtained from Kaggle and contains data on the aformentioned features on 114,000 tracks. We perform EDA on our features and build predictive models using multiple linear regression with LASSO and Ridge regularization. The optimal regularization parameter was found with K-fold CV and the best prediction model was determined through RMSE and CV error.

Our repository contains the following files:
- data/: folder containing spotify data (raw and cleaned)
- figures/: folder containing visualizations (figures)
- results/: folder containing data results (data tables)
- utils/: folder with functions and pytest 
- clean_spotify.ipynb: notebook for cleaning spotify data
- EDA.ipynb: notebook for performing EDA
- linear_regression.ipynb: notebook for creating linear regression model
- main.ipynb: main notebook that summarizes our results  
- environment.yml: environment file with required packages for project 
- myst.yml: MyST file for creating project website 
- ai_documentation.txt: file listing AI prompts and outputs used 
- reference.bib: file listing references (Kaggle-spotify)

Dataset source: 
[Spotify Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group22/main)
