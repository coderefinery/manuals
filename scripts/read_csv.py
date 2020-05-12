#!/usr/bin/env python3

import pandas as pd
import sys

f_in = sys.argv[1]
csv = pd.read_csv(f_in)

# print email address and registration state
#for i,j in zip(csv['Email Address'],csv['Registration state']):
#    if j=='Pending':
#        print(i)

# print out email addresses
for i in csv['Email Address']:
    print(i)

# print out initials for hackmd
#for i in csv['Name']:
#    initials = "".join([name[0] for name in i.split()])
#    print('- '+initials)

