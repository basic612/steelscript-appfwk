from django import forms

from steelscript.appfw.core.apps.datasource.forms import fields_add_time_selection
from steelscript.appfw.core.apps.datasource.modules.analysis import AnalysisTable
from steelscript.appfw.core.apps.datasource.models import TableField, Table, Column
from steelscript.appfw.core.libs.fields import Function

from steelscript.appfw.core.apps.report.models import Report, Section
from steelscript.appfw.core.apps.report.modules import raw

from . import criteria_functions as funcs

report = Report(title='Criteria Section Keywords')
report.save()


# Section
section = Section.create(report=report, title='Section 0', section_keywords=['k1'])
section.save()

# Table
a = AnalysisTable.create('test-criteria-sectionkeywords-1', tables={},
                         function=funcs.analysis_echo_criteria)
TableField.create(keyword='k1', label='Key 1', obj=a, initial='r1')

a.add_column('key', 'Key', iskey=True, datatype="string")
a.add_column('value', 'Value', datatype="string")

raw.TableWidget.create(section, a, 'Table 1')

# Section
section = Section.create(report=report, title='Section 1', section_keywords=['k1'])
section.save()

# Table
a = AnalysisTable.create('test-criteria-sectionkeywords-2', tables={},
                         function=funcs.analysis_echo_criteria)
TableField.create(keyword='k1', label='Key 1', obj=a, initial='r1')

a.add_column('key', 'Key', iskey=True, datatype="string")
a.add_column('value', 'Value', datatype="string")

raw.TableWidget.create(section, a, 'Table 2')
