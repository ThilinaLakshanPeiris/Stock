

from django.urls import path
from stc import views

from stc.views import DepotDetail, DepotList, QRconditionView, Region_auth_Detail, Region_auth_List, RegionDetail, RegionList, User_details_Detail, User_details_List, UserLevelDetail, UserLevelList, UsersDetail, UsersList, documentDetail, documentList, master_dataDetail, master_dataList, movementDetail, movementList, qrDetail, qrList


urlpatterns = [
    path('users/', UsersDetail.as_view()),
    path('users/<int:pk>/', UsersList.as_view()),
    
    path('userLevel/', UserLevelDetail.as_view()),
    path('userLevel/<int:pk>/', UserLevelList.as_view()),
    
    path('Region/', RegionDetail.as_view()),
    path('Region/<int:pk>/', RegionList.as_view()),
    
    path('depot/', DepotDetail.as_view()),
    path('depot/<int:pk>/', DepotList.as_view()),
    
    path('regionAuth/', Region_auth_Detail.as_view()),
    path('regionAuth/<int:pk>/', Region_auth_List.as_view()),
    
    path('userDetails/', User_details_Detail.as_view()),
    path('userDetails/<int:pk>/', User_details_List.as_view()),
    
    path('masterData/', master_dataDetail.as_view()),
    path('masterData/<int:pk>/', master_dataList.as_view()),
    
    path('document/', documentDetail.as_view()),
    path('document/<int:pk>/', documentList.as_view()),
    
    path('movement/', movementDetail.as_view()),
    path('movement/<int:pk>/', movementList.as_view()),
    
    path('qrData/<int:input_number>/', QRconditionView.as_view(), name='data-view'),
    
    # below urls are for testing-------------------------------------------------------
    path('qr/', qrDetail.as_view()),
    path('qr/<int:pk>/', qrList.as_view()),
    # path('qr/<int:variable_id>/', views.your_view_function),

]