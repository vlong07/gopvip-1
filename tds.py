
import os, json, sys, requests 
from sys import platform
from time import sleep
from datetime import datetime
from random import randint
from pystyle import Colors, Colorate
import uuid, re
from bs4 import BeautifulSoup
import os, json, sys, requests 
__check__ = requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/sever.txt').text
if "off" in __check__:
  exit("")
  
vLongzZ()
vLongzZz()
vanlongzZ()
vanlongzZz()
api_fb()
api_cookie()
api_tds()
api_like()
api_camxuc()


class Facebook_Api (object):
	def __init__(self, cookie):
		self.cookie = cookie
		self.user_id = cookie.split('c_user=')[1].split(';')[0]
		self.headers = {'authority': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'en-US,en;q=0.9','cookie': cookie}
	
	def get_thongtin(self):
		try:
		
			home = requests.get('https://m.facebook.com/profile.php',headers=self.headers).text
			self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten = home.split('<title>')[1].split('</title>')[0]
			self.user_id = self.cookie.split('c_user=')[1].split(';')[0]
			return ten, self.user_id
		except:
			return 0
	def like(self, id, type):
		if '_' in id:
			uid = id.split('_')[1]
		else:
			uid = id
		list = {'LIKE':1, 'LOVE':2, 'CARE':3, 'HAHA':4, 'WOW':5, 'SAD':6, 'ANGRY':7}
		headers = {
        "authority": "m.facebook.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        
        "sec-ch-ua-mobile": "?0",
        'sec-ch-ua-platform': '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3",
        "cookie":self.cookie
}
		
		try:
			link = 'https://m.facebook.com/reactions/picker/?ft_id='+uid
			data = requests.get(link, headers=headers).text
			get = data.split('<a href="')
			cx = get[list[type]].split('" style="display:block">')[0].replace("amp;", "").replace(";", "&")
			reac = requests.get('https://m.facebook.com'+cx, headers = headers).text
			
			return True
		except:
			return False 
	
class TraoDoiSub_Api (object):
	def __init__ (self, token):
		self.token = token
	
	def main(self):
		try:
			main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
			try:
				return main['data']
			except:
				False
		except:
			return False 
	
	def run(self, id):
		try:
			run = requests.get(f'https://traodoisub.com/api/?fields=run&id={id}&access_token={self.token}').json()
			try:
				run['data']['id']
				return True
			except:
				return False
		except:
			return False

	def get_job(self, type):
		try:
			get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}',headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
			return get
		except:
			return False 
		
	def nhan_xu(self, type, id):
		try:
			nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}',headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}).json()
			try:
				xu = nhan['data']['xu']
				msg = nhan['data']['msg']
				return msg, xu
			except:
				return nhan
		except:
			return False


def namtool(so):
	a= "\033[1;31m────"*so
	print(a)
def hoanthanh(dem, id, type, msg, xu):
	uid = id.split('_')[1] if '_' in id else id
	time=datetime.now().strftime("%H:%M:%S")
	print(f'\033[1;36m[{dem}\033[1;36m]\033[1;36m[\033[38;5;205m{time}\033[1;36m][\033[38;5;122m{type}\033[1;36m]\033[1;36m[\033[1;33mvL\033[1;36m][\033[38;5;048m{msg}]\033[1;36m[\033[38;5;225m{xu}\033[1;36m]')

def error(id, type):
    current_time = datetime.now().strftime("%H:%M:%S")
    uid = id.split('_')[1] if '_' in id else id
    error_message = f"[ THẤT BẠI ] ID: [ {uid} ] JOB: [ {type} ]"
    print(Colorate.Horizontal(Colors.red_to_purple, error_message), end='\r'); sleep(1); print('                                                         ', end = '\r')

