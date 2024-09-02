# (코드설명) kml 파일을 다음카카오 지도상에 표시할 수 있는 코드로 변환
# (사전준비) 구글어스 프로 프로그램과 시장 지도를 이용하여 다각형을 지도상에 표시한 후 kml 파일 형태로 저장

from bs4 import BeautifulSoup
import csv

file_name = "하복대시장.kml"

with open(file_name, 'r', encoding = "utf-8") as f:
        s = BeautifulSoup(f, 'xml')
        content =s.find_all('coordinates')

        coord_result = []
        if len(content) == 1:
            coords_str = content[0].text
            coords_str = coords_str.replace("\n","").replace("\t","")

            coords_list = coords_str.split(" ")

            for coord in coords_list:
                coord_detail = coord.split(",")
                if len(coord_detail) == 3:
                    coord_result.append([coord_detail[1], coord_detail[0]])
                    print(coord_detail)
                    
            #print(coords_str)
            
        else:
            print("파일 점검 필요")
        print(coord_result)

js_code = f''' "{file_name.split('.')[0]}" : [ \n'''

for i in range(len(coord_result)-1):
    temp = f"new kakao.maps.LatLng({coord_result[i][0]}, {coord_result[i][1]} ), \n"
    #print(temp)
    js_code = js_code + temp

js_code = js_code + "],"
print(js_code)

"""
"가경터미널시장" : [ 
        new kakao.maps.LatLng(36.62799151195114, 127.43713454567325), 
        new kakao.maps.LatLng(36.6274705948595, 127.43573443262054), 
        new kakao.maps.LatLng(36.62726825421333, 127.4358309921414), 
        new kakao.maps.LatLng(36.62707882844614, 127.4352999147766), 
        new kakao.maps.LatLng(36.627272559339, 127.4351818975844), 
        new kakao.maps.LatLng(36.626433055286284, 127.43288592675466), 
        new kakao.maps.LatLng(36.62676885800468, 127.43264989237028), 
        new kakao.maps.LatLng(36.62763418903611, 127.43504242272093), 
        new kakao.maps.LatLng(36.62837896866158, 127.43461863371262), 
        new kakao.maps.LatLng(36.6285468659645, 127.4350799736457), 
        new kakao.maps.LatLng(36.62778917267259, 127.43552522032527), 
        new kakao.maps.LatLng(36.62830147747534, 127.43691460454237) 
   ],
"""
