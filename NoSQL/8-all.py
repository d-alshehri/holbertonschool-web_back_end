#!/usr/bin/env python3
"""8-all.py

Contains a function to list all documents in a PyMongo collection.
"""

def list_all(mongo_collection):
    """
    List all documents in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.

    Returns:
        list: List of documents in the collection. Empty list if none.
    """
    return list(mongo_collection.find())
