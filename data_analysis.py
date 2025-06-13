import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#load the data
matches=pd.read_csv('Datasets/cleaned_matches.csv')
deliveries=pd.read_csv('Datasets/cleaned_deliveries.csv')

print(matches.head())
print(deliveries.head())


#count the wins of top 5 teams
top_teams= matches['winner'].value_counts().head(5)


#plot
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5)) 
sns.barplot(x=top_teams.values,y=top_teams.index,hue=top_teams.index,palette='viridis',legend=False)
plt.title('top 5 teams(winners)')
plt.xlabel('no of wins')
plt.ylabel('teams')
plt.tight_layout()
plt.savefig("outputs/top5_teams.png")
plt.show()
plt.clf()



# Top 10 players with most "player of the match" awards
top_players = matches['player_of_match'].value_counts().head(10)

# Plot 2
sns.barplot(x=top_players.values, y=top_players.index, palette="magma")
plt.title("Top 10 Players of the Match")
plt.xlabel("Number of Awards")
plt.ylabel("Player")
plt.savefig('outputs/top_players.png')
plt.show()
plt.clf()


