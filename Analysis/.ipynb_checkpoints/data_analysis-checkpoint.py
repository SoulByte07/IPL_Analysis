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


#plot 1
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


# Create a new column
matches['toss_match_win'] = matches['toss_winner'] == matches['winner']

# Count how often toss winner also won the match
toss_result = matches['toss_match_win'].value_counts()

# Plot 3
sns.barplot(x=toss_result.index, y=toss_result.values, palette="Set2")
plt.xticks([0, 1], ['Lost Match', 'Won Match'])
plt.title("Does Toss Winner Also Win Match?")
plt.ylabel("Number of Matches")
plt.savefig('outputs/toss_results.png')
plt.show()
plt.clf()


#Most Matches Played in Which City (Venue Analysis)
venue_counts = matches['venue'].value_counts().head(10)

#plot 4
sns.barplot(y=venue_counts.index, x=venue_counts.values, palette="cubehelix")
plt.title("Top 10 Most Used Venues")
plt.xlabel("No. of Matches")
plt.ylabel("Venue")
plt.savefig('outputs/venue_counts.png')
plt.show()
plt.clf()



#Bat First vs Chase

#recult type counts
result_type=matches['toss_decision'].value_counts()

# Pie chart
plt.pie(result_type, labels=result_type.index, autopct='%1.1f%%', colors=['#FFDDC1', '#B5EAD7'])
plt.title("Match Wins: Batting First vs Chasing")
plt.savefig('outputs/result_type.png')
plt.show()
plt.clf()


#Year-wise Match Count
matches_per_year = matches['season'].value_counts().sort_index()

#plot 5
sns.lineplot(x=matches_per_year.index, y=matches_per_year.values, marker='o')
plt.title("IPL Matches Per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.savefig("outputs/matches_per_year.png")
plt.show()
plt.clf()


# sucessful team per season
season_winner = matches.groupby(['season', 'winner']).size().reset_index(name='wins')

# Get max win team per season
top_per_season = season_winner.loc[season_winner.groupby('season')['wins'].idxmax()]

# Display as table
print(top_per_season[['season', 'winner', 'wins']])

