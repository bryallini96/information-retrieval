file_path = 'dataset/dataset.txt'


def load_data():
    file_content = read_file()
    celebrities = dict(zip(file_content[0].split(), [int(i) for i in file_content[1].split()]))
    followers = dict(zip([int(i) for i in file_content[2].split()], file_content[3].split()))

    limit = 4 + len(celebrities) * 2

    celebrity_ids = []
    followers_ids = []
    for i in range(4, limit, 2):
        celebrity_ids.append(int(file_content[i]))
        followers_ids.append([int(i) for i in file_content[i + 1].split()])

    celebrities_followers = dict(zip(celebrity_ids, followers_ids))

    followers_id = []
    following_id = []
    for i in range(limit, len(file_content) - 2, 2):
        followers_id.append(int(file_content[i]))
        following_id.append([int(i) for i in file_content[i + 1].split()])

    followers_following = dict(zip(followers_id, following_id))

    return dict(celebrities=celebrities, followers=followers, celebrities_followers=celebrities_followers,
                followers_following=followers_following)


def read_file():
    file = open(file_path)
    file_content = file.read().strip().split('\n')
    file.close()
    return file_content