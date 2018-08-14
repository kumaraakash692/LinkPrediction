import networkx.generators.random_graphs as rangr
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import random
from gem.evaluation import evaluation_measures
from gem.utils import train_test_split, graph_util, evaluation_util
from gem.embedding.lap	 import LaplacianEigenmaps
from gem.embedding.hope     import HOPE
from gem.embedding.node2vec import node2vec
from gem.embedding.verse import verse
import sys
import pickle
from gem.evaluation import metrics as scores
import csv
import pandas

list_graphs = ['gem/data/vk_2016']
list_graphs1 = ['gem/data/vk_2017']
list_directed = [True]
fig_name = ['VK']

dimensions=[2,4,8,16,32,64,128]
num_samples=5

# MAP for supervised 

# for fig in xrange(len(fig_name)):

# 	MAP1_DEEPWALK=np.zeros((len(dimensions),num_samples))
# 	MAP1_n2vA=np.zeros((len(dimensions),num_samples))
# 	MAP1_n2vB=np.zeros((len(dimensions),num_samples))
# 	MAP1_VERSE=np.zeros((len(dimensions),num_samples))
# 	MAP1_us=np.zeros((1,num_samples))

# 	MAP2_DEEPWALK=np.zeros((len(dimensions),num_samples))
# 	MAP2_n2vA=np.zeros((len(dimensions),num_samples))
# 	MAP2_n2vB=np.zeros((len(dimensions),num_samples))
# 	MAP2_VERSE=np.zeros((len(dimensions),num_samples))
# 	MAP2_us=np.zeros((1,num_samples))

# 	for it1 in xrange(num_samples):

# 		file_name='SAVER_TE_SUP/'+fig_name[fig]+'/graph_and_samples.p'
# 		parameter_file=open(file_name, 'rb')
# 		train_digraph = pickle.load(parameter_file)
# 		train_digraph1 = pickle.load(parameter_file)
# 		test_digraph =  pickle.load(parameter_file)
# 		parameter_file.close()
		
# 		trp, trn = evaluation_measures.create_edge_dataset(train_digraph, train_digraph1)
# 		test_digraph1, node_l = graph_util.sample_graph(test_digraph, 1024)

# 		print ("evaluating for VERSE")
# 		for it2 in xrange(len(dimensions)):
# 			train_digraph_temp=train_digraph.copy()
# 			print (it1,it2)
# 			dim=dimensions[it2]		
# 			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/VERSE1_'+str(dim)
# 			parameter_file=open(file_name, 'rb')
# 			X1 = pickle.load(parameter_file)
# 			parameter_file.close()
# 			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/VERSE2_'+str(dim)
# 			parameter_file=open(file_name, 'rb')
# 			X2 = pickle.load(parameter_file)
# 			parameter_file.close()
# 			embedding=verse(d=dim, alpha=0.85, threads=3, nsamples=3)
# 			MAP1_VERSE[it2][it1],MAP2_VERSE[it2][it1] = evaluation_measures.calc_map_s(embedding, X1, X2, train_digraph_temp, train_digraph1, node_l, test_digraph1, trp, trn, 1)

# 		print ("evaluating for DEEPWALK")
# 		for it2 in xrange(len(dimensions)):
# 			train_digraph_temp=train_digraph.copy()
# 			print (it1,it2)
# 			dim=dimensions[it2]		
# 			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/DEEPWALK1_'+str(dim)
# 			parameter_file=open(file_name, 'rb')
# 			X1 = pickle.load(parameter_file)
# 			parameter_file.close()
# 			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/DEEPWALK2_'+str(dim)
# 			parameter_file=open(file_name, 'rb')
# 			X2 = pickle.load(parameter_file)
# 			parameter_file.close()
# 			embedding=node2vec(d=dim, max_iter=1, walk_len=80, num_walks=10, con_size=10, ret_p=1, inout_p=1)
# 			MAP1_DEEPWALK[it2][it1],MAP2_DEEPWALK[it2][it1] = evaluation_measures.calc_map_s(embedding, X1, X2, train_digraph_temp, train_digraph1, node_l, test_digraph1, trp, trn, 0)

