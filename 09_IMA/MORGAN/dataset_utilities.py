import os
import pickle
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import networkx as nx
import re
import config as cf
import xml.etree.ElementTree as ET
import tkinter as tk
from jinja2 import Environment, FileSystemLoader
import shutil
import random
import math
import pandas as pd
from tabulate import tabulate

import matplotlib.pyplot as plt
import pandas as pd


def preprocess_term(term):
    return term.split(',')[0].split(' ')[0].replace('(', '').replace(')', '')


def extract_operations_from_list(list):
    classes= []
    attrs = []

    for elem in list:
        list_ops = str(elem).split(' ')
        if len(list_ops) == 3:
            classes.append(f'{list_ops[0]},{list_ops[2]}')
            attrs.append(f'{list_ops[1]},{list_ops[2]}')


    return classes, attrs





def get_attributes_from_metaclass(metaclass):
    list_attrs= metaclass.split(' ')[1:-1]
    list_results=[]
    for attr in list_attrs:
        list_results.append(attr.split(',')[0].replace('(', ''))

    return list_results



def create_tuple_list(label_list, data_list):
    list_tuple=[]
    for l, d in zip(label_list, data_list):
        tuple_data = l, d
        list_tuple.append(tuple_data)

    return list_tuple

def split_dataset(filename):
    labels = []
    test_docs = []
    train_docs = []
    with open(filename, 'r', encoding='utf8', errors='ignore') as f:
        for line in f:
            if line.find('\t') != -1:
                content = line.split('\t')
                labels.append(content[0])
                graph_tot = content[1].split(" ")[:-1]
                size = (len(graph_tot * 2) / 3)
                split_test = graph_tot[int(size): -1]
                string_train = ' '.join([str(elem) for elem in graph_tot])
                string_test = ' '.join([str(elem) for elem in split_test])
                train_docs.append(string_train)
                test_docs.append(string_test)

    return train_docs, test_docs, labels


def load_file(filename):
    labels = []
    docs = []
    with open(filename,'r', encoding='utf8', errors='ignore') as f:
        for line in f:
            if line.find('\t')!=-1:
                content = line.split('\t')
                if len(content) > 0:
                    labels.append(content[0])
                    docs.append(content[1])
            else:
                content = line
                if len(content) > 0:
                    content = line.replace('event', '')
                    docs.append(content.lstrip())
    return  docs


def get_gt_classes(filename):
    docs = []
    try:
        with open(filename,'r', encoding='utf8', errors='ignore') as f:
            for line in f:
                if line.find('\t')!= -1:
                    content = line.split('\t')
                    #docs.append(content[1].split(' ')[0])
                    docs.append(tuple(content[1].split(' ')))
                else:
                    content = line
                    if len(content) > 0:
                        content = line.replace('event', '')
                        docs.append(content.lstrip())
    except:
        print(filename)
        return None
    return docs



def clean_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", "", string)
    string = re.sub(r"!", " ! ", string)
    ## nlp here ##
    #string = re.sub(r"\(", "", string)
    #string = re.sub(r"\)", "", string)
    ##
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower().split()


def find_unique_values(train_data):
    with open("unique_values.txt", "w", encoding="utf8", errors="ignore") as res:
        for train in train_data:
            attrs = train.split(" ")
            unique = set(attrs)
            for u in unique:
                res.write(u + "\n")


def preprocessing(docs):
    preprocessed_docs = []
    stemmer = PorterStemmer()
    wordnet_lemmatizer = WordNetLemmatizer()

    for doc in docs:
        clean_doc = clean_str(doc)
        new_values = []
        #print(new_values)
        preprocessed_docs.append([stemmer.stem(w) for w in clean_doc])
        #preprocessed_docs.append([wordnet_lemmatizer.lemmatize(w) for w in clean_doc])
    return preprocessed_docs


def get_vocab_train(train_docs):
    vocab = dict()
    for doc in train_docs:
        for word in doc:
            if word not in vocab:
                vocab[word] = len(vocab)
    return vocab


