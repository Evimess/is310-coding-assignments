from bs4 import BeautifulSoup
import requests
import pandas as pd
url = pd.read_csv("cleaned_pudding_data.csv")
url = url[:1000]
def scrape_article(url):
    response = requests.get(url)
    html_string = response.text
    return html_string
url['text'] = url['link'].apply(scrape_article)
url.to_csv('/Users/evan/is310-coding-assignments/web_scraping_assignments/pudding_movie_dialogue.csv', index=False)
# response = requests.get("cleaned_pudding_data.csv")
# soup = BeautifulSoup(response.text, "html.parser")


# links = soup.find_all('a')

# for link in links:
#     if "Archives" in link.get('href'):
#         print(link.get_text())
#         volume_url = "https://cleaned_pudding_data.csv" + link.get('href')
#         volume_response = requests.get(volume_url)
#         volume_soup = BeautifulSoup(volume_response.text, "html.parser")
#         print(volume_soup.get_text())