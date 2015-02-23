# Assignment-Grading-Suite
Set of scripts to automate TA grading.

### selection 

select only qualified submissionts from `submissions`, and copy into `reports`

Usage: `python selection.py section date(MMDD)`

### compile

generate html files from `reports` into `published`

Usage: `python compile.py`

### organize 

move all html reports into `grading`

Usage: `python organize foldername`

### seat pattern

randomly assign seating pattern to each student, and generate the pattern in `roster`

Usage: `python assignSeat.py sec_num`
