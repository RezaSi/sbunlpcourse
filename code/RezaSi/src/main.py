from hazm import *
import os


def generate_output(input_file, output_file):
    input_file = open(input_file, "r")
    output_file = open(output_file, "w+")

    input_str = input_file.read()
    sentences = sent_tokenize(input_str)

    stemer = Stemmer()
    normalizer = Normalizer()
    lematizer = Lemmatizer()

    for sent in sentences:
        tokens = word_tokenize(sent)
        counter = 0
        for token in tokens:
            output_file.write(str(counter) + "\t" + normalizer.normalize(token).replace("_", u'\u200c') +
                              "\t" + stemer.stem(token).replace("_", u'\u200c') +
                              "\t" + lematizer.lemmatize(token).split("#")[0] + "\t_\t_")
            output_file.write("\n")
            counter += 1
        output_file.write("\n")


path = '../../sbunlpcourse/data'
files = os.scandir(path)

for file in files:
    if file.is_dir():
        print('Processing Folder : ', file.name)
        input_file = path + '/' + file.name + '/' + file.name + '.txt'
        output_file = path + '/' + 'RezaSi' + '/' + file.name + '.out'
        if os.path.isfile(input_file):
            generate_output(input_file, output_file)
        else:
            print('Warning folder ' + file.name + ' Missing input file')
