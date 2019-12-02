# author: riccardo.ciprini
#
# email: riccardo.ciprini@artgroup-spa.com

import random
import string


char_ita = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
char_ita_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
char_japan = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "が", "ぎ", "ぐ", "げ", "ご", "さ", "し", "す", "せ", "そ", "ざ", "じ", "ず", "ぜ", "ぞ", "た", "ち", "つ", "て", "と", "だ", "ぢ", "づ", "で", "ど", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "わ", "ゐ", "ゑ", "を"]
char_china = ["阿", "贝", "色", "德", "饿", "艾", "弗", "日", "阿", "什", "伊", "鸡", "卡", "艾", "勒", "艾", "马", "艾", "娜", "哦", "佩", "苦", "艾", "和", "丝", "特", "玉", "维", "独", "布", "勒", "维", "伊", "克", "斯", "格", "黑", "克", "贼", "德"]
char_korea = ["하", "악", "안", "알", "암", "압", "앙", "앞", "애", "액", "앵", "야", "얀", "약", "양", "얘", "어", "억", "언", "얼", "엄", "업", "엉", "에", "여", "역", "연","열", "염", "엽", "영", "예", "오", "옥", "온", "올", "옴", "옹", "와", "완", "왈", "왕", "왜", "외", "왼", "욕", "요", "용", "우", "욱", "운", "울", "움", "웅", "워", "원", "월", "유", "육", "윤", "율", "융", "윷", "으", "은", "을", "음", "읍", "응", "의", "이", "익", "인", "일", "임", "입", "잉","잎"]
achar = ["á", "à", "â", "ã", "ä", "å", "æ", "ā", "ă", "ą"]
cchar = ["ç", "ć", "č"]
dchar = ["ď", "đ"]
echar = ["é", "è", "ê", "ë", "ē", "ė", "ę", "ě", "ĕ", "ǝ"]
gchar = ["ģ", "ǧ"]
ochar = ["œ"]
ichar = ["í", "ì", "î", "ï", "ĩ", "į", "ı"]



def contatti_ita_lower():
	f = open("contatti_ita_lower.vcf", "w+")
	n1 = random.choice(char_ita)
	n2 = random.choice(char_ita)
	n3 = random.choice(char_ita)
	n4 = random.choice(char_ita)
	n5 = random.choice(char_ita)
	n6 = random.choice(char_ita)
	n7 = random.choice(char_ita)
	n8 = random.choice(char_ita)
	name = n1+n2+n3+n4+n5+n6+n7+n8
	c1 = random.choice(char_ita)
	c2 = random.choice(char_ita)
	c3 = random.choice(char_ita)
	c4 = random.choice(char_ita)
	c5 = random.choice(char_ita)
	c6 = random.choice(char_ita)
	c7 = random.choice(char_ita)
	surname = c1+c2+c3+c4+c5+c6+c7
	f.write("BEGIN:VCARD\r\n")
	f.write("VERSION:3.0\r\n")
	f.write("PRODID:-//Apple Inc.//iOS 12.4//EN\r\n")
	string = i+i+i+i+i+i
	string2 = j+j+j+j+j+j
	tel = str(generate_number())
	f.write("N:"+name+";"+surname+";;;\r\n")
	f.write("FN:"+name+" "+surname+"\r\n")
	f.write("EMAIL;type=INTERNET;type=HOME;type=pref:"+name+"@"+surname+".it\r\n")
	tel2 = str(generate_number())
	via = generate_street(1)[0]
	via2 = generate_street(1)[1]
	via3 = generate_street(1)[2]
	city = generate_street(1)[3]
	city2 = generate_street(1)[4]
	cap = str(generate_street(1)[5])
	naz = generate_street(1)[6]
	web = randomString(10)
	f.write("TEL;type=WORK;type=VOICE:"+tel2[:3]+" "+tel2[-7:]+"\r\n")
	f.write("item1.ADR;type=HOME;type=pref:;;"+via+" "+via2+";"+city+";"+city2+";"+cap+";"+city2+"\r\n")
	f.write("item1.X-ABADR:it\r\n")
	f.write("item2.ADR;type=WORK:;;"+via+" "+via2+";"+city+";"+city2+";"+cap+";"+city2+"\r\n")
	f.write("item3.URL;type=pref:http://www."+web+".it\r\n")
	f.write("item3.X-ABLabel:_$!<HomePage>!$_\r\n")
	f.write("REV:2019-07-03T09:25:15Z\r\n")
	f.write("END:VCARD\r\n")
	f.close()
	print("\nContatti ITA con lettere minuscole creati.\n")


def contatti_ita_upper():
	print("\nCreo i contatti upper ita.")

def contatti_ita_mixed():
	print("\nCreo contatti ita mixed.")

def contatti_china():
	print("\nCreo contatti china.")

def contatti_japan():
	print("\nCreo contatti japan.")

def contatti_korea():
	print("\nCreo contatti korea.")

def contatti_special():
	print("\nCreo contatti special.")

def contatti_special_mixed():
	print("\nCreo contatti special mixed.")


def menu():
	while(1):
		print("Programma che crea file con contatti VCF.")
		a = input("1 - Ita lower char\n2 - Ita upper char\n3 - Ita mixed\n4 - China\n5- Japan\n6 - Korea\n7- Special Char\n8 - Special Char Mixed\nb - Exit\n")
		if a == "1":
			contatti_ita_lower()
		elif a == "2":
			contatti_ita_upper()
		elif a == "3":
			contatti_ita_mixed()
		elif a == "4":
			contatti_china()
		elif a == "5":
			contatti_japan()
		elif a == "6":
			contatti_korea()
		elif a == "7":
			contatti_special()
		elif a == "8":
			contatti_special_mixed()
		else:
			print("Esco dal programma.")
			exit()


if __name__ == '__main__':
	try:
		menu()
	except KeyboardInterrupt:
		print("Esco dal programma.")
		exit()