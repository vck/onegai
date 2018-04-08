import sys
import csv
import random
import string
import numpy as np

columns = string.ascii_lowercase

def generate_data(nums=100, cols=4):

	"""
	generate data with size nums

	:args
	nums: int -> how many rows?
	cols: int -> how many columns?
	"""
	data = np.random.randn(nums, cols)

	return data


def generate_column_name(size):
	
	column = [random.choice(columns) for _ in range(size)]
	return column


if __name__ == '__main__':
	
	size = int(sys.argv[1])
	col = int(sys.argv[2])
	filename = sys.argv[3]


	data = generate_data(nums=size, cols=col)
	print(f'generating data with col={col} and size={size} to={filename}')
	
	data = data.tolist()

	header = generate_column_name(col)

	print('reading file...')
	with open(filename, 'a') as __file:
		writer = csv.writer(__file)
			
		writer.writerow(header)
		
		print('writing data...')	
		for row in data:
			writer.writerow(row)

	print(f'data has been written to {filename}')

