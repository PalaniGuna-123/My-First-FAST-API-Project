
from fastapi import FastAPI

app = FastAPI()
@app.get("/recommend")
def recommend_items(age:int , interest:str):
    '''
    Example: GET /recommend?age=25&interest=technology
    '''
    if age < 18:
        category="Teenagers"
    elif age < 40:
        category="Adults"
    else:
        category="Seniors"

    recommendations =[]
    if interest.lower()=="music":
        recommendations =["Spotify Playlist", "Apple Music", "YouTube Music", "concert tickets"]
    elif interest.lower()=="Sports":
        recommendations =["Nike Shoes", "Adidas Apparel", "Sports Equipment", "Fitness Tracker", "Gym Membership","Running Shoes"]
    elif interest.lower()=="books":
        recommendations =["Fiction Novels", "Non-fiction Books", "E-books", "Audiobooks", "Bookstore Gift Card"]
    else:
        recommendations=["Gift Card", "Subscription Box", "Experience Gift", "Personalized Item"]
    return {"category": category, "recommendations": recommendations}
    
    