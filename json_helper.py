import json
import pickle


def read_json(path):
    f = open(path)

    data = json.load(f)
    # print(data)
    return data


def read_all_json_files():
    list = []
    list.append(
        read_json('/Users/dhannya/Projects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json'))
    print(list)


def write_pickle(data, path):
    with open(path, 'wb') as f:  # open a text file
        pickle.dump(student_names, f)  # serialize the list


student_names = ['Alice', 'Bob', 'Elena', 'Jane', 'Kyle']
write_pickle(student_names,
             '/Users/dhannya/Projects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/super_smash_characters.pickle')


def load_pickle(path):
    with open(path, 'rb') as f:
        student_names_loaded = pickle.load(f)  # deserialize using load()
        print(student_names_loaded)  # print student names

load_pickle('/Users/dhannya/Projects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/super_smash_characters.pickle')
