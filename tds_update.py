# tự httprequest để lấy func (cmt, share...)
# open source nên không có input token tds hay cookie Facebook
import os, json, sys, requests 
__check__ = requests.get('https://raw.githubusercontent.com/luvanlong2007/gopvip/main/u.txt').text
if "off" in __check__:
  exit("Suỵt")
import requests, os, sys, base64, time, json, re, uuid
from datetime import datetime
os.system("clear")
ck =input("Nhập Cookie FB : ")
InputToken = input("Token TDS : ")

exec("""\nHeadersTds = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "max-age=0", "sec-ch-ua": "\\"Not-A.Brand\\";v=\\"99\\", \\"Chromium\\";v=\\"124\\"", "sec-ch-ua-mobile": "?1", "sec-ch-ua-platform": "\\"Android\\"", "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1"}\n""")
exec("""\nheaders_fb = {"accept": "*/*", "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", "content-type": "application/x-www-form-urlencoded", "sec-ch-prefers-color-scheme": "light", "sec-ch-ua": "\\"Not-A.Brand\\";v=\\"99\\", \\"Chromium\\";v=\\"124\\"", "sec-ch-ua-full-version-list": "\\"Not-A.Brand\\";v=\\"99.0.0.0\\", \\"Chromium\\";v=\\"124.0.6327.4\\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "\\"\\"", "sec-ch-ua-platform": "\\"Linux\\"", "sec-ch-ua-platform-version": "\\"\\"", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "x-asbd-id": "129477", "x-fb-friendly-name": "CometUFIFeedbackReactMutation", "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"}\n""")
exec("""\nheaders_mbasic = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", "dpr": "1.850000023841858", "sec-ch-prefers-color-scheme": "light", "sec-ch-ua": "\\"Not-A.Brand\\";v=\\"99\\", \\"Chromium\\";v=\\"124\\"", "sec-ch-ua-full-version-list": "\\"Not-A.Brand\\";v=\\"99.0.0.0\\", \\"Chromium\\";v=\\"124.0.6327.4\\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "\\"\\"", "sec-ch-ua-platform": "\\"Linux\\"", "sec-ch-ua-platform-version": "\\"\\"", "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "same-origin", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "viewport-width": "980"}\n""")
def countdown1(seconds: int): # delay get job tds anti band
	while seconds:
		timer = f'{seconds // 60:02d}:{seconds % 60:02d}';print(f'Delay Lấy Nhiệm Vụ {timer}                    ', end='\r');time.sleep(1);seconds -= 1
def countdown(seconds: int): # delay job anti spam
	while seconds:
		timer = f'{seconds // 60:02d}:{seconds % 60:02d}';print(f'Đang Chờ Delay {timer}                    ', end='\r');time.sleep(1);seconds -= 1
def get_substring_after_underscore(text): # lấy id phía sau _ nếu có 
	return text.split('_')[1] if '_' in text else text

def _encode_to_base64(_data):
	byte_representation = _data.encode('utf-8')
	base64_bytes = base64.b64encode(byte_representation)
	base64_string = base64_bytes.decode('utf-8')
	return base64_string

def GetThongTin(cookie): # lấy data Facebook
	try:
		_heads={"accept": "*/*", "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7", "content-type": "application/x-www-form-urlencoded", "sec-ch-prefers-color-scheme": "light", "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"", "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "\"\"", "sec-ch-ua-platform": "\"Linux\"", "sec-ch-ua-platform-version": "\"\"", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "x-asbd-id": "129477", "x-fb-friendly-name": "ProfileCometTimelineListViewRootQuery", "x-fb-lsd": "7_RkODA0fo-6ShZlbFpHEW"}
		with requests.get("https://www.facebook.com/me", headers=_heads, cookies={"cookie": cookie}) as noo:
			with requests.get(noo.url, headers=_heads, cookies={"cookie": cookie}) as vcl:
				_sea = vcl.text.split(',"NAME":"')[1].split('",')[0]
				_name = bytes(_sea, "utf-8").decode("unicode_escape")
				_fb1 = vcl.text.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
				_idfb = cookie.split("; c_user=")[1].split(";")[0]
				if _fb1 or _idfb or _name:
					return [_fb1, _idfb, _name]
				else:return False
	except BaseException as err:
		return str(err) 

