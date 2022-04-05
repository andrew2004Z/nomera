import requests
import time
from bs4 import BeautifulSoup as bs

def test_id(id):
    response = requests.get(f'https://migalki.net/image.php?id={id}', params={})
    return response
sp = []
for i in range(600, 6000):
    if test_id(i).status_code == 200:
        soup = bs(test_id(i).text, "html.parser")
        try:
           vacancies_names = soup.find_all('input', class_='form-control input-lg')[-1]['value']
           p = requests.get(vacancies_names)
           out = open(f"data/{vacancies_names.split('/')[-1]}", "wb")
           out.write(p.content)
           out.close()
        except:
            pass
        print(i)

#for i in sp:
#    p = requests.get(i)
#    out = open(f"data/{i.split('/')[-1]}", "wb")
#    out.write(p.content)
#    out.close()