def get_vocab(train_docs, test_docs):
    vocab = dict()

    for doc in train_docs:
        for word in doc:
            if word not in vocab:
                vocab[word] = len(vocab)

    for doc in test_docs:
        for word in doc:
            if word not in vocab:
                vocab[word] = len(vocab)

    return vocab


def create_graphs_of_words(docs, vocab, window_size):
        graphs = list()
        for idx, doc in enumerate(docs):
            G = nx.Graph()
            for i in range(len(doc)):
                if doc[i] not in G.nodes():
                    G.add_node(doc[i])
                    G.nodes[doc[i]]['label'] = vocab[doc[i]]
            for i in range(len(doc)):
                for j in range(i + 1, i + window_size):
                    if j < len(doc):
                        G.add_edge(doc[i], doc[j])

            graphs.append(G)

        return graphs


def convert_string_to_list(list_element):
    str_format=''
    return str_format.join(list_element)


def encoding_data(train_context):

    data = load_file(train_context)
    train_preprocessed = preprocessing(data)
    find_unique_values(data)
    return train_preprocessed, data


def encoding_training_data_dump(train_context):
    train_data = load_file(train_context)
    train_preprocessed = preprocessing(train_data)
    find_unique_values(train_data)

    # Store the preprocessed data in a file using pickle
    with open(cf.DUMP_TRAIN, "wb") as f:
        pickle.dump(train_preprocessed, f)

    print("Dump successfully created")

    return train_preprocessed, train_data


def load_preprocessed_data(filename):
    with open(filename, "rb") as f:
        train_preprocessed = pickle.load(f)
    return train_preprocessed


def preprocess_test_data(test_context):
    y_test, test_data = load_file(test_context)
    test_preprocessed = preprocessing(test_data)
    return test_preprocessed


def match_operations(predicted, actual, gt_data):
    match = [value for value in predicted if value in actual]
    dict_op={}
    for op in gt_data:
        splitted_op = op.split(" ")
        for rec in match:
            if splitted_op[0] == rec:
                dict_op.update({rec: splitted_op})

    return dict_op


def success_rate(predicted, actual, n):
    if actual:
        match = [value for value in predicted if value in actual]

        if len(match) >= n:
            return 1
        else:
            return 0
    else:
        return 0



def precision(predicted,actual):
    if actual and predicted:
        true_p = len([value for value in predicted if value in actual])
        false_p = len([value for value in predicted if value not in actual])
        return (true_p / (true_p + false_p))*100
    else:
        return 0


def precision_cl(predicted, actual, specific_elements):
    if actual and predicted:
        # If specific_elements is provided, filter predicted and actual lists based on it
        if specific_elements:
            predicted = [value for value in predicted if value in specific_elements]
            actual = [value for value in actual if value in specific_elements]

        true_p = len([value for value in predicted if value in actual])
        false_p = len([value for value in predicted if value not in actual])

        # Avoid division by zero if there are no relevant predictions
        if true_p + false_p == 0:
            return 0

        return (true_p / (true_p + false_p)) * 100
    else:
        return 0


def recall_cl(predicted, actual, specific_elements):
    if actual and predicted:
        # If specific_elements is provided, filter predicted and actual lists based on it
        if specific_elements:
            predicted = [value for value in predicted if value in specific_elements]
            actual = [value for value in actual if value in specific_elements]

        true_p = len([value for value in predicted if value in actual])
        false_n = len([value for value in actual if value not in predicted])

        # Avoid division by zero if there are no relevant actual elements
        if true_p + false_n == 0:
            return 0

        return (true_p / (true_p + false_n)) * 100
    else:
        return 0


def recall(predicted,actual):
    if actual and predicted:
        # true_p = len([value for value in predicted if value in actual])
        false_n = len([value for value in actual if value not in predicted])
        true_p = len([value for value in predicted if value in actual])
        return (true_p/(true_p + false_n))*100
    else:
        return 0


def format_dict(dict):

    out_string = ""
    i = 0
    for key, value in dict.items():
        out_string += str(key)+":"+str(value)+"#"
    return out_string


