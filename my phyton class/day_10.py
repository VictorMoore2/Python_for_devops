#Application Programming Interface (API)

""" GET: Retrieve data from a server.
POST: Send data to a server.
PUT: Update existing data on a server.
DELETE: Remove data from a server. """

import requests
#Make a get request to the API
""" response = requests.get("https://jsonplaceholder.typicode.com/posts")

#Check if the request was successful
if response.status_code ==200:
    post = response.json() #Parse JSON response
    for post in post[ :5]: #Display the first 5 posts
        print(f"Title:{post['title']}\nBody:{post['body']}\n")
else:
    print("Failed to retrieve data:",response.status_code) """

#Fetching Data from External services
#Using Query Parameters
""" user_id = 1
response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")

if response.status_code ==200:
    posts = response.json()
    for post in posts:
        print(f"Title:{post['title']}\n")
else:
    print("failed to retrieve data:",response.status_code) """

#Sending Data with POST requests
""" new_post = {
    "title": "My New Post",
    "body": "This is a post",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

if response.status_code == 201:
    print("Post created successfully:", response.json())
else:
    print("Failed to create post:", response.status_code) """

#Introduction to web scraping with beautiful soup
#parsing HTML with beautifulsoup
#webscripting

""" from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the web page:",response.status_code)

soup = BeautifulSoup(html_content, 'lxml')
#parse the HTML content

#Print the title of the page
print(soup.title.string) """

#webscripting for automation

#handling dynamic content with Selenuim
from selenium import webdriver
from selenium.webdriver.common.by import  By

driver = webdriver.Chrome()

driver.get("https://example-blog.com")

#Wait for the page to load and find elements
titles = driver.find_elements(By.TAG_NAME, 'h2')


for title in titles:
    print(title.text)

driver.quit()


