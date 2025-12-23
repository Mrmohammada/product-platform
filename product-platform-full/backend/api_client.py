import requests

API_URL = "https://adinapp.ir/app/supermarket/extra/api/product/api.php"

def call_api(api_key, action, params=None):
    data = {"api_key": api_key, "action": action}
    if params:
        data.update(params)
    r = requests.post(API_URL, data=data, timeout=20)
    r.raise_for_status()
    return r.json()
