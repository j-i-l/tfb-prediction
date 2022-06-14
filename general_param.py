import os

data_path = os.path.join('.', 'data')
interim_data_path = os.path.join(data_path, 'interim')
engineered_data_path = os.path.join(data_path, 'engineered')
binding_seqs = os.path.join(data_path, 'peak_data.txt')
control_seqs = os.path.join(data_path, 'shuffled_data.txt')
data_header = ['genome', 'chrom', 'chrom_start', 'chrom_stop', 'name', 'strength', 'orientation', 'sequence']

cleanded_data = os.path.join(interim_data_path, 'cleaned.p')

kmers_data = os.path.join(engineered_data_path, 'labeled_kmers.p')

random_state = 12

# See Feature_Engineering.ipynb for details:
kmer_size = 5
ngram_nbr = 30
