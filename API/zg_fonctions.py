from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from math import sqrt

def get_engine(): 
    # Creation du moteur de requètes
    
    engine_uri = URL.create(
        drivername="postgresql",
        username="postgres",
        password="root",
        host="localhost",
        database="SAE",
        port="5432"
    )

    engine = create_engine(engine_uri)
    return engine

def ind(note):
    # Renvoi de l'indice de désirabilité    
    
    return (note**2.7)/(10**2.7)

def dis(x1, y1, x2, y2):
    #Calcul des distances

    xd = x2 - x1
    yd = y2 - y1 

    return sqrt((xd**2)+(yd**2))