def _Bypass(cookie, fb1):
	try:
		with requests.post('https://mbasic.facebook.com/checkpoint/601051028565049/submit/', headers=headers_mbasic, cookies={"cookie": cookie}, data={"fb_dtsg": fb1}) as rs:
			_search = rs.text.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			if _search:return True
			else:return False
	except BaseException as err:
		return str(err)

def DangNhapTds(Token): 
	Url = f"https://traodoisub.com/api/?fields=profile&access_token={Token}"
	try:
		with requests.get(Url, headers=HeadersTds) as wow:
			if 'error' not in wow.json():
				DataGet = wow.json()['data']
				UserTds = DataGet['user']
				XuTds = DataGet['xu']
				XudieTds = DataGet['xudie']
				return [UserTds, XuTds, XudieTds]
			else:return False
	except BaseException as err:
		return str(err)
	
	
def CauHinhFB(Token, ID):
	Url = "https://traodoisub.com/api/?fields=run&id=%s&access_token=%s" % (ID, Token)
	try:
		with requests.get(Url, headers=HeadersTds) as wow:
			DataTds =  wow.json()['data']
			Id = DataTds['id']
			Msg = DataTds['msg']
			if DataTds:
				return [Id, Msg]
			else:return False 
	except BaseException as err:
		return str(err)


def LayNhiemVu(Token, Type):
	Url = "https://traodoisub.com/api/?fields=%s&access_token=%s" % (Type, Token)
	try:
		wow = requests.get(Url, headers=HeadersTds)
		return wow #
	except BaseException as err:
		return str(err)
