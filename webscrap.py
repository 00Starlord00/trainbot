from datetime import date, time, timedelta
import requests
from bs4 import BeautifulSoup

def train_delay(trainNo, journeyStn):
	'''Return delay'''
	yesterday = date.today() - timedelta(1)
	startDate = yesterday.strftime("%d/%m/%Y")
	journeyDate = date.today().strftime("%d/%m/%Y")
	baseURL = f'https://enquiry.indianrail.gov.in/xyzabc/SelectedDateOfTrain?trainNo={trainNo}&startDate={startDate}&journeyStn={journeyStn}&journeyDate={journeyDate}&boardDeboard=0&langFile=props.en-us'
	r=requests.get(baseURL,verify=False)
	soup = BeautifulSoup(r.text, 'html.parser')

	trainName = (soup.find('div', {'id':'trainDetailDiv'}).find_all('div')[0].find_all('div')[1].text).strip()
	
	delay = soup.find('div', {'id':'qrdStnMainDiv'}).find_all('table')[2].find('tr')\
	.find_all('td')[1].find_all('span')[1].find('font').text

	if(delay == 'Right time'):
		live_status = f'Train: {trainName}\nStatus: ON TIME'
	else:
		live_status = f'Train: {trainName}\nDelay: {delay}'
	
	return live_status

if __name__ == '__main__':
	print(train_delay('19016','PLG'))