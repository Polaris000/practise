from postal.parser import parse_address
from postal.expand import expand_address
import pandas as pd

cols = ['address']
df = pd.read_csv('address_data2.csv', delimiter='\n', names=cols)
print(df)

with open('output.csv', 'w') as x:
	for i in df['address']:

		x.write(str(parse_address(i)) + '\n')

