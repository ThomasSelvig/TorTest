# run as admin for tor service to work
import requests, datetime, subprocess

def newIdentity():
	stop = subprocess.run("tor --service stop", capture_output=True)
	start = subprocess.run("tor --service start", capture_output=True)
	
	if " success" in start.stdout.decode():
		return True

	print(start.stdout.decode().strip())
	return False


def main():
	s = requests.Session()
	s.proxies = {
		"http": "socks5://127.0.0.1:9050",
		"https": "socks5://127.0.0.1:9050"
	}

	a = datetime.datetime.now()
	for i in range(10):
		print(newIdentity(), end=" ")
		print(s.get("http://icanhazip.com").text)

	secs = round((datetime.datetime.now()-a).total_seconds(), 2)
	print("Seconds:", secs)
	print("Req/sec:", round(secs/10, 2))


if __name__ == '__main__':
	main()