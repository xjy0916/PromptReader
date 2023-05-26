import numpy as np
import torch
import spacy
nlp = spacy.load('en_core_web_sm')

def dataset_process():
    all_vocab = ['<pad>']
    all_emb = [[0.] * 300]
    text_lines = ['5-years']
    for word in text_lines:
        doc = nlp(word)
        for item in doc:
            if item.text not in all_vocab:
                all_vocab.append(item.text)
    print(all_vocab)




if __name__ == '__main__':
    dataset_process()
