# -*- coding: utf-8 -*-

# import the html content and media class
import fresh_tomatoes
import media

# This is where instances of the class Movie are defined.
# The order of each input agrees with media class constructor

# Thor movie: movie title, storyline, poster, image and movie trailer
thor = media.Movie(
    "Thor",
    "The powerful, but arrogant god Thor, is cast out of Asgard to live "
    "amongst humans in Midgard (Earth), where he soon becomes one of their "
    "finest defenders.",
    "images/thor.jpg",
    "https://www.youtube.com/watch?v=JOddp-nlNvQ"  # NOQA
)

# Iron Man movie: movie title, storyline, poster, image and movie trailer
iron_man = media.Movie(
    "Iron Man",
    "After being held captive in an Afghan cave, billionaire engineer Tony "
    "Stark creates a unique weaponized suit of armor to fight evil.",
    "images/iron_man.jpg",
    "https://www.youtube.com/watch?v=8hYlB38asDY"  # NOQA
)

# Dr Strange movie: movie title, storyline, poster, image and movie trailer
dr_strange = media.Movie(
    "Dr. Strange",
    "While on a journey of physical and spiritual healing, a brilliant "
    "neurosurgeon is drawn into the world of the mystic arts.",
    "images/dr_strange.jpg",
    "https://www.youtube.com/watch?v=HSzx-zryEgM"  # NOQA
)

# Black Panther: movie title, storyline, poster, image and movie trailer
pantera_negra = media.Movie(
    "Black Panther",
    "T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step "
    "forward to lead his people into a new future and must confront a "
    "challenger from his country's past.",
    "images/black_panther.jpg",
    "https://www.youtube.com/watch?v=xjDjIWPwcPU"  # NOQA
)

# Guardians of the Galaxy movie: movie title, storyline, poster, image and
# movie trailer
g_galaxy = media.Movie(
    "Guardians of the Galaxy",
    "A group of intergalactic criminals are forced to work together to stop a "
    "fanatical warrior from taking control of the universe.",
    "images/g_galaxy.jpg",
    "https://www.youtube.com/watch?v=XdWyeT1VZrY"  # NOQA
)

# Spider Man movie: movie title, storyline, poster, image and movie trailer
spider_man = media.Movie(
    "Spider Man",
    "Peter Parker balances his life as an ordinary high school student in "
    "Queens with his superhero alter-ego Spider-Man, and finds himself on "
    "the trail of a new menace prowling the skies of New York City.",
    "images/spider.jpg",
    "https://www.youtube.com/watch?v=39udgGPyYMg"  # NOQA
)

# The Avengers movie: movie title, storyline, poster, image and movie trailer
avengers = media.Movie(
    "The Avengers",
    "Earth's mightiest heroes must come together and learn to fight as a team "
    "if they are going to stop the mischievous Loki and his alien army from "
    "enslaving humanity.",
    "images/avengers.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8"  # NOQA
)

# Ant Man movie: movie title, storyline, poster, image and movie trailer
ant_man = media.Movie(
    "Ant Man",
    "Armed with the astonishing ability to shrink in scale but increase in "
    "strength, master thief Scott Lang must embrace his inner-hero and help "
    "his mentor, Dr. Hank Pym, protect the secret behind his spectacular "
    "Ant-Man Suit from a new generation of towering threats.",
    "images/ant_man.jpg",
    "https://www.youtube.com/watch?v=pWdKf3MneyI"  # NOQA
)

# Captain America movie: movie title, storyline, poster, image and movie
# trailer
captain = media.Movie(
    "Captain America",
    "Steve Rogers, a rejected military soldier transforms into Captain America"
    " after taking a dose of a 'Super-Soldier serum'",
    "images/cap_america.jpg",
    "https://www.youtube.com/watch?v=6y3oHJnfnjU"  # NOQA
)

# we create a list for pass the movies into open_movies_page
movies = [captain, iron_man, thor, dr_strange, avengers, pantera_negra,
          ant_man, spider_man, g_galaxy]

fresh_tomatoes.open_movies_page(movies)
