import pandas
import numpy
import matplotlib.pyplot as plt

class DataPreparation: 
	def __init__(self, csv_path):
		"""
		Cette classe prend en entrée un chemin de fichier csv.
		Elle split le jeu de donnée en 2 bases 
		+ une train 75 %
		+ une test 25 %
		Ce 2 bases, la classe va les splits en 2 

		+ un vecteur x (qui contient les indexs temporels)
		+ un vecteyr y (qui contient les valeurs à prédire)
		En tout cette va extraire 4 arrays.
		x_train= probleme du train
		y_train= solution train
		x_test = probleme test
		y_test = solution test
		"""
		self.dataset_df = pandas.read_csv(csv_path)
		self.dataset_df["Years"] = pandas.to_datetime(self.dataset_df["Years"])
		self.prepare_data()

	def prepare_data(self):
		number_of_rows = len(self.dataset_df)
		self.dataset_df["index_mesure"] = numpy.arange(0, number_of_rows, 1) 
		df2= pandas.get_dummies(self.dataset_df, columns=['month_name']) #get dummies
		self.dataset_df.join(df2)

		dataset_train_df = self.dataset_df.iloc[ : int(number_of_rows*0.75)] #slicing de dataframe 75% pour l'entrainement
		dataset_test_df = self.dataset_df.iloc[int(number_of_rows*0.75): ]  #slicing des 25 % restant pour les test

		self.x_train = dataset_train_df[['index_mesure','January','February','Marsh','April','May','June','July','August','September','October','November','December']].values #rajouter les 12 mois de l'année 
		self.y_train = dataset_train_df[['Sales']].values

		self.x_test = dataset_test_df[['index_mesure','January','February','Marsh','April','May','June','July','August','September','October','November','December']].values #rajouter les 12 mois
		self.y_test = dataset_test_df[['Sales']].values


	def show_graph(self):
		plt.figure(figsize=(15, 6))
		plt.plot(self.dataset_df["month"], self.dataset_df["sales"], "o:")
		plt.show()