################################
def _Like(cookie, id, type, fb1, idfb):
	try:
		Reac = {"LIKE": "1635855486666999","LOVE": "1678524932434102","CARE": "613557422527858","HAHA": "115940658764963","WOW": "478547315650144","SAD": "908563459236466","ANGRY": "444813342392137"};Id_Reac = Reac.get(type);_data={'av': idfb,'__usid': r'6-Tsfgotwhb2nus:Psfgosvgerpwk:0-Asfgotw11gc1if-RV=6:F=','__aaid': '0','__user': idfb,'__a': '1','__req': '2c','__hs': '19896.HYP:comet_pkg.2.1..2.1','dpr': '1','__ccg': 'EXCELLENT','__rev': '1014402108','__s': '5vdtpn:wbz2hc:8r67q5','__hsi': '7383159623287270781','__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17xt3odE98K361twYwJyE24wJwpUe8hwaG1sw9u0LVEtwMw65xO2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwKxm5oe8464-5pUfEdK261eBx_wHwdG7FoarCwLyES0Io88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fy8bUaU','__csr': 'gug_2A4A8gkqTf2Ih6RFnbk9mBqaBaTs8_tntineDdSyWqiGRYCiPi_SJuLCGcHBaiQXtLpXsyjIymm8oFJswG8CSGGLzAq8AiWZ6VGDgyQiiTBKU-8GczE9USmi4A9DBABHgWEK3K9y9prxaEa9KqQV8qUlxW22u4EnznDxSewLxq3W2K16BxiE5VqwbW1dz8qwCwjoeEvwaKVU6q0yo5a2i58aE7W0CE5O0fdw1jim0dNw7ewPBG0688025ew0bki0cow3c8C05Vo0aNF40BU0rmU3LDwaO06hU06RG6U1g82Bw0Gxw6Gw','__comet_req': '15','fb_dtsg': fb1,'jazoest': '25509','lsd': '2JgeTE-rDuLtIVUViHpGjH','__spin_r': '1014402108','__spin_b': 'trunk','__spin_t': '1719025807','fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation','variables': fr'{{"input":{{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1719027162723,322693,4748854339,,","feedback_id":"{_encode_to_base64("feedback:"+str(id))}","feedback_reaction_id":"{Id_Reac}","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":["AZWUDdylhKB7Q-Esd2HQq9i7j4CmKRfjJP03XBxVNfpztKO0WSnXmh5gtIcplhFxZdk33kQBTHSXLNH-zJaEXFlMxQOu_JG98LVXCvCqk1XLyQqGKuL_dCYK7qSwJmt89TDw1KPpL-BPxB9qLIil1D_4Thuoa4XMgovMVLAXncnXCsoQvAnchMg6ksQOIEX3CqRCqIIKd47O7F7PYR1TkMNbeeSccW83SEUmtuyO5Jc_wiY0ZrrPejfiJeLgtk3snxyTd-JXW1nvjBRjfbLySxmh69u-N_cuDwvqp7A1QwK5pgV49vJlHP63g4do1q6D6kQmTWtBY7iA-beU44knFS7aCLNiq1aGN9Hhg0QTIYJ9rXXEeHbUuAPSK419ieoaj4rb_4lA-Wdaz3oWiWwH0EIzGs0Zj3srHRqfR94oe4PbJ6gz5f64k0kQ2QRWReCO5kpQeiAd1f25oP9yiH_MbpTcfxMr-z83luvUWMF6K0-A-NXEuF5AiCLkWDapNyRwpuGMs8FIdUJmPXF9TGe3wslF5sZRVTKAWRdFMVAsUn-lFT8tVAZVvd4UtScTnmxc1YOArpHD-_Lzt7NDdbuPQWQohqkGVlQVLMoJNZnF_oRLL8je6-ra17lJ8inQPICnw7GP-ne_3A03eT4zA6YsxCC3eIhQK-xyodjfm1j0cMvydXhB89fjTcuz0Uoy0oPyfstl7Sm-AUoGugNch3Mz2jQAXo0E_FX4mbkMYX2WUBW2XSNxssYZYaRXC4FUIrQoVhAJbxU6lomRQIPY8aCS0Ge9iUk8nHq4YZzJgmB7VnFRUd8Oe1sSSiIUWpMNVBONuCIT9Wjipt1lxWEs4KjlHk-SRaEZc_eX4mLwS0RcycI8eXg6kzw2WOlPvGDWalTaMryy6QdJLjoqwidHO21JSbAWPqrBzQAEcoSau_UHC6soSO9UgcBQqdAKBfJbdMhBkmxSwVoxJR_puqsTfuCT6Aa_gFixolGrbgxx5h2-XAARx4SbGplK5kWMw27FpMvgpctU248HpEQ7zGJRTJylE84EWcVHMlVm0pGZb8tlrZSQQme6zxPWbzoQv3xY8CsH4UDu1gBhmWe_wL6KwZJxj3wRrlle54cqhzStoGL5JQwMGaxdwITRusdKgmwwEQJxxH63GvPwqL9oRMvIaHyGfKegOVyG2HMyxmiQmtb5EtaFd6n3JjMCBF74Kcn33TJhQ1yjHoltdO_tKqnj0nPVgRGfN-kdJA7G6HZFvz6j82WfKmzi1lgpUcoZ5T8Fwpx-yyBHV0J4sGF0qR4uBYNcTGkFtbD0tZnUxfy_POfmf8E3phVJrS__XIvnlB5c6yvyGGdYvafQkszlRrTAzDu9pH6TZo1K3Jc1a-wfPWZJ3uBJ_cku-YeTj8piEmR-cMeyWTJR7InVB2IFZx2AoyElAFbMuPVZVp64RgC3ugiyC1nY7HycH2T3POGARB6wP4RFXybScGN4OGwM8e3W2p-Za1BTR09lHRlzeukops0DSBUkhr9GrgMZaw7eAsztGlIXZ_4"],"session_id":"{uuid.uuid4()}","actor_id":"{idfb}","client_mutation_id":"3"}},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}}','server_timestamps': 'true','doc_id': '7047198228715224',}
		with requests.post("https://www.facebook.com/api/graphql/", headers=headers_fb, cookies={"cookie": cookie}, params=_data) as rss:
			if '{"data":{"feedback_react":{"feedback":{"id":' in rss.text:
				return True
			else:return False
	except BaseException as err:
		return str(err)