def Nhap_Cookie():
	list_cookie = []
	i = 0
	while True:
		i += 1
		cookie = input(f'\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;31mNhập Cookie Facebook Thứ: \033[1;33m{i}: ')
		if cookie == '' and i > 1:
			break
		fb = Facebook_Api(cookie)
		name = fb.get_thongtin()
		if name != 0:
			ten = name[0]
			print('\033[1;31m────────────────────────────────────────────────────────────')
			print(f'\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;33mTên Facebook: {ten}')
			list_cookie.append(cookie)
			print('\033[1;31m────────────────────────────────────────────────────────────')
		else:
			print('Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
			print('\033[1;31m────────────────────────────────────────────────────────────')
			i-=1
	return list_cookie
def chongblock(delaybl):
	for i in range(delaybl, -1, -1):
		print(f' \033[1;36mĐang hoạt động chống block sẽ chạy lại sau {i} giây  ',end = '\r');sleep(1); print('                                                        ', end = '\r')
def chongloi_delay(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    return result if b >= 0 else -result

def nghingoi(delaymin, delaymax):
    delaymin_tmr = chongloi_delay(delaymin, 1000)
    delaymax_tmr = chongloi_delay(delaymax, 1000)
    delay = randint(delaymin_tmr, delaymax_tmr)
    delay_text_vs = ["X    ", "XX   ", "XXX  ", "XXXX ", "XXXXX"]
    delay_main = len(delay_text_vs)
    for i in range(delay, -100, -100):
        text = delay_text_vs[(delay - i) // 100 % delay_main]
        print(Colorate.Horizontal(Colors.red_to_white, f' [vLongzZ] [DELAY] [{text}] [{str(round(i / 1000, 3))}]'), end='\r');sleep(0.1)

def main():
	vLongvipprohehe = 0
	dem = 0
	
	while True:
		if os.path.exists('configtds.txt'):
			with open('configtds.txt', 'r') as f:
				token = f.read()
			tds = TraoDoiSub_Api(token)
			data = tds.main()
			try:
				
				print('\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mNhập [\033[1;33m1\033[1;33m] \033[1;37mGiữ Lại Tài Khoản '+ data['user'] )
				print('\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mNhập [\033[1;33m2\033[1;33m] \033[1;37mNhập Access_Token TDS Mới')
				chon = input('\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mNhập \033[1;31m==>:\033[1;33m ')
				if chon == '2':
					os.remove('configtds.txt')
				elif chon == '1':
					pass
				else:
					print('\033[1;31mLựa chọn không xác định !!!');namtool(14)
					continue 
			except:
				os.remove('configtds.txt')
		if not os.path.exists('configtds.txt'):
			token = input('\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mNhập Access_Token TDS:\033[1;33m ')
			with open('configtds.txt', 'w') as f:
				f.write(token)
		with open('configtds.txt', 'r') as f:
			token = f.read()
		tds = TraoDoiSub_Api(token)
		data = tds.main()
		try:
			xu = data['xu']
			xudie = data['xudie']
			user = data['user']
			break
		except:
			print('\033[1;31mAccess Token Không Hợp Lệ! Xin Thử Lại ')
			os.remove('configtds.txt')
			continue 
	print('\033[1;31m────────────────────────────────────────────────────────────')
	
	while True:
		if os.path.exists('Cookie_FB.txt'):
			print('\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mNhập [\033[1;33m1\033[1;33m] \033[1;37mSử Dụng Cookie Facebook Đã Lưu ')
			print('\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mNhập [\033[1;33m2\033[1;33m] \033[1;37mNhập Cookie Facebook Mới')
			chon = input('\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mVui Lòng Nhập:\033[1;33m ')
			if chon == '1':
				print('\033[1;32mĐang Lấy Dữ Liệu Đã Lưu');sleep(1)
				with open('Cookie_FB.txt', 'r') as f:
					list_cookie = json.loads(f.read())
					break
			elif chon == '2':
				os.remove('Cookie_FB.txt'); namtool(14)
			else:
				print('\033[1;31mLựa Chọn Không Xác Định.'); namtool(14); continue
		if not os.path.exists('Cookie_FB.txt'):
			list_cookie = Nhap_Cookie()
			with open('Cookie_FB.txt', 'w') as f:
				json.dump(list_cookie, f)
			break
	
	print(f'\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mTên Tài Khoản: \033[1;33m{user} ')
	print(f'\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mXu Hiện Tại: \033[1;33m{xu}')
	print(f'\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mXu Bị Phạt: \033[1;33m{xudie} ')
	print(f'\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;37mSố Cookie: {len(list_cookie)} ')
	print('\033[1;31m────────────────────────────────────────────────────────────')
	print('Mặc Định Chạy Nhiệm Vụ Like + Cảm Xúc')
	print('Và Đã Update Cho Giảm Thiểu Bị Block')
	print('\033[1;31m────────────────────────────────────────────────────────────')
	print('\033[1;31m[\033[1;37mvL\033[1;31m] \033[1;37m=> \033[1;36mCó Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ 123...)')
	nhiemvu = '12'
	delaymin = '3'
	delaymax = '10'
	nvblock = '10'
	delaybl = '5'
	doinick = '10'
	print('\033[1;31m────────────────────────────────────────────────────────────')
	while True:
		if len(list_cookie) == 0:
			print('\033[1;31mĐã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại  ')
			list_cookie = Nhap_Cookie()
			with open('Cookie_FB.txt', 'w') as f:
				json.dump(list_cookie, f)
		for cookie in list_cookie:
			loilike, loicx = 0, 0
			fb = Facebook_Api(cookie)
			name = fb.get_thongtin()
			if name != 0:
				ten = name[0]
				id = name[1]
			else:
				id = cookie.split('c_user=')[1].split(';')[0]
				print(f'\033[1;31mCookie Tài Khoản {id} Die', end='\r');sleep(5); print('                                     ', end = '\r' )
				list_cookie.remove(cookie)
				continue
			cau_hinh = tds.run(id)
			if cau_hinh == True:
				print(f'\033[1;33mĐang Cấu Hình ID FB: {id} \033[1;31m| \033[1;32mTên FB: {ten}')
				print('\033[1;31m────────────────────────────────────────────────────────────')
			else:
				print(f'\033[1;31mCấu Hình Thất Bại ID FB: {id} \033[1;31m| Tên FB: {ten} ', end = '\r')
				continue
			vLongvipprohehe = 0
			while True:
			
				nvlike = 1 if '1' in nhiemvu else 0
				nvlike2 = 1 if '1' in nhiemvu else 0
				nvcx = 1 if '2' in nhiemvu else 0
				if nvlike == 1:
					listlike = tds.get_job('like')
					if listlike == False:
						print('\033[1;31mKhông Get Được Nhiệm Vụ Like              ', end = '\r');sleep(5); print('                                                        ', end = '\r')
						nvlike = 0
					elif 'error' in listlike.text:
						if listlike.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listlike.json()['countdown']
							print(f'\033[1;31mĐang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(coun, 3))}              ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listlike.json()['error'] , end ='\r')
						nvlike = 0
					else:
						listlike = listlike.json()
						if len(listlike) == 0:
							print('\033[1;31mHết Nhiệm Vụ Like                             ', end = '\r');sleep(5); print('                                                        ', end = '\r')
							nvlike = 0
						else:
							print(f'\033[1;37mTìm Thấy {len(listlike)} Nhiệm Vụ Like                       ', end = '\r')
							for x in listlike:
								id = x['id']
								like = fb.like(id, 'LIKE')
								if like == False:
									error(id, 'LIKE')
									loilike += 1
								else:
									nhan=tds.nhan_xu('LIKE', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'LIKE', msg, xu)
										loilike = 0
										if dem % doinick == 0:
											namtool(14); print(f'\033[1;37mSố Xu Hiện Tại: \033[1;33m{xu} \033[1;31m| \033[1;37mSố Tài Khoản Facebook \033[1;33m{len(list_cookie)}'); namtool(14); vLongvipprohehe = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'LIKE')
										loilike += 1
								
								if loilike >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  \033[1;31mCookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' \033[1;31mTài Khoản {ten} Đã Bị Block Like !!!					')
									list_cookie.remove(cookie)
									vLongvipprohehe = 1
									break
			
				if vLongvipprohehe == 1:
					break
			
				if nvlike2 == 1:
					listlike2 = tds.get_job('likegiare')
					if listlike2 == False:
						print('\033[1;31mKhông Get Được Nhiệm Vụ Like 2                        ', end = '\r');sleep(5); print('                                                        ', end = '\r')
						nvlike2 = 0
					elif 'error' in listlike2.text:
						if listlike2.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listlike2.json()['countdown']
							print(f'\033[1;31mĐang Get Nhiệm Vụ Like 2, COUNTDOWN: {str(round(coun, 3))}                 ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listlike2.json()['error'] , end ='\r')
						nvlike2 = 0
					else:
						listlike2 = listlike2.json()
						if len(listlike2) == 0:
							print('\033[1;31mHết Nhiệm Vụ Like 2                                  ', end = '\r');sleep(5); print('                                                        ', end = '\r')
							nvlike2 = 0
						else:
							print(f'\033[1;37mTìm Thấy {len(listlike2)} Nhiệm Vụ Like 2                  ', end = '\r')
							for x in listlike2:
								id = x['id']
								like = fb.like(id, 'LIKE')
								if like == False:
									error(id, 'LIKE 2')
									loilike+=1
								else:
									nhan=tds.nhan_xu('LIKEGIARE', id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, 'LIKE 2', msg, xu)
										loilike=0
										if dem % doinick == 0:
											namtool(14); print(f'\033[1;37mSố Xu Hiện Tại: \033[1;33m{xu} \033[1;31m| \033[1;37mSố Tài Khoản Facebook \033[1;33m{len(list_cookie)}'); namtool(14); vLongvipprohehe = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, 'LIKE 2')
										loilike+=1
								

								if loilike >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f' \033[1;31m Cookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' \033[1;31mTài Khoản {ten} Đã Bị Block Like !!!					')
									list_cookie.remove(cookie)
									vLongvipprohehe = 1
									break
				if vLongvipprohehe == 1:
					break
			
				if nvcx == 1:
					listcx = tds.get_job('reaction')
					if listcx == False:
						print('\033[1;31mKhông Get Được Nhiệm Vụ Cảm Xúc                             ', end = '\r');sleep(5); print('                                                        ', end = '\r')
						nvcx = 0
					elif 'error' in listcx.text:
						if listcx.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listcx.json()['countdown']
							print(f'\033[1;31mĐang Get Nhiệm Vụ Cảm Xúc, COUNTDOWN: {str(round(coun, 3))}                 ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						else:
							print(listcx.json()['error'] , end ='\r')
						nvcx = 0
					else:
						listcx = listcx.json()
						if len(listcx) == 0:
							print('Hết Nhiệm Vụ Cảm Xúc                                 ', end = '\r');sleep(5); print('                                                        ', end = '\r')
							nvcx = 0
						else:
							print(f'\033[1;37mTìm Thấy {len(listcx)} Nhiệm Vụ Cảm Xúc                           ', end = '\r')
							for x in listcx:
								id = x['id']
								type = x['type']
								reac = fb.like(id, type)
								if reac == False:
									error(id, type)
									loilike += 1
								else:
									nhan=tds.nhan_xu(type, id)
									try:
										xu = nhan[1]
										msg = nhan[0] 
										dem+=1
										hoanthanh(dem, id, type, msg, xu)
										loilike = 0
										if dem % doinick == 0:
											namtool(14); print(f'\033[1;37mSố Xu Hiện Tại: \033[1;33m{xu} \033[1;31m| \033[1;37mSố Tài Khoản Facebook \033[1;33m{len(list_cookie)}'); namtool(14); vLongvipprohehe = 1; break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											nghingoi(delaymin, delaymax)
									except:
										error(id, type)
										loilike += 1
								
								
								if loilike >= 5:
									name = fb.get_thongtin()
									if name == 0:
										print(f'  \033[1;31mCookie Tài Khoản {ten} Đã Bị Out !!!                ')
									else:
										print(f' \033[1;31mTài Khoản {ten} Đã Bị Block Cảm Xúc !!!					')
									list_cookie.remove(cookie)
									vLongvipprohehe = 1
									break

				if vLongvipprohehe == 1:
					break
				if nvcx + nvlike == 0:
					for i in range(5, 0, -1):
						print(f' \033[1;31mTất Cả Các Nhiệm Vụ Đã Hết, Vui Lòng Chờ {i} Giây ', end = '\r');sleep(5); print('                                                        ', end = '\r')
	
if __name__ == '__main__':
	main()