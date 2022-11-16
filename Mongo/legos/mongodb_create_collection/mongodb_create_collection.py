##
##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
import pprint
from pydantic import BaseModel, Field
from typing import List


class InputSchema(BaseModel):
    database_name: str = Field(
        title='Database Name',
        description='Name of the MongoDB database'
    )
    collection_name: str = Field(
        title='Collection Name',
        description='Name of the MongoDB collection'
    )


def mongodb_create_collection_printer(output):
    if output[0] is None:
        return
    print("\n\n")
    if isinstance(output[0], Exception):
        pprint.pprint("Error : {}".format(output[0]))
    else:
        pprint.pprint("List of all collections after creating new one")
        pprint.pprint(output[0])
        collection_name = output[1]
        if collection_name in output[0]:
            pprint.pprint("Collection created successfully !!!")


def mongodb_create_collection(handle, database_name: str, collection_name: str) -> List:
    """mongodb_create_collection create collection in mongodb.

        :type handle: object
        :param handle: Object returned from task.validate(...).

        :type database_name: str
        :param database_name: Name of the MongoDB database.

        :type collection_name: str
        :param collection_name: Name of the MongoDB collection.

        :rtype: List of all collections after creating new one.
    """
    # Input param validation.

    try:
        db = handle[database_name]
        db.create_collection(collection_name)
        # Verification
        collection_list = db.list_collection_names()
        return [collection_list, collection_name]
    except Exception as e:
        return [e]
