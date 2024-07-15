from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from EMR.mongo_utils import MongoDB
from bson.objectid import ObjectId


def index(request):
    if request.session.get('member_id'):
        return render(request, "patientmeds/index.html")
    else:
        return render(request, "login/index.html")


class Meds(APIView):
    def get(self, request):
        if request.session.get('member_id'):
            db = MongoDB()
            meds_collection = db.get_patients_collection()
            meds = list(meds_collection.find({"user_name": request.session.get('member_id')}))
            return Response(meds, status=status.HTTP_200_OK)
        else:
            return render(request, "login/index.html")

    def post(self, request):
        if request.session.get('member_id'):
            db = MongoDB()
            meds_collection = db.get_patients_collection()
            med_data = {
                "user_name": request.session.get('member_id'),
                "meds_name": request.data.get("meds_name"),
                "meds_strength": request.data.get("meds_strength"),
                "meds_dir": request.data.get("meds_dir"),
                "meds_status": request.data.get("meds_status"),
                "meds_date": request.data.get("meds_date")
            }
            meds_collection.insert_one(med_data)
            meds = list(meds_collection.find({"meds_name": {"$regex": request.data.get("meds_name")}}))
            return Response(meds, status=status.HTTP_201_CREATED)
        else:
            return render(request, "login/index.html")

    def put(self, request, patientmeds_id):
        if request.session.get('member_id'):
            db = MongoDB()
            meds_collection = db.get_patients_collection()
            updated_data = {
                "meds_name": request.data.get("meds_name"),
                "meds_strength": request.data.get("meds_strength"),
                "meds_dir": request.data.get("meds_dir"),
                "meds_status": request.data.get("meds_status"),
                "meds_date": request.data.get("meds_date")
            }
            meds_collection.update_one(
                {"_id": ObjectId(patientmeds_id), "user_name": request.session.get('member_id')},
                {"$set": updated_data}
            )
            return Response(status=status.HTTP_200_OK)
        else:
            return render(request, "login/index.html")

    def delete(self, request, patientmeds_id):
        if request.session.get('member_id'):
            db = MongoDB()
            meds_collection = db.get_patients_collection()
            meds_collection.delete_one({"_id": ObjectId(patientmeds_id), "user_name": request.session.get('member_id')})
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

#
def some_view_function(request):
    db = MongoDB()
    patients_collection = db.get_patients_collection()
    all_patients = list(patients_collection.find({}))

    # Continue with your logic using the data fetched
    return render(request, 'some_template.html', {'patients': all_patients})
