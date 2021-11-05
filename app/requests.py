
import urllib.request,json
from .models import Source,Article
from datetime import datetime

# Getting api key
api_key = None
# Getting the news base url
base_url = None

# Getting the article  url
# article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    article_url = app.config['ARTICLE_BASE_URL']

def get_source(category):
    '''
	Function that gets the json response to our url request
	'''
    get_source_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
       source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id') 
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        
        source_object = Source(id,name,description,url,category,country,language)
        source_results.append(source_object)

    return source_results

def get_article(id):
    '''
    Function that processes the article and returns a list of article objects
    '''
    get_article_url = article_url.format(id,api_key)
    print(get_article_url)
    with urllib.request.urlopen(get_article_url) as url:
        article_results = json.loads(url.read())


        articles_object = None
        if article_results['articles']:
            article_object = process_article(article_results['articles'])

    return article_object

def process_article(article_list):
	
    article_object = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        
        if urlToImage:
            article_result = Article(id,name,author,title,description,url,urlToImage,publishedAt)
            
            article_object.append(article_result)	
    return article_object
