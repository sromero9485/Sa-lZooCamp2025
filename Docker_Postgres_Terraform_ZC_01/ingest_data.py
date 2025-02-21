#!/usr/bin/env python
# coding: utf-8
import os 
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse



def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
     

    csv_name = 'output.csv'
   
    os.system(f"wget {url} -o {csv_name}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    df_iter = pd.read_csv(csv_name, iterator = True, chunksize = 80000)

    df = next(df_iter)

    df.tpep_pickup_datetime= pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime= pd.to_datetime(df.tpep_dropoff_datetime)
    df.fare_amount= pd.to_numeric(df.fare_amount)
    df.trip_distance= pd.to_numeric(df.trip_distance)
    df.extra= pd.to_numeric(df.extra)
    df.mta_tax= pd.to_numeric(df.mta_tax)
    df.tip_amount= pd.to_numeric(df.tip_amount)
    df.tolls_amount= pd.to_numeric(df.tolls_amount)
    df.improvement_surcharge= pd.to_numeric(df.improvement_surcharge)
    df.total_amount= pd.to_numeric(df.total_amount)
    df.congestion_surcharge= pd.to_numeric(df.congestion_surcharge)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")


    df.to_sql(name=table_name, com=engine, if_exists='append')

    while True:
        t_start=time()
        df = next(df_iter) 
        df.tpep_pickup_datetime= pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime= pd.to_datetime(df.tpep_dropoff_datetime)
        df.fare_amount= pd.to_numeric(df.fare_amount)
        df.trip_distance= pd.to_numeric(df.trip_distance)
        df.extra= pd.to_numeric(df.extra)
        df.mta_tax= pd.to_numeric(df.mta_tax)
        df.tip_amount= pd.to_numeric(df.tip_amount)
        df.tolls_amount= pd.to_numeric(df.tolls_amount)
        df.improvement_surcharge= pd.to_numeric(df.improvement_surcharge)
        df.total_amount= pd.to_numeric(df.total_amount)
        df.congestion_surcharge= pd.to_numeric(df.congestion_surcharge)

        df.to_sql(name="yello_taxi_data", con=engine, if_exists="append")
        t_end=time()

        print("inserted anothe chunk... took %.2f second" % (t_end-t_start))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                        prog='DataIngestion',
                        description='Ingest CSV data to Postgres')
    # user, password, host, port, database, tablename, csv path

    parser.add_argument('--user', help= 'user name0')           
    parser.add_argument('--password', help='password')   
    parser.add_argument('--host', help='host')
    parser.add_argument('--db', help='database')
    parser.add_argument('--port', help='port')
    parser.add_argument('--table_name', help='table name')
    parser.add_argument('--url', help='csv path')

    args = parser.parse_args()

    main(args)

