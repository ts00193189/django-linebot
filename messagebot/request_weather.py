from datetime import datetime

import requests
from decouple import config



class WeatherReportRequester:
    def __init__(self):
        self.base_url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore'
        self.auth_key = config('WEATHER_API_KEY')

    def get_report(self, locations):
        data = self.get_data(locations)
        report = self.parse_report(data)
        return report

    def parse_report(self, data):
        element_map = {'Wx': '天氣狀況', 'PoP': '降雨機率', 'MaxT': '最高溫度', 'MinT': '最低溫度', 'CI': '溫度感受'}
        reports = []
        for info in data['records']['location']:
            report = {}
            report['location'] = info['locationName']
            report['time'] = []
            for weather_time in info['weatherElement'][0]['time']:
                weather_report = {}
                weather_report['start_time'] = datetime.strptime(weather_time['startTime'], '%Y-%m-%d %H:%M:%S')

                report['time'].append(weather_report)

            idx = 0
            for weather_report in report['time']:
                for weather_element in info['weatherElement']:
                    weather_report[element_map[weather_element['elementName']]] = weather_element['time'][idx]['parameter']['parameterName']
                idx += 1
            reports.append(report)
        #print(reports)
        return reports

    def get_data(self, locations):
        data_id = 'F-C0032-001'
        url = '{}/{}'.format(self.base_url, data_id)
        payload = {'Authorization': self.auth_key,
                   'locationName': [self.location_check(location) for location in locations]}

        response = requests.get(url, params=payload)
        return response.json()

    def location_check(self, location):
        country = {'宜蘭', '花蓮', '臺東', '澎湖', '金門',
                   '連江', '苗栗', '彰化', '南投', '雲林',
                   '嘉義', '屏東', '新竹'}
        city = {'臺北', '新北', '桃園', '臺中', '臺南',
                '高雄', '基隆', '新竹', '嘉義'}

        location = location.replace('台', '臺')
        if location in country and location in city:
            location = [location + '市', location + '縣']
        elif location in city:
            location = location + '市'
        elif location in country:
            location = location + '縣'
        else:
            return None

        return location

request = WeatherReportRequester()
request.get_report(['台中', '台北'])
