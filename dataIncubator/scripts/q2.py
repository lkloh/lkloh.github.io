
import os, csv, math
from scipy.stats import *


# ************************************************************* #

def get_integer(i):
	try:
		return int(i)
	except:
		return -1

def read_int_from_row(headers, row, label):
	index = headers.index(label)
	value = get_integer(row[index])
	return value 

def read_float_from_row(headers, row, label):
	index = headers.index(label)
	value = get_float(row[index])
	return value 

def get_float(f):
	try:
		return float(f)
	except:
		return -1	

def get_floats(headers, row, labels):
	all_floats = []
	for label in labels:
		index = headers.index(label)
		value = get_float(row[index])
		all_floats.append(value)
	return all_floats

# ************************************************************* #

def question_1_SAT_4year_college():
	'''
	Write the four-year colleges we want to investigate to a file.
	Using 2014-2015 school year to compute, 
	as they applied in 2013-2014 academic year.
	Only takes those with valid entries. 
	'''
	write_file = open("Q2Colleges_question1.csv", 'w')
	with open('CollegeScorecard_Raw_Data/MERGED2014_15_PP.csv') as csvfile:
		# read data from the files 
		student_reader = csv.reader(csvfile, delimiter=',')
		first_row = True
		all_headers = []
		for row in student_reader:
			if first_row:
				all_headers = row
				#print all_headers[1]
				first_row = False
			else:
				# CCUGPROF: Carnegie Classification -- undergraduate profile
				# Four year schools have values from between 5 - 15.
				index = all_headers.index("CCUGPROF")

				value_ranges = range(5,15+1) # all values for name
				process_body(write_file, row, index, value_ranges)
	'''
	Parse that file and find the average sat score
	'''
	print 'Average SAT score is: %.10f' % get_average_sat_score(all_headers)

	# delete file
	os.remove('Q2Colleges_question1.csv')


def get_average_sat_score(all_headers):
	# SAT_AVG: Average SAT equivalent score of students admitted
	average_sat_score_index = all_headers.index("SAT_AVG")

	# UGDS: Enrollment of undergraduate certificate/degree-seeking students
	average_enrollment_degree_seeking_student_index = all_headers.index("UGDS")

	total_sat_score = 0
	num_people = 0
	with open("Q2Colleges_question1.csv", 'r') as csvfile:
		student_reader = csv.reader(csvfile, delimiter=',')
		for row in student_reader:
			avg_sat_score = get_integer(row[average_sat_score_index])
			num_enrolled_students = get_integer(row[average_enrollment_degree_seeking_student_index])
			if avg_sat_score > 0 and num_enrolled_students > 0:
				num_admitted_students = num_enrolled_students / 4.0
				total_sat_score += avg_sat_score * num_admitted_students
				num_people += num_admitted_students
	return total_sat_score / num_people



def process_body(write_file, array, index, value_ranges):
	value = get_integer(array[index])
	if value in value_ranges:
		line = ", ".join(array)
		write_file.write(line)


# ************************************************************* #


'''
What is the Pearson correlation coefficient between the 
average SAT score of students at an institution and the 
percent that are still enrolled after two years? 
Consider all types of institutions, but ignore those with invalid entries. 
Consider only data from 2013.

Cannot figure out from 
'''
def question_2():
	print 'cannot be computed from available data'

# ************************************************************* #

def question_3_and_4():
	'''
	* HI_INC_COMP_ORIG_YR4_RT: Percent of high-income (above $75,000 in nominal family income) students who completed within 4 years at original institution
	* HI_INC_COMP_4YR_TRANS_YR4_RT: Percent of high-income (above $75,000 in nominal family income) students who transferred to a 4-year institution and completed within 4 years
	'''
	high_income_var_names = ['HI_INC_COMP_ORIG_YR4_RT', 'HI_INC_COMP_4YR_TRANS_YR4_RT']

	'''
	* MD_INC_COMP_ORIG_YR4_RT: Percent of middle-income (between $30,000 and $75,000 in nominal family income) students who completed within 4 years at original institution
	* MD_INC_COMP_4YR_TRANS_YR4_RT: Percent of middle-income (between $30,000 and $75,000 in nominal family income) students who transferred to a 4-year institution and completed within 4 years
	'''
	mid_income_var_names = ['MD_INC_COMP_ORIG_YR4_RT', 'MD_INC_COMP_4YR_TRANS_YR4_RT']

	'''
	* LO_INC_COMP_ORIG_YR4_RT: Percent of low-income (less than $30,000 in nominal family income) students who completed within 4 years at original institution
	* LO_INC_COMP_4YR_TRANS_YR4_RT: Percent of low-income (less than $30,000 in nominal family income) students who transferred to a 4-year institution and completed within 4 years
	'''
	low_income_var_names = ['LO_INC_COMP_ORIG_YR4_RT', 'LO_INC_COMP_4YR_TRANS_YR4_RT']

	write_file = open("Q2Colleges_question3.csv", 'w')

	high_income_completion_percentage = []
	low_income_completion_percentage = []

	with open('CollegeScorecard_Raw_Data/MERGED2013_14_PP.csv') as csvfile:
		# read data from the files 
		student_reader = csv.reader(csvfile, delimiter=',')
		first_row = True
		headers = []
		for row in student_reader:
			if first_row:
				headers = row
				first_row = False
			else:
				[has_required_data, high_complete_percent, low_complete_percent] \
					= get_completion_figures(headers, row, \
						high_income_var_names, mid_income_var_names, low_income_var_names)
				if has_required_data:
					high_income_completion_percentage.append(high_complete_percent)
					low_income_completion_percentage.append(low_complete_percent)

	find_income_completion_percent_different(high_income_completion_percentage, low_income_completion_percentage)

	income_completion_t_test(high_income_completion_percentage, low_income_completion_percentage)




