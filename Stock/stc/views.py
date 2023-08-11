import logging
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from stc.models import depot, document, master_data, movement, region, region_auth, user_details, user_level, users
from .serializers import MyTokenObtainPairSerializer, documentSerializer, master_dataSerializer, movementSerializer, qrSerializer, region_authSerializer, regionSerializer, user_detailsSerializer, user_levelSerializer, usersSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from stc.serializers import depotSerializer

from stc import serializers

# Create your views here.

# Users


class UsersDetail(generics.ListCreateAPIView):
    serializer_class = usersSerializer
    queryset = users.objects.all()
    pagination_class = LimitOffsetPagination


class UsersList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = usersSerializer
    queryset = users.objects.all()

# UserLevel


class UserLevelDetail(generics.ListCreateAPIView):
    serializer_class = user_levelSerializer
    queryset = user_level.objects.all()
    pagination_class = LimitOffsetPagination


class UserLevelList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = user_levelSerializer
    queryset = user_level.objects.all()

# Region


class RegionDetail(generics.ListCreateAPIView):
    serializer_class = regionSerializer
    queryset = region.objects.all()
    pagination_class = LimitOffsetPagination


class RegionList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = regionSerializer
    queryset = region.objects.all()

# Depot


class DepotDetail(generics.ListCreateAPIView):
    serializer_class = depotSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        querySet = depot.objects.all()
        region_id = self.request.query_params.get('region')

        if region_id is not None:
            querySet = querySet.filter(region_id=region_id)
            if not querySet:
                raise serializers.ValidationError(
                    {"authorize": "No Records Found."})
        return querySet


class DepotList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = depotSerializer
    queryset = depot.objects.all()

# Region_auth


class Region_auth_Detail(generics.ListCreateAPIView):
    serializer_class = region_authSerializer
    queryset = region_auth.objects.all()
    pagination_class = LimitOffsetPagination


