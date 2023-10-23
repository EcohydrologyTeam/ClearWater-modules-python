# TODO: figure out imports

import clearwater_modules.shared.processes as shared_processes
from clearwater_modules import base
from clearwater_modules.nsm1.carbon.model import CarbonBudget
from clearwater_modules.nsm1.alkalinity import processes


@base.register_variable(models=CarbonBudget)
class Variable(base.Variable):
    ...


Variable(
    name='depth',
    long_name='Average water depth in cell',
    units='m',
    description='Average water depth in cell computed by dividing volume by surface area',
    use='dynamic',
    process=shared_processes.compute_depth
)

Variable(
    name='knit_T',
    long_name='Nitrification rate corrected for temperature',
    units='1/d',
    description='Nitrification rate corrected for temperature',
    use='dynamic',
    process=processes.knit_T
)

Variable(
    name='kdnit_T',
    long_name='Denitrification rate corrected for temperature',
    units='1/d',
    description='Denitrification rate corrected for temperature',
    use='dynamic',
    process=processes.kdnit_T
)

Variable(
    name='Alk_denitrification',
    long_name='Alkalinity change due to denitrification',
    units='mg/L/d',
    description='Alkalinity change due to denitrification',
    use='dynamic',
    process=processes.Alk_denitrification
)

Variable(
    name='Alk_nitrification',
    long_name='Alkalinity change due to nitrification',
    units='mg/L/d',
    description='Alkalinity change due to nitrification',
    use='dynamic',
    process=processes.Alk_nitrification
)

Variable(
    name='Alk_algal_growth',
    long_name='Alkalinity change due to algal growth',
    units='mg/L/d',
    description='Alkalinity change due to algal growth',
    use='dynamic',
    process=processes.Alk_algal_growth
)

Variable(
    name='Alk_algal_respiration',
    long_name='Alkalinity change due to algal respiration',
    units='mg/L/d',
    description='Alkalinity change due to algal respiration',
    use='dynamic',
    process=processes.Alk_algal_respiration
)

Variable(
    name='Alk_benthic_algae_growth',
    long_name='Alkalinity change due to benthic algae growth',
    units='mg/L/d',
    description='Alkalinity change due to benthic algae growth',
    use='dynamic',
    process=processes.Alk_benthic_algae_growth
)

Variable(
    name='Alk_benthic_algae_respiration',
    long_name='Alkalinity change due to benthic algae growth',
    units='mg/L/d',
    description='Alkalinity change due to benthic algae growth',
    use='dynamic',
    process=processes.Alk_benthic_algae_respiration
)

Variable(
    name='dAlkdt',
    long_name='Alkalinity concentration change per timestep',
    units='mg/L/d',
    description='Alkalinity concentration change per timestep',
    use='dynamic',
    process=processes.dAlkdt
)
