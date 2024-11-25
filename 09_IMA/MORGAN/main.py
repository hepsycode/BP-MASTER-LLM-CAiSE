from GNN_engine import get_recommendations, eval_recommendations_time, eval_recommendations_classes
import os
import dataset_utilities as du

import config as cf

import csv



def main(type):
    if type == "1":
        du.parse_xes_traces(cf.XES_TRAIN_SRC, cf.XES_TRAIN_DST, True)
        du.encoding_training_data_dump(cf.XES_TRAIN_DST+cf.KB_TRAIN)
        return
    elif type == "2":
        du.parse_xes_traces(cf.XES_TEST_SRC, cf.XES_TEST_DST, False)
        preprocessed_train = du.load_preprocessed_data(cf.DUMP_TRAIN)
        train_data = du.load_file(cf.XES_TRAIN_DST + cf.KB_TRAIN)
        for file in os.listdir(cf.XES_TEST_DST):
            get_recommendations(train_preprocessed=preprocessed_train, train_data=train_data, test_context=cf.XES_TEST_DST+file,
                                  n_items = 5)
        return
    elif type == "3":
        du.parse_xes_traces(cf.XES_SESSION_TRAIN_SRC, cf.XES_SESSION_TRAIN_DST, True)
        du.create_path_if_not_exists(cf.XES_SESSION_TRAIN_DST)
        preprocessed_train,train_data = du.encoding_training_data_dump(cf.XES_SESSION_TRAIN_DST + cf.KB_TRAIN)
        for file in os.listdir(cf.XES_TEST_DST):
            get_recommendations(train_preprocessed=preprocessed_train, train_data=train_data, test_context=cf.XES_TEST_DST+file,
                                  n_items = 10)

    elif type == "4":

        du.create_cross_validation_folders(cf.XES_TRAIN_SRC,cf.CROSS_ROOT_STD, 5)
        du.create_path_if_not_exists(cf.RESULTS_CROSS_FOLD)
        results_csv_path = f'{cf.RESULTS_CROSS_FOLD}/results_context_{cf.CONTEXT_RATIO}_cutoff_{cf.CUT_OFF}.csv'

        #Open the CSV file in append mode, so we don't overwrite existing data
        with open(results_csv_path, mode='w', newline='') as file:
            # Create a CSV writer object
            csv_writer = csv.writer(file)

            # Optionally, write headers if the file is newly created or empty
            # Uncomment the next line if you want to write headers
            csv_writer.writerow(['Fold', 'Avg Precision', 'Avg Recall', 'Avg F1'])

            for fold in os.listdir(cf.CROSS_ROOT_STD):

                # Construct paths
                in_fold_train, in_fold_test, out_fold_train, out_fold_test, out_fold_gt = du.building_paths(fold)

                # Preprocess and encode data
                #du.parse_xes_traces(in_fold_test, out_fold_test, False)
                #du.parse_xes_traces(in_fold_train, out_fold_train, True)
                du.combine_files(in_fold_train, out_fold_train)

                preprocessed_train, train_data = du.encoding_training_data_dump(cf.CROSS_ROOT_STD + fold + cf.CROSS_KB_SRC)

                # Initialize metrics accumulators
                total_precision = 0
                total_recall = 0
                total_f1 = 0
                file_count = 0
                total_pr_time = 0.0
                total_rec_time = 0.0

                # Iterate through each test file
                for file in os.listdir(out_fold_test):


                    du.split_file_by_ratio(out_fold_test + file, cf.CONTEXT_RATIO, out_fold_gt + file)

                    pr, rec, f1, pr_time, rec_time = eval_recommendations_time(train_preprocessed=preprocessed_train, train_data=train_data,
                                                       test_context=out_fold_test + file, gt_context=out_fold_gt + file,
                                                       n_items=cf.CUT_OFF)

                    # Accumulate metrics
                    total_precision += pr
                    total_recall += rec
                    total_f1 += f1
                    total_pr_time += pr_time
                    total_rec_time += rec_time
                    file_count += 1

                # Calculate and write average metrics for the fold to the CSV file
                if file_count > 0:
                    avg_precision = total_precision / file_count
                    avg_recall = total_recall / file_count
                    avg_f1 = total_f1 / file_count
                    avg_pr_time = total_pr_time / file_count
                    avg_rec_time = total_rec_time / file_count

                    # Write the fold and its average metrics to the CSV file
                    csv_writer.writerow([fold, avg_precision, avg_recall, avg_f1,avg_pr_time,avg_rec_time])
                else:
                    print(f"Fold {fold}: No files to process.")
    elif type == "5":
         #du.parse_xes_traces('real_XES/', 'real_XES-MORGAN/', False)
         du.merge_folders(folder1='IST-extension/XES-D1-MG/', folder2='ST-extension/XES-MORGAN-LLM-GPT4/',
                                  result_folder='IST-extension/xes_mixed_dataset_02_ratio', ratio=0.2)

    return


