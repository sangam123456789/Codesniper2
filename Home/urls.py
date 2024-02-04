from django.contrib import admin
from django.urls import path , include
from Home import views

admin.site.site_header = "Welcome Mr. Administrator"
admin.site.site_title = "This is Admin zone"
admin.site.index_title = "Databases"
urlpatterns =[
    path('', views.home , name = 'home'),
    path('signout', views.signout , name = 'signout'),
    path('signin', views.signin , name = 'signin'),
    path('signup', views.signup , name = 'signup'),
    path('Add', views.addf , name = 'addf'),
    path('templates', views.templates , name = 'templates'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('Brain', views.brainf , name = 'brainf'),
    path('Recursion', views.recursionf , name = 'recursionf'),
    path('Beginner', views.beginnerf , name = 'beginnerf'),
    path('Brute', views.brutef , name = 'brutef'),
    path('Bit', views.bitf , name = 'bitf'),
    path('Greed', views.greedf , name = 'greedf'),
    path('Sub', views.subf , name = 'subf'),
    path('Implement', views.implementf , name = 'implementf'),
    path('Sort', views.sortf , name = 'sortf'),
    path('Binary', views.binaryf , name = 'binaryf'),
    path('Pointer', views.pointerf , name = 'pointerf'),
    path('Hash', views.hashf , name = 'hashf'),
    path('Pair', views.pairf , name = 'pairf'),
    path('Dpstand', views.dpstandf , name = 'dpstandf'),
    path('Dp', views.dpf , name = 'dpf'),
    path('Tree', views.treef , name = 'treef'),
    path('Graph', views.graphf , name = 'graphf'),
    path('DSU', views.dsuf , name = 'dsuf'),
    path('Segtree', views.segtreef , name = 'segtreef'),
    path('Mixed', views.mixedf , name = 'mixedf'),
    path('Search', views.searchf , name = 'searchf'),
]
 