def income_completion_t_test(high_income_completion_percentage, low_income_completion_percentage):
	t_statistic, p_value = ttest_ind(high_income_completion_percentage, low_income_completion_percentage, equal_var=True)
	significance_level = 0.05

	if p_value < significance_level:
		print "Significant, log p = %.10f" % math.log10(p_value)
	else:
		print "Not significant, log p = %.10f" % math.log10(p_value)
	


def find_income_completion_percent_different(high_income_completion_percentage, low_income_completion_percentage):
	num_schools_with_data = len(high_income_completion_percentage)
	difference = (sum(high_income_completion_percentage) - sum(low_income_completion_percentage)) / float(num_schools_with_data)

	print "Difference in percentage is %.10f" % difference



def get_completion_figures(headers, row, high_income_var_names, mid_income_var_names, low_income_var_names):
	# high
	high_orig_index = headers.index(high_income_var_names[0])
	high_orig_percent = get_float(row[high_orig_index])

	high_trans_index = headers.index(high_income_var_names[1])
	high_trans_percent = get_float(row[high_trans_index])

	# mid
	mid_orig_index = headers.index(mid_income_var_names[0])
	mid_orig_percent = get_float(row[mid_orig_index])

	mid_trans_index = headers.index(mid_income_var_names[1])
	mid_trans_percent = get_float(row[mid_trans_index])

	# low
	low_orig_index = headers.index(low_income_var_names[0]) 
	low_orig_percent = get_float(row[low_orig_index])

	low_trans_index = headers.index(low_income_var_names[1])
	low_trans_percent = get_float(row[low_trans_index]) 

	# checking
	if high_orig_percent>0 and high_trans_percent>0 \
		and mid_orig_percent>0 and mid_trans_percent>0 \
		and low_orig_percent>0 and low_trans_percent>0:
		return True, high_orig_percent + high_trans_percent, low_orig_percent + low_trans_percent
	else:
		return False, -1, -1

# ************************************************************* #



def get_min_diversity(array):
	minInd = -1
	minPercent = 1.0
	for i in range(len(array)):
		value = array[i]
		if value >= 0.0 and value < minPercent:
			minPercent = value
			minInd = i

	return minInd, minPercent

def get_max_diversity(array):
	maxInd = -1
	maxPercent = 0.0
	for i in range(len(array)):
		value = array[i] 
		if (value >= 0.0) and (value > maxPercent):
			maxPercent = value
			maxInd = i
	return maxInd, maxPercent


'''
MAXIMUM DIVERSITY OF STUDENT BODY

UGDS_WHITE: Total share of enrollment of undergraduate degree-seeking students who are white
UGDS_BLACK: Total share of enrollment of undergraduate degree-seeking students who are black
UGDS_HISP: Total share of enrollment of undergraduate degree-seeking students who are Hispanic
UGDS_ASIAN: Total share of enrollment of undergraduate degree-seeking students who are Asian
UGDS_AIAN: Total share of enrollment of undergraduate degree-seeking students who are American Indian/Alaska Native
UGDS_NHPI: Total share of enrollment of undergraduate degree-seeking students who are Native Hawaiian/Pacific Islander
UGDS_2MOR: Total share of enrollment of undergraduate degree-seeking students who are two or more races
UGDS_NRA: Total share of enrollment of undergraduate degree-seeking students who are non-resident aliens
UGDS_UNKN: Total share of enrollment of undergraduate degree-seeking students whose race is unknown
UGDS_WHITENH: Total share of enrollment of undergraduate degree-seeking students who are white non-Hispanic
UGDS_BLACKNH: Total share of enrollment of undergraduate degree-seeking students who are black non-Hispanic
UGDS_API: Total share of enrollment of undergraduate degree-seeking students who are Asian/Pacific Islander
UGDS_AIANOLD: Total share of enrollment of undergraduate degree-seeking students who are American Indian/Alaska Native
UGDS_HISPOLD: Total share of enrollment of undergraduate degree-seeking students who are Hispanic
'''
def question_5_diversity():
	diversity_labels = ['UGDS_WHITE', 'UGDS_BLACK', 'UGDS_HISP', 'UGDS_ASIAN', 'UGDS_AIAN', 'UGDS_NHPI', 'UGDS_2MOR', 'UGDS_NRA', 'UGDS_UNKN', 'UGDS_WHITENH', 'UGDS_BLACKNH', 'UGDS_API', 'UGDS_AIANOLD', 'UGDS_HISPOLD']

	with open('CollegeScorecard_Raw_Data/MERGED2013_14_PP.csv') as csvfile:
		# read data from the files 
		student_reader = csv.reader(csvfile, delimiter=',')
		first_row = True
		headers = []
		maxDiversity = 1.0
		for row in student_reader:
			if first_row:
				headers = row
				first_row = False
			else:
				diversity_percentages = get_floats(headers, row, diversity_labels)
				if any([percent>0 for percent in diversity_percentages]):
					minIndex, minPercent = get_min_diversity(diversity_percentages)
					maxIndex, maxPercent = get_max_diversity(diversity_percentages)
					if (minPercent >= 0.0) and (maxPercent >= 0.0):
						maxDiversity = min(maxDiversity, maxPercent - minPercent)

		print "Metric of most diverse institution: %.10f" % maxDiversity




