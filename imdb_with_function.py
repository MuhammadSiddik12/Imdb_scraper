from requests import get            
from bs4 import BeautifulSoup as s  
import json   

def movie_scraping(td,rating1,d,main):     
    for i,j in zip(td,rating1):    
        d["name"]=i.find("a").text  # find the name of movies
        d["year"]=i.find("span").text # find the year when the movie release
        d["position"]=i.text.split("\n")[1].replace(".","").strip() # find the positon and remove the spaces and \n
        d["link"]="https://www.imdb.com"+i.find("a")["href"] # find the link of movie
        d["rating"]=j.find("strong").text # find the rating of movie
        d_copy=d.copy() # copy the dictionary 
        main.append(d_copy)
    with open("imdb.json","w") as imdb: # open the file 
        imdb.write(json.dumps(main,indent=2)) # and dumps the file into json
        imdb.close() # closing the file

def page_info():
    page=get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in") # link of website
    soup=s(page.text,"html.parser")         # convert data into readable format
    body=soup.find("tbody",class_="lister-list") 
    td=body.findAll('td',class_="titleColumn")
    rating1=body.findAll("td",class_="ratingColumn imdbRating")    
    d,main={},[]
    movie_scraping(td,rating1,d,main)
page_info()
