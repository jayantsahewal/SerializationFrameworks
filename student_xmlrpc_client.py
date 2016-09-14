# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:27:37 2016

@author: jayantsahewal
"""

import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=True)
#print proxy.list_contents('/tmp')
print proxy.add_student(100,"Abc Def","111 St, abc City, pq State - 11111", "100-456-7890")
print proxy.add_student(101,"Ghi Jkl","222 St, def City, rs State - 22222", "101-457-7891")
print proxy.add_student(102,"Mno Pqr","333 St, ghi City, tu State - 33333", "102-458-7892")
print proxy.add_student(103,"Stu Vwx","444 St, jkl City, vw State - 44444", "103-459-7893")
print proxy.add_student(104,"Yza Bcd","555 St, mno City, xy State - 55555", "104-460-7894")
print proxy.display_student(101)
print proxy.display_student(102)
print proxy.update_student(104, "phone", "204-456-7890")
print proxy.display_student(104)
print proxy.remove_student(104)
print proxy.display_student(104)
print proxy.add_student(100,"Abc Def","111 St, abc City, pq State - 11111", "100-456-7890")
print proxy.add_student(101,"Ghi Jkl","222 St, def City, rs State - 22222", "101-457-7891")
print proxy.add_student(102,"Mno Pqr","333 St, ghi City, tu State - 33333", "102-458-7892")
print proxy.add_student(103,"Stu Vwx","444 St, jkl City, vw State - 44444", "103-459-7893")
print proxy.add_student(104,"Yza Bcd","555 St, mno City, xy State - 55555", "104-460-7894") 
#proxy.display_student(100)