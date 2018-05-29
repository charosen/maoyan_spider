from nose.tools import *
from maoyan_spider import spider

def test_getPageOffset():
    assert_equal(spider.getPageOffset(), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90'])

def test_getOnePage():
    html = spider.getOnePage('10')
    assert html.ok, 'status_code is wrong.'
    assert_equal(html.status_code, 200)
    assert_equal(html.url, 'http://maoyan.com/board/4?offset=10')
#    print(html.text)

def test_getEveryMovie():
    movies = spider.getEveryMovie(spider.getOnePage('10').text)
    assert movies is not None, "getEveryMovie returns None."
    assert isinstance(movies, list), "getEveryMovie returns no list."
    assert_equal(len(movies), 10)
    with open('movie_test.txt', 'w') as f:
        f.write(movies[0])

#    for movie in movies:
#        print(movie)
# def setup():
#     print("SETUP!")

# def teardown():
#     print("TEAR DOWN!")

# def test_basic():
#     print("I RAN!", end='')
