import random 
import requests, json 

url = "https://api.apilayer.com/short_url/hash"
headers= {"apikey": "oSuyI00nLsek8z5xMbX6DOp7PHrFgrmM"}

tag = input("Enter topic tag (press enter to skip): ").lower()
r = requests.get(f"https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&tagged={tag}&site=stackoverflow").json()
num = int(input("Number of questions needed (>0): "))
question_list = dict()
c = 0
for i in r["items"] :
    if c == num :
        break
    if i["answer_count"] < 2 :
        r2 = requests.get(f"https://api-ssl.bitly.com/v4/shorten")
        payload = f"{i["link"]}".encode("utf-8")
        response = requests.request("POST", url, headers=headers, data = payload)
        question_list[i["title"]] = response.json()["short_url"]
    c += 1


with open("questions.txt", "w") as f :
    f.write(f"{list(question_list.keys())[0]} ({question_list[list(question_list.keys())[0]]})\n")

with open("questions.txt", "a") as f :
    for i in question_list.keys() :
        f.write(f"{i} ({question_list[i]})\n")
    
print("DONE!")
