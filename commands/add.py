from datetime import datetime

def add(name: str, reviews: int):
    today = datetime.today() 
    concept = {
               "name": name,
               "date_added": today.strftime("%d-%m-%Y"),
               "reviews": reviews,
               }
    return concept
    

    

