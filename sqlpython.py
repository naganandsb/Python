# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 08:04:56 2021

@author: DELL
"""

import sqlite3 as sq


con = sq.Connection("nag.db")
crs = con.cursor()
crs.execute("""Create table nag1(sr_no integer, name varchar(200) )""")
con.commit()