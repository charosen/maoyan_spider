import requests, re


url_base = 'http://maoyan.com/board/4'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}


def getPageOffset():
    return [str(page * 10) for page in range(10)]

def getOnePage(offset):
    # get the page offset param, use it to send a get request and return the response object
    params = {'offset': offset}
    html = requests.get(url_base, headers=headers, params=params)
    return html

def getEveryMovie(page_html):
    # use regex to select all movies html code block out of one page
    return re.findall('<dd>(.*?)</dd>', page_html, re.S)

def getInfo(movie_html):
    info = {}

    match = re.search('data-src="(.*?)"\salt="(.*?)"\s', movie_html, re.S)

    info['name'] = match.group(2)
    info['star'] = re.search('star">(.*?)</p>', movie_html, re.S).group(1).strip()
    info['releasetime'] = re.search('releasetime">(.*?)</p>', movie_html).group(1)
    info['pic'] = match.group(1)

    return info

def saveInfo(movie_dict):

    with open('maoyan_top100_movie.txt', 'a') as f:
        for key, value in movie_dict.items():
            f.writelines(key + ': ' + value + '\n')
        f.writelines('\n')



# test:
if __name__ == '__main__':

    pages = getPageOffset()
    for page in pages:
        page_html = getOnePage(page)
        movies = getEveryMovie(page_html.text)
        count = 0
        for movie in movies:
            count ++
            print(f'>> we are here {count}.')
            movie_info = getInfo(movie)
            saveInfo(movie_info)
