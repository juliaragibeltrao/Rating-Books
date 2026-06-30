import pandas as pd
import ast
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sys.stdout.reconfigure(encoding="utf-8")

TABLEAU10 = ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
             "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC"]

sns.set_theme(style="white", rc={
    "font.size": 12,
    "axes.facecolor": "white",
    "axes.edgecolor": "#cccccc",
    "axes.grid": False,
    "xtick.color": "#555555",
    "ytick.color": "#555555",
    "text.color": "#333333",
})

df = pd.read_csv("books_1.Best_Books_Ever.csv")
df["genres"] = df["genres"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else [])
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df_exploded = df.explode("genres")

genre_stats = df_exploded.groupby("genres").agg(
    total_ratings=("numRatings", "sum"),
    avg_rating=("rating", "mean"),
    book_count=("title", "nunique"),
).sort_values("total_ratings", ascending=False)

reliable = genre_stats[genre_stats["book_count"] >= 5].sort_values("avg_rating", ascending=False).head(15)

def stylized_barh(data, values, title, xlabel, color, fmt_func, xlim=None):
    fig, ax = plt.subplots(figsize=(12, 6))
    vals = data[values].values
    bars = ax.barh(range(len(data)), vals, color=color, height=0.6, zorder=3)
    ax.set_yticks(range(len(data)))
    ax.set_yticklabels(data.index, fontsize=11)
    ax.set_xlabel(xlabel, fontsize=12, color="#555555")
    ax.set_title(title, fontsize=16, fontweight="bold", pad=15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")
    ax.tick_params(axis="y", left=False)
    ax.tick_params(axis="x", colors="#555555")
    if xlim:
        ax.set_xlim(xlim)
    for bar, val in zip(bars, vals):
        ax.text(val + (vals[-1]*0.01 if vals[-1] > 0 else 0.005),
                bar.get_y() + bar.get_height()/2,
                fmt_func(val), va="center", fontsize=10, color="#555555")
    plt.tight_layout()

print("=" * 70)
print("1. GÊNEROS COM MAIS AVALIAÇÕES (TOP 15)")
print("=" * 70)
display = genre_stats[["total_ratings", "avg_rating", "book_count"]].head(15).copy()
display["total_ratings"] = display["total_ratings"].apply(lambda x: f"{x:,.0f}")
print(display.to_string())
print()

top_data = genre_stats.head(15).sort_values("total_ratings")
stylized_barh(top_data, "total_ratings",
    "Gêneros com Mais Avaliações", "Total de Avaliações",
    TABLEAU10[0], lambda v: f"{v/1e6:.1f}M")
plt.show()
print()

print("=" * 70)
print("1b. GÊNEROS COM MELHORES NOTAS MÉDIAS (mín. 5 livros, TOP 15)")
print("=" * 70)
display2 = reliable[["total_ratings", "avg_rating", "book_count"]].copy()
display2["total_ratings"] = display2["total_ratings"].apply(lambda x: f"{x:,.0f}")
print(display2.to_string())
print()

top_avg = reliable.sort_values("avg_rating")
colors_avg = [TABLEAU10[2] if v >= 4.3 else TABLEAU10[0] for v in top_avg["avg_rating"].values]

fig2, ax2 = plt.subplots(figsize=(12, 6))
vals_avg = top_avg["avg_rating"].values
bars2 = ax2.barh(range(len(top_avg)), vals_avg, color=colors_avg, height=0.6, zorder=3)
ax2.set_yticks(range(len(top_avg)))
ax2.set_yticklabels(top_avg.index, fontsize=11)
ax2.set_xlabel("Nota Média", fontsize=12, color="#555555")
ax2.set_title("Gêneros com Melhores Notas (mín. 5 livros)", fontsize=16, fontweight="bold", pad=15)
ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)
ax2.spines["left"].set_color("#cccccc"); ax2.spines["bottom"].set_color("#cccccc")
ax2.tick_params(axis="y", left=False); ax2.tick_params(axis="x", colors="#555555")
ax2.set_xlim(4.0, 4.7)
for bar, val in zip(bars2, vals_avg):
    ax2.text(val + 0.005, bar.get_y() + bar.get_height()/2,
             f"{val:.2f}", va="center", fontsize=10, color="#555555", fontweight="bold")
plt.tight_layout()
plt.show()
print()