# 		print ("evaluating for n2vA")
# 		for it2 in xrange(len(dimensions)):
# 			train_digraph_temp=train_digraph.copy()
# 			print (it1,it2)
# 			dim=dimensions[it2]		
# 			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/n2vA1_'+str(dim)
# 			parameter_file=open(file_name, 'rb')
# 			X1 = pickle.load(parameter_file)
# 			parameter_file.close()
# 			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/n2vA2_'+str(dim)
# 			parameter_file=open(file_name, 'rb')
# 			X2 = pickle.load(parameter_file)
# 			parameter_file.close()
# 			embedding=node2vec(d=dim, max_iter=1, walk_len=80, num_walks=10, con_size=10, ret_p=4, inout_p=0.5)
# 			MAP1_n2vA[it2][it1],MAP2_n2vA[it2][it1] = evaluation_measures.calc_map_s(embedding, X1, X2, train_digraph_temp, train_digraph1, node_l, test_digraph1, trp, trn, 0)

# 		print ("evaluating for n2vB")
# 		for it2 in xrange(len(dimensions)):
# 			train_digraph_temp=train_digraph.copy()
# 			print (it1,it2)
# 			dim=dimensions[it2]		
# 			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/n2vB1_'+str(dim)
# 			parameter_file=open(file_name, 'rb')
# 			X1 = pickle.load(parameter_file)
# 			parameter_file.close()
# 			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/n2vB2_'+str(dim)
# 			parameter_file=open(file_name, 'rb')
# 			X2 = pickle.load(parameter_file)
# 			parameter_file.close()
# 			embedding=node2vec(d=dim, max_iter=1, walk_len=80, num_walks=10, con_size=10, ret_p=0.5, inout_p=4)
# 			MAP1_n2vB[it2][it1],MAP2_n2vB[it2][it1] = evaluation_measures.calc_map_s(embedding, X1, X2, train_digraph_temp, train_digraph1, node_l, test_digraph1, trp, trn, 0)
		
# 		print ("evaluating for heuristic")
# 		train_digraph_temp=train_digraph.copy()
# 		MAP1_us[0][it1],MAP2_us[0][it1] = evaluation_measures.calc_map_heu_s(node_l, train_digraph_temp, train_digraph1, test_digraph1, trp, trn)

# 	mean_DEEPWALK = np.mean(MAP1_DEEPWALK,axis=1)
# 	std_DEEPWALK = np.std(MAP1_DEEPWALK,axis=1)
# 	mean_n2vA = np.mean(MAP1_n2vA,axis=1)
# 	std_n2vA = np.std(MAP1_n2vA,axis=1)
# 	mean_n2vB = np.mean(MAP1_n2vB,axis=1)
# 	std_n2vB = np.std(MAP1_n2vB,axis=1)
# 	mean_VERSE = np.mean(MAP1_VERSE,axis=1)
# 	std_VERSE = np.std(MAP1_VERSE,axis=1)
# 	mean_us = np.mean(MAP1_us,axis=1)
# 	std_us = np.std(MAP1_us,axis=1)

# 	with open('MAP_S1_FINAL.csv','a') as outfile:
# 		writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
# 		writer.writerow(['MAP FOR SUPERIVSED 1']);
# 		writer.writerow([fig_name[fig]]);
# 		writer.writerow(['DEEPWALK']);writer.writerow(mean_DEEPWALK);writer.writerow(std_DEEPWALK)
# 		writer.writerow(['n2vA']);writer.writerow(mean_n2vA);writer.writerow(std_n2vA)
# 		writer.writerow(['n2vB']);writer.writerow(mean_n2vB);writer.writerow(std_n2vB)
# 		writer.writerow(['VERSE']);writer.writerow(mean_VERSE);writer.writerow(std_VERSE)
# 		writer.writerow(['heuristic']);writer.writerow(mean_us);writer.writerow(std_us)

