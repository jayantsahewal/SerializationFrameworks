# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:23:15 2016

@author: jayantsahewal
"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True)

# Expose needed functions

student_list = {}

def add_student(id, name, address, phone):
    global student_list
    if id in student_list.keys():
        return "Student already exists. Use update_student() to update student info."
    else:
        student_info = {"Name":name, "Address":address, 
                    "Phone":phone}
        student_list[id] = student_info
    return "Added student with id " + str(id)

def display_student(sid):
    global student_list    
    for id, student in student_list.iteritems():
        if id == sid:
            str_id = "Id of the student is: " + str(id)
            str_name = "Name of the student is: " + student["Name"]
            str_address = "Address of the student is: " + student["Address"]
            str_phone = "Phone number of the student is: " + student["Phone"]
            return str_id + "\n" + str_name + "\n" + str_address + "\n" + str_phone
    return "Can't display. Invalid Student id."

def update_student(sid, sinfoType, newValue):
    global student_list    
    for id, student in student_list.iteritems():
        if id == sid:
            for infoType, value in student.iteritems():
                if infoType.lower() == sinfoType.lower():
                    student[infoType] = newValue
                    return str(infoType) + " for student id " + str(id) + " updated to " + str(newValue)
            return "Invalid arguments. Only possible values are name, phone or address"
    return "Can't update. Invalid Student id"

def remove_student(sid):
    global student_list
    for id, student in student_list.iteritems():
        if id == sid:
            student_list.pop(id)
            return "removed student with id " + str(id)
    return "Can't remove student. Invalid student id."
    
#server.register_function(list_contents)
server.register_function(add_student)
server.register_function(display_student)
server.register_function(update_student)
server.register_function(remove_student)

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'