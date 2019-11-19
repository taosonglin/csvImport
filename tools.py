import re
import csv
import time
from information import *


def get_csv_title(csvfile):
    """
    input:    csvfile path
    output:   title form of mysql table
    """
    with open(csvfile, 'r')as f:
        reader = csv.reader(f)
        for each in reader:
            if True:
                field_list = each
                break
    return field_list


def transform_date(date):
    """
    input a date like xx/xx/xxxx form,
    this func will transform it to xxxx-xx-xx
    """
    if date == '':
        date = None
    else:
        ret = date.split('/')
        date = ret[2] + '-' + ret[0] + '-' + ret[1]
    return date


def transform_decimal(num):
    """
    transform  csv float number to mysql decimal type
    """
    if num == '':
        return None
    if len(re.findall(r'^\..*', num)) != 0:
        num = '0' + num
    num_str = num.replace(',', '')
    return num_str


def transform_int(num):
    """
    transfrom csv int number to mysql int number

    """
    if num == '':
        return None
    num_str = num.replace(',', '')
    return int(num_str)


def make_create_table_sql(csvfile, table_name, primary_key):
    """
    intput csv file path,return the sql sentence to create table for it

    """
    field_list = get_csv_title(csvfile)
    sql_head = 'create table if not exists `{0}` (`{1}` INT(10),'.format(table_name, primary_key)
    sql_tail = 'primary key (`%s`))engine=innodb default charset=utf8;' % primary_key
    sql_mid = ''
    for field in field_list:
        if field in corax_fields:
            sql_mid += '`'+field+'`'+' '+ corax_field_dic[field] + ','

    return sql_head + sql_mid + sql_tail


def handle_line(line, fields):
    """
    modify line's value by marked_index of field_list
    """
    num = len(fields)
    for index in range(num):
        type = corax_field_dic[fields[index]]
        if type == 'DATE':
            line[index] = transform_date(line[index])
            continue
        if type in INT_TYPES:
            line[index] = transform_int(line[index])
            continue
        if type in DECIMAL_TYPES:
            line[index] = transform_decimal(line[index])
            continue
        if line[index] == None:
            continue
        if line[index] == '':
            line[index] = None

    return line


def make_insert_sql(fields, csvfile, start_pk_value=0):
    """
     return insert sql sentence of the table create by input csvfile
    """
    sqls = []
    f = open(csvfile, 'r')
    lines = csv.reader(f)
    pk = start_pk_value

    for line in lines:
        if line[0] == fields[0]:
            continue
        line = handle_line(line, fields)
        vals = (str(pk),)
        for item in line:
            val = (item,)
            vals += val
        sqls.append(vals)
        pk += 1
    f.close()
    return sqls, pk

def handle_configPath(configPath):
    """
    Return config by input configPath
    """
    with open(configPath, 'r')as f:
        text = f.readlines()
    config = {}
    for line in text:
        line = line.strip('\n')
        ret = line.split('=')
        config[ret[0]] = ret[1]
    return config

def now():
    """
       Return time
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

def make_fields_format(file):
    fields = get_csv_title(file)
    base = "(%s"
    for field in fields:
        base += ",%s"
    base += ");"
    return base