# 	mean_DEEPWALK = np.mean(MAP2_DEEPWALK,axis=1)
# 	std_DEEPWALK = np.std(MAP2_DEEPWALK,axis=1)
# 	mean_n2vA = np.mean(MAP2_n2vA,axis=1)
# 	std_n2vA = np.std(MAP2_n2vA,axis=1)
# 	mean_n2vB = np.mean(MAP2_n2vB,axis=1)
# 	std_n2vB = np.std(MAP2_n2vB,axis=1)
# 	mean_VERSE = np.mean(MAP2_VERSE,axis=1)
# 	std_VERSE = np.std(MAP2_VERSE,axis=1)
# 	mean_us = np.mean(MAP2_us,axis=1)
# 	std_us = np.std(MAP2_us,axis=1)

# 	with open('MAP_S2_FINAL.csv','a') as outfile:
# 		writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
# 		writer.writerow(['MAP FOR SUPERIVSED 2']);
# 		writer.writerow([fig_name[fig]]);
# 		writer.writerow(['DEEPWALK']);writer.writerow(mean_DEEPWALK);writer.writerow(std_DEEPWALK)
# 		writer.writerow(['n2vA']);writer.writerow(mean_n2vA);writer.writerow(std_n2vA)
# 		writer.writerow(['n2vB']);writer.writerow(mean_n2vB);writer.writerow(std_n2vB)
# 		writer.writerow(['VERSE']);writer.writerow(mean_VERSE);writer.writerow(std_VERSE)
# 		writer.writerow(['heuristic']);writer.writerow(mean_us);writer.writerow(std_us)	


ratios = [-1,0.5]

