# CreateContributionTestScript.py
#
# Developed by Jeffrey Rissman
#
# This is a Python script that is used to generate a Vensim command script.
# The Vensim command script will perform one run with all selected policies
# enabled, one run with all policies disabled (a BAU run),
# and one run with each defined subset (or "group") within the set of selected
# policies turned off or turned on (depending on a user setting in this script).


# File Names
# ----------
# Rather than including input and output file names in the code below, we assign all the file
# names to variables in this section.  This allows the names to be easily changed if desired.
ModelFile = "EPS.mdl" # The name of the Vensim model file (typically with .mdl or .vpm extension)
OutputScript = "GeneratedContributionTestScript.cmd" # The desired filename of the Vensim command script to be generated
RunResultsFile = "ContributionTestResults.tsv" # The desired filename for TSV file containing model run results
OutputVarsFile = "OutputVarsToExport.lst" # The name of the file containing a list of variables to be included in the RunResultsFile
                                          # May optionally also be used as a SAVELIST for Vensim (see below)

# Other Settings
# --------------
RunName = "MostRecentRun" # The desired name for all runs performed.  Used as the filename for the VDF files that Vensim creates
EnableOrDisableGroups = "Disable" # Should each group be enabled or disabled in turn?
								 # Essentially, this is testing either the contribution of a group in the proximity of the
								 # BAU case ("Enable") or in the proximity of a scenario defined in the non-zero values of
								 # the policies listed below ("Disable").
PolicySchedule = 1 # The number of the policy implementation schedule file to be used (in InputData/plcy-schd/FoPITY)


# Index definitions
# -----------------
# Each policy is a Python list.  The numbers below are a key to the meaning of the four entries
# that compose each policy, so we can refer to them by meaningful names in the code.
# Note that the fourth entry in each policy, Settings, is itself a list that contains various
# setting values.  Do not change any names or numbers in this section.
Enabled = 0
LongName = 1
ShortName = 2
Settings = 3
Group = 4


# Policy Options
# --------------
# This section specifies which policies should be included in the Vensim command script
# (called here "enabled" policies) and what setting values for those policies should
# be included.  Unless you are using "Enable" Groups mode, all non-repeating
# combinations of the settings for enabled policies will
# be included in the Vensim command script, so do not enable too many policies at once, or
# Vensim will be unable to complete the necessary runs in a reasonable amount of time.
# Each policy is on a single line:
  # You may change the first entry of each policy to "True" to enable the policy or "False" to disable it.
  # The second and third entries are the long and short name of the policy, used internally by this script.  Do not change these names.
  # The fourth entry in each policy is a list of setting values enclosed with square brackets.
    # You may change these values, add more values (separated by commas), and delete values.
    # Any enabled policy must have a minimum of one setting value.  A policy that is disabled
    # and a policy with a setting of zero produce identical results.
  # The fifth entry in each policy is its group name.  By default, each policy is in its own group (and its subscripts share that group).
    # Change the group names so multiple policies share a name (like "financial policies") to cause them to be enabled or disabled together.

