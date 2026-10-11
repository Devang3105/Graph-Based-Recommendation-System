
import networkx as nx
import matplotlib.pyplot as plt

# 1. Create the user-movie graph
G = nx.Graph()

users = ["User1", "User2", "User3", "User4", "User5"]
movies = [
    "Movie A", "Movie B", "Movie C",
    "Movie D", "Movie E", "Movie F"
]

G.add_nodes_from(users, bipartite=0)
G.add_nodes_from(movies, bipartite=1)

G.add_edges_from([
    ("User1", "Movie A"),
    ("User1", "Movie B"),
    ("User1", "Movie C"),
    ("User2", "Movie A"),
    ("User2", "Movie B"),
    ("User2", "Movie D"),
    ("User3", "Movie C"),
    ("User3", "Movie E"),
    ("User4", "Movie E"),
    ("User4", "Movie F"),
    ("User5", "Movie B"),
    ("User5", "Movie D")
])

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# 2. Select target user
target = "User1"
watched = set(G.neighbors(target))

print("\nTarget user:", target)
print("Watched movies:", sorted(watched))

# 3. Find similar users
similar = {}

for movie in watched:
    for user in G.neighbors(movie):
        if user != target:
            similar[user] = similar.get(user, 0) + 1

print("\nSimilar users:")
for user, score in sorted(similar.items()):
    print(f"{user}: {score} common movies")

# 4. Generate scored recommendations
recommend = {}

for user in similar:
    for movie in G.neighbors(user):
        if movie not in watched:
            recommend[movie] = recommend.get(movie, 0) + 1

ranked = sorted(
    recommend.items(),
    key=lambda item: (-item[1], item[0])
)

print("\nRanked movie recommendations:")
if ranked:
    for movie, score in ranked:
        print(f"{movie}: recommendation score = {score}")
else:
    print("No recommendations available.")

# 5. Visualize and save graph
pos = nx.bipartite_layout(G, users)

colors = [
    "skyblue" if node in users else "lightgreen"
    for node in G.nodes()
]

plt.figure(figsize=(10, 6))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=colors,
    node_size=1700,
    font_size=9,
    edge_color="gray"
)

plt.title("Graph-Based Movie Recommendation System")
plt.tight_layout()
plt.savefig("graph.png", dpi=300, bbox_inches="tight")
plt.show()