for rat in xrange(len(ratios)):

	for fig in xrange(len(fig_name)):

		AP1_DEEPWALK=np.zeros((len(dimensions),num_samples))
		AP1_n2vA=np.zeros((len(dimensions),num_samples))
		AP1_n2vB=np.zeros((len(dimensions),num_samples))
		AP1_VERSE=np.zeros((len(dimensions),num_samples))
		AP1_us=np.zeros((1,num_samples))

		AP2_DEEPWALK=np.zeros((len(dimensions),num_samples))
		AP2_n2vA=np.zeros((len(dimensions),num_samples))
		AP2_n2vB=np.zeros((len(dimensions),num_samples))
		AP2_VERSE=np.zeros((len(dimensions),num_samples))
		AP2_us=np.zeros((1,num_samples))

		ROC1_DEEPWALK=np.zeros((len(dimensions),num_samples))
		ROC1_n2vA=np.zeros((len(dimensions),num_samples))
		ROC1_n2vB=np.zeros((len(dimensions),num_samples))
		ROC1_VERSE=np.zeros((len(dimensions),num_samples))
		ROC1_us=np.zeros((1,num_samples))

		ROC2_DEEPWALK=np.zeros((len(dimensions),num_samples))
		ROC2_n2vA=np.zeros((len(dimensions),num_samples))
		ROC2_n2vB=np.zeros((len(dimensions),num_samples))
		ROC2_VERSE=np.zeros((len(dimensions),num_samples))
		ROC2_us=np.zeros((1,num_samples))

		for it1 in xrange(num_samples):

			file_name='SAVER_TE_SUP/'+fig_name[fig]+'/graph_and_samples.p'
			parameter_file=open(file_name, 'rb')
			train_digraph = pickle.load(parameter_file)
			train_digraph1 = pickle.load(parameter_file)
			test_digraph =  pickle.load(parameter_file)
			parameter_file.close()

			trp, trn = evaluation_measures.create_edge_dataset(train_digraph, train_digraph1)
			train_digraph_temp = train_digraph.copy()
			for (st,ed) in train_digraph1.edges():
				train_digraph_temp.add_edge(st,ed)
	
			sample_edges = evaluation_measures.sample_edge_new(train_digraph_temp,test_digraph,ratios[rat])
			
			print ("evaluating for heuristic")
			train_digraph_temp=train_digraph.copy()
			AP1_us[0][it1],AP2_us[0][it1],ROC1_us[0][it1],ROC2_us[0][it1] = evaluation_measures.calc_aproc_heu_s(train_digraph_temp, train_digraph1, test_digraph, trp, trn, sample_edges)

			print ("evaluating for DEEPWALK")
			for it2 in xrange(len(dimensions)):
				train_digraph_temp=train_digraph.copy()
				print (it1,it2)
				dim=dimensions[it2]		
				file_name='SAVER_TE_SUP/'+fig_name[fig]+'/DEEPWALK1_'+str(dim)
				parameter_file=open(file_name, 'rb')
				X1 = pickle.load(parameter_file)
				parameter_file.close()
				file_name='SAVER_TE_SUP/'+fig_name[fig]+'/DEEPWALK2_'+str(dim)
				parameter_file=open(file_name, 'rb')
				X2 = pickle.load(parameter_file)
				parameter_file.close()
				embedding=node2vec(d=dim, max_iter=1, walk_len=80, num_walks=10, con_size=10, ret_p=1, inout_p=1)
				AP1,AP2,ROC1,ROC2 = evaluation_measures.calc_aproc_s(embedding, X1, X2, train_digraph_temp, train_digraph1, test_digraph, sample_edges, trp, trn, 0)
				AP1_DEEPWALK[it2][it1] = AP1; AP2_DEEPWALK[it2][it1] = AP2;
				ROC1_DEEPWALK[it2][it1] = ROC1; ROC2_DEEPWALK[it2][it1] = ROC2

			print ("evaluating for n2vA")
			for it2 in xrange(len(dimensions)):
				train_digraph_temp=train_digraph.copy()
				print (it1,it2)
				dim=dimensions[it2]		
				file_name='SAVER_TE_SUP/'+fig_name[fig]+'/n2vA1_'+str(dim)
				parameter_file=open(file_name, 'rb')
				X1 = pickle.load(parameter_file)
				parameter_file.close()
				file_name='SAVER_TE_SUP/'+fig_name[fig]+'/n2vA2_'+str(dim)
				parameter_file=open(file_name, 'rb')
				X2 = pickle.load(parameter_file)
				parameter_file.close()
				embedding=node2vec(d=dim, max_iter=1, walk_len=80, num_walks=10, con_size=10, ret_p=4, inout_p=0.5)
				AP1,AP2,ROC1,ROC2 = evaluation_measures.calc_aproc_s(embedding, X1, X2, train_digraph_temp, train_digraph1, test_digraph, sample_edges, trp, trn, 0)
				AP1_n2vA[it2][it1] = AP1; AP2_n2vA[it2][it1] = AP2;
				ROC1_n2vA[it2][it1] = ROC1; ROC2_n2vA[it2][it1] = ROC2

			print ("evaluating for n2vB")
			for it2 in xrange(len(dimensions)):
				train_digraph_temp=train_digraph.copy()
				print (it1,it2)
				dim=dimensions[it2]		
				file_name='SAVER_TE_SUP/'+fig_name[fig]+'/n2vB1_'+str(dim)
				parameter_file=open(file_name, 'rb')
				X1 = pickle.load(parameter_file)
				parameter_file.close()
				file_name='SAVER_TE_SUP/'+fig_name[fig]+'/n2vB2_'+str(dim)
				parameter_file=open(file_name, 'rb')
				X2 = pickle.load(parameter_file)
				parameter_file.close()
				embedding=node2vec(d=dim, max_iter=1, walk_len=80, num_walks=10, con_size=10, ret_p=0.5, inout_p=4)
				AP1,AP2,ROC1,ROC2 = evaluation_measures.calc_aproc_s(embedding, X1, X2, train_digraph_temp, train_digraph1, test_digraph, sample_edges, trp, trn, 0)
				AP1_n2vB[it2][it1] = AP1; AP2_n2vB[it2][it1] = AP2;
				ROC1_n2vB[it2][it1] = ROC1; ROC2_n2vB[it2][it1] = ROC2

			print ("evaluating for VERSE")
			for it2 in xrange(len(dimensions)):
				train_digraph_temp=train_digraph.copy()
				print (it1,it2)
				dim=dimensions[it2]		
				file_name='SAVER_TE_SUP/'+fig_name[fig]+'/VERSE1_'+str(dim)
				parameter_file=open(file_name, 'rb')
				X1 = pickle.load(parameter_file)
				parameter_file.close()
				file_name='SAVER_TE_SUP/'+fig_name[fig]+'/VERSE2_'+str(dim)
				parameter_file=open(file_name, 'rb')
				X2 = pickle.load(parameter_file)
				parameter_file.close()
				embedding=verse(d=dim, alpha=0.85, threads=3, nsamples=3)
				AP1,AP2,ROC1,ROC2 = evaluation_measures.calc_aproc_s(embedding, X1, X2, train_digraph_temp, train_digraph1, test_digraph, sample_edges, trp, trn, 1)
				AP1_VERSE[it2][it1] = AP1; AP2_VERSE[it2][it1] = AP2;
				ROC1_VERSE[it2][it1] = ROC1; ROC2_VERSE[it2][it1] = ROC2

		mean_DEEPWALK = np.mean(AP1_DEEPWALK,axis=1)
		std_DEEPWALK = np.std(AP1_DEEPWALK,axis=1)
		mean_n2vA = np.mean(AP1_n2vA,axis=1)
		std_n2vA = np.std(AP1_n2vA,axis=1)
		mean_n2vB = np.mean(AP1_n2vB,axis=1)
		std_n2vB = np.std(AP1_n2vB,axis=1)
		mean_VERSE = np.mean(AP1_VERSE,axis=1)
		std_VERSE = np.std(AP1_VERSE,axis=1)
		mean_us = np.mean(AP1_us,axis=1)
		std_us = np.std(AP1_us,axis=1)

		with open('AP_S1_FINAL.csv','a') as outfile:
			writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
			writer.writerow([fig_name[fig]]);
			writer.writerow([ratios[rat]]);
			writer.writerow(['AP FOR SUPERIVSED 1']);
			writer.writerow(['DEEPWALK']);writer.writerow(mean_DEEPWALK);writer.writerow(std_DEEPWALK)
			writer.writerow(['n2vA']);writer.writerow(mean_n2vA);writer.writerow(std_n2vA)
			writer.writerow(['n2vB']);writer.writerow(mean_n2vB);writer.writerow(std_n2vB)
			writer.writerow(['VERSE']);writer.writerow(mean_VERSE);writer.writerow(std_VERSE)
			writer.writerow(['heuristic']);writer.writerow(mean_us);writer.writerow(std_us)

		mean_DEEPWALK = np.mean(ROC1_DEEPWALK,axis=1)
		std_DEEPWALK = np.std(ROC1_DEEPWALK,axis=1)
		mean_n2vA = np.mean(ROC1_n2vA,axis=1)
		std_n2vA = np.std(ROC1_n2vA,axis=1)
		mean_n2vB = np.mean(ROC1_n2vB,axis=1)
		std_n2vB = np.std(ROC1_n2vB,axis=1)
		mean_VERSE = np.mean(ROC1_VERSE,axis=1)
		std_VERSE = np.std(ROC1_VERSE,axis=1)
		mean_us = np.mean(ROC1_us,axis=1)
		std_us = np.std(ROC1_us,axis=1)

		with open('ROC_S1_FINAL.csv','a') as outfile:
			writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
			writer.writerow([fig_name[fig]]);
			writer.writerow([ratios[rat]]);
			writer.writerow(['ROC for SUPERIVSED 1']);
			writer.writerow(['DEEPWALK']);writer.writerow(mean_DEEPWALK);writer.writerow(std_DEEPWALK)
			writer.writerow(['n2vA']);writer.writerow(mean_n2vA);writer.writerow(std_n2vA)
			writer.writerow(['n2vB']);writer.writerow(mean_n2vB);writer.writerow(std_n2vB)
			writer.writerow(['VERSE']);writer.writerow(mean_VERSE);writer.writerow(std_VERSE)
			writer.writerow(['heuristic']);writer.writerow(mean_us);writer.writerow(std_us)

		mean_DEEPWALK = np.mean(AP2_DEEPWALK,axis=1)
		std_DEEPWALK = np.std(AP2_DEEPWALK,axis=1)
		mean_n2vA = np.mean(AP2_n2vA,axis=1)
		std_n2vA = np.std(AP2_n2vA,axis=1)
		mean_n2vB = np.mean(AP2_n2vB,axis=1)
		std_n2vB = np.std(AP2_n2vB,axis=1)
		mean_VERSE = np.mean(AP2_VERSE,axis=1)
		std_VERSE = np.std(AP2_VERSE,axis=1)
		mean_us = np.mean(AP2_us,axis=1)
		std_us = np.std(AP2_us,axis=1)

		with open('AP_S2_FINAL.csv','a') as outfile:
			writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
			writer.writerow([fig_name[fig]]);
			writer.writerow([ratios[rat]]);
			writer.writerow(['AP FOR SUPERIVSED 2']);
			writer.writerow(['DEEPWALK']);writer.writerow(mean_DEEPWALK);writer.writerow(std_DEEPWALK)
			writer.writerow(['n2vA']);writer.writerow(mean_n2vA);writer.writerow(std_n2vA)
			writer.writerow(['n2vB']);writer.writerow(mean_n2vB);writer.writerow(std_n2vB)
			writer.writerow(['VERSE']);writer.writerow(mean_VERSE);writer.writerow(std_VERSE)
			writer.writerow(['heuristic']);writer.writerow(mean_us);writer.writerow(std_us)

		mean_DEEPWALK = np.mean(ROC2_DEEPWALK,axis=1)
		std_DEEPWALK = np.std(ROC2_DEEPWALK,axis=1)
		mean_n2vA = np.mean(ROC2_n2vA,axis=1)
		std_n2vA = np.std(ROC2_n2vA,axis=1)
		mean_n2vB = np.mean(ROC2_n2vB,axis=1)
		std_n2vB = np.std(ROC2_n2vB,axis=1)
		mean_VERSE = np.mean(ROC2_VERSE,axis=1)
		std_VERSE = np.std(ROC2_VERSE,axis=1)
		mean_us = np.mean(ROC2_us,axis=1)
		std_us = np.std(ROC2_us,axis=1)

		with open('ROC_S2_FINAL.csv','a') as outfile:
			writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
			writer.writerow([fig_name[fig]]);
			writer.writerow([ratios[rat]]);
			writer.writerow(['ROC for SUPERIVSED 2']);
			writer.writerow(['DEEPWALK']);writer.writerow(mean_DEEPWALK);writer.writerow(std_DEEPWALK)
			writer.writerow(['n2vA']);writer.writerow(mean_n2vA);writer.writerow(std_n2vA)
			writer.writerow(['n2vB']);writer.writerow(mean_n2vB);writer.writerow(std_n2vB)
			writer.writerow(['VERSE']);writer.writerow(mean_VERSE);writer.writerow(std_VERSE)
			writer.writerow(['heuristic']);writer.writerow(mean_us);writer.writerow(std_us)


# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