def create_path_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def combine_files(input_folder, output_file):
    # Ensure the input folder exists
    output_file = output_file + '/train.txt'
    if not os.path.isdir(input_folder):
        print("Input folder does not exist")
        return

    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Iterate over each file in the directory
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            # Check if it's a file
            if os.path.isfile(file_path):
                # Open the file and read its content
                with open(file_path, 'r') as infile:
                    contents = infile.read()
                    # Write the content to the output file
                    outfile.write(contents + "\n") # Add a newline between files

def parse_xes_traces(in_path, out_path, is_train):
    create_path_if_not_exists(out_path)
    if is_train:
        with open(f"{out_path}train.txt", 'w', encoding='utf8', errors='ignore') as res:
            for file in os.listdir(in_path):
                try:
                    tree = ET.parse(in_path + file)
                    root = tree.getroot()
                    for trace in root.findall('trace'):
                        if len(trace) > 0:
                            for event in trace:
                                event_data = {'class': '', 'featureName': '', 'eventType': ''}
                                for attribute in event:
                                    key = attribute.attrib.get('key')
                                    if key in event_data:
                                        event_data[key] = attribute.attrib.get('value', '')
                                res.write(
                                    f"event\t{event_data['class']} {event_data['featureName']} {event_data['eventType']}\n")

                except:
                    print("No log trace in file", file)
    else:
        for file_name in os.listdir(in_path):
            input_file_path = os.path.join(in_path, file_name)
            output_file_path = os.path.join(out_path, file_name)

            try:
                with open(input_file_path, 'r', encoding='utf8') as input_file:
                    tree = ET.parse(input_file)
                    root = tree.getroot()

                with open(output_file_path, 'w', encoding='utf8') as res:
                    for trace in root.findall('trace'):
                        if len(trace) > 0:
                            for event in trace:
                                event_data = {'class': '', 'featureName': '', 'eventType': ''}
                                for attribute in event:
                                    key = attribute.attrib.get('key')
                                    if key in event_data:
                                        event_data[key] = attribute.attrib.get('value', '')
                                res.write(
                                    f"event\t{event_data['class']} {event_data['featureName']} {event_data['eventType']}\n")

            except ET.ParseError:
                print(f"No log trace in file or XML parsing error: {file_name}")
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")






def aggregate_cluster_files(path, outpath, filename):
    with open(outpath + filename, 'wb') as wfd:
        for f in os.listdir(path):
            try:
                with open(path + f, 'rb') as fd:
                    shutil.copyfileobj(fd, wfd)
            except:
                continue


def creates_train_file(directory_path, output_file_path):
    """
    Reads the content of all files in the specified directory and writes it into a single output file.

    Parameters:
    directory_path (str): The path to the directory containing the files to merge.
    output_file_path (str): The path to the output file where the merged content will be written.
    """
    # Open the output file in write mode
    with open(output_file_path, 'w') as output_file:
        # Iterate over all the items in the directory
        for item in os.listdir(directory_path):
            # Construct the full path of the item
            item_path = os.path.join(directory_path, item)
            # Check if the item is a file
            if os.path.isfile(item_path):
                # Open the file in read mode
                with open(item_path, 'r') as input_file:
                    # Read the content of the file
                    file_content = input_file.read()
                    # Write the content to the output file
                    output_file.write(file_content + "\n")