def running_rq3_experiment(type):
    root_experiments = "04 - Dataset-Industrial"
    #du.parse_xes_traces(root_experiments + '/XES-PM/', root_experiments +'/XES-MORGAN/', False)

    #du.create_path_if_not_exists(root_experiments+'/train_mixed/')
    #du.aggregate_cluster_files(root_experiments+'/xes_mixed_dataset_05_ratio/', root_experiments+'/train_files/', 'train_m05.txt')

    #du.create_path_if_not_exists(cf.RESULTS_CROSS_FOLD)
    #results_csv_path = f'{cf.RESULTS_CROSS_FOLD}/results_context_{cf.CONTEXT_RATIO}_cutoff_{cf.CUT_OFF}.csv'
    for i in range(1,6):

        results_csv_path = f"{root_experiments}/C3.2/results_rq3_dm08_m{i}_{type}.csv"
        #du.create_path_if_not_exists(results_csv_path)
        # Open the CSV file in append mode, so we don't overwrite existing data
        with open(results_csv_path, mode='w', newline='') as file:
            # Create a CSV writer object
            csv_writer = csv.writer(file)

            # Optionally, write headers if the file is newly created or empty
            # Uncomment the next line if you want to write headers
            csv_writer.writerow(['Fold', 'Avg Precision', 'Avg Recall', 'Avg F1', 'Avg pr time', 'Avg rec time'])


            out_fold_test = root_experiments + f'/test_{i}/'
            out_fold_gt = root_experiments + f'/gt_{i}/'

            # out_fold_test = root_experiments + "/test_4/"
            # out_fold_gt = root_experiments + "/gt_4/"


            # preprocessed_train, train_data = du.encoding_training_data_dump(cf.CROSS_ROOT_STD + fold + cf.CROSS_KB_SRC)
            preprocessed_train, train_data = du.encoding_training_data_dump(
                root_experiments + '/train_mixed/train_mixed_08.txt')


            # Initialize metrics accumulators
            total_precision = 0
            total_recall = 0
            total_f1 = 0
            file_count = 0
            total_pr_time = 0.0
            total_rec_time = 0.0

            # Iterate through each test file
            for file_test in os.listdir(out_fold_test):
                #du.split_file_by_ratio(out_fold_test + file_test, cf.CONTEXT_RATIO, out_fold_gt + file_test)

                pr, rec, f1, pr_time, rec_time = eval_recommendations_time(
                    train_preprocessed=preprocessed_train,
                    train_data=train_data,
                    test_context=out_fold_test + file_test,
                    gt_context=out_fold_gt + file_test,
                    n_items=cf.CUT_OFF, type=type)

                # Accumulate metrics
                total_precision += pr
                total_recall += rec
                total_f1 += f1
                total_pr_time += pr_time
                total_rec_time += rec_time
                file_count += 1

            # Calculate and write average metrics for the fold to the CSV file
            if file_count > 0:
                avg_precision = total_precision / file_count
                avg_recall = total_recall / file_count
                avg_f1 = total_f1 / file_count
                avg_pr_time = total_pr_time / file_count
                avg_rec_time = total_rec_time / file_count

                # Write the fold and its average metrics to the CSV file
                csv_writer.writerow([avg_precision, avg_recall, avg_f1, avg_pr_time, avg_rec_time])
            else:
                print(f" No files to process.")



