import sqlite3
import requests


apiV3 = '5b8d80b80e618bfd8c5231c61e467b5b'

apiV4 = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YjhkODBiODBlNjE4YmZkOGM1MjMxYzYxZTQ2N2I1YiIsInN1YiI6IjVmMjNkMTJiMzUwMzk4MDAzNGU4ZjhjYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UKM2eCYlo3fU7bVfy-srHpTaFTif9VWAub3SiAxx5zo'

url = 'https://api.themoviedb.org/3'

type = '/movie/popular'

total_movie_list = []


for page_number in range(1,2):

    params = {'api_key': apiV3, 'language':"ko-KR", 'page':page_number}
    URL = url + type
    res = requests.get(URL, params=params)
    movie_list = res.json()['results']
    total_movie_list += movie_list


print(len(total_movie_list))

      



con = sqlite3.connect('db.sqlite3')
cur = con.cursor()


for movie in total_movie_list:
  # cur.execute('''INSERT INTO movies_movie (adult, id, original_language, original_title, overview, popularity, poster_path, release_date, title, video, vote_average, vote_count) VALUES (?, ?, ?, ? , ?, ? ,? , ? , ?, ? , ? , ?)''', (movie["adult"], movie["id"], movie["original_language"], movie["original_title"], movie["overview"], movie["popularity"], movie["poster_path"], movie["release_date"], movie["title"], movie["video"], movie["vote_average"], movie["vote_count"]))
  for genre in movie['genre_ids']:
        cur.execute('''INSERT INTO movies_movie_genre_ids (movie_id, genre_id) VALUES(?, ?)''',(movie['id'], genre))

con.commit()
con.close()

