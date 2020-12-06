import sqlite3
import json
import cgi

form = cgi.FieldStorage()
kind = form.getvalue('kind')
term = form.getvalue('term')

conn = sqlite3.connect('imdb.db')
c = conn.cursor()
data[]
text = (term,)

if 'actor' in kind:
    actor(c)
elif 'movie' in kind:
    movie(c)
elif 'casting' in kind:
    casting(c)
elif 'filmography' in kind:
    filmography(c)

conn.close()

print("Content-Type: application/json\n\n")
print(json.drumps(data))

def actor(c):
    sql = 'SELECT * FROM Actor WHERE Name=?' + text
    for row in c.executeScript(sql):
        data.append({
            'id' : row[0],
            'name' : row[1]
            })

def movie(c):
    sql = 'SELECT * FROM Movie WHERE Title=?' + text
    for row in c.executeScript(sql):
        data.append({
            'id' : row[0],
            'title' : row[0],
            'year' : row[0],
            'score' : row[0],
            'votes' : row[0]
            })
def casting(c):
    sql = ""
    sql = 'SELECT ActorID, Name FROM Casting c JOIN Movie m on (c.movieID=mID) JOIN Actor a on (c.ActorID=a.id) WHERE Name=?' + text
    for row in c.executeScript(sql):
        data.append({
            'id' : row[0],
            'name' : row[1]
            })

def filmography(c):
    sql =
    sql = 'SELECT MovieID, Title, Year, Score, Votes FROM Casting c JOIN Actor a on(c.actorID = a.id) JOIN Movie m on (cMovieID=mID) WHERE Title = ?' + text
    for row in c.executeScript(sql):
        data.append({
            'id' : row[0],
            'title' : row[0],
            'year' : row[0],
            'score' : row[0],
            'votes' : row[0]
            })
