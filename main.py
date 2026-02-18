
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class User(BaseModel): #this class is called Data Model
    name : str
    age : int
    interest : List[str]

class UserResponse(BaseModel):
    message : str
    user :User
    recommandations : List[str]

@app.post("/recommend", response_model=UserResponse)
def recommend_items(user: User):
    '''
    Example: POST /recommend
    {
        "name": "Guna",
        "age": 30,
        "interest": ["music", "sports"]
    }
    '''
    first_interest = user.interest[0] if user.interest else "general"
    recommendations = []
    if first_interest.lower() == "music":
        recommendations = ["Spotify Playlist", "Apple Music", "YouTube Music", "concert tickets"] 
    elif first_interest.lower() == "sports":
        recommendations = ["Nike Shoes", "Adidas Apparel", "Sports Equipment", "Fitness Tracker", "Gym Membership","Running Shoes"]
    elif first_interest.lower() == "books":
        recommendations = ["Fiction Novels", "Non-fiction Books", "E-books", "Audiobooks", "Bookstore Gift Card"]
    else: 
        recommendations = ["Gift Card", "Subscription Box", "Experience Gift", "Personalized Item"]    

  
    
    return UserResponse(
        message=f"Hello {user.name}, based on your interest in {first_interest}, we recommend the following items.",
        user=user,
        recommandations=recommendations
    )