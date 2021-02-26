import json


'''
    I did'nt know how many files will be merged
    to each other, so that i had considered arbitrary
    quanity*. 

    This peace of code may be ugly but can hadlle
    mumerous files, show matches, count them and 
    remove blocks with similar items.
'''


class NoFileToProcess(Exception):

    message = "root - ERROR - File doesn't exists"

    def __init__(self, message=message):
        self.message = message

    def __str__(self):
        return str(self.message)


# def parse_user(output_file, *input_files):
def parse_user(output_file, *input_files):
    try:
        # forming a list of json files
        list_of_files = [i for i in input_files]
        condition = len(list_of_files) > 0

        # list to fullfill unique items
        data = []

        if condition:
            for json_file in list_of_files:
                with open(json_file, "r") as file:
                    line = json.load(file)
                    data.extend(line)

                    # assighning the counter
                    counter = 0
                    for i in range(len(data)):

                        # checking dicts for similar items
                        for dic in data:
                            for pair in list(dic.items()):
                                i = i + 1
                                if i + 1 > len(data):
                                    break

                                # assighn the match
                                match = pair in list(data[i].items())

                                # detecting, depicting match
                                if match:
                                    counter += 1
                                    print(
                                        f'Next item detected: {(list(data[i].items()))} and was removed')

                                    # removing the whole item when a match
                                    data.remove(dic)
                                    data = sorted(
                                        data, key=lambda i: i['name'])

            print(f'Number of matches: {counter}')

            # checking the data
            json_data = json.dumps(data, indent=2)

            # recording of procesed data
            with open(output_file, 'w') as file:
                json.dump(json_data, file)

            return json_data

        if not condition:
            raise NoFileToProcess

    except NoFileToProcess as er:
        er = str(er)
        return er[:er.index('d')] + str(output_file) + ' ' + er[er.index('d'):]


# output file
output_file = 'user3.json'

# input files
f1 = 'user1.json'
f2 = 'user2.json'

print(parse_user(output_file, 'user1.json', 'user2.json'))
