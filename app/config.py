class config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={} '

class prodconfig(config):
    '''
    production configuration child class
    
    Args:
        config: The parent configuration class with General configuration settings
    '''
    pass

class Devconfig(config):
    '''
    Development configuration child class
    
    Args:
        config: The parent configuration class with child configuration settings
    '''

    
    DEBUG = True