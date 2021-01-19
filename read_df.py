from dxc import ai
import json
import sys


def read_file():
	inp = json.loads(sys.argv[1])
	if (inp["loc"] == "remote"):
		if (inp["type"]== "csv"):
			df=ai.read_data_frame_from_remote_csv(inp["url"])
		elif (inp["type"]== "json"):
			df=ai.read_data_frame_from_remote_json(inp["url"])
	elif (inp["loc"] == "local"):
		if (inp["type"]== "csv"):
			df=ai.read_data_frame_from_local_csv()
		elif (inp["type"]== "json"):
			df=ai.read_data_frame_from_local_json()

	df.to_csv("df_tmp.csv",index=False)

if __name__ == "__main__":
	read_file()
