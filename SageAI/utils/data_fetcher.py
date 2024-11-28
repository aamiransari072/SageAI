import requests
from SageAI.src.config.configuration import getConfig
from bs4 import BeautifulSoup
import nltk


nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



def search_engine(query):


    endpoint = "https://www.googleapis.com/customsearch/v1"
    config = getConfig()
    params = config.get_config()
    params["q"] = query
    response = requests.get(endpoint,params=params)

    if response.status_code == 200:
        results = response.json().get('items',[])
        extracted_result = [{
            "title": result.get('title'),
            "link": result.get('link'),
            "snippet": result.get('snippet')

        }
        for result in results
        
        ]
        return extracted_result
    else:
        print(f'Erro: {response.status_code} - {response.text}')
        return []
    


def get_para(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content,'html5lib')
    para = soup.find_all('p')

    cleand = []
    for p in para:
        for unwanted in p(['a', 'br', 'script', 'style']):
            unwanted.decompose()
        text = p.get_text(separator=" ", strip=True)
        cleand.append(text)
    return "\n".join(cleand)
        
        
def get_data(query):
    config = getConfig()
    print(f"Trying to get response")
    response = search_engine(query)
    # print(f"Respnse: {response}")
    print(f"Response find")
    data = []
    for r in response:
        url = r['link']
        temp = get_para(url)
        data.append(temp)
    return data


def process_data(data):
    stop_words = set(stopwords.words('english'))
    processd_data = []
    for d in data:
        tokens = word_tokenize(d.lower())
        fillter_token = [
            word for word in tokens if word.isalpha() and word not in stop_words
        ]
        processd_data.append(" ".join(fillter_token))
    ans = ""
    for d in processd_data:
        ans +=d
    return ans