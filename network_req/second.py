import json
import httpx

def get(url: str, path: str) -> httpx.Response:
    res: httpx.Response = httpx.get(f"{url}/{path}")
    if res.is_error:
        print(f"\033[31m{res.status_code}\033[0m", res.reason_phrase)
    return res

def post(url: str, path: str, payload: dict) -> httpx.Response:
    res: httpx.Response = httpx.post(url=f"{url}/{path}", json=payload)
    if res.is_error:
        print(f"\033[31m{res.status_code}\033[0m", res.reason_phrase)
    return res

def put(url: str, path: str, new_data: dict) -> httpx.Response:
    temp_res = get(url, path)
    data = temp_res.json()
    data.update(new_data)
    res = httpx.put(f"{url}/{path}", json=data)
    if res.is_error:
        print(f"\033[31m{res.status_code}\033[0m", res.reason_phrase)
    return res

def patch(url: str, path: str, new_data: dict) -> httpx.Response:
    res = httpx.patch(f"{url}/{path}", json=new_data)
    return res

def delete(url: str, path: str) -> httpx.Response:
    res = httpx.delete(url=f"{url}/{path}")
    return res

url = "https://jsonplaceholder.typicode.com"

new_data: dict = {}
new_data.update({"userId": 45})
new_data.update({"title": "I am the GOAT"})
new_data.update({"body": "good body of work. good body of work. good body of work. good body of work. good body of work."})


response = delete(url, "posts/2")
print(response.status_code, response.reason_phrase)
print(response.text)
