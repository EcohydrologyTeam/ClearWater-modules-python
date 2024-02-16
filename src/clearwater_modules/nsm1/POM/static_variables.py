"""
File contains static variables related to the POM module
"""

import clearwater_modules.base as base
from clearwater_modules.nsm1.model import NutrientBudget


@base.register_variable(models=NutrientBudget)
class Variable(base.Variable):
    ...



Variable(
    name='kpom_20',
    long_name='POM dissolution rate at 20C',
    units='1/d',
    description='POM dissolution rate at 20C',
    use='static'
)


Variable(
    name='focm',
    long_name='ratio of carbon to organic matter',
    units='mg-C/mg-D',
    description='ratio of carbon to organic matter',
    use='static'
)

Variable(
    name='vb',
    long_name='burial velocity of POM2 in bed sediment',
    units='m/a',
    description='burial velocity of POM2 in bed sediment',
    use='static'
)