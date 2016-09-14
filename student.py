# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:23:24 2016

@author: jayantsahewal
"""

'''
Student information will be stored in a dictionary. In this dictionary each 
key will correspond to student id. And, value will again be a dictionary 
containing student name, address and phone number. For example:
Student = {123:{Name: "Jayant Sahewal", 
Address: "111 St, abc City, xyz State - 11111", Phone: "123-456-7890"}}
'''
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
            return "Invalid arguments. only possible values are name, phone or address"
    return "Can't update. Invalid Student id"

def remove_student(sid):
    global student_list
    for id, student in student_list.iteritems():
        if id == sid:
            student_list.pop(id)
            return "removed student with id " + str(id)
    return "Can't remove student. Invalid student id."

def main():
    print add_student(100,"Abc Def","111 St, abc City, pq State - 11111", "100-456-7890")
    print add_student(101,"Ghi Jkl","222 St, def City, rs State - 22222", "101-457-7891")
    print add_student(102,"Mno Pqr","333 St, ghi City, tu State - 33333", "102-458-7892")
    print add_student(103,"Stu Vwx","444 St, jkl City, vw State - 44444", "103-459-7893")
    print add_student(104,"Yza Bcd","555 St, mno City, xy State - 55555", "104-460-7894")
    print display_student(102)
    print display_student(103)
    print update_student(104, "phone", "204-456-7890")
    print display_student(104)    
    print remove_student(104)
    print display_student(104)
    print add_student(100,"Abc Def","111 St, abc City, pq State - 11111", "100-456-7890")
    print add_student(101,"Ghi Jkl","222 St, def City, rs State - 22222", "101-457-7891")
    print add_student(102,"Mno Pqr","333 St, ghi City, tu State - 33333", "102-458-7892")
    print add_student(103,"Stu Vwx","444 St, jkl City, vw State - 44444", "103-459-7893")
    print add_student(104,"Yza Bcd","555 St, mno City, xy State - 55555", "104-460-7894")    

if __name__ == "__main__":
    main()
    