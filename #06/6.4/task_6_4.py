import json


class Student(object):

    counter = 0
    full_name = ''
    avg_rank = 0.0
    courses = []

    def __init__(self, full_name=full_name, avg_rank=avg_rank, courses=courses):
        Student.counter += 1
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, file):
        with open(file, mode='r') as file:
            data = json.load(file)

        if isinstance(data, dict):
            return f"{data['full_name']} {data['avg_rank']} {data['courses']}"

        if isinstance(data, list):

            def extract(data):
                arr = []
                keys = ["full_name", "avg_rank", "courses"]

                for item in data:
                    for k, v in item.items():
                        if k in keys:
                            arr.append(v)
                        elif isinstance(v, (dict, list)):
                            extract(v, arr, keys)
                        else:
                            pass
                return arr
            values = extract(data)

        return values


user1 = Student.from_json('2020-01.json')
user2 = Student.from_json('2020_2.json')
print(user1)
print(user2)


class Group(object):

    def __init__(self, title=str, students=list):
        self.title = title
        self.students = students

    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):

        Group.title = str(filename)[:-5]
        Group.students = list(list_of_groups)

        return cls(Group.title,  Group.students)

    @classmethod
    def create_group_from_file(cls, students_file):
        Group.title = str(students_file)[:-5]
        with open(students_file, mode='r') as file:
            data = json.load(file)
        # return data
        if isinstance(data, dict):
            div = []
            for key, value in data.items():
                if key == 'full_name':
                    div += [value]

            return Group.title, div
        if isinstance(data, list):

            def extract(data):
                arr = []
                keys = ["full_name"]

                for item in data:
                    for k, v in item.items():
                        if k in keys:
                            arr.append(v)
                        elif isinstance(v, dict):
                            extract(data)
                        else:
                            pass
                return arr

            result = extract(data)
            return Group.title, result


g1 = Group.create_group_from_file('2020-01.json')
g2 = Group.create_group_from_file('2020_2.json')

print(g1)
print(g2)

data0 = Group.serialize_to_json([user2], '2020_2.json')
data1 = Group.serialize_to_json([user1], '2020-01.json')


json_data0 = json.dumps(data0, default=lambda o: o.__dict__, indent=4)
json_data1 = json.dumps(data1, default=lambda o: o.__dict__, indent=4)

merged = json_data0 + json_data1
print(merged)
