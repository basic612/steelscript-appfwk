# Copyright (c) 2014 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the MIT License
# accompanying the software ("License").  This software is distributed "AS IS"
# as set forth in the License.


from steelscript.appfwk.apps.plugins.builtin.whois.libs.whois import whois

from steelscript.appfwk.apps.datasource.modules.analysis import AnalysisTable
from steelscript.netprofiler.appfwk.datasources.netprofiler import NetProfilerGroupbyTable
from steelscript.appfwk.apps.report.models import Report
import steelscript.appfwk.apps.report.modules.yui3 as yui3

# helper libraries

#
# NetProfiler report
#

report = Report.create("Whois", position=5)

report.add_section()

# Define a Table that gets external hosts by avg bytes
table = NetProfilerGroupbyTable.create('5-hosts', groupby='host', duration='1 hour',
                                    filterexpr='not srv host 10/8 and not srv host 192.168/16')

table.add_column('host_ip', 'IP Addr', iskey=True, datatype='string')
table.add_column('avg_bytes', 'Avg Bytes', units='B/s', issortcol=True)


# Create an Analysis table that calls the 'whois' function to craete a link to
# 'whois'
whoistable = AnalysisTable.create('5-whois-hosts',
                                  tables={'t': table},
                                  function=whois)
whoistable.copy_columns(table)
whoistable.add_column('whois', label="Whois link", datatype='html')

report.add_widget(yui3.TableWidget, whoistable, "Link table", width=12)
