#!/usr/bin/env python3
"""11-schools_by_topic.py

Contains a function to return schools having a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: List of documents (schools) containing the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
