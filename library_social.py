import json
import requests
# import re

with open("all_libraries.json", "r") as f:
    data = json.load(f)

# social_media_pattern = r"(facebook\.com|twitter\.com|instagram\.com|linkedin\.com|youtube\.com)"


social_media_sites = ['facebook.com','twitter.com','instagram.com','linkedin.com','youtube.com','nextdoor.com']

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=3)
session.mount("http://", adapter)
session.mount("https://", adapter)

# this makes the request look more like a real web browser, it might not matter but worth setting 
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
})




for library in data:
    url = library['url']

    try:
        r = session.get(url)

        if r.status_code == 200:
            print(f"URL: {url}")

            # lets check each url in the html, we will lower case the html to make sure it might match the lowercase website names
            # and store the results in the same dictonary            
            for site in social_media_sites:
                if site in r.text.lower():
                    library[site] = True
                else:
                    library[site] = False


            # no connection error so record that
            library['connection_error'] = False

            # # match = re.search(social_media_pattern, r.text)
            # if match:
            #     print(f"{url} contains a social media link: {match.group(0)}")
            # else:
            #     print(f"{url} does not contain a social media link.")

            
        else:
            # if there was an error record that too
            library['connection_error'] = True
            library['connection_error_code'] = r.status_code
            print(f"Failed to retrieve {url}. Status code: {r.status_code}")
    except Exception as e:
        library['connection_error'] = True
        print(f"Failed to retrieve {url}: {e}")

    # write out the results
    json.dump(data,open('all_libraries_with_sites.json','w'),indent=2)