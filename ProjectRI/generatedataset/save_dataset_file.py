class SaveDataSetFile:

    def __init__(self, file_path):
        self.file_path = file_path

    def generate_data_set_file(self, celebrities_dic, followers_dic, celebrities_followers_dic, followers_following_dic):
        f = open(self.file_path, "a+")
        for key in celebrities_dic.keys():
            f.write(str(key))
            f.write("\t")
        f.write('\n')

        for key in celebrities_dic.values():
            f.write(str(key))
            f.write("\t")
        f.write('\n')

        for key in followers_dic.keys():
            f.write(str(key))
            f.write("\t")
        f.write('\n')

        for key in followers_dic.values():
            f.write(str(key))
            f.write("\t")
        f.write('\n')

        for key, value in celebrities_followers_dic.items():
            f.write(str(key))
            f.write('\n')
            for i in value:
                f.write(str(i))
                f.write("\t")
            f.write('\n')

        for key, value in followers_following_dic.items():
            f.write(str(key))
            f.write('\n')
            for i in value:
                f.write(str(i))
                f.write("\t")
            f.write('\n')
        print("File Saved")