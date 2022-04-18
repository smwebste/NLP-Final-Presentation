import subprocess
'''
BAD: "train_res.py", "train_with_reg.py",
GOOD: 
'''
train = [
    "train_no_plan.py", 
    "train_no_sns.py", 
    "train_res_seed_16.py", 
    "train_no_symbolic.py", 
]

for program in train:
    subprocess.call(['python', program])
    print("Finished:" + program)