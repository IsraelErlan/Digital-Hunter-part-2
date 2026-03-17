from fastapi import APIRouter, HTTPException
from db.sql_queries import Queries
from maps_data.DigitalHunter_map import plot_map_with_geometry

router = APIRouter()

@router.post('/free_query')
def run_sql_query(query: str):
    try:
        result = Queries.run_query(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/low_priority_level')
def get_targets_with_low_priority_and_distance_greater_than_5_km():
    try:
        result = Queries.get_targets_with_low_priority_and_distance_greater_than_5_km()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/count_intelligence_by_signal_type')
def count_intelligence_by_signal_type():
    try:
        result = Queries.count_intelligence_by_signal_type()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/detection_unknown_targets')
def detection_unknown_targets():
    try:
        result = Queries.detection_unknown_targets()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@router.get('/get_targets_with_unusual_activity')
def get_targets_with_unusual_activity():
    try:
        result = Queries.get_targets_with_unusual_activity()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post('/get_line_graph')
def get_line_graph(entity_id: str):
    try:
        result = Queries.get_locations_by_entity_id(entity_id)
        plot_map_with_geometry(result)
        return {"amount of places": len(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