try:
	_xxx_ = DangNhapTds(InputToken)
	print(f"Tên Tài Khoản: {_xxx_[0]}\nXu Hiện Tại: {_xxx_[1]}\nXu Bị Trừ: {_xxx_[2]}")
except:
	Text = "Access_token không hợp lệ! xin hãy thử lại!";print(Text.upper());exit()
print("-"*50)

# check cookie
_cc_ = GetThongTin(ck)
if _cc_ == False:print("Cookie Die!");exit()
elif len(_cc_) == 3:pass
else:print(_cc_);exit()

# import id vào tds 
_ch_ = CauHinhFB(InputToken, _cc_[1])
if _ch_ == False:
	print("Cấu Hình Thất Bại! (%s)" % (_cc_[1]));exit()
elif len(_ch_) == 2:
	print("-"*50);print("Đang Cấu Hình ID: %s | Tên Fb: %s " % (_ch_[0], _cc_[2]));print("-"*50)
else:print(_ch_);exit()

# gét gô!
ListNV = ["like", "likevip", "likesieure", "reaction"] # input Nhiệm Vụ cần làm 
dem=0
while True:
	for NhiemVu in ListNV:
		LayNV = LayNhiemVu(InputToken, NhiemVu)
		if 'error' in LayNV.json():
			_nv_ = LayNV.json();count = _nv_['countdown'];_c = 'countdown'
			print(f"Đang Lấy Nhiệm Vụ {NhiemVu.upper()}, {_c.upper()} {count}     ", end="\r");time.sleep(2)
			countdown1(15) #delay get job
		elif len(LayNV.json()) == 0:print(f"Hết Nhiệm Vụ {NhiemVu.upper()}                     ",end="\r");time.sleep(2)
		elif len(LayNV.json()) > 0:
			_nv = LayNV.json()
			for x in _nv: 
				
				if NhiemVu == "like" or NhiemVu == "likevip" or NhiemVu == "likesieure":
					uid = get_substring_after_underscore(x['id'])
					id = x['id']
					_type_ = NhiemVu.upper()
					_style_ = "LIKE"
					_like = _Like(ck, uid, _style_, _cc_[0], _cc_[1])
					if _like == False:
						STATUS = False
						print(f"FAIL LIKE : {uid}                            ",end="\r");time.sleep(3)
						_bypass = _Bypass(ck, _cc_[0])
						if _bypass == True:pass
						elif _bypass == False:print("Cookie Die!");exit()
						else:pass
					elif _like == True:STATUS =True
					else:print(_like);STATUS= False
				elif NhiemVu == "reaction":
					uid = get_substring_after_underscore(x['id'])
					id = x['id']
					_type_ = x['type']
					_reac = _Like(ck, uid, _type_, _cc_[0], _cc_[1])
					if _reac == False:
						STATUS = False
						print(f"FAIL LIKE : {uid}                            ",end="\r");time.sleep(3)
						_bypass = _Bypass(ck, _cc_[0])
						if _bypass == True:pass
						elif _bypass == False:print("Cookie Die!");exit()
						else:pass
					elif _reac == True:STATUS =True
					else:print(_like);STATUS= False
				if STATUS == True: # nhận xu
					try:
						Url = f"https://traodoisub.com/api/coin/?type={_type_}&id={id}&access_token={InputToken}"
						coin =  requests.get(Url, headers=HeadersTds)
						if 'error' not in coin.json():
							_data = coin.json()['data']
							_xu = _data['xu']
							_msg = _data['msg']
							dem+=1
							_now = datetime.now()
							print(f'[{dem}] {_now.strftime("%H:%M:%S")} {_type_} {uid} {_msg} {_xu}  ')
							countdown(30)
							if dem == 300:
								print("Đã Đạt Giới Hạn Nhiệm Vụ");exit()
							else:pass
						else:print(f"FAIL COIN : {uid}                            ", end="\r");time.sleep(4)
					except BaseException as err:
						print(str(err))
							
				
				
				else:pass
						
						
						
					
		
		
		
		else:print(LayNV.json()) # chờ if giới hạn nhiemvu thì print nó ra or exit + thêm các điều kiện khác vào...
			
	
	
	
	
	
