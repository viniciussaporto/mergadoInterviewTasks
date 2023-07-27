import requests
from bs4 import BeautifulSoup

url = "https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Find all the match data elements
match_data = soup.find_all("div", class_="list-score-structured-wapper")

# Define your favorite team
favorite_team = "Mountfield"


for data in match_data:
    # Get the date of the match
    date_time_container = data.find("div", class_="datetime-container")
    date = date_time_container.find("div").text.strip()

    # Get the home and away teams
    match_container = data.find("div", class_="match-container")
    home_team = match_container.find(
        "div", class_="team-container team-home"
    ).text.strip()
    away_team = match_container.find(
        "div", class_="team-container team-away"
    ).text.strip()

    # Get the score
    score_container = match_container.find(
        "div", class_="score-container backbone-view score-small"
    )
    score = score_container.text.strip()

    # Check if your favorite team won the match
    if favorite_team in score:
        defeated_team = home_team if favorite_team == away_team else away_team
        print(f"{date} - we defeated {defeated_team}")

    """
    Didn't work.
    Not sure if the website blocks or if it doesn't work with the scripts present in it
    to update the match details dynamically.
    Can either get a complete print of the html code, or nothing if using html parser, lxml
    or other method to scrape.
    Good challenge! :D
    """
