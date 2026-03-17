from fastapi import APIRouter, HTTPException
from db.sql_queries import Queries

router = APIRouter()

@router.get('/high_priority_targets')
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


