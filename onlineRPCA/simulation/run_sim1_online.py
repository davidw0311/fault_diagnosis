# -*- coding: utf-8 -*-
"""
Created on Thu May 05 16:21:40 2016

@author: wexiao
"""
from sim1 import simulation
import pickle

# define parameters
pms = {}
pms['method'] = 'online'

pms['m'] = 40
pms['n'] = 500
pms['r'] = [10, 50]
pms['rho'] = [0.01, 0.1]
pms['nrep'] = 50
pms['seed'] = 12345

pms['burnin'] = 200
pms['win_size'] = 200
pms['track_cp_burnin'] = 200
pms['n_check_cp'] = 20
pms['alpha'] = 0.01
pms['proportion'] = 0.5
pms['n_positive'] = 3
pms['min_test_size'] = 100
pms['tolerance_num'] = 0
pms['factor'] = 1


all_results = {}
for i in range(len(pms['r'])):
	for j in range(len(pms['rho'])):
		all_results['r%d_rho%d' % (i+1, j+1)] = simulation(method=pms['method'], m=pms['m'], n=pms['n'], 
			r=pms['r'][i], rho=pms['rho'][j], nrep=pms['nrep'], seed=pms['seed'], 
		    burnin=pms['burnin'], win_size=pms['win_size'], track_cp_burnin=pms['track_cp_burnin'], n_check_cp=pms['n_check_cp'], 
		    alpha=pms['alpha'], proportion=pms['proportion'], n_positive=pms['n_positive'], min_test_size=pms['min_test_size'], 
		    tolerance_num=pms['tolerance_num'], factor=pms['factor'])

all_results['pms'] = pms

with open(r'result/all_results_sim1_online_v2.pickle', 'wb') as handle:
    pickle.dump(all_results, handle)