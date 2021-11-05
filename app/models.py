class Source:
    '''
    Source class to define source Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country



class Article:
    '''
    Article class to define article Objects
    '''

    all_articles = []

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
 


    # def save_article(self):
    #     Article.all_articles.append(self)


    # @classmethod
    # def clear_articles(cls):
    #     Article.all_articles.clear()

    # @classmethod
    # def get_articles(cls,id):

    #     response = []

    #     for article in cls.all_articles:
    #         if article.id == id:
    #             response.append(article)

    #     return response