# Copyright (c) 2013 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the 
# MIT License set forth at:
#   https://github.com/riverbed/flyscript-portal/blob/master/LICENSE ("License").  
# This software is distributed "AS IS" as set forth in the License.


from django.conf.urls import patterns, url
import steelscript.appfw.core.apps.help.views as views


urlpatterns = patterns(
    'steelscript.appfw.core.apps.help.views',
    #url(r'^$', views.ReportView.as_view()),

    url(r'^(?P<device_type>[a-z]+)/$',
        views.ColumnHelper.as_view()),

#    url(r'^shark/$',
#        views.SharkColumns.as_view()),

)
