#!/usr/bin/env python


# splits the string in the required form 
def splitter(data):
    obj = {}
    for i in data.split('/'):
        obj[i.split(':')[0]] = i.split(':')[1]
    return obj

# joins the string from the regular form
def joiner(data):
    return '/'.join([i+':'+data[i] for i in data])

def check_modes(accept,reject, mode):
    return mode in accept and mode not in reject 
