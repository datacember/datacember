import requests
import time

'''
payload = {
    "sql": "SELECT * FROM davis"
}
'''

#execution = requests.post('http://127.0.0.1:8999/sql', json=payload)

class datacember:
    def __init__(self, username: str, password: str,
                 endpoint: str = 'http://127.0.0.1:8999', database='antartica'):

        self.username = username
        self.password = password
        self.endpoint = endpoint

    def __enter__(self):
        response = requests.post(
            self.endpoint+"/auth",
            json={
                "username": self.username,
                "password": self.password
            }
        )
        response = response.json()
        if 'auth' in response:
            if response['auth']:
                # minting a new token server side
                auth_token = response['token']
                return lambda sql: datacember_cursor(self.endpoint+'/sql',
                                                     sql,
                                                     auth_token)

        raise Exception("Failed to verify user")


    def __exit__(self, *args, **kwargs):
        pass


def datacember_cursor(endpoint: str, sql: str, auth_token: str, debug=True):
    response = requests.post(endpoint, json={"token": auth_token, "sql": sql})
    if response.status_code == 429:
        raise Exception("Rate limit. Exceeded 20 per minute")

    response = response.json()

    if debug:
        print(auth_token, endpoint)

    if 'error' in response:
        raise Exception(response['error'])

    if 'content' in response:
        return response['content']


## Example
'''
datacember = datacember("wingfooted", "password")
with datacember as antartica:
    content = antartica("SELECT * FROM davis")
    print(content)
    for i in tqdm.tqdm(range(100)):
        content = antartica("SELECT * FROM mawson")
        print(i, str(content)[:50])
        time.sleep(1)
    # timeout line
    content = antartica("SELECT * FROM davis")
    print(content)
'''