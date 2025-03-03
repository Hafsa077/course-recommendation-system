# main.py
from api_caller import fetch_jobs_data

if __name__ == "__main__":
    jobs = fetch_jobs_data()
    print(jobs)
