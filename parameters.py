### USER DEFINED VARIABLES ###

# DIRECTORIES
insertion_dir = '/user08/tsilva/PROJECTS/pHLIP/pHLIP-256/analysis/insertion/ASP14'
prot_dir      = '/user08/tsilva/PROJECTS/pHLIP/pHLIP-256/analysis/profile/dats_res04'
criteria_dir  = '/user08/tsilva/PROJECTS/pHLIP/pHLIP-256/analysis/profile/crit'

# pH VALUES AND REPLICATES
pH_values   = ['04.00','05.00','06.00','07.00'] # pH values need to be of str type, convertable to float type
replicates  = ['1','2','3','4','5']             # the same goes for replicate values
prot_lifetime = 10                       # tauprot of CpHMD (20); tauprot / 2 of CpHMD for pHRE

# INSERTION RANGE
min_value = -10
max_value = 10
step      = 0.5
bin_size  = 0.5

# FIT PARAMETERS
fit = "Hill"
mono_variation = 0.05
tolerance      = 0.001
cutoff         = 100 # the standard cutoff is 50 points


# EXCLUSION CRITERIA PARAMETERS
crits_names = ['dssp', 'angle1','angle2']
crits = [{'crit_min': 70,
          'crit_max': 100},
        {'crit_min': 45,
         'crit_max': 90},
         {'crit_min': 0,
         'crit_max': 30}]

output_file = "profile_RE256_all_100"

#1
#real	1m58.704s

#2 after excluding useless insertion points on reading 
#real	1m13.184s

#3 with prot_lifetime
#real	0m46.136s
