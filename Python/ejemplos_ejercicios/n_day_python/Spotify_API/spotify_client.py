#!/usr/bin/env python
# coding: utf-8

# In[2]:


import base64
import requests
import datetime
from urllib.parse import urlencode


# In[1]:


client_id = ''
client_secret = ''


# In[3]:


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        RETURNS A BASE 64 ENCODE STRING
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_id == None or client_secret == None:
            raise Exception("TOU MUST SET client_id AND client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        # print(r.json())
        if r.status_code not in range(200, 299):
            raise Exception("COULD NOT AUTHENTICATE CLIENTE")
            # return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        # print(f"access_token -> {access_token}")
        # print(f"now -> {now}")
        # print(f"expires_in -> {expires_in}")
        # print(f"expires -> {expires}")
        return True

    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token()
        return token

    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        return headers

    def get_resource(self, lookup_id, resource_type="albums", version="v1"):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        print(f"endpoint -> {endpoint}")
        headers = self.get_resource_header()
        print(f"headers -> {headers}")
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            print(r.status_code)
            return {}
        print(r.status_code)
        return r.json()

    def get_album(self, _id):
        return self.get_resource(_id, resource_type="albums")

    def get_artist(self, _id):
        return self.get_resource(_id, resource_type="artists")

    def base_search(self, query_params):
        headers = self.get_resource_header()
        endpoint_search = "https://api.spotify.com/v1/search"
        lookup_url = f"{endpoint_search}?{query_params}"
        print(lookup_url)
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        print(r.status_code)
        return r.json()

    def search(self, query=None, operator=None, operator_query=None, search_type='artist'):
        if query == None:
            raise Exception("A query is required")
        if isinstance(query, dict):
            query = " ".join([f"{k}:{v}" for k, v in query.items()])
        if operator != None and operator_query != None:
            if operator.lower() == "or" or operator.lower() == "not":
                operator = operator.upper()
                if isinstance(operator_query, str):
                    query = f"{query} {operator} {operator_query}"
        query_params = urlencode({"q": query, "type": search_type.lower()})
        print(query_params)
        return self.base_search(query_params)
