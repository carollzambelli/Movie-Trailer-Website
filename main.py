import fresh_tomatoes
import media

# This is where instances of the class Movie are defined.
# Please note that storyline is here too, even if it has not been used in this project.

amelie = media.Movie("Amelie",
                        "Amelie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                        "https://youtu.be/sECzJY07oK4")

angry_birds = media.Movie("The Angry Birds Movie",
                        "Find out why the birds are so angry. When an island populated by happy, flightless birds is visited by mysterious green piggies, it's up to three unlikely outcasts - Red, Chuck and Bomb - to figure out what the pigs are up to.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png",
                        "https://youtu.be/QRmKa7vvct4")

big_hero_6 = media.Movie("Big Hero 6",
                        "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                        "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                        "https://youtu.be/8IdMPpKMdcc")

the_darjeeling_limited = media.Movie("The Darjeeling Limited",
                     "A year after their father's funeral, three brothers travel across India by train in an attempt to bond with each other.",
                     "http://upload.wikimedia.org/wikipedia/en/1/1e/Darjeeling_Limited_Poster.jpg",
                     "https://youtu.be/aO1bYukdvLI")

funny_face = media.Movie("Funny Face",
                     "An impromptu fashion shoot at a book store brings about a new fashion model discovery in the shop clerk.",
                     "http://upload.wikimedia.org/wikipedia/en/6/67/Funny_Face_1957.jpg",
                     "https://youtu.be/JMKm-PpD8Aw")

howls_moving_castle = media.Movie("Howl's Moving Castle",
                     "When an unconfident young woman is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking home.",
                     "http://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
                     "https://youtu.be/iwROgK94zcM")

hugo = media.Movie("Hugo",
                        "Set in 1930s Paris, an orphan who lives in the walls of a train station is wrapped up in a mystery involving his late father and an automaton.",
                        "https://upload.wikimedia.org/wikipedia/en/7/73/Hugo_Poster.jpg",
                        "https://youtu.be/hR-kP-olcpM")

inception = media.Movie("Inception",
                     "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                     "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                     "https://youtu.be/8hP9D6kZseM")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "While on a trip to Paris with his fiance's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s every day at midnight.",
                     "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://youtu.be/FAfR8omt-CY")

postmans_white_nights = media.Movie("Postman's White Nights",
                     "The film represents life in a godforsaken Russian village. The only way to reach the mainland is to cross the lake by boat and a postman became the only connection with the outside world.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b4/The_Postman%27s_White_Nights.jpg",
                     "https://youtu.be/qGgC5CkPojk")

ratatouille = media.Movie("Ratatouille",
                     "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://youtu.be/c3sBBRxDAqk")

trois_couleurs_bleu = media.Movie("Trois Couleurs: Bleu",
                     "A woman struggles to find a way to live her life after the death of her husband and child.",
                     "https://upload.wikimedia.org/wikipedia/en/2/2c/Bluevidcov.jpg",
                     "https://youtu.be/Hxu6my_t4pM")

movies = [amelie, angry_birds, big_hero_6, the_darjeeling_limited, funny_face, howls_moving_castle, hugo, inception, midnight_in_paris, postmans_white_nights, ratatouille, trois_couleurs_bleu]

fresh_tomatoes.open_movies_page(movies)
