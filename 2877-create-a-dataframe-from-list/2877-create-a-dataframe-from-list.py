import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    #create table
    return pd.DataFrame(student_data,columns=['student_id','age'])
    