def create_cross_validation_folders(source_folder,dest_folder, n_folds):
    # Check if the source folder exists
    if not os.path.isdir(source_folder):
        raise ValueError("Source folder does not exist.")
    create_path_if_not_exists(dest_folder)
    # Get all file names in the folder
    all_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Shuffle the files to ensure randomness
    random.shuffle(all_files)

    # Split the files into n_folds parts
    fold_size = len(all_files) // n_folds
    folds = [all_files[i:i + fold_size] for i in range(0, len(all_files), fold_size)]

    # Ensure that all files are included (due to integer division)
    for i in range(len(all_files) - fold_size * n_folds):
        folds[i].append(all_files[-i - 1])

    # Create train and test folders for each fold
    for i, test_files in enumerate(folds):
        train_files = [f for fold in folds if fold != test_files for f in fold]

        fold_dir = os.path.join(dest_folder, f'fold_{i + 1}')
        train_dir = os.path.join(fold_dir, 'train')
        test_dir = os.path.join(fold_dir, 'test')

        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(test_dir, exist_ok=True)

        # Copy files to train and test directories
        for f in train_files:
            shutil.copy(os.path.join(source_folder, f), train_dir)
        for f in test_files:
            shutil.copy(os.path.join(source_folder, f), test_dir)


def split_file_by_ratio(original_file_path, ratio, new_file_path):
    """
    Splits the content of the original file into two files based on a given ratio. The original file is modified
    to contain only a certain ratio of the total lines, and the remaining lines are written to a new file.

    Parameters:
    original_file_path (str): The path to the original file.
    ratio (float): The ratio of lines to keep in the original file (e.g., 0.5 for half the lines).
    new_file_path (str): The path to the new file where the exceeding lines will be written.
    """
    # Open the original file and read its lines
    with open(original_file_path, 'r') as file:
        lines = file.readlines()

    random.shuffle(lines)
    # Calculate the number of lines to keep based on the ratio
    line_count = int(len(lines) * ratio)

    # Lines to keep in the original file
    lines_to_keep = lines[:line_count]
    # Lines to move to the new file
    lines_to_move = lines[line_count:]

    # Write the lines to keep back into the original file
    with open(original_file_path, 'w') as file:
        file.writelines(lines_to_keep)

    # Write the exceeding lines to the new file
    with open(new_file_path, 'w') as file:
        file.writelines(lines_to_move)


def building_paths(fold):
    in_fold_train = cf.CROSS_ROOT_STD + fold + cf.XES_TRAIN_CROSS_SRC
    in_fold_test = cf.CROSS_ROOT_STD + fold + cf.XES_TEST_CROSS_SRC
    out_fold_train = cf.CROSS_ROOT_STD + fold + cf.XES_TRAIN_CROSS_DST
    out_fold_test = cf.CROSS_ROOT_STD + fold + cf.XES_TEST_CROSS_DST
    out_fold_gt = cf.CROSS_ROOT_STD + fold + cf.XES_GT_CROSS_DST

    # Ensure paths exist
    create_path_if_not_exists(in_fold_train)
    create_path_if_not_exists(in_fold_test)
    create_path_if_not_exists(out_fold_train)
    create_path_if_not_exists(out_fold_test)
    create_path_if_not_exists(out_fold_gt)

    return in_fold_train, in_fold_test, out_fold_train, out_fold_test, out_fold_gt



#
#
# def split_and_merge_folders(folder1, folder2, ratio, dest_folder):
#     # Ensure the destination folder exists
#     if not os.path.exists(dest_folder):
#         os.makedirs(dest_folder)
#
#     # Get the list of files from both folders
#     files1 = os.listdir(folder1)
#     files2 = os.listdir(folder2)
#
#     # Calculate the number of files to replace from folder 1 with files from folder 2
#     num_files_to_replace = int(len(files1) * ratio)
#     num_files_to_keep = len(files1) - num_files_to_replace
#
#     try:
#         # Select random files to replace in the first folder
#         files_to_replace = random.sample(files1, num_files_to_replace)
#     except ValueError:
#         # If the sample size is larger than the population, take all files
#         files_to_replace = files1
#
#     try:
#         # Select random files from the second folder to replace those in the first folder
#         replacement_files = random.sample(files2, num_files_to_replace)
#     except ValueError:
#         # If the sample size is larger than the population, take all files
#         replacement_files = files2
#
#     # Get the list of files to keep from the first folder
#     files_to_keep = [file for file in files1 if file not in files_to_replace]
#
#     # Function to generate a unique filename
#     def get_unique_filename(dest_path, filename):
#         base, ext = os.path.splitext(filename)
#         counter = 1
#         new_filename = filename
#         while os.path.exists(os.path.join(dest_path, new_filename)):
#             new_filename = f"{base}_{counter}{ext}"
#             counter += 1
#         return new_filename
#
#     # Copy the files to keep from the first folder to the destination folder
#     for file_name in files_to_keep:
#         dest_file = get_unique_filename(dest_folder, file_name)
#         shutil.copy(os.path.join(folder1, file_name), os.path.join(dest_folder, dest_file))
#
#     # Copy the replacement files from the second folder to the destination folder with "synthetic_" prefix
#     for file_name in replacement_files:
#         new_file_name = "synthetic_" + file_name
#         dest_file = get_unique_filename(dest_folder, new_file_name)
#         shutil.copy(os.path.join(folder2, file_name), os.path.join(dest_folder, dest_file))


