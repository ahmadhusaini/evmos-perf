import requests
import pandas
import csv
import sys



# Prometheus api endpoint for query 
URL = "http://localhost:9090/api/v1/query"

CSV_PATH = "/home/ahmad/Desktop/Blockchain/evmos-perf/perf.csv"

# Memory Query
PROMQL1 = {'query':'avg_over_time(rpc_requests[5m])'}

# CPU Query
PROMQL2 = {'query':'avg_over_time(tendermint_consensus_total_txs[5m])'}

print("row,instance,rpc_requests,tendermint_consensus_total_txs")

line_no = 1


rows = []
row = 0

r1 = requests.get(url = URL, params = PROMQL1)

r2 = requests.get(url = URL, params = PROMQL2)

r1_json = r1.json()['data']['result']
r2_json = r2.json()['data']['result']

columns = [ "row", "instance", "rpc_requests", "tendermint_consensus_total_txs"]
rows.append(columns)
row = row + 1

for result in r1_json:
    l = []
    l.append(result['metric'].get('instance', ''))
    l.append(result['value'][1])
    rows.append(l)

for result in r2_json:
    l = []
    l.append(result['value'][1])
    rows[row].append(l[0])
    row = row + 1

for ro in rows:
    line = str(line_no)
    line = line + "," + ro[0] + "," + ro[1] + "," + ro[2]
    print(str(line))
    line_no = line_no + 1
    # open the file in the write mode
    with open(CSV_PATH, 'w', encoding='UTF8') as f:
      # create the csv writer
      writer = csv.writer(f)
      # write a row to the csv file
      writer.writerow(ro)


df = pandas.read_csv(CSV_PATH)

print(df)
    