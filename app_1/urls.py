from django.urls import path
from . import views


#urlpatterns = [
#path("", views.index,name="index"),
#path("", views.bond_universe,name="bond_universe")
#] 


urlpatterns = [
path("", views.index,name="index"),
path("add_issuer/", views.add_issuer,name="add_issuer"),
path("add_position/", views.add_position,name="add_position"),
path("add_security/", views.add_security,name="add_security"),
path("update_security/<bond_id>", views.update_security,name="update_security"),
path("delete_security/<bond_id>", views.delete_security,name="delete_security"),
path("update_position/<pos_id>", views.update_position,name="update_position"),
path("delete_position/<pos_id>", views.delete_position,name="delete_position"),
path("update_issuer/<issuer_id>", views.update_issuer,name="update_issuer"),
path("delete_issuer/<issuer_id>", views.delete_issuer,name="delete_issuer")
] 