def merge_folders(folder1, folder2, result_folder, ratio):
    """
    Merge two folders such that the result folder contains a specified ratio of files
    from the first folder and the remaining files from the second folder.

    :param folder1: Path to the first folder
    :param folder2: Path to the second folder
    :param result_folder: Path to the result folder
    :param ratio: Ratio of files to take from the first folder (e.g., 0.2 for 20%)
    """
    # Create the result folder if it doesn't exist
    os.makedirs(result_folder, exist_ok=True)

    # List all files in both folders
    files1 = sorted(os.listdir(folder1))
    files2 = sorted(os.listdir(folder2))

    # Ensure both folders have the same filenames
    if files1 != files2:
        raise ValueError("The files in both folders should have the same names.")

    # Calculate the number of files to take from each folder
    total_files = len(files1)
    num_from_folder1 = math.ceil(total_files * ratio)
    num_from_folder2 = total_files - num_from_folder1

    # Copy files from folder1
    for i in range(num_from_folder1):
        src_path = os.path.join(folder1, files1[i])
        dest_path = os.path.join(result_folder, files1[i])
        shutil.copy(src_path, dest_path)

    # Copy files from folder2
    for i in range(num_from_folder2):
        src_path = os.path.join(folder2, files2[i + num_from_folder1])
        dest_path = os.path.join(result_folder, files2[i + num_from_folder1])
        shutil.copy(src_path, dest_path)

    print(f"Files successfully copied to {result_folder}")


def rename_files(directory):
    """
    Renames files in the specified directory based on the specified naming pattern:
    Swaps 'results_context_0.2_cutoff_3.csv' with 'results_context_0.8_cutoff_3.csv' and similar patterns.

    Args:
    directory (str): The path to the directory containing the files to be renamed.
    """
    for filename in os.listdir(directory):
        # Check for files with specific patterns and rename them accordingly
        if filename.startswith('results_context_') and filename.endswith('.csv'):
            parts = filename.split('_')
            if parts[2] == '0.2' and parts[4] in ['3', '5', '10']:
                new_filename = filename.replace('0.2', '0.8')
            elif parts[2] == '0.8' and parts[4] in ['3', '5', '10']:
                new_filename = filename.replace('0.8', '0.2')
            else:
                continue
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed "{filename}" to "{new_filename}"')


def csv_to_latex(filepath, output_filepath):
    # Read the CSV file
    df = pd.read_csv(filepath)

    # Remove the first column
    df = df.iloc[:, 1:]

    # Divide all values by 100 (assuming all other columns are numeric)
    df = df.apply(lambda x: x / 100 if x.dtype.kind in 'biufc' else x)

    # Drop the last two columns (after removing the first and modifying)
    df = df.iloc[:, :-2]

    # Convert the DataFrame to a LaTeX format
    latex_str = tabulate(df, tablefmt="latex", headers="keys", showindex="never")

    # Write the LaTeX string to a file
    with open(output_filepath, 'w') as f:
        f.write(latex_str)