def running_rq2_experiment(type):
    list_co = [3,5,10]
    list_cr = [0.2,0.5,0.8]

    for cr in list_cr:
        for co in list_co:
            du.create_cross_validation_folders(cf.XES_TRAIN_SRC, cf.CROSS_ROOT_STD, 5)
            du.create_path_if_not_exists(cf.RESULTS_CROSS_FOLD)
            results_csv_path = f'{cf.RESULTS_CROSS_FOLD}/results_context_{cr}_cutoff_{co}.csv'

            # Open the CSV file in append mode, so we don't overwrite existing data
            with open(results_csv_path, mode='w', newline='') as file:
                # Create a CSV writer object
                csv_writer = csv.writer(file)

                # Optionally, write headers if the file is newly created or empty
                # Uncomment the next line if you want to write headers
                csv_writer.writerow(['Fold', 'Avg Precision', 'Avg Recall', 'Avg F1', 'Avg pr time', 'Avg rec time'])

                for fold in os.listdir(cf.CROSS_ROOT_STD):

                    # Construct paths
                    in_fold_train, in_fold_test, out_fold_train, out_fold_test, out_fold_gt = du.building_paths(fold)

                    du.combine_files(in_fold_train, out_fold_train)

                    preprocessed_train, train_data = du.encoding_training_data_dump(cf.CROSS_ROOT_STD + fold + cf.CROSS_KB_SRC)
                    #preprocessed_train, train_data = du.encoding_training_data_dump('04 - Dataset-Industrial/train_manual/train.txt')
                    # Initialize metrics accumulators
                    total_precision = 0
                    total_recall = 0
                    total_f1 = 0
                    file_count = 0
                    total_pr_time = 0.0
                    total_rec_time = 0.0

                    # Iterate through each test file
                    for file in os.listdir(out_fold_test):
                        du.split_file_by_ratio(out_fold_test + file, cr, out_fold_gt + file)

                        pr, rec, f1, pr_time, rec_time = eval_recommendations_time(train_preprocessed=preprocessed_train,
                                                                                   train_data=train_data,
                                                                                   test_context=out_fold_test + file,
                                                                                   gt_context=out_fold_gt + file,
                                                                                   n_items=co, type=type)

                        # Accumulate metrics
                        total_precision += pr
                        total_recall += rec
                        total_f1 += f1
                        total_pr_time += pr_time
                        total_rec_time += rec_time
                        file_count += 1

                    # Calculate and write average metrics for the fold to the CSV file
                    if file_count > 0:
                        avg_precision = total_precision / file_count
                        avg_recall = total_recall / file_count
                        avg_f1 = total_f1 / file_count
                        avg_pr_time = total_pr_time / file_count
                        avg_rec_time = total_rec_time / file_count

                        # Write the fold and its average metrics to the CSV file
                        csv_writer.writerow([fold, avg_precision, avg_recall, avg_f1, avg_pr_time, avg_rec_time])
                    else:
                        print(f"Fold {fold}: No files to process.")