class Region_auth_List(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = region_authSerializer
    queryset = region_auth.objects.all()

# User_details


class User_details_Detail(generics.ListCreateAPIView):
    serializer_class = user_detailsSerializer
    queryset = user_details.objects.all()
    pagination_class = LimitOffsetPagination


class User_details_List(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = user_detailsSerializer
    queryset = user_details.objects.all()

# master_data


class master_dataDetail(generics.ListCreateAPIView):
    serializer_class = master_dataSerializer
    queryset = master_data.objects.all()
    pagination_class = LimitOffsetPagination


class master_dataList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = master_dataSerializer
    queryset = master_data.objects.all()

# document


class documentDetail(generics.ListCreateAPIView):
    serializer_class = documentSerializer
    queryset = document.objects.all()
    pagination_class = LimitOffsetPagination


class documentList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = documentSerializer
    queryset = document.objects.all()

# movement


class movementDetail(generics.ListCreateAPIView):
    serializer_class = movementSerializer
    queryset = movement.objects.all()
    pagination_class = LimitOffsetPagination


class movementList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = movementSerializer
    queryset = movement.objects.all()
    
# qr 
class qrDetail(generics.ListCreateAPIView):
    serializer_class = qrSerializer
    queryset = master_data.objects.all()
    pagination_class = LimitOffsetPagination

class qrList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = qrSerializer
    queryset = master_data.objects.all()




# QR Checking function
class QRconditionView(APIView):
    def get(self, request,input_number):
        # Get the input number from the frontend
        # global input_number 
        try:
            #  input_number = int(input('enter visible material number :- '))
             input_number = int(input_number)
        except Exception as e:
            # Handle exceptions and return an appropriate response
            error_data = {'error': str(e)}
            return JsonResponse(error_data, status=500)  
                
        # input_number = int(46)
        
        queryset = master_data.objects.all()
        serializer = master_dataSerializer(queryset, many=True)
        data = serializer.data
        index = 0
        try:
            while index < len(data):
                if input_number == int(data[index].get('visible_material_no')):
                    try:
            
                        if data[index].get('material_no') is not None:
                            try:
                                if data[index].get('active') == 1:
                                    # new_qr_id = input('Enter new QR Code (integer) :- ')
                                    if data[index].get('qr_id') == "":
        # lastely added 8/8
                                     #======Call this API===========  path('masterData/<int:pk>/', master_dataList.as_view()),=========================
                                       
                                        return Response({"visible_material_no ":data[index].get('visible_material_no'),
                                                        "material_no": data[index].get('material_no'),
                                                        "active(1) or not(2) ":data[index].get('active'),
                                                        "index is ":index,
                                                        "available ":True,
                                                        # "QR ID ":data[index].get('qr_id'),
                                                        "use this URL to update the qr_id":"path('masterData/<int:pk> or material_no/', master_dataList.as_view())"})   
                                        
                                    else:
                                        return Response({"visible_material_no ":data[index].get('visible_material_no'),
                                                        "material_no": data[index].get('material_no'),
                                                        "active(1) or not(2) ":data[index].get('active') ,
                                                        "index is ":index ,
                                                        "available ":False,
                                                        "Comment":' qr_id is already there'
                                                        # "QR ID ":new_qr_id +' qr_id is already there'
                                                        })
                                        # logging.warning('qr_id is already there')
                                        # break
                                else:
                                    return Response({"visible_material_no ":data[index].get('visible_material_no'),
                                                    "material_no": data[index].get('material_no'),
                                                    "active(1) or notactive(2 any num) ": data[index].get('active') ,
                                                    "index is ":index })
                                    # logging.warning('active state is not (1) material number is out of stock')
                                    # break
                                # return Response({"visible_material_no ":data[index].get('visible_material_no'), "index is ":index, "available ":True})  
                            except Exception as e:
                                # Handle exceptions and return an appropriate response
                                error_data = {'error': str(e)}
                                return JsonResponse(error_data, status=500)  # Use an appropriate status code
                            
                        else:
                            return Response({"visible_material_no ":False})
                            # print('material_no is not there')
                            # break    
                        
                    except Exception as e:
                        # Handle exceptions and return an appropriate response
                        error_data = {'error': str(e)}
                        return JsonResponse(error_data, status=500)  # Use an appropriate status code
                    
                else:  
                    
                    index += 1
            return Response({"visible_material_no ":False})
            
        except Exception as e:
            # Handle exceptions and return an appropriate response
            error_data = {'error': str(e)}
            return JsonResponse(error_data, status=500)  
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        # return Response(data[2])
        
# ==========================================================================================
        # if input_number is not None:
        #     try:
        #         queryset = master_data.objects.all()
        #         serializer = master_dataSerializer(queryset, many=True)
        #         data = serializer.data
        #         data_length = len(data)  # Get the length of the data array using len()
        #         result_list = []
        #         index = 0
        #         # return Response({"message": "ok"})
        #         while index < data_length :
        #             visible_material_no = int(data[index].get('visible_material_no')) 
        #             # if data[index].get('visible_material_no') is not None :
        #             if  visible_material_no != input_number:
        #                 # Get the qr_id from the current record
        #                 qr_id_data = data[index].get('qr_id')
        #                 material_no_data = data[index].get('material_no')
        #                 visible_material_no = data[index].get('visible_material_no')
        #                 # Log the qr_id and the length of the data array together
        #                 logging.warning(f"\n qr_id: {qr_id_data},\n data_length: {data_length},\n {index}")
        #                 # logging.warning(f"\n qr_id: {qr_id_data},\n data_length: {data_length}, \n dataIndex:{data[index]}, {index}")
        #                 print(visible_material_no)
        #                 result_list.append({
        #                     "qr_id": qr_id_data,
        #                     "material_no": material_no_data,
        #                     "visible_material_no": visible_material_no
        #                 })                         
        #                 index += 1                                          
        #             else:
        #                 return Response({
        #                     "nooooooooooooooooooooooo visible_material_no",data_length 
                            
        #                 })
                        
                        
        #         logging.warning(result_list)
        #         return Response({"material NUM": 'true'})
        #         # return Response(result_list,{"material NUM": 'true'})
            
        #     except master_data.DoesNotExist:
        #         error_msg = "Data not found."
        #         return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)
        # else:
        #     error_msg = "Input number not provided."
        #     return Response({"error": error_msg}, status=status.HTTP_400_BAD_REQUEST)

# ======================================================================================================

# class QRconditionView(APIView):
#     def get(self, request):
#         # Your condition to check against the database
        
#         if master_data.visible_material_no is not None:

#             try:
#                 queryset = master_data.objects.all()
#                 serializer = master_dataSerializer(queryset, many=True)
#                 data =serializer.data
#                 data_length = len(data)  # Get the length of the data array using len()
#                 index = 0
#                 result_list = []
#                 while index < data_length :
#                     if data[index].get('visible_material_no') is not None:
#                         # Get the qr_id from the current record
#                         qr_id_data = data[index].get('qr_id')
#                         material_no_data = data[index].get('material_no')
#                         # Log the qr_id and the length of the data array together
#                         logging.warning(f"\n qr_id: {qr_id_data},\n data_length: {data_length},\n {index}")
#                         # logging.warning(f"\n qr_id: {qr_id_data},\n data_length: {data_length}, \n dataIndex:{data[index]}, {index}")
                        
#                         index += 1
#                         result_list.append({
#                             "qr_id": qr_id_data,
#                             "material_no": material_no_data
#                         })
#                         # continue
#                         # return Response({
                            
#                         #     "qr_id": qr_id_data,
#                         #     "material_no": data[index].get('material_no'),
                      
#                         # })
                                                
#                     else:
#                         return Response({
#                             "nooooooooooooooooooooooooooooooooo visible_material_no"
#                         })
#                 # if data and data[0].get('visible_material_no') is not None:
#                 #     # Get the qr_id from the first record
#                 #     qr_id_data = data[0].get('qr_id') 
#                 #     logging.warning(data[0].get('qr_id'),len(data))
#                 #     return Response({"qr_id": qr_id_data,
#                 #                      "material_no":data[0].get('material_no')})
                
#                 # return Response(serializer.data)
#                 return Response(result_list)
           
#             except master_data.DoesNotExist:
#                 error_msg = "Data not found."
#                 return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)

#             qr_id_data = data_model_instance.qr_id
#             return Response({"qr_id": qr_id_data})
#         else:
#             error_msg = "Condition not met. Data not available."
#             return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)
        
    #   ----------------------under this code is working-----------------------------------------------------------------------------

# QR Checking function
# class QRconditionView(APIView):
#     def get(self, request):
#         # Your condition to check against the database
        
#         if master_data.visible_material_no is not None:

#             try:
#                 queryset = master_data.objects.all()
#                 serializer = master_dataSerializer(queryset, many=True)
#                 data =serializer.data
#                 data_length = len(data)  # Get the length of the data array using len()
#                 index = 0
#                 result_list = []
#                 while index < data_length :
#                     if data[index].get('visible_material_no') is not None:
#                         # Get the qr_id from the current record
#                         qr_id_data = data[index].get('qr_id')
#                         material_no_data = data[index].get('material_no')
#                         # Log the qr_id and the length of the data array together
#                         logging.warning(f"\n qr_id: {qr_id_data},\n data_length: {data_length},\n {index}")
#                         # logging.warning(f"\n qr_id: {qr_id_data},\n data_length: {data_length}, \n dataIndex:{data[index]}, {index}")
                        
#                         index += 1
#                         result_list.append({
#                             "qr_id": qr_id_data,
#                             "material_no": material_no_data
#                         })
#                         # continue
#                         # return Response({
                            
#                         #     "qr_id": qr_id_data,
#                         #     "material_no": data[index].get('material_no'),
                      
#                         # })
                                                
#                     else:
#                         return Response({
#                             "nooooooooooooooooooooooooooooooooo visible_material_no"
#                         })
#                 # if data and data[0].get('visible_material_no') is not None:
#                 #     # Get the qr_id from the first record
#                 #     qr_id_data = data[0].get('qr_id') 
#                 #     logging.warning(data[0].get('qr_id'),len(data))
#                 #     return Response({"qr_id": qr_id_data,
#                 #                      "material_no":data[0].get('material_no')})
                
#                 # return Response(serializer.data)
#                 return Response(result_list)
           
#             except master_data.DoesNotExist:
#                 error_msg = "Data not found."
#                 return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)

#             qr_id_data = data_model_instance.qr_id
#             return Response({"qr_id": qr_id_data})
#         else:
#             error_msg = "Condition not met. Data not available."
#             return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)
    #   -----------------------------------------------------------------------------------------------------------------------------  
# # QR Checking function
# class QRconditionView(APIView):
#     def get(self, request):
#         # Your condition to check against the database
        
#         if master_data.visible_material_no is not None:

#             try:
#                 queryset = master_data.objects.all()
#                 serializer = master_dataSerializer(queryset, many=True)
#                 data =serializer.data
#                 if data and data[0].get('visible_material_no') is not None:
#                     # Get the qr_id from the first record
#                     qr_id_data = data[0].get('qr_id') 
#                     logging.warning(data[0].get('qr_id'))
#                     return Response({"qr_id": qr_id_data,
#                                      "material_no":data[0].get('material_no')})
                
#                 return Response(serializer.data)
           
#             except master_data.DoesNotExist:
#                 error_msg = "Data not found."
#                 return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)

#             qr_id_data = data_model_instance.qr_id
#             return Response({"qr_id": qr_id_data})
#         else:
#             error_msg = "Condition not met. Data not available."
#             return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)

