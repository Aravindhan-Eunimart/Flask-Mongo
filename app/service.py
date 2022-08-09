from dbcon import student_collection
from flask import Response
# from bson import ObjectId


def get_single_record(id):
    row = student_collection.find_one({"id": int(id)})
    if row != None:
        del row['_id']
        return dict(row)
    else:
        return Response(status=404)


def get_all_records():
    rows = student_collection.find({})
    result = []
    for row in rows:
        del row['_id']
        result.append(row)
    return result


def create_record(req_data):
    if not isinstance(req_data, list):
        student_collection.insert_one(req_data)
        # student_datas = [req_data]
    else:
        # student_datas = req_data
        student_collection.insert_many(req_data)

    return Response(status=201)


def delete_single_record(id):
    result = student_collection.delete_one({"id": int(id)})
    if result.deleted_count == 1:
        return Response(status=204)
    return Response(status=404)


def delete_all_records():
    student_collection.delete_many({})
    return Response(status=204)
