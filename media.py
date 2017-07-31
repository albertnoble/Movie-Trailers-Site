import webbrowser


class Movie():

    """
      A class that contains the movie object information and funtions to
      retrive the information
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube
                 ):
        """ Inits Movie with movie title, storyline, poster image, and trailer

            Args:
                movie_title: the movies title
                storyline: Movies story line
                poster_image: A url of the poster image
                trailer_youtube: A url of the trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens up a tab to play the trailer of the movie"""
        webbrowser.open(self.trailer_youtube_url)

    def show_info(self):
        """Display the title and storyline of the movie"""
        print(self.title)
        print(self.storyline)
