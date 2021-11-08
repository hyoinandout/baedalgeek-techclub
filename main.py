# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pymongo import MongoClient
from pymongo.cursor import CursorType


def inserted_item_one(mongo, data, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_one(data).inserted_id
    return result

def find_item(mongo,condition=None,db_name=None,collection_name=None):
    result = mongo[db_name][collection_name].find(condition, {"_id":False}, no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)
    return result

def delete_item_one(mongo,condition=None,db_name=None,collection_name=None):
    result = mongo[db_name][collection_name].delete_one(condition)
    return result

def delete_item_many(mongo,condition=None,db_name=None,collection_name=None):
    result = mongo[db_name][collection_name].delete_many(condition)
    return result

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    host = "localhost"
    port = "27017"
    mongo = MongoClient(host, int(port))
    print(mongo)
    s = dict()
    s["user"] = input()
    s["age"] = int(input())
    inserted_item_one(mongo, s, "baedalgeek_test", "User")
    cursor = find_item(mongo,None,"baedalgeek_test","User")
    for list in cursor:
        print(list["user"])
        print(list["age"])
    #delete_item_many(mongo,{},"baedalgeek_test","User")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
