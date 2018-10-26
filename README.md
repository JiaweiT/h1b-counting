# Read Me

This is a repository developed for insight data engineer coding challenge.  
The function  is that given a h1b dataset as input, generate two file as output

    1. top_10_occupations.txt: Top 10 occupations for certified visa applications
    2. top_10_states.txt: Top 10 states for certified visa applications


### How to run the statistics

1. copy and paste the file in the input directory, rename the file as 'h1b_input.csv ' (without quotes)
2. run the run.sh  
To run the run.sh, open a terminal, change the working directory to this repository, then type in the command

```
./run.sh
```
&emsp;&emsp;If the system suggests that your don't have the right, run 
```
chmod +x run.sh
```
&emsp;&emsp;Then run the run.sh using the command above again.
3. check the results in the output folder.  

### My program design
The lauguage I used: python 3

	state_dict = {} # store the state name as key and and count as value
    occupation_dict = {} # store the occupation name as key and and count as value
	while file is not end:
    	read the next line
        if it is the first line: # which should be column names:
        	find out the column index of state name, occupation name (SOC Name) and status
        else:
        	if status == 'CERTIFIED':
            	update state_dict and occupation_dict 
                # if the key don't exist, create the item and init count as 1
                
    find out the top 10 states, expand the result if more than 1 state has the same tenth largest count
    calculate the percentage, round to the nearest 0.1
    write the result to the top_10_states.txt
    
    find out the top 10 occupations, expand the result if more than 1 occupation has the same tenth largest count
    calculate the percentage, round to the nearest 0.1
    write the result to the top_10_occupations.txt
                
                
        
        

### Repo directory structure

The directory structure for my repo looks like this:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_counting.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── my-own-test_2
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
              ├── my-own-test_2014
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
              ├── my-own-test_2015
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
              ├── my-own-test_2016
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```




