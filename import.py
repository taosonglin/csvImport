import pymysql
from tools import *

if __name__ == '__main__':

    """
	below two params must be set by user
	param:table_names       table name you want to create.
    param:input             the path of csv file.
    
    """
    input={}
    table_names = ['TSO','EPS','Cap_Change','Dividend','INDEX_EOD','SSE_EQ_EOD','SZSE_EQ_EOD']
    input['TSO']=['./Files/SSE_TSO_20191112.csv','./Files/SZSE_TSO_20191112.csv']
    input['EPS']=['./Files/SSE_EPS_20191009.csv','./Files/SZSE_EPS_20191009.csv']
    input['Cap_Change']=['./Files/SSE_Cap_Change_Aug_30_2019.csv','./Files/SZSE_Cap_Change_Aug_30_2019.csv']
    input['Dividend']=['./Files/SSE_Dividend_Aug_30_2019.csv','./Files/SZSE_Dividend_Aug_30_2019.csv']
    input['INDEX_EOD']=['./Files/CSI_2019010120190831.csv']
    input['SSE_EQ_EOD']=['./Files/SSE_2019010120190802_Include_Delisted.csv']
    input['SZSE_EQ_EOD']=['./Files/SZSE_2019010120190802_Include_Delisted.csv']

    primary_keys = {}
    sql_head = {}
    for name in table_names:
        primary_keys[name] = name + '_ID'
        fields_format = make_fields_format(input[name][0])
        sql_head[name] = 'insert into %s values ' % name + fields_format

    # create table
    conn = pymysql.connect("localhost", "root", "dld2019!", "deeplense", charset='utf8')
    cur = conn.cursor()
    for name in table_names:
        ddl_sql = make_create_table_sql(input[name][0], name, primary_keys[name])
        cur.execute(ddl_sql)
    conn.commit()

    # insert from csv file to mysql
    start = now()
    insert_count = 0
    for name in table_names:
        print("insert to %s....." % name)
        sql = sql_head[name]
        fields = get_csv_title(input[name][0])
        pk=0
        for file in input[name]:
            values,pk = make_insert_sql(fields, file,pk)
            cur.executemany(sql, values)
            print("import csv finished:\t%s" % file)

    conn.commit()
    conn.close()
    end = now()
    print ("start:%s\n"%start, "end:%s"%end)
