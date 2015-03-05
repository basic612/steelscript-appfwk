# Copyright (c) 2014 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the MIT License
# accompanying the software ("License").  This software is distributed "AS IS"
# as set forth in the License.

import json

from . import reportrunner


class WidgetTokenTest(reportrunner.ReportRunnerTestCase):

    report = 'token_report'

    def setUp(self):
        super(WidgetTokenTest, self).setUp()
        self.criteria = {'endtime_0': '3/4/2015',
                         'endtime_1': '16:00 pm',
                         'duration': '15min',
                         'resolution': '2min'}
        widgets = self.run_report(self.criteria)
        url = widgets.keys()[0]
        # url="/report/appfwk/<report_slug>/widgets/<widget_slug>/jobs/1/"
        self.base_url = url.rsplit('/', 3)[0]

        post_url = self.base_url+'/authtoken/'
        criteria_json = json.dumps(self.criteria)
        response = self.client.post(post_url,
                                    data={'criteria': criteria_json})

        self.token = response.data['auth']

    def run_get_url(self, url=None, code=None):
        response = self.client.get(url)
        assert response.status_code == code

    def test_normal(self):
        get_url = self.base_url + '/render/?auth=%s' % self.token
        self.run_get_url(url=get_url, code=200)

    def test_no_token(self):
        get_url = self.base_url + '/render/'
        self.run_get_url(url=get_url, code=403)

    def test_wrong_token(self):
        get_url = self.base_url + '/render/?auth=wrongtoken'
        self.run_get_url(url=get_url, code=403)

    def test_wrong_url(self):
        no_widget_slug = self.base_url.rsplit('/', 1)[0]
        get_url = no_widget_slug + '/wrong-widget/render/?auth=%s' % self.token
        self.run_get_url(url=get_url, code=403)
