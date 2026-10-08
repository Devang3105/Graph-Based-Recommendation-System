import networkx as nx
import matplotlib.pyplot as plt

# 1. Initialize bipartite graph
G = nx.Graph()
users = ["User1", "User2", "User3", "User4", "User5"]
movies = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E", "Movie F"]

G.add_nodes_from(users, bipartite=0)
G.add_nodes_from(movies, bipartite=1)

G.add_edges_from([
    ("User1", "Movie A"), ("User1", "Movie B"), ("User1", "Movie C"),
    ("User2", "Movie A"), ("User2", "Movie B"), ("User2", "Movie D"),
    ("User3", "Movie C"), ("User3", "Movie E"),
    ("User4", "Movie E"), ("User4", "Movie F"),
    ("User5", "Movie B"), ("User5", "Movie D")
])

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

print("\nInteractions:")
for user, movie in G.edges():
    print(f"  {user} -> {movie}")

# 2. Collaborative filtering logic for target user
target = "User1"
watched = set(G.neighbors(target))
print(f"\nMovies watched by {target}:", sorted(watched))

# Find overlapping users
similar = {}
for movie in watched:
    for user in G.neighbors(movie):
        if user != target:
            similar[user] = similar.get(user, 0) + 1
print("Similar users (common movies):", similar)

# Find unvisited movies watched by similar users
recommend = {}
for user in similar:
    for movie in G.neighbors(user):
        if movie not in watched:
            recommend[movie] = recommend.get(movie, 0) + 1
print(f"Recommended movies for {target}:", sorted(recommend))

# 3. Visualization
pos = nx.bipartite_layout(G, users)
colors = ["skyblue" if n in users else "lightgreen" for n in G.nodes()]

plt.figure(figsize=(8, 5))
nx.draw(
    G, pos,
    with_labels=True,
    node_color=colors,
    node_size=1500,
    font_size=8,
    edge_color="gray"
)
plt.title("User-Movie Recommendation Graph")
plt.show()