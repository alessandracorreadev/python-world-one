import requests

url = url = "https://pudim.com.br/"

try:
    answer = requests.get(url, timeout=5)
except requests.ConnectionError:
    print("\033[31mThe Pudim website is not accessible.\033[m")
else:
    print("\033[32mThe Pudim website is accessible.\033[m")
    print(answer.text)


