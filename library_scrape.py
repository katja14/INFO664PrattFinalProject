import requests
from bs4 import BeautifulSoup
import json
import time
import re

all_items = []

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District%20of%20Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New%20Hampshire", "New%20Jersey", "New%20Mexico", "New%20York", "North%20Carolina", "North%20Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode%20Island", "South%20Carolina", "South%20Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West%20Virginia", "Wisconsin", "Wyoming"]

for a_state in states:
    state_url = f"https://librarytechnology.org/libraries/public.pl?State={a_state}"
    print(state_url)
    
    r = requests.get(state_url)
    

    soup = BeautifulSoup(r.text, features="html.parser")
    
    library_urls = []
    link_element = soup.find("a", {"target": "LibraryWindow"})
    href_value = link_element.get("href")
    title_value = link_element.get("title")

    
    if href_value == title_value:
        library_url = href_value
        
        for library_url in library_urls:
            print(library_url)