PotentialPolicies = (

	# Transportation Sector Policies
	(False,"Percentage Reduction of Separately Regulated Pollutants[LDVs]","Conventional Pollutant Standards - LDVs",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[HDVs]","Conventional Pollutant Standards - HDVs",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[aircraft]","Conventional Pollutant Standards - aircraft",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[rail]","Conventional Pollutant Standards - rail",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[ships]","Conventional Pollutant Standards - ships",[0,1],"Conventional Pollutant Standard"),
	(False,"Percentage Reduction of Separately Regulated Pollutants[motorbikes]","Conventional Pollutant Standards - motorbikes",[0,1],"Conventional Pollutant Standard"),
	(False,"Boolean EV Perks","Electric Vehicle Perks",[0,1],"EV Perks"),
	(False,"Additional Minimum Required EV Sales Percentage[passenger,LDVs]","Electric Vehicle Sales Mandate - Passenger LDVs",[0,1],"EV Sales Mandate"),
	(False,"Additional Minimum Required EV Sales Percentage[passenger,HDVs]","Electric Vehicle Sales Mandate - Passenger HDVs",[0,1],"EV Sales Mandate"),
	(False,"Additional Minimum Required EV Sales Percentage[freight,HDVs]","Electric Vehicle Sales Mandate - Freight HDVs",[0,1],"EV Sales Mandate"),
	(False,"Additional Minimum Required EV Sales Percentage[passenger,motorbikes]","Electric Vehicle Sales Mandate - Passenger Motorbikes",[0,1],"EV Sales Mandate"),
	(False,"Additional EV Subsidy Percentage[passenger,LDVs]","Electric Vehicle Subsidy - Passenger LDVs",[0,0.5],"EV Subsidy"),
	(False,"LDVs Feebate Rate","Feebate",[0,1],"Feebate"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[gasoline vehicle,LDVs]","Fuel Economy Standard - Gasoline Engine LDVs",[0,1],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[diesel vehicle,HDVs]","Fuel Economy Standard - Diesel Engine HDVs",[0,0.66],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[nonroad vehicle,aircraft]","Fuel Economy Standard - All Aircraft",[0,0.54],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[nonroad vehicle,rail]","Fuel Economy Standard - All Rail",[0,0.2],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[nonroad vehicle,ships]","Fuel Economy Standard - All Ships",[0,0.2],"Vehicle Fuel Economy Standards"),
	(False,"Percentage Additional Improvement of Fuel Economy Std[gasoline vehicle,motorbikes]","Fuel Economy Standard - Gasoline Engine Motorbikes",[0,0.74],"Vehicle Fuel Economy Standards"),
	(False,"Additional LCFS Percentage","Low Carbon Fuel Standard",[0,0.2],"Low Carbon Fuel Standard"),
	(False,"Fraction of TDM Package Implemented[passenger]","Transportation Demand Management - Passengers",[0,1],"Transportation Demand Management"),
	(False,"Fraction of TDM Package Implemented[freight]","Transportation Demand Management - Freight",[0,1],"Transportation Demand Management"),

	# Buildings Sector Policies
	(False,"Percent New Nonelec Component Sales Shifted to Elec[urban residential]","Building Component Electrification - Urban Residential",[0,1],"Building Component Electrification"),
	(False,"Percent New Nonelec Component Sales Shifted to Elec[rural residential]","Building Component Electrification - Rural Residential",[0,1],"Building Component Electrification"),
	(False,"Percent New Nonelec Component Sales Shifted to Elec[commercial]","Building Component Electrification - Commercial",[0,1],"Building Component Electrification"),
	(False,"Reduction in E Use Allowed by Component Eff Std[heating,urban residential]","Building Energy Efficiency Standards - Urban Residential Heating",[0,0.22],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,urban residential]","Building Energy Efficiency Standards - Urban Residential Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[envelope,urban residential]","Building Energy Efficiency Standards - Urban Residential Envelope",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[lighting,urban residential]","Building Energy Efficiency Standards - Urban Residential Lighting",[0,0.4],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[appliances,urban residential]","Building Energy Efficiency Standards - Urban Residential Appliances",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[other component,urban residential]","Building Energy Efficiency Standards - Urban Residential Other Components",[0,0.11],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[heating,rural residential]","Building Energy Efficiency Standards - Rural Residential Heating",[0,0.22],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,rural residential]","Building Energy Efficiency Standards - Rural Residential Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[envelope,rural residential]","Building Energy Efficiency Standards - Rural Residential Envelope",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[lighting,rural residential]","Building Energy Efficiency Standards - Rural Residential Lighting",[0,0.4],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[appliances,rural residential]","Building Energy Efficiency Standards - Rural Residential Appliances",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[other component,rural residential]","Building Energy Efficiency Standards - Rural Residential Other Components",[0,0.11],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[heating,commercial]","Building Energy Efficiency Standards - Commercial Heating",[0,0.22],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,commercial]","Building Energy Efficiency Standards - Commercial Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[envelope,commercial]","Building Energy Efficiency Standards - Commercial Envelope",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[lighting,commercial]","Building Energy Efficiency Standards - Commercial Lighting",[0,0.4],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[appliances,commercial]","Building Energy Efficiency Standards - Commercial Appliances",[0,0.38],"Building Energy Efficiency Standards"),
	(False,"Reduction in E Use Allowed by Component Eff Std[other component,commercial]","Building Energy Efficiency Standards - Commercial Other Components",[0,0.11],"Building Energy Efficiency Standards"),
	(False,"Boolean Improved Contractor Edu and Training","Contractor Training",[0,1],"Contractor Training"),
	(False,"Min Fraction of Total Elec Demand to be Met by Distributed Solar PV","Distributed Solar Carve-Out",[0,0.24],"Distributed Solar Promotion"),
	(False,"Perc Subsidy for Distributed Solar PV Capacity","Distributed Solar Subsidy",[0,0.5],"Distributed Solar Promotion"),
	(False,"Boolean Improved Device Labeling","Improved Labeling",[0,1],"Improved Labeling"),
	(False,"Fraction of Commercial Components Replaced Annually due to Retrofitting Policy[heating]","Increased Retrofitting - Heating",[0,0.034],"Increased Retrofitting"),
	(False,"Fraction of Commercial Components Replaced Annually due to Retrofitting Policy[cooling and ventilation]","Increased Retrofitting - Cooling and Ventilation",[0,0.034],"Increased Retrofitting"),
	(False,"Fraction of Commercial Components Replaced Annually due to Retrofitting Policy[envelope]","Increased Retrofitting - Envelope",[0,0.034],"Increased Retrofitting"),
	(False,"Fraction of Commercial Components Replaced Annually due to Retrofitting Policy[lighting]","Increased Retrofitting - Lighting",[0,0.034],"Increased Retrofitting"),
	(False,"Fraction of Commercial Components Replaced Annually due to Retrofitting Policy[appliances]","Increased Retrofitting - Appliances",[0,0.034],"Increased Retrofitting"),
	(False,"Fraction of Commercial Components Replaced Annually due to Retrofitting Policy[other component]","Increased Retrofitting - Other Components",[0,0.034],"Increased Retrofitting"),
	(False,"Boolean Rebate Program for Efficient Components[heating]","Rebate for Efficient Products - Heating",[0,1],"Rebate for Efficient Products"),
	(False,"Boolean Rebate Program for Efficient Components[cooling and ventilation]","Rebate for Efficient Products - Cooling and Ventilation",[0,1],"Rebate for Efficient Products"),
	(False,"Boolean Rebate Program for Efficient Components[appliances]","Rebate for Efficient Products - Appliances",[0,1],"Rebate for Efficient Products"),

	# Electricity Sector Policies
	(False,"Boolean Ban New Power Plants[hard coal es]","Ban New Power Plants - Hard Coal",[0,1],"Ban New Power Plants"),
	(False,"Boolean Ban New Power Plants[natural gas nonpeaker es]","Ban New Power Plants - Natural Gas Nonpeaker",[0,1],"Ban New Power Plants"),
	(False,"Boolean Ban New Power Plants[nuclear es]","Ban New Power Plants - Nuclear",[0,1],"Ban New Power Plants"),
	(False,"Boolean Ban New Power Plants[hydro es]","Ban New Power Plants - Hydro",[0,1],"Ban New Power Plants"),
	(False,"Boolean Ban New Power Plants[lignite es]","Ban New Power Plants - Lignite",[0,1],"Ban New Power Plants"),
	(False,"Percent Change in Electricity Exports","Change Electricity Exports",[-0.5,1],"Electricity Imports and Exports"),
	(False,"Percent Change in Electricity Imports","Change Electricity Imports",[-0.5,1],"Electricity Imports and Exports"),
	(False,"Fraction of Additional Demand Response Potential Achieved","Demand Response",[0,1],"Demand Response"),
	(False,"Annual Additional Capacity Retired due to Early Retirement Policy[hard coal es]","Early Retirement of Power Plants - Hard Coal",[0,10000],"Early Retirement of Power Plants"),
	(False,"Annual Additional Capacity Retired due to Early Retirement Policy[nuclear es]","Early Retirement of Power Plants - Nuclear",[0,10000],"Early Retirement of Power Plants"),
	(False,"Additional Battery Storage Annual Growth Percentage","Grid-Scale Electricity Storage",[0,0.16],"Grid-Scale Electricity Storage"),
	(False,"Percentage Increase in Transmission Capacity vs BAU","Increase Transmission",[0,1.13],"Increase Transmission"),
	(False,"Nuclear Capacity Lifetime Extension","Nuclear Plant Lifetime Extension",[0,20],"Nuclear Lifetime Extension"),
	(False,"Percentage Reduction in Plant Downtime[natural gas nonpeaker es,preexisting retiring]","Reduce Plant Downtime - Preexisting Natural Gas Nonpeaker",[0,0.6],"Reduce Plant Downtime"),
	(False,"Percentage Reduction in Plant Downtime[onshore wind es,newly built]","Reduce Plant Downtime - New Onshore Wind",[0,0.25],"Reduce Plant Downtime"),
	(False,"Percentage Reduction in Plant Downtime[solar PV es,newly built]","Reduce Plant Downtime - New Solar PV",[0,0.3],"Reduce Plant Downtime"),
	(False,"Percentage Reduction in Plant Downtime[offshore wind es,newly built]","Reduce Plant Downtime - New Offshore Wind",[0,0.25],"Reduce Plant Downtime"),
	(False,"Percent Reduction in Soft Costs of Capacity Construction[onshore wind es]","Reduce Soft Costs - Onshore Wind",[0,0.9],"Reduce Soft Costs"),
	(False,"Percent Reduction in Soft Costs of Capacity Construction[solar PV es]","Reduce Soft Costs - Solar PV",[0,0.9],"Reduce Soft Costs"),
	(False,"Percent Reduction in Soft Costs of Capacity Construction[offshore wind es]","Reduce Soft Costs - Offshore Wind",[0,0.9],"Reduce Soft Costs"),
	(False,"Percentage TnD Losses Avoided","Reduce Transmission & Distribution Losses",[0,0.4],"Reduce T&D Losses"),
	(False,"Additional Renewable Portfolio Std Percentage","Renewable Portfolio Standard",[0,0.88],"Renewable Portfolio Standard"),
	(False,"Subsidy for Elec Production by Fuel[nuclear es]","Subsidy for Electricity Production - Nuclear",[0,60],"Subsidy for Electricity Production"),
	(False,"Subsidy for Elec Production by Fuel[onshore wind es]","Subsidy for Electricity Production - Onshore Wind",[0,60],"Subsidy for Electricity Production"),
	(False,"Subsidy for Elec Production by Fuel[solar PV es]","Subsidy for Electricity Production - Solar PV",[0,60],"Subsidy for Electricity Production"),
	(False,"Subsidy for Elec Production by Fuel[solar thermal es]","Subsidy for Electricity Production - Solar Thermal",[0,60],"Subsidy for Electricity Production"),
	(False,"Subsidy for Elec Production by Fuel[biomass es]","Subsidy for Electricity Production - Biomass",[0,60],"Subsidy for Electricity Production"),
	(False,"Subsidy for Elec Production by Fuel[offshore wind es]","Subsidy for Electricity Production - Offshore Wind",[0,60],"Subsidy for Electricity Production"),

	# Industry Sector Policies
	(False,"Fraction of Cement Clinker Substitution Made","Cement Clinker Substitution",[0,1],"Cement Clinker Substitution"),
	(False,"Fraction of Potential Cogeneration and Waste Heat Recovery Adopted","Cogeneration and Waste Heat Recovery",[0,1],"Cogeneration and Waste Heat Recovery"),
	(False,"Fraction of Energy Savings from Early Facility Retirement Achieved","Early Retirement of Industrial Facilities",[0,1],"Early Retirement of Industrial Facilities"),
	(False,"Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates]","Industry Energy Efficiency Standards - Cement",[0,0.33],"Industry Energy Efficiency Standards"),
	(False,"Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems]","Industry Energy Efficiency Standards - Natural Gas and Petroleum",[0,0.33],"Industry Energy Efficiency Standards"),
	(False,"Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel]","Industry Energy Efficiency Standards - Iron and Steel",[0,0.33],"Industry Energy Efficiency Standards"),
	(False,"Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals]","Industry Energy Efficiency Standards - Chemicals",[0,0.33],"Industry Energy Efficiency Standards"),
	(False,"Percentage Improvement in Eqpt Efficiency Standards above BAU[mining]","Industry Energy Efficiency Standards - Mining",[0,0.33],"Industry Energy Efficiency Standards"),
	(False,"Percentage Improvement in Eqpt Efficiency Standards above BAU[waste management]","Industry Energy Efficiency Standards - Waste Management",[0,0.33],"Industry Energy Efficiency Standards"),
	(False,"Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture]","Industry Energy Efficiency Standards - Agriculture",[0,0.33],"Industry Energy Efficiency Standards"),
	(False,"Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries]","Industry Energy Efficiency Standards - Other Industries",[0,0.33],"Industry Energy Efficiency Standards"),
	(False,"Fraction of Installation and System Integration Issues Remedied","Improved System Design",[0,1],"Improved System Design"),
	(False,"Fraction of Hard Coal Use Converted to Other Fuels","Electrify Hard Coal Processes",[0,1],"Industrial Electrification"),
	(False,"Fraction of Natural Gas Use Converted to Other Fuels","Electrify NG Processes",[0,0.5],"Industrial Electrification"),
	(False,"Fraction of Methane Capture Opportunities Achieved","Methane Capture",[0,1],"Methane Capture and Destruction"),
	(False,"Fraction of Methane Destruction Opportunities Achieved","Methane Destruction",[0,1],"Methane Capture and Destruction"),
	(False,"Fraction of F Gases Avoided","Reduce F-gases",[0,1],"Reduce F-gases"),
	(False,"Fraction of Addressable Process Emissions Avoided via Worker Training","Worker Training",[0,1],"Worker Training"),

	# Agriculture, Land Use, and Forestry Policies
	(False,"Fraction of Afforestation and Reforestation Achieved","Afforestation and Reforestation",[0,1],"Afforestation and Reforestation"),
	(False,"Fraction of Forest Set Asides Achieved","Forest Set-Asides",[0,1],"Forest Set-Asides"),
	(False,"Fraction of Abatement from Cropland Management Achieved","Cropland Management",[0,1],"Cropland Management"),
	(False,"Fraction of Improved Forest Management Achieved","Improved Forest Management",[0,1],"Improved Forest Management"),
	(False,"Fraction of Abatement from Livestock Measures Achieved","Livestock Measures",[0,1],"Livestock Measures"),
	(False,"Fraction of Abatement from Rice Cultivation Measures Achieved","Rice Cultivation Measures",[0,1],"Rice Cultivation Measures"),

	# District Heat Sector Policies
	(False,"Fraction of Non CHP Heat Production Converted to CHP","Convert Non-CHP Heat Production",[0,1],"Convert Non-CHP Heat Production"),
	(False,"Fraction of District Heat Hard Coal Use Converted to Other Fuels","Hard Coal to NG Switching",[0,1],"District Heat Fuel Switching"),

	# Cross-Sector Policies
	(False,"Fraction of Potential Additional CCS Achieved","Carbon Capture and Sequestration",[0,1],"Carbon Capture and Sequestration"),
	(False,"Carbon Tax[transportation sector]","Carbon Tax - Transportation Sector",[0,300],"Carbon Tax"),
	(False,"Carbon Tax[electricity sector]","Carbon Tax - Electricity Sector",[0,300],"Carbon Tax"),
	(False,"Carbon Tax[residential buildings sector]","Carbon Tax - Residential Bldg Sector",[0,300],"Carbon Tax"),
	(False,"Carbon Tax[commercial buildings sector]","Carbon Tax - Commercial Bldg Sector",[0,300],"Carbon Tax"),
	(False,"Carbon Tax[industry sector]","Carbon Tax - Industry Sector",[0,300],"Carbon Tax"),
	(False,"Percent Reduction in BAU Subsidies[hard coal]","End Existing Subsidies - Hard Coal",[0,1],"End Existing Subsidies"),
	(False,"Percent Reduction in BAU Subsidies[natural gas]","End Existing Subsidies - Natural Gas",[0,1],"End Existing Subsidies"),
	(False,"Percent Reduction in BAU Subsidies[nuclear]","End Existing Subsidies - Nuclear",[0,1],"End Existing Subsidies"),
	(False,"Percent Reduction in BAU Subsidies[solar]","End Existing Subsidies - Solar",[0,1],"End Existing Subsidies"),
	(False,"Percent Reduction in BAU Subsidies[petroleum gasoline]","End Existing Subsidies - Petroleum Gasoline",[0,1],"End Existing Subsidies"),
	(False,"Percent Reduction in BAU Subsidies[petroleum diesel]","End Existing Subsidies - Petroleum Diesel",[0,1],"End Existing Subsidies"),
	(False,"Additional Fuel Tax Rate by Fuel[electricity]","Fuel Taxes - Electricity",[0,0.2],"Fuel Taxes"),
	(False,"Additional Fuel Tax Rate by Fuel[hard coal]","Fuel Taxes - Hard Coal",[0,0.2],"Fuel Taxes"),
	(False,"Additional Fuel Tax Rate by Fuel[natural gas]","Fuel Taxes - Natural Gas",[0,0.2],"Fuel Taxes"),
	(False,"Additional Fuel Tax Rate by Fuel[petroleum gasoline]","Fuel Taxes - Petroleum Gasoline",[0,0.2],"Fuel Taxes"),
	(False,"Additional Fuel Tax Rate by Fuel[petroleum diesel]","Fuel Taxes - Petroleum Diesel",[0,0.2],"Fuel Taxes"),

	# Research & Development Levers
	(False,"RnD Building Capital Cost Perc Reduction[heating]","Capital Cost Reduction - Buildings: Heating",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[cooling and ventilation]","Capital Cost Reduction - Buildings: Cooling and Ventilation",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[envelope]","Capital Cost Reduction - Buildings: Envelope",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[lighting]","Capital Cost Reduction - Buildings: Lighting",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[appliances]","Capital Cost Reduction - Buildings: Appliances",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Capital Cost Perc Reduction[other component]","Capital Cost Reduction - Buildings: Other Components",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD CCS Capital Cost Perc Reduction","Capital Cost Reduction",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[hard coal es]","Capital Cost Reduction - Electricity: Hard Coal",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[natural gas nonpeaker es]","Capital Cost Reduction - Electricity: Natural Gas Nonpeaker",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[nuclear es]","Capital Cost Reduction - Electricity: Nuclear",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[hydro es]","Capital Cost Reduction - Electricity: Hydro",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[onshore wind es]","Capital Cost Reduction - Electricity: Onshore Wind",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[solar PV es]","Capital Cost Reduction - Electricity: Solar PV",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[solar thermal es]","Capital Cost Reduction - Electricity: Solar Thermal",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[biomass es]","Capital Cost Reduction - Electricity: Biomass",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[natural gas peaker es]","Capital Cost Reduction - Electricity: Natural Gas Peaker",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[lignite es]","Capital Cost Reduction - Electricity: Lignite",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Electricity Capital Cost Perc Reduction[offshore wind es]","Capital Cost Reduction - Electricity: Offshore Wind",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[cement and other carbonates]","Capital Cost Reduction - Industry: Cement",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[natural gas and petroleum systems]","Capital Cost Reduction - Industry: Natural Gas and Petroleum",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[iron and steel]","Capital Cost Reduction - Industry: Iron and Steel",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[chemicals]","Capital Cost Reduction - Industry: Chemicals",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[mining]","Capital Cost Reduction - Industry: Mining",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[waste management]","Capital Cost Reduction - Industry: Waste Management",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[agriculture]","Capital Cost Reduction - Industry: Agriculture",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Industry Capital Cost Perc Reduction[other industries]","Capital Cost Reduction - Industry: Other Industries",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[battery electric vehicle]","Capital Cost Reduction - Vehicles: Battery Electric",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[natural gas vehicle]","Capital Cost Reduction - Vehicles: Natural Gas",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[gasoline vehicle]","Capital Cost Reduction - Vehicles: Gasoline Engine",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[diesel vehicle]","Capital Cost Reduction - Vehicles: Diesel Engine",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[plugin hybrid vehicle]","Capital Cost Reduction - Vehicles: Plug-in Hybrid",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Transportation Capital Cost Perc Reduction[nonroad vehicle]","Capital Cost Reduction - Vehicles: Non-road",[0,0.4],"RnD Capital Cost Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[heating]","Fuel Use Reduction - Buildings: Heating",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[cooling and ventilation]","Fuel Use Reduction - Buildings: Cooling and Ventilation",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[lighting]","Fuel Use Reduction - Buildings: Lighting",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[appliances]","Fuel Use Reduction - Buildings: Appliances",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Building Fuel Use Perc Reduction[other component]","Fuel Use Reduction - Buildings: Other Components",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD CCS Fuel Use Perc Reduction","Fuel Use Reduction",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[hard coal es]","Fuel Use Reduction - Electricity: Hard Coal",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[natural gas nonpeaker es]","Fuel Use Reduction - Electricity: Natural Gas Nonpeaker",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[nuclear es]","Fuel Use Reduction - Electricity: Nuclear",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[biomass es]","Fuel Use Reduction - Electricity: Biomass",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[natural gas peaker es]","Fuel Use Reduction - Electricity: Natural Gas Peaker",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Electricity Fuel Use Perc Reduction[lignite es]","Fuel Use Reduction - Electricity: Lignite",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[cement and other carbonates]","Fuel Use Reduction - Industry: Cement",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[natural gas and petroleum systems]","Fuel Use Reduction - Industry: Natural Gas and Petroleum",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[iron and steel]","Fuel Use Reduction - Industry: Iron and Steel",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[chemicals]","Fuel Use Reduction - Industry: Chemicals",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[mining]","Fuel Use Reduction - Industry: Mining",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[waste management]","Fuel Use Reduction - Industry: Waste Management",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[agriculture]","Fuel Use Reduction - Industry: Agriculture",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Industry Fuel Use Perc Reduction[other industries]","Fuel Use Reduction - Industry: Other Industries",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[battery electric vehicle]","Fuel Use Reduction - Vehicles: Battery Electric",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[natural gas vehicle]","Fuel Use Reduction - Vehicles: Natural Gas",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[gasoline vehicle]","Fuel Use Reduction - Vehicles: Gasoline Engine",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[diesel vehicle]","Fuel Use Reduction - Vehicles: Diesel Engine",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[plugin hybrid vehicle]","Fuel Use Reduction - Vehicles: Plug-in Hybrid",[0,0.4],"RnD Fuel Use Reductions"),
	(False,"RnD Transportation Fuel Use Perc Reduction[nonroad vehicle]","Fuel Use Reduction - Vehicles: Non-road",[0,0.4],"RnD Fuel Use Reductions")
)

# Building the Policy List
# ------------------------
# Every policy, whether enabled or not, appears in a tuple called "PotentialPolicies" that was constructed above.
# Now we construct the actual list of policies to be included (named "Policies") by
# checking which of the policies have been enabled.

Policies = []
for PotentialPolicy in PotentialPolicies:
	if PotentialPolicy[Enabled]:
		Policies.append(PotentialPolicy)


# Exit with an error if no policies were enabled in the script.  We write the error to the output
# file because it's likely a user will run this without a console and won't be able to see the
# message produced by sys.exit()
if len(Policies) < 1:
	f = open(OutputScript, 'w')
	ErrorMessage = "Error: No policies were enabled in the Python script.  Before running the script, you must enable at least one policy."
	f.write(ErrorMessage)
	f.close()
	import sys
	sys.exit(ErrorMessage)


# Building the Groups List
# ------------------------
# We create a list of all the unique groups that are used by enabled policies.
Groups = []
for Policy in Policies:
	if Policy[Group] not in Groups:
		Groups.append(Policy[Group])


# Generate Vensim Command Script
# ------------------------------
# We begin by creating a new file to serve as the Vensim command script (overwriting
# any older version at that filename).  We then tell Vensim to load
# the model file, and we give it a RUNNAME that will be used for all runs.  (It is
# overwritten each run.)
f = open(OutputScript, 'w')
f.write('SPECIAL>LOADMODEL|"' + ModelFile + '"\n')
f.write("SIMULATE>RUNNAME|" + RunName + "\n")

# The following options may be useful in certain cases, but they cause Vensim to
# produce an output window for each simulation that acknowledges the completion of
# the command.  These output windows accumulate over the course of many runs and
# cause slow-downs (and potentially crashes).  Therefore, these lines are usually
# best left commented out, unless you are doing only a few runs.
# f.write("SPECIAL>NOINTERACTION\n")
# f.write("SIMULATE>SAVELIST|" + OutputVarsFile + "\n")
f.write("\n")

def PerformRunsWithEnabledGroups():

	# First, we do a run with all of the groups disabled
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|||||:")
	f.write("\tEnabledPolicyGroup=None")
	f.write("\tEnabledPolicies=None\n\n")

	# Next, we do a run with each group enabled in turn
	for EnabledGroup in Groups:

		# We create an empty string that we'll use to track the policies enabled in each group
		EnabledPolicies=""

		# We activate policies if their group name matches the currently enabled group
		for Policy in Policies:
			if Policy[Group] == EnabledGroup:
				f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
				# We add the policy to the EnabledPolicies string
				if len(EnabledPolicies) > 0:
					EnabledPolicies += ", "
				EnabledPolicies += Policy[ShortName]

		# We include a SETVAL instruction to select the correct policy implementation schedule file
		f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
		
		# We perform our run and log the output
		f.write("MENU>RUN|O\n")
		f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
		f.write("\tEnabledPolicyGroup=" + str(EnabledGroup))
		f.write("\tEnabledPolicies=" + EnabledPolicies + "\n\n")
	
	# Finally, we do a run with all of the policy groups enabled (a full policy case run)
	
	# We include a SETVAL instruction to select the correct policy implementation schedule file
	f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
	
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
	f.write("\tEnabledPolicyGroup=All")
	f.write("\tEnabledPolicies=All\n\n")
	
def PerformRunsWithDisabledGroups():

	# First, we do a run with all of the groups enabled
	for Policy in Policies:
		f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
	
	# We include a SETVAL instruction to select the correct policy implementation schedule file
	f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
	
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|||||:")
	f.write("\tDisabledPolicyGroup=None")
	f.write("\tDisabledPolicies=None\n\n")

	# Next, we do a run with each group disabled in turn
	for DisabledGroup in Groups:

		# We create an empty string that we'll use to track the policies disabled in each group
		DisabledPolicies=""

		# We activate policies if their group name does not match the currently disabled group
		for Policy in Policies:
			if Policy[Group] != DisabledGroup:
				f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
			# Otherwise, we add the policy to the DisabledPolicies string
			else:
				if len(DisabledPolicies) > 0:
					DisabledPolicies += ", "
				DisabledPolicies += Policy[ShortName]
		
		# We include a SETVAL instruction to select the correct policy implementation schedule file
		f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
		
		# We perform our run and log the output
		f.write("MENU>RUN|O\n")
		f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
		f.write("\tDisabledPolicyGroup=" + str(DisabledGroup))
		f.write("\tDisabledPolicies=" + DisabledPolicies + "\n\n")
	
	# Finally, we do a run with all of the groups disabled (a BAU case run)
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdf|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
	f.write("\tDisabledPolicyGroup=All")
	f.write("\tDisabledPolicies=All\n\n")
	
if EnableOrDisableGroups == "Enable":
	PerformRunsWithEnabledGroups()
else:
	PerformRunsWithDisabledGroups()

# We are done writing the Vensim command script and therefore close the file.
f.close()