def running_classes_experiment(type, classes):
    list_co = [10]
    list_cr = [0.2]
    for key, value in classes.items():

        for cr in list_cr:
            for co in list_co:
            #du.create_cross_validation_folders(cf.XES_TRAIN_SRC, cf.CROSS_ROOT_STD, 5)
            #du.create_path_if_not_exists(cf.RESULTS_CROSS_FOLD)
                results_csv_path = f'{cf.RESULTS_CROSS_FOLD}/results_dms_cat_{key}_{cr}_cutoff_{co}.csv'

                # Open the CSV file in append mode, so we don't overwrite existing data
                with open(results_csv_path, mode='w', newline='') as file:
                    # Create a CSV writer object
                    csv_writer = csv.writer(file)

                    # Optionally, write headers if the file is newly created or empty
                    # Uncomment the next line if you want to write headers
                    csv_writer.writerow(['Fold', 'Avg Precision', 'Avg Recall', 'Avg F1', 'Avg pr time', 'Avg rec time'])

                    for fold in os.listdir(cf.CROSS_ROOT_STD):

                        # Construct paths
                        in_fold_train, in_fold_test, out_fold_train, out_fold_test, out_fold_gt = du.building_paths(fold)

                        #du.combine_files(in_fold_train, out_fold_train)

                        preprocessed_train, train_data = du.encoding_training_data_dump(cf.CROSS_ROOT_STD + fold + cf.CROSS_KB_SRC)
                        #preprocessed_train, train_data = du.encoding_training_data_dump('04 - Dataset-Industrial/train_manual/train.txt')
                        # Initialize metrics accumulators
                        total_precision = 0
                        total_recall = 0
                        total_f1 = 0
                        file_count = 0
                        total_pr_time = 0.0
                        total_rec_time = 0.0

                        # Iterate through each test file
                        for file in os.listdir(out_fold_test):
                            #du.split_file_by_ratio(out_fold_test + file, cr, out_fold_gt + file)

                            pr, rec, f1, pr_time, rec_time = eval_recommendations_classes(train_preprocessed=preprocessed_train,
                                                                                       train_data=train_data,
                                                                                       test_context=out_fold_test + file,
                                                                                       gt_context=out_fold_gt + file,
                                                                                       n_items=co, type=type,classes=classes[key])

                            # Accumulate metrics
                            total_precision += pr
                            total_recall += rec
                            total_f1 += f1
                            total_pr_time += pr_time
                            total_rec_time += rec_time
                            file_count += 1

                        # Calculate and write average metrics for the fold to the CSV file
                        if file_count > 0:
                            avg_precision = total_precision / file_count
                            avg_recall = total_recall / file_count
                            avg_f1 = total_f1 / file_count
                            avg_pr_time = total_pr_time / file_count
                            avg_rec_time = total_rec_time / file_count

                            # Write the fold and its average metrics to the CSV file
                            csv_writer.writerow([fold, avg_precision, avg_recall, avg_f1, avg_pr_time, avg_rec_time])
                        else:
                            print(f"Fold {fold}: No files to process.")

if __name__ == "__main__":
    #du.merge_folders(folder1='Datasets/Dataset_D1/', folder2='Datasets/Dataset_D2/',
                      #result_folder='Datasets/Dataset_Dm05', ratio=0.5)
    #du.parse_xes_traces('Datasets/Dataset_D1/BPMN_Designer', 'Datasets/D1_MG/', False)
    classes = du.extract_categories("Datasets/Features.csv")
    running_classes_experiment("class",classes)
    #running_rq2_experiment("attrs")


    #running_rq3_experiment("class")

    # print("Select configuration:\n1.train \n2.recommendation from KB \n3.recommendation from last session \n4.cross fold validation")
    # conf = input("Insert configuration: ")
    # main(conf)

    # list_co = [3,5,10]
    # list_cr = [0.2,0.5,0.8]
    # for cr in list_cr:
    #     for co in list_co:
    #         du.csv_to_latex(f'results_class_five_fold_mixed/results_context_{cr}_cutoff_{co}.csv', f'latex_results/results_class_mixed_context_{cr}_cutoff_{co}.tex')
    # #du.create_cross_validation_folders(cf.XES_TRAIN_SRC, cf.CROSS_ROOT_STD, 5)




