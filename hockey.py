import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089"
)

if response.status_code != 200:
    print("Failed to retrieve the website content.")
    exit()

soup = BeautifulSoup(response.content, "html.parser")

match_results = soup.select('div.date-show')
if not match_results:
    print("No match elements found. Check if the website structure has changed.")
    exit()

for match_result in match_results:
    date_element = match_result.select_one('div.datetime-container')
    if date_element:
        date = date_element.text.strip().split('•')[0].strip()
    else:
        print("Date not found.")
        continue

    match_container = match_result.select_one('div.match-container')
    if not match_container:
        print("Match container not found.")
        continue

    score_element = match_container.select_one('div.score-container')
    if not score_element:
        print("Score element not found.")
        continue

    scores = score_element.find_all('div', class_='score')
    if len(scores) >= 3:
        home_team_score = scores[0].text.strip()
        away_team_score = scores[2].text.strip()
    else:
        print("Home and away team scores not found.")
        continue

    home_team_element = match_container.select_one('div.team-container.team-home div.team-name')
    if home_team_element:
        home_team = home_team_element.text.strip()
    else:
        print("Home team not found.")
        continue

    away_team_element = match_container.select_one('div.team-container.team-away div.team-name')
    if away_team_element:
        away_team = away_team_element.text.strip()
    else:
        print("Away team not found.")
        continue

    # Filter the matches by the name of your favorite team
    if "Mountfield" in home_team.lower() or "Mountfield" in away_team.lower():
        print(f"{date} we defeated {home_team} ({home_team_score} - {away_team_score})")
