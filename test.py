import argparse

parser = argparse.ArgumentParser()
parser.add_argument('argument1', help='the 1st argument')
parser.add_argument('argument2', help='the 2nd argument')


all_arguments = parser.parse_args()

arguments1 = all_arguments.argument1
arguments2 = all_arguments.argument2

print(f"arguments1: {arguments1}")
print(f"arguments1_type: {type(arguments1)}")

print(f"arguments2: {arguments2}")
print(f"arguments2_type: {type(arguments2)}")

# print(f"{type(arguments1)}

