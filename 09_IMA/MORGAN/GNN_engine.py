import os
import time


from grakel.utils import graph_from_networkx
from jinja2 import Environment, FileSystemLoader
import tkinter as tk

from custom_kernel_matrix import CustomKernelMatrix
import dataset_utilities as du
import config as cf



def compute_recommendations(G_train, train_data, G_test, n):
    ranked_list = ()
    list_sim = []
    for g, rec in zip(G_train, train_data):
        try:
            if len(G_test[n]) > 0:
                sim = compute_kernel_similarity(g, G_test[n])
                if sim[0][0] > 0:
                    tuple_g = rec, sim[0][0]
                    list_sim.append(tuple_g)
                ranked_list = sorted(list_sim, key=lambda tup: tup[1], reverse=True)
            else:
                continue
        except IndexError:
            continue

    return set(ranked_list)



def compute_kernel_similarity(g_train,g_test):
    sp_kernel = CustomKernelMatrix()
    sp_kernel.fit_transform([g_train])
    sp_kernel.transform([g_test])
    return sp_kernel.transform([g_test])



def join_rec(dict_results):
    #cut_rec = dict_results
    combined_list = []

    for elem in dict_results:
        #rec_graph = elem[0].split(' ')

        combined_list.append(elem[0])


    return combined_list




def get_recommendations(train_preprocessed, train_data,test_context,n_items):

    with open(test_context, 'r', errors='ignore', encoding='utf-8') as f:
        lenght = len(f.readlines())
        test_preprocessed, test_data = du.encoding_data(test_context)

        vocab = du.get_vocab(train_preprocessed, test_preprocessed)
        G_train_nx = du.create_graphs_of_words(train_preprocessed, vocab, 3)
        G_test_nx = du.create_graphs_of_words(test_preprocessed, vocab, 3)
        G_train = list(graph_from_networkx(G_train_nx, node_labels_tag='label'))
        G_test = list(graph_from_networkx(G_test_nx, node_labels_tag='label'))
        start = time.time()

        for i in range(0, lenght):
            results = compute_recommendations(G_train, train_data, G_test, i)
            rec_graph = join_rec(results)
        end = time.time()
        enlapsed = end - start

        print("Rec time: ", enlapsed)
        gt_data = du.get_gt_classes(test_context)

        if gt_data:
            rec_graph = set(rec_graph)
            rec_graph = list(rec_graph)[0:n_items]



            list_gt_global = gt_data

            print('recommended operations ', rec_graph)
            if list_gt_global:
                operations = du.match_operations(rec_graph,list_gt_global,test_data)

            produce_recommendations_dump(operations, test_context)

            show_recommendations(recommendations=rec_graph)

def eval_recommendations(train_preprocessed, train_data,test_context,gt_context, n_items):

    with open(test_context, 'r', errors='ignore', encoding='utf-8') as f:
        lenght = len(f.readlines())
        test_preprocessed, test_data = du.encoding_data(test_context)

        vocab = du.get_vocab(train_preprocessed, test_preprocessed)
        G_train_nx = du.create_graphs_of_words(train_preprocessed, vocab, 3)
        G_test_nx = du.create_graphs_of_words(test_preprocessed, vocab, 3)
        G_train = list(graph_from_networkx(G_train_nx, node_labels_tag='label'))
        G_test = list(graph_from_networkx(G_test_nx, node_labels_tag='label'))
        start = time.time()
        rec_graph = []
        for i in range(0, lenght):
            results = compute_recommendations(G_train, train_data, G_test, i)
            rec_graph = join_rec(results)
        end = time.time()
        enlapsed = end - start

        print("Rec time: ", enlapsed)
        gt_data = du.load_file(gt_context)
        pr = 0.0
        rec = 0.0
        f1 = 0.0
        if gt_data:
            rec_graph = set(rec_graph)
            rec_graph = list(rec_graph)[0:n_items]

            list_gt_global = gt_data


            print('recommended operations ', rec_graph)
            print('gt operations', gt_data)

            pr = du.precision(rec_graph, gt_data)
            rec = du.recall(rec_graph, gt_data)
            print(pr,rec)
            if pr == 0.0 or rec == 0.0:
                f1 = 0.0
            else:
                f1 = 2 * (pr * rec) / (pr + rec)
            # if list_gt_global:
            #     operations = du.match_operations(rec_graph,list_gt_global,test_data)

            #produce_recommendations_dump(operations, test_context)

        return pr, rec, f1




import time

