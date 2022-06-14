import os

data_path = os.path.join('.', 'data')
binding_seqs = os.path.join(data_path, 'peak_data.txt')
control_seqs = os.path.join(data_path, 'shuffled_data.txt')
data_header = ['genome', 'chrom', 'chrom_start', 'chrom_stop', 'name', 'strength', 'orientation', 'sequence']
cleanded_data = os.path.join(data_path, 'cleaned.csv')
