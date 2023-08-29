from fastapi import APIRouter,HTTPException
from controller.google_map import getAdventure, getShop, getVisit, concatenateAllDF, getTypeByPlace
from controller.recommendation import recommend_places
import pandas as pd


place = APIRouter()

@place.get('/places/{location_map}')
async def get_all_places(location_map: str):
    try:
        adventure_data = await getAdventure(location_map)
        visit_data = await getVisit(location_map)
        shop_data = await getShop(location_map)
        # Concatenate dataframes
        combined_data = pd.concat([adventure_data, visit_data, shop_data], axis=0)
        
        return combined_data.to_dict('records')
    except Exception as e:
        print("error :", str(e))
        return {"error": str(e)}

@place.get('/place-adv/{location_map}')
async def get_adv_places(location_map: str):
    try:
        adventure_data = await getAdventure(location_map)
        return adventure_data.to_dict('records')
    except Exception as e:
        print("error :", str(e))
        return {"error": str(e)}

@place.get('/place-shop/{location_map}')
async def get_adv_places(location_map: str):
    try:
        shop_data = await getShop(location_map)
        return shop_data.to_dict('records')
    except Exception as e:
        print("error :", str(e))
        return {"error": str(e)}
    
@place.get('/place-visit/{location_map}')
async def get_adv_places(location_map: str):
    try:
        visit_data = await getVisit(location_map)
        return visit_data.to_dict('records')
    except Exception as e:
        print("error :", str(e))
        return {"error": str(e)}
    
@place.get('/recommend/{location_map}')
async def get_recommend(location_map: str, query: str):
    try:
        res = concatenateAllDF()
        csv_file_path = "all_data.csv"
        target_type =  await getTypeByPlace(location_map, query)
        recommended_places = recommend_places(csv_file_path, target_type)
        return recommended_places
    except Exception as e:
        print("error :", str(e))
        return {"error": str(e)}
    
    