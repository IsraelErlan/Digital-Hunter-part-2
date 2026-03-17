from sql_connection import SQL

class Queries:
    
    cursor = SQL.get_cursor()

    @classmethod
    def run_query(cls, query: str):
        cls.cursor(query)
        result = cls.cursor.fetchall()
        return result

    @classmethod
    def get_targets_with_low_priority_and_distance_greater_than_5_km(cls):
        query = '''SELECT `entity_id`, `target_name`, `priority_level`
                    FROM `targets` 
                    WHERE (`priority` = 1 OR priority = 2) 
                    AND `movement_distance_km` > 5'''
        result = cls.run_query(query)
        return result
    
    @classmethod
    def count_intelligence_by_signal_type(cls):
        query = ''' SELECT `signal_type`, COUNT(*)
                    FROM `intel_signals` 
                    GROUP BY `signal_type` 
                    ORDER BY COUNT(*) DESC'''
        result = cls.run_query(query)
        return result