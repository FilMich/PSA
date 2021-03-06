#!/usr/env python3
APP_VERSION = '1.0'

class Movie:
    def __init__(self, paTitle, paYear, paGenere, paEarnings, paRating, paDuration):
        self.aTitle = paTitle
        self.aYear = paYear
        self.aGenere = paGenere
        self.aEarnings = paEarnings
        self.aRating = paRating
        self.aDuration = paDuration

    def toString(self):
        return '{:20} {} {:10} ${:4} {:3}% {:3}m'.format(self.aTitle,
                                                            self.aYear,
                                                            self.aGenere,
                                                            self.aEarnings,
                                                            self.aRating,
                                                            self.aDuration)
        
class MovieLibrary():
    def __init__(self):
        self.aMovies = list()
    def addMovie(self, paMovie):
        self.aMovies.append(paMovie)
    def removeMovie(self, paMovieIndex):
        self.aMovies.pop(paMovieIndex)
    def printLibrary(self, paPrintIndex):
        if(paPrintIndex):
            indexSrtring = ' ID '
        else:
            indexSrtring = ''
        header = '{}{:20} {} {:10} {:4} {:3} {:3}'.format(indexSrtring, 'Title',
                                                            'Year',
                                                            'Genere',
                                                            'Earn',
                                                            'Rat',
                                                            'Time')
        print(header)
        print('-'*len(header))
        index = 0
        for movie in self.aMovies:
            print(movie.toString())
            if paPrintIndex:
                indexSrtring = '{:3} '.format(index)
            else:
                indexSrtring = ''
            print(indexSrtring + movie.toString())
            index += 1


def menu(paMovieLibrary):
    while True:
        print("Welcome to Movie Library v{}".format(APP_VERSION))
        print(' Add movie (1)')
        print(' Remove movie (2)')
        print(' Show library content (3)')
        print(' Quit program (q)')
        opt = input('Select an option from the menu: ')

        if opt == '1':
            addMovie(paMovieLibrary)
        elif opt == '2':
            removeMovie(paMovieLibrary)
        elif opt == '3':
            paMovieLibrary.printLibrary(False)
        elif opt == 'q':
            print('Bye! Thanks for usage.')
            exit(0)
        else:
            print('Incorrect option!!!')

def addMovie(paMovieLibrary):
    title = input('Enter movie title: ')
    year = input('Enter year: ')
    genere = input('Enter genere: ')
    earn = input('Enter movie earnings in milions of $: ')
    rating = input('Enter rating in %: ')
    duration = input('Enter duration in minutes: ')

    movie = Movie(title, year, genere, earn, rating, duration)
    paMovieLibrary.addMovie(movie)

def removeMovie(paMovieLibrary):
    paMovieLibrary.printLibrary(True)

    index = input('Enter movie index for removal: ')
    paMovieLibrary.removeMovie(int(index))

if __name__ == "__main__":
    library = MovieLibrary()
    menu(library)