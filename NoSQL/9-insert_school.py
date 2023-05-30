#!/usr/bin/env python3
""" Python function that inserts a new document in a collection based on kwargs:"""


def insert_school(mongo_collection, **kwargs):
    """insert a new document in a collection based on"""
    new_document = mongo_collection.insert_one(
        kwargs)  # retrive the new document
    return new_document.inserted_id  # new document id
