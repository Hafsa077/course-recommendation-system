import requests

def fetch_jobs_data():
    url = "https://indeed-indeed.p.rapidapi.com/apigetjobs"

    querystring = {"v":"2","format":"json"}

    headers = {
        "x-rapidapi-key": "bd98e657famshdc878745f9d4aadp1f090fjsnb14af66878ef",
        "x-rapidapi-host": "indeed-indeed.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    return response.json()
