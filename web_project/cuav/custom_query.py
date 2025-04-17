from django.db import connections

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
class Custom_sql:
   
    def device_count(self):
    
        with connections['cuav'].cursor() as cursor:
            cursor.execute("""
            select v.name as vendor,CASE WHEN LENGTH(md.name)=0  THEN v.name || '_device' ELSE md.name end as device , count(tm.id) as count
            from measuring_device md 
            inner join target_measurement tm 
            on md.id =tm.measuring_device_id 
            inner join vendor v 
            on md.vendor_id =v.id 
            group by v.name ,md.name , md.id """)
            result_list = dictfetchall(cursor)
        return result_list