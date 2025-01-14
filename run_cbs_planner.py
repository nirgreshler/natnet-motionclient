import os

SCENARIO_FILE = 'data/scenario.scen'
MAP_FILE = 'data/map.map'

#os.path.p
#exit_code = os.system('wsl ~/CBSH2-RTC/cbs -m ~/CBSH2-RTC/random-32-32-20.map -a random-32-32-20-random-1.scen -o test.csv --outputPaths=paths.txt -k 30 -t 60')
exit_code = os.system(f'wsl ~/CBSH2-RTC/cbs -m {MAP_FILE} -a {SCENARIO_FILE} -o test.csv --outputPaths=paths4.txt -k 2 -t 60')

if exit_code != 0:
    print('Error running the planner')