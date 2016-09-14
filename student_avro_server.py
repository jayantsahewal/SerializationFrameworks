# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:10:45 2016

@author: jayantsahewal
"""

#!/usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import avro.ipc as ipc
import avro.protocol as protocol
import avro.schema as schema

PROTOCOL = protocol.parse(open("student.avpr").read())

student_list = {}

def add_student(id, name, address, phone):
    print "received request to add a student."
    global student_list
    if id in student_list.keys():
        return "Student already exists. Use update_student() to update student info."
    else:
        student_info = {"Name":name, "Address":address, 
                    "Phone":phone}
        student_list[id] = student_info
    return "Added student with id " + str(id)

def display_student(sid):
    print "received request to display student information."
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
    print "received request to update student information."
    global student_list    
    for id, student in student_list.iteritems():
        if id == sid:
            for infoType, value in student.iteritems():
                if infoType.lower() == sinfoType.lower():
                    student[infoType] = newValue
                    return str(infoType) + " for student id " + str(id) + " updated to " + str(newValue)
            return "Invalid arguments. Only possible values are name, phone or address."
    return "Can't update. Invalid Student id"

def remove_student(sid):
    print "received request to remove student."
    global student_list
    for id, student in student_list.iteritems():
        if id == sid:
            student_list.pop(id)
            return "removed student with id " + str(id)
    return "Can't remove student. Invalid student id."

class MailResponder(ipc.Responder):
    def __init__(self):
        ipc.Responder.__init__(self, PROTOCOL)

    def invoke(self, msg, req):
        if msg.name == 'send':
            message = req['message']
            func_name = message['function_name']
            arg1 = message['argument1']
            arg2 = message['argument2']
            arg3 = message['argument3']
            arg4 = message['argument4']
            if func_name.lower() == "add_student":
                return add_student(arg1, arg2, arg3, arg4)
            elif func_name.lower() == "display_student":
                return display_student(arg1)
            elif func_name.lower() == "update_student":
                return update_student(arg1, arg2, arg3)
            elif func_name.lower() == "remove_student":
                return remove_student(arg1)
            else:
                return "invalid function"
        else:
            raise schema.AvroException("unexpected message:", msg.getname())

class MailHandler(BaseHTTPRequestHandler):
  def do_POST(self):
    self.responder = MailResponder()
    call_request_reader = ipc.FramedReader(self.rfile)
    call_request = call_request_reader.read_framed_message()
    resp_body = self.responder.respond(call_request)
    self.send_response(200)
    self.send_header('Content-Type', 'avro/binary')
    self.end_headers()
    resp_writer = ipc.FramedWriter(self.wfile)
    resp_writer.write_framed_message(resp_body)

server_addr = ('localhost', 9090)

if __name__ == '__main__':
    server = HTTPServer(server_addr, MailHandler)
    server.allow_reuse_address = True
    try:
        print 'Use Control-C to exit'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Exiting'