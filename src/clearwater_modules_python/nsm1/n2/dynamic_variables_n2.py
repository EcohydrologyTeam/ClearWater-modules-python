"""
File includes dynamic variables computed in N2 module. Dynamic variables may be accessed by other modules.
"""

import clearwater_modules_python.shared.processes as shared_processes
from clearwater_modules_python import base
from clearwater_modules_python.nsm1.model import NutrientBudget
import clearwater_modules_python.nsm1.n2.n2_processes as n2_processes


@base.register_variable(models=NutrientBudget)
class Variable(base.Variable):
    ...

Variable(
    name='KHN2_tc',
    long_name='Henrys law constant',
    units='mol/L/atm',
    description='Henrys law constant temperature corrected',
    use='dynamic',
    process=n2_processes.KHN2_tc
)

Variable(
    name='P_wv',
    long_name='Partial pressure water vapor',
    units='atm',
    description='Partial pressure water vapor',
    use='dynamic',
    process=n2_processes.P_wv
)

Variable(
    name='N2sat',
    long_name='N2 at saturation',
    units='mg-N/L',
    description='N2 at saturation f(Twater and atm pressure)',
    use='dynamic',
    process=n2_processes.N2sat
)

Variable(
    name='dN2dt',
    long_name='Change in N2 air concentration',
    units='mg-N/L/d',
    description='Change in N2 air concentration',
    use='dynamic',
    process=n2_processes.dN2dt
)

Variable(
    name='TDG',
    long_name='Total dissolved gas',
    units='%',
    description='Total dissolved gas',
    use='dynamic',
    process=n2_processes.TDG
)