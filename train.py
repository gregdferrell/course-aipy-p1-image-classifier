# Script to train a neural network on the given data directory. Prints out training loss, validation loss, and
# validation accuracy as the network trains.
#
# Basic usage: python train.py data_dir
#
# Options:
# - Set directory to save checkpoints: python train.py data_dir --save_dir save_directory
# - Choose architecture: python train.py data_dir --arch "vgg13"
# - Set hyperparameters: python train.py data_dir --learning_rate 0.01 --hidden_units 512 --epochs 20
# - Use GPU for training: python train.py data_dir --gpu

import argparse


def get_input_args():
	"""
	Retrieves and parses the command line arguments created and defined using the argparse module.
	:return: parse_args() -data structure that stores the command line arguments object
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("data_dir", help="the directory where the image data is stored", default="images")
	parser.add_argument("-sd", "--save_dir", help="the directory to save the training checkpoint", default=".")
	parser.add_argument("-a", "--arch", help="the neural network architecture to use",
						choices=["vgg11", "vgg13", "vgg16", "vgg19"], default="vgg16")
	parser.add_argument("-lr", "--learning_rate", help="the learning rate of the network when training", type=float,
						default=.0001)
	parser.add_argument("-dr", "--dropout_rate", help="the dropout rate of the network when training", type=float,
						default=.2)
	parser.add_argument("-hu", "--hidden_units", help="the number of hidden units in the network", default=12544)
	parser.add_argument("-e", "--epochs", help="the number of epochs to use when training", type=int, default=6)
	parser.add_argument("-g", "--gpu", help="flag to use a GPU when training", action="store_true")
	parser.add_argument("-v", "--verbose", help="flag to print verbose output", action="store_true")

	args = parser.parse_args()

	if args.verbose:
		print(f"Input args: {args}")

	return args


def main():
	args = get_input_args()


if __name__ == "__main__":
	main()