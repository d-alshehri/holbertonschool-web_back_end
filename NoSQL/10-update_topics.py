#!/usr/bin/env python3
"""10-update_topics.py

Contains a function to update the topics of a school document by name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on its name.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        name (str): The name of the school document to update.
        topics (list of str): List of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
