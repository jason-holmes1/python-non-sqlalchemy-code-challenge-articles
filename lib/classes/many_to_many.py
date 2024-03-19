class Article:
    all = []
    def __init__(self, author, magazine, title: str):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string of length between 5 and 50 characters, inclusive")
        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        self._author = author
        

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        self._magazine = magazine
        
   
    
class Author:
    def __init__(self, name: str, magazine=None, title=None):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a string of length greater than 0")
        self._name = name
        self._magazine = magazine
        self._title = title

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def magazines(self):
        return self._magazine
    @magazines.setter
    def magazines(self, magazine):
        self._magazine = magazine
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title

    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))


    def add_article(self, magazine, title):
        new_article = Article(self,magazine,title)
        return new_article
        
    def topic_areas(self):
        if Author.articles(self) == []:
            return None
        return list(set([magazine.category for magazine in self.magazines()]))
class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or (len(new_name)<2 or len(new_name)>16):
            raise ValueError("Name must be a string of length between 2 and 16 characters, inclusive")
        self._name = new_name
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) <= 0:
            raise ValueError("Category must be a string of length greater than 0")
        self._category = new_category
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        
    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))
        
    def article_titles(self):
        if Magazine.articles(self) == []:
            return None
        return [article.title for article in Magazine.articles(self)]
        
    def contributing_authors(self):
        d ={Author: 0}
        for article in self.articles():
           if article.author in d:
               d[article.author] += 1
           else:
               d[article.author] = 1
        contributors = []
        for author in d:
            article_count = d[author]
            if article_count >= 2:
                contributors.append(author)
        if contributors == []:
            return None
        return contributors