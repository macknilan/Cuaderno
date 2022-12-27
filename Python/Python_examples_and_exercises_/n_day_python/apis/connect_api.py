import datetime
import os

import pandas as pd
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Movies_db:
    """
    CONECT TO API https://www.themoviedb.org/
    """

    def __init__(self, list_id=None):
        self.list_id = list_id

    def v_3(self):
        """GET A LIST OF THE CURRENT POPULAR MOVIES ON TMDB. THIS LIST UPDATES DAILY."""
        # ENVIRONMENT VARIABLES
        # https://api.themoviedb.org/3/movie/popular?api_key=<<KEY>>&language=en-US&page=1
        API_KEY_V3 = ""
        API_VERSION = 3
        API_BASE_URL = f"https://api.themoviedb.org/{API_VERSION}"
        endpoint_path = "/movie/popular"
        q_string_page = 1
        ENDPOINT = f"{API_BASE_URL}{endpoint_path}?api_key={API_KEY_V3}&page={q_string_page}"
        # ENDPOINT -> https://api.themoviedb.org/3/movie/popular?api_key=<<KEY>>&page=1
        r = requests.get(ENDPOINT)
        if r.status_code in range(200, 299):
            data = r.json()
            results = data["results"]
            if len(results) > 0:
                # print(results[0].keys())
                movie_ids = set()
                # print(f"movie_ids -> {movie_ids}")
                for result in results:
                    _id = result["id"]
                    # print(result["title"], _id)  # Cruella 337404
                    movie_ids.add(_id)
                # print(list(movie_ids))
        movie_data = []
        if len(movie_ids) > 0:
            """GET THE PRIMARY INFORMATION ABOUT EACH MOVIE."""
            endpoint_path_get_details = "/movie/"
            for movie_id in movie_ids:
                ENDPOINT_GET_DETAILS = f"{API_BASE_URL}{endpoint_path_get_details}{movie_id}?api_key={API_KEY_V3}"
                r = requests.get(ENDPOINT_GET_DETAILS)
                if r.status_code in range(200, 299):
                    movie_data.append(r.json())
            # print(f"movie_data -> {movie_data}")

            df = pd.DataFrame(movie_data)
            path_data_movies = os.path.join(BASE_DIR, "folder_data_movies")
            if not os.path.exists(path_data_movies):
                # raise Exception("This path does not exist")
                os.makedirs(path_data_movies, exist_ok=True)
                file = os.path.join("folder_data_movies", f"movies-{datetime.datetime.now()}.csv")
                df.to_csv(file, index=False)
                return True
            else:
                os.makedirs(path_data_movies, exist_ok=True)
                file = os.path.join("folder_data_movies", f"movies-{datetime.datetime.now()}.csv")
                df.to_csv(file, index=False)
                return True

    def v_4(self):
        # ENVIRONMENT VARIABLES
        API_KEY_V4 = ""
        API_VERSION = 4
        BASE_URL = f"https://api.themoviedb.org/{API_VERSION}/list/"
        HEADERS = {
            "Authorization": f"Bearer {API_KEY_V4}",
            "Content-Type": "application/json;charset=utf-8",
        }
        q_string_list_id = 1
        q_string_page = 1
        # q_string_language = "en-US"
        q_string_sort_by = "release_date.desc"

        ENDPOINT = f"{BASE_URL}{q_string_list_id}?page={q_string_page}&sort_by={q_string_sort_by}"

        req = requests.get(ENDPOINT, headers=HEADERS)
        if req.status_code in range(200, 299):
            data = req.json()
            results = data["results"]

        # print(f"ENDPOINT -> {ENDPOINT}")
        # ENDPOINT -> https://api.themoviedb.org/4/list/1?page=1&sort_by=release_date.desc
        print(f"req.status_code -> {req.status_code}")
        # print(f"req.text -> {req.text}")
        print(f"results -> {results}")


# v_4
# python3 -i send_mail.pyc
# obj = Movies_db()
# obj.v_4()
# v_3
# python3 -i send_mail.pyc
# obj.v_3()
