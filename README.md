# Graph-Based Recommendation System using Python

## 1. Project Overview

**Course:** GTU PBL (Beyond the Syllabus)  
**Subject:** Python for Data Science (BE05000231)

This project implements a simple movie recommendation system using graph theory and collaborative filtering. Users and movies are represented as nodes, while movie-watching interactions are represented as edges.

The system identifies users who have watched common movies and recommends other movies watched by those similar users.

## 2. Objectives

- Represent user-movie interactions using a graph.
- Identify similar users through common movie interactions.
- Recommend movies that the target user has not watched.
- Rank recommendations using a simple recommendation score.
- Visualize the graph using NetworkX and Matplotlib.

## 3. Technologies Used

- Python
- NetworkX
- Matplotlib

## 4. Methodology

1. Create a graph containing user nodes and movie nodes.
2. Add edges representing movies watched by users.
3. Select a target user.
4. Identify similar users based on common movies.
5. Generate recommendations from movies watched by similar users.
6. Rank recommendations according to their scores.
7. Visualize and save the graph.

## 5. Installation and Execution

Install Python 3 and the required dependencies.

```bash
pip install -r requirements.txt
python recommendation_system.py
```

## 6. Expected Results

The program displays the number of graph nodes and edges, movies watched by the target user, similar users, and ranked movie recommendations.

For the sample dataset, User1 should receive Movie D and Movie E as recommendations, with Movie D ranked higher.

The graph visualization is saved as `graph.png`.

## 7. Limitations

This project uses a small, manually defined dataset. Recommendation scores are based on the number of similar users who watched a movie. The system does not use real movie ratings, a production dataset, or a trained machine-learning model.

## 8. Future Scope

- Use a larger movie dataset.
- Include movie ratings and user preferences.
- Explore weighted similarity and more advanced recommendation algorithms.
- Develop a web interface for users to receive recommendations.

## 9. Conclusion

The project demonstrates how graph theory and collaborative filtering can be used to recommend movies based on relationships between users and movies.
