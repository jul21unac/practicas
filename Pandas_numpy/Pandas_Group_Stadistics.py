from itertools import groupby

import pandas as pd
import numpy as np


if __name__ == "__main__":

    fligths = pd.read_csv("../data_2/T_T100D_MARKET_US_CARRIER_ONLY.csv")

    fligths_count = fligths['UNIQUE_CARRIER_NAME'].value_counts()

    print("---- count fligth by company -----")
    print(fligths_count)

    fligths_cc = fligths.copy()
    fligths_cc['COUNT'] = fligths_cc.groupby(["ORIGIN","UNIQUE_CARRIER_NAME"])["UNIQUE_CARRIER_NAME"].transform('count')


    fligth_sort = fligths_cc.sort_values(by=['UNIQUE_CARRIER_NAME','COUNT', 'ORIGIN'], ascending=[True,False,True])

    fligth_colum = fligth_sort[['UNIQUE_CARRIER_NAME', 'ORIGIN', 'COUNT']]

    fligth_nd            = fligth_colum.drop_duplicates().copy()


    #print(fligth_nd.head(50))
    fligth_nd['Rank_Optimized'] = (
        fligth_nd.groupby('UNIQUE_CARRIER_NAME')['COUNT']
        .rank(method='first', ascending=False)  # 'first' para desempatar por orden de aparición
        .astype(int)  # Convertir a entero
    )

    top_airports_rank = fligth_nd[fligth_nd['Rank_Optimized'] == 1]

    print("---- the bussiest destination by company -----")
    print(top_airports_rank.head(100))

    fligths_jfk = fligths.query('DEST == "JFK"').copy()

    fligths_jfk["count"] = fligths_jfk.groupby(["UNIQUE_CARRIER_NAME"])["UNIQUE_CARRIER_NAME"].transform('count')

    fligths_jfk_column = fligths_jfk[["UNIQUE_CARRIER_NAME","count"]]

    fligths_jfk_column_nd = fligths_jfk_column.drop_duplicates()

    fligths_jfk_column_nd_order = fligths_jfk_column_nd.sort_values(by=['count'], ascending=[False])

    print("----company with the most fligths to JFk  -----")
    print(fligths_jfk_column_nd_order.head(1).to_string())