print("=" * 70)
print("2. LIVROS MAIS BEM AVALIADOS DENTRO DE CADA GÊNERO (TOP 3)")
print("=" * 70)
df_exploded["rank_in_genre"] = df_exploded.groupby("genres")["rating"].rank("dense", ascending=False)
top_books = df_exploded[df_exploded["rank_in_genre"] <= 3][["genres", "title", "author", "rating"]].drop_duplicates()
top_books_sample = top_books.groupby("genres").head(3).head(50)
print(top_books_sample.to_string(index=False))
print()

print("=" * 70)
print("3. AUTORES QUE SE DESTACAM POR GÊNERO (MELHOR NOTA MÉDIA, mín. 2 livros)")
print("=" * 70)
author_genre = df_exploded.groupby(["genres", "author"]).agg(
    avg_rating=("rating", "mean"),
    book_count=("title", "nunique"),
).reset_index()
author_genre = author_genre[author_genre["book_count"] >= 2]
top_authors = author_genre.loc[author_genre.groupby("genres")["avg_rating"].idxmax()]
top_authors = top_authors.sort_values("avg_rating", ascending=False).head(20)
top_authors["avg_rating"] = top_authors["avg_rating"].round(2)
print(top_authors[["genres", "author", "avg_rating", "book_count"]].to_string(index=False))
print()

print("=" * 70)
print("4. LIVROS MAIS CAROS (TOP 20)")
print("=" * 70)
expensive = df.dropna(subset=["price"]).nlargest(20, "price")
expensive_display = expensive.copy()
expensive_display["price_display"] = expensive["price"].apply(lambda x: f"${x:.2f}")
expensive_display["numRatings"] = expensive["numRatings"].apply(lambda x: f"{x:,.0f}")
print(expensive_display[["title", "author", "price_display", "rating", "numRatings"]].to_string(index=False))
print()

top_expensive = expensive.sort_values("price")
fig3, ax3 = plt.subplots(figsize=(14, 8))
short_titles = [t[:55] + "..." if len(t) > 55 else t for t in top_expensive["title"].values]
vals_price = top_expensive["price"].values
bars3 = ax3.barh(range(len(top_expensive)), vals_price, color=TABLEAU10[3], height=0.6, zorder=3)
ax3.set_yticks(range(len(top_expensive)))
ax3.set_yticklabels(short_titles, fontsize=10)
ax3.set_xlabel("Preço ($)", fontsize=12, color="#555555")
ax3.set_title("Livros Mais Caros", fontsize=16, fontweight="bold", pad=15)
ax3.spines["top"].set_visible(False); ax3.spines["right"].set_visible(False)
ax3.spines["left"].set_color("#cccccc"); ax3.spines["bottom"].set_color("#cccccc")
ax3.tick_params(axis="y", left=False); ax3.tick_params(axis="x", colors="#555555")
for bar, val in zip(bars3, vals_price):
    ax3.text(val + 5, bar.get_y() + bar.get_height()/2,
             f"${val:.0f}", va="center", fontsize=10, color="#555555", fontweight="bold")
plt.tight_layout()
plt.show()
print()

print("=" * 70)
print("EXTRA: Preço vs Nota vs Avaliações")
print("=" * 70)
sample = df[df["numRatings"] > 1000].sample(min(3000, len(df)), random_state=42)
fig4, ax4 = plt.subplots(figsize=(11, 7))
scatter = ax4.scatter(
    sample["numRatings"].values, sample["rating"].values,
    c=sample["price"].fillna(0).values, alpha=0.6, s=15,
    cmap="viridis", edgecolors="none", zorder=3
)
ax4.set_xscale("log")
ax4.set_xlabel("Número de Avaliações", fontsize=12, color="#555555")
ax4.set_ylabel("Nota Média", fontsize=12, color="#555555")
ax4.set_title("Relação: Avaliações vs Nota (cor = preço)", fontsize=16, fontweight="bold", pad=15)
ax4.spines["top"].set_visible(False); ax4.spines["right"].set_visible(False)
ax4.spines["left"].set_color("#cccccc"); ax4.spines["bottom"].set_color("#cccccc")
ax4.tick_params(colors="#555555")
cbar = plt.colorbar(scatter, ax=ax4, shrink=0.7)
cbar.set_label("Preço ($)", fontsize=11, color="#555555")
cbar.ax.tick_params(colors="#555555")
plt.tight_layout()
plt.show()
