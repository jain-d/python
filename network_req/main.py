import httpx
import json

def main():
    web_one = "https://jsonplaceholder.typicode.com"

    #web_two = "https://httpbin.org/get"

    response: httpx.Response = httpx.get(f"{web_one}/posts/2")

    data = response.encoding

    print(type(data))
    print(data)



if __name__ == "__main__":
    main()
