from data_preparation import DataPreparation
from additif import Additif


csv_path = r"C:\Users\yzedira\Desktop\pypy\vente_maillots_de_bain(1).csv"
data_preparation_object = DataPreparation(csv_path) 
regression_object = Additif(data_preparation_object)

data_preparation_object.show_graph()