#!/usr/bin/python
import sys

'''
Developed by Jiawei Tang on Oct 24, 2019 for Insight Data Engineering - Coding Challenge

Input:
1. input_path, from stdin, a file path of the H1B data, I am using the .csv file format
2. occupation_path, from stdin, a file path for the output occupation data
3. state_path, from stdin, a file path for the output state data

Output:
1. top_10_states.txt, contains 3 columns('TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE'), sep = ';'
2. top_10_occupations.txt, contains 3 columns('TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE'), sep = ';'
'''

def main(argv=None):
    
    # get input_file_path from command line
    if argv is None:
        argv = sys.argv
    input_path = argv[-3]
    occupation_path = argv[-2]
    state_path = argv[-1]    
    
    # read the file
    with open(input_path,"r") as csvfile:
        line_count = 0
        state_dict = {}
        occupation_dict = {}
        for row in csvfile.readlines():   
            row = row.strip('\n').split(';')
            
            # get column names and find out index of state, job title and status
            if line_count == 0:
                state_idx = None
                title_idx = None
                status_idx = None            
                for i in range(len(row)):
                    # I think that EMPLOYER_STATE is better than worksite state 
                    if 'STATE' in row [i] and 'WORK' in row [i] and state_idx is None:
                        state_idx = i
                    elif 'SOC_NAME' in row [i]:
                        title_idx = i
                    elif 'STATUS' in row [i]:
                        status_idx = i

                    if state_idx and title_idx and status_idx:
                        break   
            else:

                if row[status_idx] == 'CERTIFIED':
                    try:
                        state_dict[row[state_idx].strip('\"')] += 1
                    except:
                        state_dict[row[state_idx].strip('\"')] = 1
                    try:
                        occupation_dict[row[title_idx].strip('\"')] += 1
                    except:
                        occupation_dict[row[title_idx].strip('\"')] = 1
            # use the two lines below to control row number when testing
#             if line_count == 1000:
#                 break
            line_count += 1
    print(f'Processed {line_count} lines.')
    
    # Find out top 10 state
    state_result = sorted(state_dict.items(), reverse=True, key = lambda x: x[1])
    if len(state_dict) <= 10:
        n = len(state_dict)
    else:
        n = 10        
        # get all sates with same number as the 10th state
        while state_result[n][1] == state_result[9][1]:
            n += 1
    total = sum(state_dict.values())
    with open(state_path,"w") as file:
        file.write(';'.join(['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']))
        file.write('\n')
        for i in range(n): 
            # kept one decimal place
            percent = str(round(state_result[i][1]/total*100, 1)) + '%'
            file.write(';'.join([str(state_result[i][0]), str(state_result[i][1]), percent]))
            file.write('\n')
    print('top_10_states.txt output finished')    

    # Find out top 10 occupation
    # The occupations dictionary might be very large, by using partial sort or distibuted system may solve the problem.
    occupation_result = sorted(occupation_dict.items(), reverse=True, key = lambda x: x[1])
    if len(occupation_dict) <= 10:
        n = len(occupation_dict)
    else:
        n = 10   
    # get all sates with same number as the 10th occupation
        while occupation_result[n][1] == occupation_result[9][1]:
            n += 1
        total = sum(occupation_dict.values())
    with open(occupation_path,"w") as file:
        file.write(';'.join(['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']))
        file.write('\n')
        for i in range(n):
            # kept one decimal place
            percent = str(round(occupation_result[i][1]/total*100, 1)) + '%'
            file.write(';'.join([str(occupation_result[i][0]), str(occupation_result[i][1]), percent]))
            file.write('\n')
    print('top_10_occupations.txt output finished')  
    
if __name__ == "__main__":
    sys.exit(main())
