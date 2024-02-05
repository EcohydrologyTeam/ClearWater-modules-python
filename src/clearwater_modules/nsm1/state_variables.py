import xarray as xr

from clearwater_modules import base
from clearwater_modules.nsm1.model import NutrientBudget
import clearwater_modules.nsm1.algae.algae_processes as algae_processes
import clearwater_modules.nsm1.balgae.balgae_processes as balgae_processes
import clearwater_modules.nsm1.nitrogen.nitrogen_processes as nitrogen_processes
import clearwater_modules.nsm1.carbon.processes as carbon_processes
import clearwater_modules.nsm1.CBOD.processes as CBOD_processes
import clearwater_modules.nsm1.DOX.processes as DOX_processes
import clearwater_modules.nsm1.alkalinity.processes as alkalinity_processes
import clearwater_modules.nsm1.n2.n2_processes as n2_processes
import clearwater_modules.nsm1.phosphorus.phosphorus_processes as phosphorus_processes
import clearwater_modules.nsm1.POM.processes as POM_processes
import clearwater_modules.nsm1.pathogens.pathogen_processes as pathogen_processes
import clearwater_modules.shared.processes as shared_processes
import clearwater_modules.tsm as tsm

@base.register_variable(models=NutrientBudget)
class Variable(base.Variable):
    """NSM1 state variables."""
    ...

# TODO: remove mock_equation
def mock_equation(water_temp_c: float) -> float:
    return water_temp_c ** 2

# TODO: import state variables from CWR such as surface_area volume, and timestep, as well as kah inputs

Variable(
    name='Ap',
    long_name='Algae Concentration',
    units='ug-Chla/L',
    description='Algal Concentration',
    use='state',
    process=algae_processes.Ap_new 
)

Variable(
    name='Ab',
    long_name='Benthic Algae Concentration',
    units='g-D/m^2',
    description='Benthic Algae Concentration',
    use='state',
    process=balgae_processes.Ab_new
)

Variable(
    name='NH4',
    long_name='Ammonium Concentration',
    units='mg-N/L',
    description='Ammonium Concentration',
    use='state',
    process=nitrogen_processes.NH4_new
)

Variable(
    name='NO3',
    long_name='Nitrate Concentration',
    units='mg-N/L',
    description='Nitrate Concentration',
    use='state',
    process=nitrogen_processes.NO3_new
)

Variable(
    name='OrgN',
    long_name='Organic Nitrogen Concentration',
    units='mg-N/L',
    description='Organic Nitrogen Concentration',
    use='state',
    process=nitrogen_processes.OrgN_new
)

Variable(
    name='N2',
    long_name='Nitrogen concentration air',
    units='mg-N/L',
    description='Nitrogen concentration air',
    use='state',
    process=n2_processes.N2_new
)

Variable(
    name='TIP',
    long_name='Total Inorganic Phosphorus',
    units='mg-P/L',
    description='Total Inorganic Phosphorus Concentration',
    use='state',
    process=phosphorus_processes.TIP_new
)

Variable(
    name='OrgP',
    long_name='Total Organic Phosphorus',
    units='mg-P/L',
    description='Total Organic Phosphorus Concentration',
    use='state',
    process=phosphorus_processes.OrgP_new
)

Variable(
    name='POC',
    long_name='Particulate Organic Carbon',
    units='mg-C/L',
    description='Particulate Organic Carbon Concentration',
    use='state',
    process=carbon_processes.POC_new
)

Variable(
    name='DOC',
    long_name='Dissolved Organic Carbon',
    units='mg-C/L',
    description='Dissolved Organic Carbon Concentration',
    use='state',
    process=carbon_processes.DOC_new
)

Variable(
    name='DIC',
    long_name='Dissolved Inorganic Carbon',
    units='mg-C/L',
    description='Dissolved Inorganic Carbon Concentration',
    use='state',
    process=carbon_processes.DIC_new
)

Variable(
    name='POM',
    long_name='Particulate Organic Matter',
    units='mg-D/L',
    description='Particulate Organic Matter Concentration',
    use='state',
    process=POM_processes.POM_new
)


Variable(
    name='CBOD',
    long_name='Carbonaceous Biochemical Oxygen Demand',
    units='mg-O2/L',
    description='Carbonaceous Biochemical Oxygen Demand Concentration',
    use='state',
    process=CBOD_processes.CBOD_new
)

Variable(
    name='DOX',
    long_name='Dissolved Oxygen',
    units='mg-O2/L',
    description='Dissolved Oxygen',
    use='state',
    process=DOX_processes.DOX_new
)

Variable(
    name='PX',
    long_name='Pathogen',
    units='cfu/100mL',
    description='Pathogen concentration',
    use='state',
    process=pathogen_processes.PX_new
)

Variable(
    name='Alk',
    long_name='Alkalinity',
    units='mg-CaCO3/L',
    description='Alkalinity concentration',
    use='state',
    process=alkalinity_processes.Alk_new
)

# TODO: remove mock_equation

def mock_twaterc(t_water_c: xr.DataArray) -> xr.DataArray:
    return t_water_c

def mock_depth(depth: xr.DataArray) -> xr.DataArray:
    return depth

#TODO not sure the order of calling with tsm
Variable(
    name='TwaterC',
    long_name='Water Temperature',
    units='C',
    description='Water Temperature Degree Celsius',
    use='state',
    process=mock_twaterc 
)

Variable(
    name='depth',
    long_name='Water Depth',
    units='m',
    description='Water depth from surface',
    use='state',
    process=mock_depth
)