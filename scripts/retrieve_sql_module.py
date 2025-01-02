import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

def get_connection():
    conn = psycopg2.connect(
        dbname="statcast",
        user="postgres",
        password="jamin",
        host="localhost",
        port="5432"
    )
    return conn

def get_pbp_data(years, batted_ball = 0):
    conn = get_connection()
    def query_year(year):
        if batted_ball == 1:
                query = f"""
                SELECT * FROM statcast_all
                WHERE hc_x IS NOT NULL AND
                      hc_y IS NOT NULL AND
                      launch_angle IS NOT NULL AND
                      launch_speed IS NOT NULL AND
                      game_year = {year};
                      """
        else:
            query = f"""
                SELECT * FROM statcast_all
                WHERE game_year = {year};
                """
        return pd.read_sql(query, conn)
        
    pbp_data_list = [query_year(year) for year in years]
        
    pbp_data = pd.concat(pbp_data_list, ignore_index=True)
        
    return pbp_data

def upload_to_sql(data_frame, table_name):
     engine = create_engine('postgresql://postgres:jamin@localhost:5432/statcast')

     data_frame.to_sql(
          table_name,
          engine,
          if_exists='replace',
          index=False
     )
     print(f"DataFrame {data_frame} uploaded successfully to table: {table_name}")

conn = get_connection()
years = list(range(2021,2025))
pbp_data = get_pbp_data(years, 0)
