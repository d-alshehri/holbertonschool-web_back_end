#!/usr/bin/env python3
"""9-insert_school.py

Contains a function to insert a new document into a PyMongo collection.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        **kwargs: Key-value pairs to insert as a document.

    Returns:
        ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
