import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    if field not in {"unordered_numbers", "ordered_numbers","dna_sequence"}:
        return None

    file_path=os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        seq=json.load(json_file)
        return seq[field]


def linear_search(seq, number):
    indices=[]
    count=[]
    idx=0
    while idx<len(seq):
        if seq[idx]==number:
            indices.append(idx)
            count+=1
        idx+=1
    return {"position":indices,
            "count":count,}

def pattern_search(seq, pattern):
    indices=set()
    pattern_size=len(pattern)
    left_idx=0
    pattern_size=len(pattern)
    left_idx=0
    righ_idx=pattern_size
    while righ_idx<len(seq):
        for idx in range(pattern_size):
            if pattern[idx]!=seq[left_idx+idx]:
                break
        else:
            indices.add(left_idx+pattern_size//2)
        left_idx+=1
        righ_idx+=1
    return indices



def main():
    pass


if __name__ == '__main__':
    main()