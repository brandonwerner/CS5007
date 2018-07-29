#Name: Brandon Werner
#Class: CS 5007
#Assignment 4

import sys
import copy
import numpy as np
import pandas as pd
from scipy import stats

# types are inferred correctly when reading in the data
# 0 = problem set id : int
# 2 = user id : int
# 3 = condition : string
# 30 = complete : int
# 31 = problem count : int
KEEP_LIST_INDEX = [0, 2, 3, 30, 31]

SUMMARY_STATISTICS_LABELS = []
SUMMARY_STATISTICS_LABELS.append("problem_set")
SUMMARY_STATISTICS_LABELS.append("condition")
SUMMARY_STATISTICS_LABELS.append("number_of_students")
SUMMARY_STATISTICS_LABELS.append("total_problems")
SUMMARY_STATISTICS_LABELS.append("problems_per_student_mean")
SUMMARY_STATISTICS_LABELS.append("problems_per_student_sd")
SUMMARY_STATISTICS_LABELS.append("completion_count")
SUMMARY_STATISTICS_LABELS.append("completion_percent_mean")
SUMMARY_STATISTICS_LABELS.append("completion_percent_sd")
SUMMARY_STATISTICS_LABELS.append("log_problem_count_mean")
SUMMARY_STATISTICS_LABELS.append("log_problem_count_sd")

CHI_SQUARED_LABELS = []
CHI_SQUARED_LABELS.append("problem_set")
CHI_SQUARED_LABELS.append("control_n")
CHI_SQUARED_LABELS.append("experiment_n")
CHI_SQUARED_LABELS.append("control_mean")
CHI_SQUARED_LABELS.append("experiment_mean")
CHI_SQUARED_LABELS.append("df")
CHI_SQUARED_LABELS.append("chi_squared_statistic")
CHI_SQUARED_LABELS.append("p_value")

TTEST_LABELS = []
TTEST_LABELS.append("problem_set")
TTEST_LABELS.append("control_n")
TTEST_LABELS.append("experiment_n")
TTEST_LABELS.append("control_mean")
TTEST_LABELS.append("experiment_mean")
TTEST_LABELS.append("df")
TTEST_LABELS.append("t_statistic")
TTEST_LABELS.append("p_value")


