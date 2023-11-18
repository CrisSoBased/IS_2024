from csv_to_xml_converter import CSVtoXMLConverter
import os
if __name__ == "__main__":
    
    file_path = "C:/Users/crist/Downloads/IS_2024-master/IS_2024-master/docker/volumes/data/all_players.csv"
    
    # Verifique se o arquivo existe antes de criar o conversor
    if not os.path.exists(file_path):
        print(f"O arquivo '{file_path}' não foi encontrado.")
    else:
        converter = CSVtoXMLConverter(file_path)
        print(converter.to_xml_str())
