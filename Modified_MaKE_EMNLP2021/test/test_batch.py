import subprocess
'''
    "gen_MaKE_res.py",
    "gen_wo_sns.py",
    "gen_no_plan.py",
'''
test = [    
    "gen_wo_symbolic.py",
]

for program in test:
    subprocess.call(['python', program])
    print("Finished:" + program)
