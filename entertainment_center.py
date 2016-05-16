import fresh_tomatoes  # module generates HTML to display trailer info
import media

# Define movies shown in HTML with Title, Desc, Poster Image, and Trailer

toy_story = media.Movie(
    "Toy Story",
    "Kids finds toys come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

avatar = media.Movie(
    "Avatar",
    "Marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=uZNHIU3uHT4"
    )

jurassic_park = media.Movie(
    "Jurassic Park",
    "Dinosaurs come to life",
    "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
    "https://www.youtube.com/watch?v=lc0UehYemQA"
    )

lost_ark = media.Movie(
    "Raiders of the Lost Ark",
    "College professor finds lost historical artifacts",
    "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",  # NOQA
    "https://www.youtube.com/watch?v=HqOSLZl9GUo"
    )

star_wars = media.Movie(
    "Star Wars: The Force Awakens",
    "Human fight each other in space",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=sGbxmsDFVnE"
    )

star_trek = media.Movie(
    "Star Trek: Into Darkness",
    "Humans explore space",
    "https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=r5gdbUC9mWU"
    )

# Load movie instances into an array
movies = [avatar, toy_story, jurassic_park, lost_ark, star_wars, star_trek]

# Load module to create dynamic HTML file
fresh_tomatoes.open_movies_page(movies)
