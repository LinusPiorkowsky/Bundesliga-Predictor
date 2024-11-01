import pandas as pd

# CSV File

try:
    df = pd.read_csv('/Users/linus/Bundesliga-Predictor/Bundesliga-Predictor/Datasets/2005-2022.csv')  # Pfad selbst anpassen

    # Column names
    selected_columns = [
        'MATCH_DATE',   
        'SEASON',       
        'LOCATION',     
        'MATCHDAY_NR',  
        'HOME_TEAM_NAME', 
        'AWAY_TEAM_NAME', 
        'GOALS_HOME',   
        'GOALS_AWAY',   
        'DRAW',         
        'WIN_HOME',     
        'WIN_AWAY'      
    ]

    # Load only the specific columns
    df = pd.read_csv('/Users/linus/Bundesliga-Predictor/Bundesliga-Predictor/Datasets/2005-2022.csv', usecols=selected_columns)  # Pfad selbst anpassen


except FileNotFoundError:
    print("Error: The specified CSV file was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: There was an issue parsing the CSV file. Please check its format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
        # Tests
    #print(df.head(20))  
    #print("Available Seasons:", df['SEASON'].unique())
    
    # Sort the data to ensure chronological order
    df = df.sort_values(by=['SEASON', 'MATCH_DATE']).reset_index(drop=True)

    # Define constants
    rows_per_spieltag = 9
    total_spieltage = 34

    # Dictionary to store seasons, each with a list of Spieltage arrays
    season_data = {}

    # Loop through each unique season in the data
    for season in df['SEASON'].unique():
        # Filter data for the current season
        season_df = df[df['SEASON'] == season]
        
        # Verify there are enough rows for 34 Spieltage
        if len(season_df) < rows_per_spieltag * total_spieltage:
            print(f"Warning: Not enough rows in season {season} to fill 34 Spieltage with 9 rows each.")
            continue  # Skip this season if it doesn't have enough data
        
        # List to hold Spieltage for the current season
        season_schedule = []

        # Loop through each Spieltag in the current season
        for spieltag in range(total_spieltage):
            # Extract rows for the current Spieltag
            start_row = spieltag * rows_per_spieltag
            end_row = start_row + rows_per_spieltag
            current_spieltag = season_df.iloc[start_row:end_row]  # Store as a DataFrame
            
            # Append the current Spieltag DataFrame to the season schedule
            season_schedule.append(current_spieltag)

        # Store the schedule in the dictionary with season as an integer key
        season_data[season] = season_schedule

    # Variables to select specific season and Spieltag
    selected_season = 2022  # Replace with the season you want
    selected_spieltag = 1   # Replace with the Spieltag you want 

    # Access the specific season and Spieltag
    if selected_season in season_data:
        if 1 <= selected_spieltag <= total_spieltage:
            spieltag_data = season_data[selected_season][selected_spieltag - 1]
            print(f"\nData for Season {selected_season}, Spieltag {selected_spieltag}:\n")
            print(spieltag_data.to_string(index=False))  # Print without index
        else:
            print(f"Error: Spieltag {selected_spieltag} is out of range. Please select between 1 and {total_spieltage}.")
    else:
        print(f"Error: Season {selected_season} is not available. Please check the available seasons.")
