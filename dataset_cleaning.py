import pandas as pd 

#load  both datasets
matches=pd.read_csv("matches.csv")
deliveries=pd.read_csv("deliveries.csv")

#print the first 5 rows
print(matches.head())
print(deliveries.head())

# Shape and basic info
print("Matches shape:", matches.shape)
print("Deliveries shape:", deliveries.shape)

print("\nMatches info:")
print(matches.info())

print("\nDeliveries info:")
print(deliveries.info())

# Check for nulls
print(matches.isnull().sum())
print(deliveries.isnull().sum())

#changibg teams names
team_replacements = {
    "Rising Pune Supergiants": "Rising Pune Supergiant",
    "Delhi Daredevils": "Delhi Capitals",
    "Deccan Chargers": "Sunrisers Hyderabad"
}

matches.replace(team_replacements, inplace=True)
deliveries.replace(team_replacements, inplace=True)


# Drop duplicate rows if any
matches.drop_duplicates(inplace=True)
deliveries.drop_duplicates(inplace=True)


# Save the cleaned data for future use
matches.to_csv("cleaned_matches.csv", index=False)
deliveries.to_csv("cleaned_deliveries.csv", index=False)
