import requests
from bs4 import BeautifulSoup


page = requests.get('https://github.com/trending')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repo = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

# find all instances of that class (should return 25 as shown in the github main page)
repo_list = repo.find_all(class_='Box-row')

print(len(repo_list))

for repo in repo_list:
    # find the first <a> tag and get the text. Split the text using '/' to get an array with developer name and repo name
    # developer = repo.find('span', attrs={"class": "text-normal"}).text.encode('utf-8')
    repository = repo.find('a', class_=False, id=False).text.split('/')
    # extract the developer name at index 0
    repo_name = repository[0].strip()
    # extract the repo name at index 1
    developer = repository[1].strip()
    # find the first occurance of class octicon octicon-star and get the text from the parent (which is the number of stars)
    # stars = repo.find('svg', attrs={"class": "octicon octicon-star"}).parent.text
    stars = repo.find('a', attrs={"class": "muted-link d-inline-block mr-3"}).text.strip()
    # strip() all to remove leading and traling white spaces
    print(repo_name)
    print(developer)
    print(stars)
