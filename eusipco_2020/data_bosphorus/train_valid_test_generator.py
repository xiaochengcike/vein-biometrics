"""
This code is generated by Ridvan Salih KUZU @UNIROMA3
LAST EDITED:  13.05.2020
ABOUT SCRIPT:
It is a script for generating the CSV files for train/validation/test partitions from Bosphorus database images.
It only divide the first half of the database for testing and second half of it for training/validation.
The both partitions are generated in classification mode (without pairing for verification).
"""

import argparse
import glob
import pandas as pd

parser = argparse.ArgumentParser(description='Database Partition Generator')

parser.add_argument('--database-dir', default='../data_bosphorus/Database', type=str,
                    help='path to the database root directory')
parser.add_argument('--train-val-outdir', default='../data_bosphorus/CSVFiles/output_list_train_val.csv', type=str,
                    help='path to the CSV output file including the list of train/validation partitions')
parser.add_argument('--test-outdir', default='../data_bosphorus/CSVFiles/output_list_test.csv', type=str,
                    help='path to the CSV output file including the list of test partition')

args = parser.parse_args()

def main():

    create_CSV_for_train_valid_test(args.database_dir,args.train_val_outdir,args.test_outdir)

def create_CSV_for_train_valid_test(database_root_dir,output_list_train_valid, output_list_test):
    """It generates the list of train/validation/test partitions in a given dataset (Bophorus here):
           Args:
               DATABASE_ROOT_DIR: Main directory for the Database (Bophorus in this case).
               OUTPUT_LIST_TRAIN_VALID: The output CSV file to write the generated train and valid file
                                        list for later feature extraction or training from the list.
               OUTPUT_LIST_TEST: The output CSV file to write the generated test file list
                                 for later feature extraction or training from the list.
        """
    file_bos = glob.glob(database_root_dir+"/*")

    df_train = pd.DataFrame()
    df_test = pd.DataFrame()

    counter = 0
    for X in file_bos[0:50]:
        filx = glob.glob(X + "/*")
        for fx in filx:
            df_test = df_test.append({'idx': fx, 'class': int(counter)}, ignore_index=True)
        counter += 1
    df_test = df_test.sort_values(by=['class']).reset_index(drop=True)
    df_test.to_csv(output_list_test, index=False)

    for X in file_bos[50:100]:
        filx = glob.glob(X + "/*")
        for fx in filx:
            df_train = df_train.append({'idx': fx, 'class': int(counter)}, ignore_index=True)
        counter += 1

    df_train = df_train.sort_values(by=['class']).reset_index(drop=True)
    df_train.to_csv(output_list_train_valid, index=False)


if __name__ == '__main__':
    main()