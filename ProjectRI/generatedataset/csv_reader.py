import csv
from generatedataset.data_structures import celebrities, celebrities_followers, followers, followers_following
from generatedataset.save_dataset_file import SaveDataSetFile

csv.field_size_limit(100000000)


class CsvReader:

    def __init__(self, csv_path=None):
        self.csv_path = csv_path

    def read_csv(self):
        csv_content = []
        with open(self.csv_path, newline='', encoding="utf8") as File:
            reader = csv.reader(File)
            for row in reader:
                csv_content.append(row)
        return csv_content

    def save_data(self, csv_content):
        csv_header = csv_content[0]
        username_idx, id_user_idx, query_idx = self.get_id_csv_header(csv_header, ['username', 'id', 'query'])
        csv_content = csv_content[1:]
        celebrity_url = csv_content[0][query_idx]
        celebrity_id = self.get_celebrity_name(celebrity_url)
        for line in csv_content:
            if str(celebrity_url) != line[query_idx]:
                celebrity_id = self.get_celebrity_name(line[query_idx])
                celebrity_url = line[query_idx]
            if line[id_user_idx]:
                followers[int(line[id_user_idx])] = line[username_idx]
                if not followers_following.get(line[id_user_idx]):
                    followers_following[int(line[id_user_idx])] = [celebrity_id]
                else:
                    lista = followers_following.get(line[id_user_idx])
                    lista.append(celebrity_id)
                    followers_following[int(line[id_user_idx])] = lista
                if not celebrities_followers.get(celebrity_id):
                    celebrities_followers[int(celebrity_id)] = [int(line[id_user_idx])]
                else:
                    lista = celebrities_followers.get(celebrity_id)
                    lista.append(int(line[id_user_idx]))
                    celebrities_followers[int(celebrity_id)] = lista
        return followers, followers_following, celebrities_followers

    def get_celebrity_name(self, query):
        query = str(query).replace('https://www.instagram.com/', '')
        print("Saving followers of", query)
        return celebrities.get(query)

    def get_id_csv_header(self, header, column_names):
        column_idx = []
        for column_name in range(len(column_names)):
            column_idx.append(header.index(column_names[column_name]))
        return column_idx


path = 'C:/Users/bryal/OneDrive/Escritorio/Maestría CICESE/Recuperación de Información/'
extension = '.csv'
file_names = ['Alvarito', 'AndreMarin', 'Aristegui', 'Brozo', 'CarlosGuerrero', 'carlosloret', 'Doriga', 'LCLKHSD',
              'Martinoli part2', 'Martinoli', 'periodistas-1', 'PeriodistasDeportivos-1', 'PeriodistasDeportivos-2',
              'Superman', 'WWyW']
new = CsvReader()
for file_name in file_names:
    file_path = path + file_name + extension
    setattr(new, 'csv_path', file_path)
    reader = new.read_csv()
    new.save_data(reader)

save_data = SaveDataSetFile("../project/dataset/dataset.txt")
save_data.generate_data_set_file(celebrities, followers, celebrities_followers, followers_following)
