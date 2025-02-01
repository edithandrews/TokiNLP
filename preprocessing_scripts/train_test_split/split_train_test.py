import random
from conllu import parse

def read_conllu_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        conllu_data = file.read()
    # Parse the CONLL-U data using the conllu library
    return parse(conllu_data)

def write_conllu_file(sentences, file_path):

    id = 1
    for sentence in sentences:
        sentence.metadata["sent_id"] = str(id)
        id = id+1

    with open(file_path, 'w', encoding='utf-8') as file:
        # Write the parsed and shuffled sentences back to the file
        file.write(''.join(sentence.serialize() for sentence in sentences))

def shuffle_sentences(sentences):
    # Shuffle the list of sentences randomly
    random.shuffle(sentences)
    
    # Assign new sentence IDs based on the shuffled order
    for idx, sentence in enumerate(sentences):
        for token in sentence:
            token['id'] = str(idx + 1)  # Set the sentence ID to the new order
    return sentences

def shuffle_and_split(sentences, ratio):
    """
    Shuffle the list and split it into two lists according to the given ratio.
    
    Args:
    - lst: The list to be shuffled and split.
    - ratio: A tuple (x, y) that specifies the ratio in which to split the list.
    
    Returns:
    - A tuple of two lists, split according to the given ratio.
    """
    # Shuffle the list
    random.shuffle(sentences)
    
    # Calculate the index for the split based on the ratio
    total_len = len(sentences)
    split_index = int(total_len * ratio[0] / (ratio[0] + ratio[1]))
    
    # Split the list into two parts
    list1 = sentences[:split_index]
    list2 = sentences[split_index:]

    write_conllu_file(list1, "train.connlu")
    write_conllu_file(list2, "dev.connlu")
    
    return list1, list2

def main(input_file, output_file):
    # Read the CONLL-U file using conllu
    data = read_conllu_file("connlu_data.connlu")
    shuffle_and_split(data, (0.8, 0.2))