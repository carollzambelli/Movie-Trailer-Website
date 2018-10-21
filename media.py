import webbrowser


class Movie():
    '''
     This class storage movie information and display the movie trailer
    '''

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        '''
        The constructor defines movies information (title, storyline, image and
        the url trailer)
        :param movie_title: string
        :param movie_storyline: string
        :param poster_image: string
        :param trailer_youtube: string
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''
        This function is responsable for display the movie trailer
        '''
        webbrowser.open(self.trailer_youtube_url)
