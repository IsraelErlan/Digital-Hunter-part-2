from .sql_connection import SQL

class Queries:
    

    @classmethod
    def run_query(cls, query: str):
        with SQL.get_cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    @classmethod
    def get_targets_with_low_priority_and_distance_greater_than_5_km(cls):
        query = '''SELECT `entity_id`, `target_name`, `priority_level`, `movement_distance_km`
                    FROM `targets` 
                    WHERE (`priority_level` = 1 OR `priority_level` = 2) 
                    AND `movement_distance_km` > 5'''
        result = cls.run_query(query)
        return result
    
    @classmethod
    def count_intelligence_by_signal_type(cls):
        query = ''' SELECT `signal_type`, COUNT(*) as amount_intelligence_signals
                    FROM `intel_signals` 
                    GROUP BY `signal_type` 
                    ORDER BY COUNT(*) DESC'''
        result = cls.run_query(query)
        return result
    

    @classmethod
    def detection_unknown_targets(cls):
        query = '''
                   SELECT * FROM 
                        (SELECT entity_id 
                         FROM `targets` 
                         WHERE priority_level = 99)  AS t1

                    LEFT JOIN 

                        (SELECT `entity_id`, COUNT(*) as amount
                        FROM `intel_signals` 
                        GROUP BY `entity_id`) AS t2
                    
                    ON t1.entity_id = t2.entity_id

                    ORDER BY amount DESC  
                    LIMIT 3

                    '''
        result = cls.run_query(query)
        return result



    @classmethod
    def get_targets_with_unusual_activity(cls):
        query = ''' 

            SELECT entity_id 
            FROM 
                (SELECT entity_id, SUM(distance_from_last) as sum_distance
                FROM intel_signals 
                WHERE HOUR(timestamp) BETWEEN 8 AND 19
                GROUP BY entity_id 
                HAVING SUM(distance_from_last) = 0) AS t1

                JOIN

                (SELECT entity_id, SUM(distance_from_last) as sum_distance
                FROM intel_signals 
                WHERE HOUR(timestamp) NOT BETWEEN 8 AND 19
                GROUP BY entity_id 
                HAVING SUM(distance_from_last) > 10) AS t2

                ON t1.entity_id = t2.entity_id

        '''
        result = cls.run_query(query)
        return result



    @classmethod
    def get_locations_by_entity_id(cls, entity_id):
        query = ''' SELECT `reported_lat`, `reported_lon`
                    FROM `intel_signals` 
                    WHERE `entity_id` = %s
                    ORDER BY timestamp'''
        with SQL.get_cnx() as cnx: 
            with cnx.cursor() as cursor:
                cursor.execute(query, (entity_id))
                result = cursor.fetchall()
        return result