def plot_graphs():
    # Updated data
    data = {
        'Approach': ['gpt4', 'gpt4', 'gpt4', 'mixed', 'mixed', 'mixed', 'manual', 'manual', 'manual'],
        'Metric': ['Avg Precision', 'Avg Recall', 'Avg F1', 'Avg Precision', 'Avg Recall', 'Avg F1', 'Avg Precision',
                   'Avg Recall', 'Avg F1'],
        'Value': [0.34,0.22,0.24,0.44,0.25,0.29,0.70,0.47,0.50]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Pivot the DataFrame to make it suitable for plotting
    df_pivot = df.pivot(index='Approach', columns='Metric', values='Value')

    # Reorder the columns
    df_pivot = df_pivot[['Avg Precision', 'Avg Recall', 'Avg F1']]

    # Reorder the index
    df_pivot = df_pivot.loc[['gpt4', 'mixed', 'manual']]

    # Colors for the bars
    colors = {
        'gpt4': '#FFA07A',  # Light Salmon
        'mixed': '#FF8C00',  # Dark Orange
        'manual': '#FF4500'  # Orange Red
    }

    # Plotting
    ax = df_pivot.plot(kind='bar', figsize=(10, 6), color=[colors['gpt4'], colors['mixed'], colors['manual']])
    #plt.title('Class recommendations on D4')
    plt.xlabel('Training set')
    plt.ylabel('Value')
    plt.xticks(rotation=0)
    plt.legend(title='Metric')
    plt.tight_layout()

    # Display the plot
    plt.show()





def plot_lines():
    # Updated data
    data = {
        'Approach': ['gpt4', 'mixed02', 'mixed05', 'mixed08', 'manual'],
        'Avg Precision': [40.0, 38.0, 48.0, 56.0, 74.0],
        'Avg Recall': [50.04545454545455, 47.015151515151516, 48.934731934731936, 60.382284382284375, 62.96861471861472],
        'Avg F1': [42.920634920634924, 39.86813186813187, 47.21513269339356, 56.5901710798736, 66.51964506082153]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    df['Avg Precision'] = df['Avg Precision'] / 100

    df['Avg Recall'] = df['Avg Recall'] / 100
    df['Avg F1'] = df['Avg F1'] / 100


    # Colors for the lines
    colors = {
        'gpt4': '#FFA07A',  # Light Salmon
        'manual': '#FF4500',  # Orange Red
        'mixed02': '#32CD32',  # Lime Green
        'mixed05': '#1E90FF',  # Dodger Blue
        'mixed08': '#8A2BE2'  # Blue Violet
    }

    # Line styles for the lines
    line_styles = {
        'gpt4': 'o--',
        'manual': 'o--',
        'mixed02': 'o--',
        'mixed05': 'o--',
        'mixed08': 'o--'
    }

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    for approach in df['Approach']:
        ax.plot(['Avg Precision', 'Avg Recall', 'Avg F1'],
                df[df['Approach'] == approach].iloc[0][1:],
                line_styles[approach], color=colors.get(approach, '#000000'), label=approach)

    plt.xlabel('Metric')
    plt.ylabel('Value')
    plt.legend(title='Training set')
    plt.grid(True)
    plt.tight_layout()

    # Display the plot
    plt.show()

# Call the function to plot the graph



# Call the function to plot the graph



import os


def compute_average_for_csv_files(folder_path):
    # Get list of all csv files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    for file in csv_files:
        file_path = os.path.join(folder_path, file)

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, sep=",")

        # Compute the average for each row
        print(file)

        print(df.mean())
        #row_averages = df.mean(axis=1)

        # Append the average as a new row at the end of the DataFrame
    #     avg_row = pd.DataFrame([row_averages.mean()], columns=df.columns)
    #     df = pd.concat([df, avg_row], ignore_index=True)
    #
    #     # Save the modified DataFrame back to the CSV
    #     df.to_csv(file_path, index=False)
    #
    # print("Averages computed and new row added for all files.")


def plot_graphs_class():
    # Updated data
    data = {
        'Approach': ['gpt4', 'gpt4', 'gpt4', 'mixed', 'mixed', 'mixed', 'manual', 'manual', 'manual'],
        'Metric': ['Avg Precision', 'Avg Recall', 'Avg F1', 'Avg Precision', 'Avg Recall', 'Avg F1', 'Avg Precision',
                   'Avg Recall', 'Avg F1'],
        'Value': [40.0, 50.04545454545455, 42.920634920634924,48.0,48.934731934731936,47.21513269339356,
                  74.0, 62.96861471861472, 66.51964506082153]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Divide values by 100
    df['Value'] = df['Value'] / 100

    # Pivot the DataFrame to make it suitable for plotting
    df_pivot = df.pivot(index='Approach', columns='Metric', values='Value')

    # Reorder the columns
    df_pivot = df_pivot[['Avg Precision', 'Avg Recall', 'Avg F1']]

    # Reorder the index
    df_pivot = df_pivot.loc[['gpt4', 'mixed', 'manual']]

    # Colors for the bars
    colors = {
        'gpt4': '#ADD8E6',  # Light Blue
        'mixed': '#4682B4',  # Steel Blue
        'manual': '#0000FF'  # Blue
    }

    # Plotting
    ax = df_pivot.plot(kind='bar', figsize=(10, 6), color=[colors['gpt4'], colors['mixed'], colors['manual']])
    plt.title('Comparison of Metrics by Approach')
    plt.xlabel('Approach')
    plt.ylabel('Value')
    plt.xticks(rotation=0)
    plt.legend(title='Metric')
    plt.tight_layout()

    # Display the plot
    plt.show()


def merge_csv_files(folder_path, output_file):
    """
    Merges all CSV files in the given folder into a single CSV file and adds a new column with the file name.

    Parameters:
    folder_path (str): The path to the folder containing the CSV files.
    output_file (str): The path for the output merged CSV file.

    Returns:
    None
    """
    # List to hold dataframes
    df_list = []

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            # Read CSV file into a DataFrame
            df = pd.read_csv(file_path)
            # Add a new column with the filename
            df['source_file'] = filename
            # Append the DataFrame to the list
            df_list.append(df)

    # Concatenate all DataFrames in the list
    merged_df = pd.concat(df_list, ignore_index=True)

    # Write the merged DataFrame to a CSV file
    merged_df.to_csv(output_file, index=False)

    print(f"All CSV files have been merged into {output_file} with the source_file column added.")


import pandas as pd


def extract_categories(csv):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv, delimiter=';')

    # Group by the 'Elements' column and build the result dictionary for detailed records
    result_dict = {}
    category_dict = {}
    classes = []
    for instance, group in df.groupby('Elements'):
        # Build the detailed records dictionary
        result_dict[instance] = group.drop(columns='Elements').to_dict(orient='records')

        # Extract the unique classes for each instance and store in category_dict
        # classes = group['class'].unique().tolist()
        # category_dict[instance] = classes


    for key in result_dict.keys():
        for record in result_dict[key]:
            classes.append(record.get('class'))


        #result_dict[key][0].get('class')


        category_dict[key] = set(classes)




    #result_dict.get("Artifacts")[0].get('class')
    # Display the resulting dictionary
    # for instance, records in result_dict.items():
    #     #print(f"Element: {instance}")
    #     for record in records:
    #         #print(record.get('class'))

    #print("\nCategory Dictionary:")
    #print(category_dict)



    return category_dict

#rename_files('results_class_five_fold_mixed/')

# path= "C:\\Users\\claud\\OneDrive\\Desktop\\paperTo Submit\\Repos\\modelingOperationRec_IST\\09_IMA\\MORGAN\Results\\results_RQ2\CAEX\\"
# compute_average_for_csv_files(path+"results_caex_dm05_class\\")
# merge_csv_files("C:\\Users\\claud\\OneDrive\\Desktop\\paperTo Submit\\Repos\\modelingOperationRec_IST\\09_IMA\\MORGAN\\"
#                 "Results\\results_RQ3\\HEPSYCODE\\DomainAnalysis\\","domain_analysis.csv")