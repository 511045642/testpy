

class User:
    def __init__(self, user_id: int, name: str, age: int, address: str, school: str):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.address = address
        self.school = school

    def __str__(self):
        return 'ID: {}, name: {}, age: {}, address: {}, school: {}'.format(self.user_id, self.name, self.age,
                                                                           self.address, self.school)

    def __repr__(self):
        return '<User id: {}>'.format(self.user_id)


def read_db(path):
    users = []
    with open(path) as f:
        for line in f:
            line = line.strip('\n')
            if line.startswith('#'):
                continue
            cells = line.split('\t')
            user = User(int(cells[0]), cells[1], int(cells[2]), cells[3], cells[4])
            users.append(user)
    return users


users = read_db('E:/test.txt')
print(users)

users = sorted(users, key=lambda x: x.school)

print(users)

for user in users:
    print(user)