def eval_recommendations_time(train_preprocessed, train_data, test_context, gt_context, n_items, type):
    # Start time for the entire process
    overall_start = time.time()

    # Preprocessing and training phase
    with open(test_context, 'r', errors='ignore', encoding='utf-8') as f:
        length = len(f.readlines())
        test_preprocessed, test_data = du.encoding_data(test_context)

        vocab = du.get_vocab(train_preprocessed, test_preprocessed)
        G_train_nx = du.create_graphs_of_words(train_preprocessed, vocab, 3)
        G_test_nx = du.create_graphs_of_words(test_preprocessed, vocab, 3)
        G_train = list(graph_from_networkx(G_train_nx, node_labels_tag='label'))
        G_test = list(graph_from_networkx(G_test_nx, node_labels_tag='label'))

    # End time for preprocessing and training
    preprocess_end = time.time()
    preprocess_time = preprocess_end - overall_start

    # Start time for recommendation phase
    recommendation_start = time.time()

    rec_graph = []
    for i in range(0, length):
        results = compute_recommendations(G_train, train_data, G_test, i)
        rec_graph = join_rec(results)

    # End time for recommendation phase
    recommendation_end = time.time()
    recommendation_time = recommendation_end - recommendation_start

    print("Preprocessing and training time: ", preprocess_time)
    print("Recommendation time: ", recommendation_time)

    gt_data = du.load_file(gt_context)
    pr = 0.0
    rec = 0.0
    f1 = 0.0
    if gt_data:
        rec_graph = set(rec_graph)
        rec_graph = list(rec_graph)[0:n_items]

        list_gt_global = gt_data
        #
        print('Recommended operations: ', rec_graph)
        print('GT operations: ', gt_data)

        rec_classes, rec_attrs = du.extract_operations_from_list(rec_graph)
        gt_classes, gt_attrs = du.extract_operations_from_list(gt_data)

        # pr = du.precision(rec_graph, gt_data)
        # rec = du.recall(rec_graph, gt_data)
        #

        ## all metrics

        if type == "class":

            # classes metrics

            pr = du.precision(rec_classes, list(set(gt_classes)))
            rec = du.recall(rec_classes, list(set(gt_classes)))

        if type == "attrs":
            # attrs metrics
            pr = du.precision(rec_attrs, gt_attrs)
            rec = du.recall(rec_attrs, gt_attrs)


        print(pr, rec)

        if pr == 0.0 or rec == 0.0:
            f1 = 0.0
        else:
            f1 = 2 * (pr * rec) / (pr + rec)

        # if list_gt_global:
        #     operations = du.match_operations(rec_graph, list_gt_global, test_data)

        # produce_recommendations_dump(operations, test_context)

    return pr, rec, f1, preprocess_time, recommendation_time


def eval_recommendations_classes(train_preprocessed, train_data, test_context, gt_context, n_items, type, classes):
    # Start time for the entire process
    overall_start = time.time()

    # Preprocessing and training phase
    with open(test_context, 'r', errors='ignore', encoding='utf-8') as f:
        length = len(f.readlines())
        test_preprocessed, test_data = du.encoding_data(test_context)

        vocab = du.get_vocab(train_preprocessed, test_preprocessed)
        G_train_nx = du.create_graphs_of_words(train_preprocessed, vocab, 3)
        G_test_nx = du.create_graphs_of_words(test_preprocessed, vocab, 3)
        G_train = list(graph_from_networkx(G_train_nx, node_labels_tag='label'))
        G_test = list(graph_from_networkx(G_test_nx, node_labels_tag='label'))

    # End time for preprocessing and training
    preprocess_end = time.time()
    preprocess_time = preprocess_end - overall_start

    # Start time for recommendation phase
    recommendation_start = time.time()

    rec_graph = []
    for i in range(0, length):
        results = compute_recommendations(G_train, train_data, G_test, i)
        rec_graph = join_rec(results)

    # End time for recommendation phase
    recommendation_end = time.time()
    recommendation_time = recommendation_end - recommendation_start

    print("Preprocessing and training time: ", preprocess_time)
    print("Recommendation time: ", recommendation_time)

    gt_data = du.load_file(gt_context)
    pr = 0.0
    rec = 0.0
    f1 = 0.0
    if gt_data:
        rec_graph = set(rec_graph)
        rec_graph = list(rec_graph)[0:n_items]

        list_gt_global = gt_data
        #
        print('Recommended operations: ', rec_graph)
        print('GT operations: ', gt_data)

        rec_classes, rec_attrs = du.extract_operations_from_list(rec_graph)
        gt_classes, gt_attrs = du.extract_operations_from_list(gt_data)

        # pr = du.precision(rec_graph, gt_data)
        # rec = du.recall(rec_graph, gt_data)
        #

        ## all metrics

        if type == "class":

            # classes metrics

            pr = du.precision_cl(rec_classes, list(set(gt_classes)),classes)
            rec = du.recall_cl(rec_classes, list(set(gt_classes)),classes)

        if type == "attrs":
            # attrs metrics
            pr = du.precision_cl(rec_attrs, gt_attrs,classes)
            rec = du.recall_cl(rec_attrs, gt_attrs,classes)


        print(pr, rec)

        if pr == 0.0 or rec == 0.0:
            f1 = 0.0
        else:
            f1 = 2 * (pr * rec) / (pr + rec)

        # if list_gt_global:
        #     operations = du.match_operations(rec_graph, list_gt_global, test_data)

        # produce_recommendations_dump(operations, test_context)

    return pr, rec, f1, preprocess_time, recommendation_time



def produce_recommendations_dump(recommendations, test):
    du.create_path_if_not_exists(cf.REC_DST)
    head, tail = os.path.split(test)
    #out_recs = []
    with open(f"{cf.REC_DST}/recommendations_for_{tail}", 'w') as res:
        for key, value in recommendations.items():
            out_string = value[2].strip() + " attribute" + key + " to class " + value[1]
            #out_recs.append(out_string)
            res.write(f"{out_string}\n")
            print(out_string)


# TODO: visual recommendation
import tkinter as ztk

def show_recommendations(recommendations):
    window = tk.Tk()
    window.title("Recommendations")

    # Create a frame with a specified width, height, and dark background color similar to Eclipse theme
    frame = tk.Frame(master=window, width=300, height=300, bg='#333333')  # Dark grey background
    frame.pack(fill='both', expand=True)  # Make the frame expand to fill the window

    # Convert the list of recommendations to a single string with each recommendation on a new line
    recommendations_text = '\n'.join(recommendations)

    # Create a label with the recommendations text, specifying font and background color
    label = tk.Label(master=frame, text=recommendations_text, bg='#333333', fg='white',  # Background and font color
                     font=('Arial', 12), justify='left', wraplength=280)  # Font and text alignment properties
    label.pack(padx=10, pady=10, expand=True)  # Padding and expand to make it more visually pleasing

    window.mainloop()