class Assignment4:
    def __init__(self):
        """
        Initializes self.__original_data to None
        Initializes self.__preprocessed_data to None
        Initializes self.__summary_statistics_data to None
        Initializes self.__ttest_data to None
        Initializes self.__chi_squared_data to None
        """

        self.__original_data = None
        self.__preprocessed_data = None
        self.__summary_statistics_data = None
        self.__chi_squared_data = None
        self.__ttest_data = None

    @property
    def original_data(self):
        return self.__original_data

    @original_data.setter
    def original_data(self, original_data):
        self.__original_data = original_data

    @property
    def preprocessed_data(self):
        return self.__preprocessed_data

    @preprocessed_data.setter
    def preprocessed_data(self, preprocessed_data):
        self.__preprocessed_data = preprocessed_data

    @property
    def summary_statistics(self):
        return self.__summary_statistics_data

    @summary_statistics.setter
    def summary_statistics(self, summary_statistics):
        self.__summary_statistics_data = summary_statistics

    @property
    def chi_squared_data(self):
        return self.__chi_squared_data

    @chi_squared_data.setter
    def chi_squared_data(self, chi_squared_data):
        self.__chi_squared_data = chi_squared_data

    @property
    def ttest_data(self):
        return self.__ttest_data

    @ttest_data.setter
    def ttest_data(self, ttest_data):
        self.__ttest_data = ttest_data

    def read_data(self, file_path):
        self.__original_data = pd.read_csv(file_path)



        """
        Reads data from the specified file_path into the data frame self.__data
        :param file_path: A path to the file.  The file is assumed to be in csv format
        :return: No return value
        """
        pass

    def preprocess(self):
        self.preprocessed_data = copy.deepcopy(self.original_data)

        self.__drop_columns()

        self.__fix_column_names()
        
        self.__add_log_problem_count()

        pass

    def __drop_columns(self):
        # creating drop_list variable
        drop_list = []
        # calling in index of self.__preprocessed_data.columns
        for i in self.__preprocessed_data.columns:
        # iterating through the range(number of columns) for self.__preprocessed_data.columns
            if i not in self.__preprocessed_data.columns[KEEP_LIST_INDEX]:
        # appending the index of the dropped column to the drop_list variable
                drop_list.append(i)
        self.__preprocessed_data = self.__preprocessed_data.drop(drop_list, axis=1)


        pass

    def __fix_column_names(self):
        label_mapping_dict = {}
        for i in self.preprocessed_data.columns:
            new_label = i
            new_label = new_label.replace(" ", "_")
            new_label = new_label.lower()
            label_mapping_dict[i] = new_label
        self.preprocessed_data = self.preprocessed_data.rename(columns=label_mapping_dict)

        pass

    def __add_log_problem_count(self):
        filter_1 = self.preprocessed_data[self.preprocessed_data["complete"] == 1]
        self.preprocessed_data["log_count"] = (np.log10(filter_1["problem_count"]))

        pass

    def calculate_summary_statistics(self):
        my_control_series = pd.Series()
        my_experiment_series = pd.Series()
        my_all_series = pd.Series()
        self.__summary_statistics_data = pd.DataFrame()
        unique_id_list = np.unique(self.preprocessed_data["problem_set"])

        for i in unique_id_list:
            filter_unique = self.preprocessed_data[self.preprocessed_data["problem_set"] == i]


        # calculate number of students for control
            filter_c = filter_unique[filter_unique["condition"] == 'C']
            my_control_series["problem_set_id"] = i
            my_experiment_series["problem_set_id"] = i
            my_all_series["problem_set_id"] = i
            my_control_series["condition"] = "Control"
            my_experiment_series["condition"] = "Experiments"
            my_all_series["condition"] = "All"
            my_control_series["number_of_students"] = len(filter_c["complete"])

            # calculate number of students for experiment
            filter_e = filter_unique[filter_unique["condition"] == 'E']
            my_experiment_series["number_of_students"] = len(filter_e["complete"])

            # calculate number of students for all
            my_all_series["number_of_students"]= np.count_nonzero(["complete"])

            #calculate total problem count for experiment
            my_experiment_series["total_problems"] = np.sum(filter_e["problem_count"])

            #calculate total problem count for control
            my_control_series["total_problems"]= np.sum(filter_c["problem_count"])

            # calculate total problem count for all
            my_all_series["total_problems"] = np.sum(filter_unique["problem_count"])

            #average problems per student for experiment
            my_experiment_series["problems_per_student_mean"] = np.mean(filter_e["problem_count"])

            # average problems per student for control
            my_control_series["problems_per_student_mean"] = np.mean(filter_c["problem_count"])

            # average problems per student for all
            my_all_series["problems_per_student_mean"] = np.average(filter_unique["problem_count"])

            #standard deviation problem per student for control
            my_control_series["problems_per_student_sd"] = np.std(filter_c["problem_count"])

            # standard deviation problem per student for experiment
            my_experiment_series["problems_per_student_sd"] = np.std(filter_e["problem_count"])

            # standard deviation problem per student for all
            my_all_series["problem_per_student_sd"] = np.std(filter_unique["problem_count"])

            # completion count per student for experiment
            filter_e1 = self.preprocessed_data[self.preprocessed_data["complete"] == 1]
            my_experiment_series["completion_count"] = np.sum(filter_e1["complete"])

            # completion count per student for control
            filter_c1 = self.preprocessed_data[self.preprocessed_data["complete"] == 1]
            my_control_series["completion_count"] = np.count_nonzero(filter_c1["complete"])

            # completion count per student for all
            filter_a1 = self.preprocessed_data[self.preprocessed_data["complete"] == 1]
            my_all_series["completion_count"] = np.count_nonzero(filter_a1["complete"])

            # completion percentage per student for experiment
            my_experiment_series["completion_percent_mean"] = np.mean(filter_e["complete"])

            #completion percentage per student for control
            my_control_series["completion_percent_mean"] = np.mean(filter_c["complete"])

            # completion percentage per student for all
            my_all_series["completion_percent_mean"] = np.mean(filter_unique["complete"])

            #standard deviation completion percent for experiment
            my_experiment_series["completion_percent_sd"] = np.std(filter_e["complete"])

            # standard deviation completion percent for control
            my_control_series["completion_percent_sd"] = np.std(filter_c["complete"])

            # standard deviation completion percent for all
            my_all_series["completion_percent_sd"] = np.std(filter_unique["complete"])

            #average log of problem count for experiment
            my_experiment_series["log_problem_count_mean"] = np.mean(filter_e["log_count"])

            # average log of problem count for control
            my_control_series["log_problem_count_mean"] = np.mean(filter_c["log_count"])

            # average log of problem count for all
            my_all_series["log_problem_count_mean"] = np.mean(filter_unique["log_count"])

            #standard deviation of log of problem count for experiment
            my_experiment_series["log_problem_count_sd"] = np.std(filter_e["log_count"])

            # standard deviation of log of problem count for control
            my_control_series["log_problem_count_sd"] = np.std(filter_c["log_count"])

            # standard deviation of log of problem count for all
            my_all_series["log_problem_count_sd"] = np.std(filter_unique["log_count"])

            self.__summary_statistics_data = self.__summary_statistics_data.append(my_control_series, ignore_index=True)
            self.__summary_statistics_data = self.__summary_statistics_data.append(my_experiment_series, ignore_index=True)
            self.__summary_statistics_data = self.__summary_statistics_data.append(my_all_series, ignore_index=True)
        """
        Calculated various summary statistics for each problem set and condition
            for each experiment and for each condition
                number of students
                total problem count
                average problems per student
                standard deviation problem per student
                completion count
                completion percent
                standard deviation completion percent
                average log of problem count
                standard deviation of log of problem count
        Store results in self.__summary_statistics
        Sort self.__summary_statistics by problem set then by condition
        :return: No return value
        """

        pass

    def calculate_chi_squared(self):
        """
        Performs a chi-squared test of independence on completion rates between control/experiment groups for all problem sets
        Stores the results in self.__chi_squared_data
        :return:  No return value
        """

        pass

    def calculate_ttest(self):
        """
        Performs a t-test of log(problem_count) between control/experiment groups for all problem sets
        Stores the results in self.__ttest_data
        :return:  No return value
        """

        pass

    def output_data_files(self):
        self.__summary_statistics_data.to_csv("summarystatisticsBrandon.csv", index=False)
        """
        Outputs all DataFrames (except the original) into files
        :return:  No return value
        """

        pass


if __name__ == "__main__":

    if len(sys.argv) > 1:
        file_path = sys.argv[1]

        assignment4 = Assignment4()
        assignment4.read_data(file_path)
        assignment4.preprocess()
        assignment4.calculate_summary_statistics()
        assignment4.calculate_chi_squared()
        assignment4.calculate_ttest()
        assignment4.output_data_files()

        # Get the input file path from the program arguments
        # If no path was specified do not do any of the following steps

        # Create an Assignment4 object

        # read in data using the read_data method of the Assignment4 object

        # pre-process the data using the preprocess function

        # calculate
        # for each experiment and for each condition
        #   number of students
        #   total problem count
        #   average problems per student
        #   standard deviation problem per student
        #   completion count
        #   completion percent
        #   standard deviation completion percent
        #   average log of problem count
        #   standard deviation of log of problem count

        # for each experiment
        # run chi-squared test of independence for completion rate
        # run t-test on log problem count

        # output results

    else:
        print("Enter an input file path for program arguments\n")
