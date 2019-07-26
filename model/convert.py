import json
import logging
import sys


def Stanford_to_dataturks_format(path_to_stanford_ner_data, output_json_file_path, unknown_label):
    try:
        f = open(path_to_stanford_ner_data, 'r')  # input file in Stanford NER format
        fp = open(output_json_file_path, 'w')  # output format in Dtaturks JSON File
        data_dict = {}
        annotations = []
        label_dict = {}
        entities = []
        training_data = []
        s = ''
        start = 0
        for line in f:
            if line != '\n':
                word, entity = line.split('\t')
                entities.append((0, len(word) - 1, entity))
                training_data.append((word + " is a " + entity.replace("\n", ""),
                                      {"entities": [(0, len(word) - 1, entity.replace("\n", ""))]}))

                # json.dump(training_data, fp)
                # fp.write('\n')

                print ((word + " is a " + entity.replace("\n", ""), {"entities": [(0, len(word) - 1, entity.replace("\n", ""))]}))
            else:
                data_dict['content'] = s
                s = ''
                # create groups of points having same text
                label_list = []
                for ents in list(label_dict.keys()):
                    for i in range(len(label_dict[ents])):
                        if (label_dict[ents][i]['text'] != ''):
                            l = [ents, label_dict[ents][i]]
                            for j in range(i + 1, len(label_dict[ents])):
                                if (label_dict[ents][i]['text'] == label_dict[ents][j]['text']):
                                    di = {}
                                    di['start'] = label_dict[ents][j]['start']
                                    di['end'] = label_dict[ents][j]['end']
                                    di['text'] = label_dict[ents][i]['text']
                                    l.append(di)
                                    label_dict[ents][j]['text'] = ''
                            label_list.append(l)

                for entities in label_list:
                    label = {}
                    label['label'] = [entities[0]]
                    label['points'] = entities[1:]
                    annotations.append(label)
                data_dict['annotation'] = annotations
                annotations = []
                # one json object for a training sample written to output file
                json.dump(data_dict, fp)
                fp.write('\n')
                data_dict = {}
                start = 0
                label_dict = {}
        json.dump(training_data, fp)
        fp.write('\n')
    except Exception as e:
        logging.exception("Unable to process file" + "\n" + "error = " + str(e))
        return None


if (len(sys.argv) < 2):
    print(
        "Please provide input and output data path and the label used for tagging as unknown entities as arguments in order")
    exit(0)
Stanford_to_dataturks_format(sys.argv[1], sys.argv[2], sys.argv[3])
