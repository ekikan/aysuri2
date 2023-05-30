from django.urls import path
from .views import RecordView, CreateRecordView, EditRecordView, DeleteRecordView

urlpatterns = [
    path('record/<int:record_id>/', RecordView.as_view(), name='record'),
    path('record/create/', CreateRecordView.as_view(), name='create_record'),
    path('record/<int:record_id>/edit/', EditRecordView.as_view(), name='edit_record'),
    path('record/<int:record_id>/delete/', DeleteRecordView.as_view(), name='delete_record'),
]
