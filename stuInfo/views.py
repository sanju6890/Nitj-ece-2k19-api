from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# @api_view(['GET'])
# def get_all_info(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)
#     return Response({'status':200, 'payload':serializer.data})

# @api_view(['GET'])
# def get_one_info(request, roll_no):
#     try:
#         student_obj =Student.objects.get(roll_no=roll_no)
#         serializer = StudentSerializer(student_obj)
#         return Response({'status':200, 'payload':serializer.data})
#     except Exception as e:
#         return Response({'status':500, 'message': "Given Roll No. does not exist..."})

# @api_view(['POST'])
# def post_info(request):
#     serializer=StudentSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         # print(serializer.data)
#         return Response({'status':200, 'payload':serializer.data, 'message': "Data Sent Successfully!!"})
#     else:
#         # print(serializer.errors)
#         return Response({'status':403, 'errors':serializer.errors, 'message': "Something went wrong!!"})

# @api_view(['PATCH'])
# def patch_info(request, id):
#     try:
#         student_obj =Student.objects.get(id=id)
#         serializer=StudentSerializer(student_obj, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             # print(serializer.data)
#             return Response({'status':200, 'payload':serializer.data, 'message': "Data Sent Successfully!!"})
#         else:
#             # print(serializer.errors)
#             return Response({'status':403, 'errors':serializer.errors, 'message': "Something went wrong!!"})
#     except Exception as e:
#         return Response({'status':500, 'message': "Invalid ID..."})

# @api_view(['DELETE'])
# def delete_info(request, id):
#     try:
#         student_obj=Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':200, 'message': "Data deleted Successfully!!"})
#     except Exception as e:
#         return Response({'status':500, 'message': "Invalid ID..."})
