# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:31:09 2016

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

import sys

import avro.ipc as ipc
import avro.protocol as protocol

PROTOCOL = protocol.parse(open("student.avpr").read())

server_addr = ('localhost', 9090)

class UsageError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

if __name__ == '__main__':

    # client code - attach to the server and send a message
    client = ipc.HTTPTransceiver(server_addr[0], server_addr[1])
    requestor = ipc.Requestor(PROTOCOL, client)
    
    # fill in the Message record and send it
    message = dict()
    message['function_name'] = sys.argv[1]
    message['argument1'] = sys.argv[2]
    try:
        message['argument2'] = sys.argv[3]
    except:
        message['argument2'] = ""
    try:
        message['argument3'] = sys.argv[4]
    except:
        message['argument3'] = ""
    try:
        message['argument4'] = sys.argv[5]
    except:
        message['argument4'] = ""

    params = dict()
    params['message'] = message
    print("Result: " + requestor.request('send', params))

    # cleanup
    client.close()