# ************************************************************* #

'''
OPEID: 8-digit OPE ID for institution
UGDS_WOMEN: Total share of enrollment of undergraduate degree-seeking students who are women
'''
def read_women_enrollment(d, file_name, i):
	with open(file_name, 'r') as csvfile:
		# read data from the files 
		student_reader = csv.reader(csvfile, delimiter=',')
		first_row = True
		headers = []
		for row in student_reader:
			if first_row:
				headers = row
				first_row = False
			else:
				school_id = read_int_from_row(headers, row, 'OPEID')
				women_share = read_float_from_row(headers, row, 'UGDS_WOMEN')
				if (i == 0):
					if women_share >= 0.0:
						d[school_id] = [women_share]
				else: #i > 0
					if school_id in d:
						records = d[school_id]
						if (records is not None) and (len(records) == i) and (women_share >= 0.0):
							d[school_id].append(women_share)
						else:
							del d[school_id] 





def question_6_women():
	years_to_consider = ['MERGED2001_02_PP.csv', 'MERGED2002_03_PP.csv', 'MERGED2003_04_PP.csv', 'MERGED2004_05_PP.csv', 'MERGED2005_06_PP.csv', 'MERGED2006_07_PP.csv', 'MERGED2007_08_PP.csv', 'MERGED2008_09_PP.csv', 'MERGED2009_10_PP.csv', 'MERGED2010_11_PP.csv']

	#years_to_consider = ['MERGED2001_02_PP.csv', 'MERGED2002_03_PP.csv']
	num_years_polled = len(years_to_consider)

	d = {}
	for i in range(len(years_to_consider)):
		file_name = "CollegeScorecard_Raw_Data/" + years_to_consider[i]
		read_women_enrollment(d, file_name, i)
	
	total_women_shares = 0.0
	num_schools_polled = 0
	for school_id in d:
		total_women_shares += sum(d[school_id])
		num_schools_polled += num_years_polled
	average_women_share = total_women_shares / num_schools_polled

	print "Average share of enrollment of undergraduate women seeking degrees between 2001 and 2010 is %.10f" % average_women_share

# ************************************************************* #


'''
Assume for the 2014-2015 academic year (latest info available)
'''
def question_7_region_in_city():
	region_id_range = range(0, 9+1)
	locale_id_range = [11,12,13, 21,22,23, 31,32,33, 41,42,43]

	region_number_of_schools_in_city = {}
	for region_id in range(0, 9+1):
		region_number_of_schools_in_city[region_id] = 0

	region_number_of_schools = {}
	for region_id in range(0, 9+1):
		region_number_of_schools[region_id] = 0

	filename = 'CollegeScorecard_Raw_Data/MERGED2014_15_PP.csv'

	region_number_of_schools = {}
	for region_id in range(0, 9+1):
		region_number_of_schools[region_id] = 0

	with open(filename, 'r') as csvfile:
		# read data from the files 
		student_reader = csv.reader(csvfile, delimiter=',')
		first_row = True
		headers = []

		for row in student_reader:
			if first_row:
				headers = row
				first_row = False
			else:
				region_id = read_int_from_row(headers, row, 'REGION')
				locale_id = read_int_from_row(headers, row, 'LOCALE')
				if region_id in region_id_range and locale_id in locale_id_range:
					region_number_of_schools[region_id] += 1
					if locale_id in [11,12,13]:
						region_number_of_schools_in_city[region_id] += 1

	# compute probability of being in city
	largest_probability_of_school_in_city = 0.0
	for region_id in range(0, 9+1):
		prob = float(region_number_of_schools_in_city[region_id]) / region_number_of_schools[region_id]
		largest_probability_of_school_in_city = max(largest_probability_of_school_in_city, prob)

	print "Largest probability of a academic institution in some region, is located in a city is %.10f" % largest_probability_of_school_in_city

				
	


				


	

		

# ************************************************************* #

def print_answer():
	#question_1_SAT_4year_college()
	#question_2()
	#question_3_and_4()
	#question_5_diversity()
	question_6_women()
	#question_7_region_in_city()


print_answer()











