import subprocess
test = [    
    "gen_wo_symbolic.py",
    "gen_MaKE_res.py",
    "gen_wo_sns.py",
    "gen_no_plan.py",
]

for program in test:
    subprocess.call(['python', program])
    print("Finished:" + program)
