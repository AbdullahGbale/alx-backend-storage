#!/usr/bin/env python3
'''Task 6 module
'''


def list_all(mongo_collection):
    '''Lists all documents in acollection.
    '''
    return [doc for doc in mongo_collection.find()]
