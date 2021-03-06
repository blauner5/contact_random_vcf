# author: riccardo.ciprini
#
# email: riccardo.ciprini@artgroup-spa.com

import random
import string

nomi_italiani = []
char_ita = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
char_ita_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
char_japan = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "が", "ぎ", "ぐ", "げ", "ご", "さ", "し", "す", "せ", "そ", "ざ", "じ", "ず", "ぜ", "ぞ", "た", "ち", "つ", "て", "と", "だ", "ぢ", "づ", "で", "ど", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "わ", "ゐ", "ゑ", "を"]
char_china = ["阿", "贝", "色", "德", "饿", "艾", "弗", "日", "阿", "什", "伊", "鸡", "卡", "艾", "勒", "艾", "马", "艾", "娜", "哦", "佩", "苦", "艾", "和", "丝", "特", "玉", "维", "独", "布", "勒", "维", "伊", "克", "斯", "格", "黑", "克", "贼", "德"]
char_korea = ["하", "악", "안", "알", "암", "압", "앙", "앞", "애", "액", "앵", "야", "얀", "약", "양", "얘", "어", "억", "언", "얼", "엄", "업", "엉", "에", "여", "역", "연","열", "염", "엽", "영", "예", "오", "옥", "온", "올", "옴", "옹", "와", "완", "왈", "왕", "왜", "외", "왼", "욕", "요", "용", "우", "욱", "운", "울", "움", "웅", "워", "원", "월", "유", "육", "윤", "율", "융", "윷", "으", "은", "을", "음", "읍", "응", "의", "이", "익", "인", "일", "임", "입", "잉","잎"]
mappa_caratteri = ["ẚ","Á","á","À","à","Ă","ă","Ắ","ắ","Ằ","ằ",
"Ẵ","ẵ","Ẳ","ẳ","Â","â","Ấ","ấ","Ầ","ầ","Ẫ",
"ẫ","Ẩ","ẩ","Ǎ","ǎ","Å","å","Ǻ","ǻ","Ä","ä",
"Ǟ","ǟ","Ã","ã","Ȧ","ȧ","Ǡ","ǡ","Ą","ą","Ā",
"ā","Ả","ả","Ȁ","ȁ","Ȃ","ȃ","Ạ","ạ","Ặ","ặ",
"Ậ","ậ","Ḁ","ḁ","Ⱥ","ⱥ","Æ","æ","Ǽ","ǽ","Ǣ",
"ǣ","Ḃ","ḃ","Ḅ","ḅ","Ḇ","ḇ","Ƀ","ƀ","ᵬ","Ɓ",
"ɓ","Ƃ","ƃ","Ъ","ь","ъ","ь","Ć","ć","Ĉ","ĉ","Č","č",
"Ċ","ċ","Ç","ç","Ḉ","ḉ","Ȼ","ȼ","Ƈ","ƈ","ɕ",
"Ď","ď","Ḋ","ḋ","Ḑ","ḑ","Ḍ","ḍ","Ḓ","ḓ","Ḏ",
"ḏ","Đ","đ","ᵭ","Ɖ","ɖ","Ɗ","ɗ","Ƌ","ƌ","ȡ",
"ð","É","Ə","Ǝ","ǝ","Ə","ə","é","È","è","Ĕ",
"ĕ","Ê","ê","Ế","ế","Ề","ề","Ễ","ễ","Ể","ể",
"Ě","ě","Ë","ë","Ё","е","ё","е","Ẽ","ẽ","Ė","ė","Ȩ",
"ȩ","Ḝ",
"ḝ","Ę","ę","Ē","ē","Ḗ","ḗ","Ḕ","ḕ","Ẻ","ẻ",
"Ȅ","ȅ","Ȇ","ȇ","Ẹ","ẹ","Ệ","ệ","Ḙ","ḙ","Ḛ",
"ḛ","Ɇ","ɇ","ɚ","ɝ","Ḟ","ḟ","ᵮ","Ƒ","ƒ","Ǵ",
"ǵ","Ğ","ğ","Ĝ","ĝ","Ǧ","ǧ","Ġ","ġ","Ģ","ģ",
"Ḡ","ḡ","Ǥ","ǥ","Ɠ","ɠ","Ĥ","ĥ","Ȟ","ȟ","Ḧ",
"ḧ","Ḣ","ḣ","Ḩ","ḩ","Ḥ","ḥ","Ḫ","ḫ",
"ẖ","Ħ","ħ","Ⱨ","ⱨ","Í","í","Ì","ì","Ĭ","ĭ",
"Î","î","Ǐ","ǐ","Ï","ï","Ḯ","ḯ","Ĩ","ĩ","İ",
"Į","į","Ī","ī","Ỉ","ỉ","Ȉ","ȉ","Ȋ","ȋ",
"Ị","ị","Ḭ","ḭ","ı","Ɨ","ɨ","Ĵ","ĵ","ǰ",
"ȷ","Ɉ","ɉ","ʝ","ɟ","ʄ","Ḱ","ḱ","Ǩ",
"ǩ","Ķ","ķ","Ḳ","ḳ","Ḵ","ḵ","Ƙ","ƙ","Ⱪ","ⱪ",
"Ĺ","ĺ","Ľ","ľ","Ļ","ļ","Ḷ","ḷ","Ḹ","ḹ","Ḽ",
"ḽ","Ḻ","ḻ","Ł","ł","Ł","̣","ł","Ŀ","ŀ",
"Ƚ","ƚ","Ⱡ","ⱡ","Ɫ","ɫ","ɬ","ɭ","ȴ","Ḿ","ḿ",
"Ṁ","ṁ","Ṃ","ṃ","ɱ","Ń","ń","Ǹ","ǹ","Ň","ň",
"Ñ","ñ","Ṅ","ṅ","Ņ","ņ","Ṇ","ṇ","Ṋ","ṋ","Ṉ",
"ṉ","Ɲ","ɲ","Ƞ","ƞ","ɳ","ȵ",
"Ó","ó","Ò","ò","Ŏ","ŏ","Ô","ô","Ố","ố","Ồ",
"ồ","Ỗ","ỗ","Ổ","ổ","Ǒ","ǒ","Ö","ö","Ȫ","ȫ",
"Ő","ő","Õ","õ","Ṍ","ṍ","Ṏ","ṏ","Ȭ","ȭ","Ȯ",
"ȯ","Ȱ","ȱ","Ø","ø","Ǿ","ǿ","Ǫ","ǫ","Ǭ","ǭ",
"Ō","ō","Ṓ","ṓ","Ṑ","ṑ","Ỏ","ỏ","Ȍ","ȍ","Ȏ",
"ȏ","Ơ","ơ","Ớ","ớ","Ờ","ờ","Ỡ","ỡ","Ở","ở",
"Ợ","ợ","Ọ","ọ","Ộ","ộ","Ɵ","ɵ","Œ","œ","Ṕ",
"ṕ","Ṗ","ṗ","Ᵽ","Ƥ","ƥ","ʠ",
"Ɋ","ɋ","Ŕ","ŕ","Ř","ř","Ṙ","ṙ","Ŗ","ŗ","Ȑ",
"ȑ","Ȓ","ȓ","Ṛ","ṛ","Ṝ","ṝ","Ṟ","ṟ","Ɍ","ɍ",
"ᵲ","ɼ","Ɽ","ɽ","ɾ","ᵳ","ß","Ś","ś","Ṥ","ṥ",
"Ŝ","ŝ","Š","š","Ṧ","ṧ","Ṡ","ṡ","ẛ","Ş","ş",
"Ṣ","ṣ","Ṩ","ṩ","Ș","ș","ʂ",
"§","Þ","þ","Ť","ť","̈","ẗ","Ṫ","ṫ","Ţ",
"ţ","Ṭ","ṭ","Ț","ț","Ṱ","ṱ","Ṯ","ṯ","Ŧ","ŧ",
"Ⱦ","ⱦ","ᵵ","ƫ","Ƭ","ƭ","Ʈ","ʈ","ȶ","Ú","ú",
"Ù","ù","Ŭ","ŭ","Û","û","Ǔ","ǔ","Ů","ů","Ü",
"ü","Ǘ","ǘ","Ǜ","ǜ","Ǚ","ǚ","Ǖ","ǖ","Ű","ű",
"Ũ","ũ","Ṹ","ṹ","Ų","ų","Ū","ū","Ṻ","ṻ","Ủ",
"ủ","Ȕ","ȕ","Ȗ","ȗ","Ư","ư","Ứ","ứ","Ừ","ừ",
"Ữ","ữ","Ử","ử","Ự","ự","Ụ","ụ","Ṳ","ṳ","Ṷ",
"ṷ","Ṵ","ṵ","Ʉ","ʉ","Ṽ","ṽ","Ṿ","ṿ","Ʋ","ʋ",
"Ẃ","ẃ","Ẁ","ẁ","Ŵ","ŵ","̊","ẘ","Ẅ","ẅ",
"Ẇ","ẇ","Ẉ","ẉ","Ẍ","ẍ","Ẋ","ẋ","Ý","ý","Ỳ",
"ỳ","Ŷ","ŷ","̊","ẙ","Ÿ","ÿ","Ỹ","ỹ","Ẏ",
"ẏ","Ȳ","ȳ","Ỷ","ỷ","Ỵ","ỵ","ʏ","Ɏ","ɏ","Ƴ",
"ƴ","Ź","ź","Ẑ","ẑ","Ž","ž","Ż","ż","Ẓ","ẓ",
"Ẕ","ẕ","Ƶ","ƶ","Ȥ","ȥ","ʐ","ʑ","Ⱬ","ⱬ","Ǯ",
"ǯ","ƺ"]

def generate_number():
	a = random.randint(0000000000,9999999999)
	return a

def randomString(stringLength=10):
	letters = string.ascii_lowercase
	return "".join(random.choice(letters) for i in range(stringLength))

def generate_street(tipo):
	if tipo == 3:
		i = random.choice(char_korea)
		j = random.choice(char_korea)
		z = random.choice(char_korea)
		via = i+j+z
		via2 = j+i+z
		via3 = j+i+z+z+z+i+i
		city = i+j+i+z+i+j+z+j+z+j+z
		city2 = i+i+z+i+z+i+j+i+i+z
		cap = random.randint(00000, 99999)
		naz = z+i+i+j+z+j+j+z
	elif tipo == 1:
		i = random.choice(char_ita)
		j = random.choice(char_ita)
		z = random.choice(char_ita)
		via = i+j+z
		via2 = j+i+z
		via3 = j+i+z+z+z+i+i
		city = i+j+i+z+i+j+z+j+z+j+z
		city2 = i+i+z+i+z+i+j+i+i+z
		cap = random.randint(00000, 99999)
		naz = z+i+i+j+z+j+j+z
	elif tipo == 2:
		i = random.choice(char_ita_upper)
		j = random.choice(char_ita_upper)
		z = random.choice(char_ita_upper)
		via = i+j+z
		via2 = j+i+z
		via3 = j+i+z+z+z+i+i
		city = i+j+i+z+i+j+z+j+z+j+z
		city2 = i+i+z+i+z+i+j+i+i+z
		cap = random.randint(00000, 99999)
		naz = z+i+i+j+z+j+j+z
	elif tipo == 4:
		i = random.choice(char_japan)
		j = random.choice(char_japan)
		z = random.choice(char_japan)
		via = i+j+z
		via2 = j+i+z
		via3 = j+i+z+z+z+i+i
		city = i+j+i+z+i+j+z+j+z+j+z
		city2 = i+i+z+i+z+i+j+i+i+z
		cap = random.randint(00000, 99999)
		naz = z+i+i+j+z+j+j+z
	else:
		i = random.choice(char_china)
		j = random.choice(char_china)
		z = random.choice(char_china)
		via = i+j+z
		via2 = j+i+z
		via3 = j+i+z+z+z+i+i
		city = i+j+i+z+i+j+z+j+z+j+z
		city2 = i+i+z+i+z+i+j+i+i+z
		cap = random.randint(00000, 99999)
		naz = z+i+i+j+z+j+j+z

	return via, via2, via3, city, city2, cap, naz


def contatti_reali():
	f = open("nomi_italiani.txt", "r")
	for line in f:
		a = line.replace("\n", "")
		nomi_italiani.append(a)
	f = open("contatti_ita_real.vcf", "w+")
	num_contact = int(input("Quanti contatti vuoi creare: "))
	for i in range(1, num_contact+1):
		name = random.choice(nomi_italiani)
		surname = random.choice(nomi_italiani)
		name = name.capitalize()
		surname = surname.capitalize()
		f.write("BEGIN:VCARD\r\n")
		f.write("VERSION:3.0\r\n")
		tel = str(generate_number())
		f.write("N:"+name+";"+surname+";;;\r\n")
		f.write("FN:"+name+" "+surname+"\r\n")
		f.write("TEL;type=CELL;type=VOICE;type=pref:"+tel[:3]+" "+tel[-7:]+"\r\n")
		#f.write("EMAIL;type=INTERNET;type=HOME;type=pref:"+name+"@"+surname+".it\r\n")
		#tel2 = str(generate_number())
		#via = generate_street(1)[0]
		#via2 = generate_street(1)[1]
		#via3 = generate_street(1)[2]
		#city = generate_street(1)[3]
		#city2 = generate_street(1)[4]
		#cap = str(generate_street(1)[5])
		#naz = generate_street(1)[6]
		#web = randomString(10)
		#f.write("TEL;type=WORK;type=VOICE:"+tel2[:3]+" "+tel2[-7:]+"\r\n")
		#f.write("item1.ADR;type=HOME;type=pref:;;"+via+" "+via2+";"+city+";"+city2+";"+cap+";"+city2+"\r\n")
		#f.write("item1.X-ABADR:it\r\n")
		#f.write("item2.ADR;type=WORK:;;"+via+" "+via2+";"+city+";"+city2+";"+cap+";"+city2+"\r\n")
		#f.write("item3.URL;type=pref:http://www."+web+".it\r\n")
		#f.write("item3.X-ABLabel:_$!<HomePage>!$_\r\n")
		f.write("REV:2019-07-03T09:25:15Z\r\n")
		f.write("END:VCARD\r\n")
	f.close()
	print("Creo i contatti reali.")


def contatti_ita_lower():
	f = open("contatti_ita_lower.vcf", "w+")
	num_contact = int(input("Quanti contatti vuoi creare: "))
	for i in range(1,num_contact+1):
		n1 = random.choice(char_ita)
		n2 = random.choice(char_ita)
		n3 = random.choice(char_ita)
		n4 = random.choice(char_ita)
		n5 = random.choice(char_ita)
		n6 = random.choice(char_ita)
		n7 = random.choice(char_ita)
		n8 = random.choice(char_ita)
		name = n1+n2+n3+n4+n5+n6+n7+n8 #si può fare anche n1*8
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
		tel = str(generate_number())
		f.write("N:"+name+";"+surname+";;;\r\n")
		f.write("FN:"+name+" "+surname+"\r\n")
		f.write("TEL;type=CELL;type=VOICE;type=pref:"+tel[:3]+" "+tel[-7:]+"\r\n")
		#f.write("EMAIL;type=INTERNET;type=HOME;type=pref:"+name+"@"+surname+".it\r\n")
		#tel2 = str(generate_number())
		#via = generate_street(1)[0]
		#via2 = generate_street(1)[1]
		#via3 = generate_street(1)[2]
		#city = generate_street(1)[3]
		#city2 = generate_street(1)[4]
		#cap = str(generate_street(1)[5])
		#naz = generate_street(1)[6]
		#web = randomString(10)
		#f.write("TEL;type=WORK;type=VOICE:"+tel2[:3]+" "+tel2[-7:]+"\r\n")
		#f.write("item1.ADR;type=HOME;type=pref:;;"+via+" "+via2+";"+city+";"+city2+";"+cap+";"+city2+"\r\n")
		#f.write("item1.X-ABADR:it\r\n")
		#f.write("item2.ADR;type=WORK:;;"+via+" "+via2+";"+city+";"+city2+";"+cap+";"+city2+"\r\n")
		#f.write("item3.URL;type=pref:http://www."+web+".it\r\n")
		#f.write("item3.X-ABLabel:_$!<HomePage>!$_\r\n")
		f.write("REV:2019-07-03T09:25:15Z\r\n")
		f.write("END:VCARD\r\n")
	f.close()
	print("\nContatti ITA con lettere minuscole creati.\n")


def contatti_ita_upper():
	f = open("contatti_ita_lower.vcf", "w+")
	num_contact = int(input("Quanti contatti vuoi creare: "))
	for i in range(1,num_contact+1):
		n1 = random.choice(char_ita_upper)
		n2 = random.choice(char_ita_upper)
		n3 = random.choice(char_ita_upper)
		n4 = random.choice(char_ita_upper)
		n5 = random.choice(char_ita_upper)
		n6 = random.choice(char_ita_upper)
		n7 = random.choice(char_ita_upper)
		n8 = random.choice(char_ita_upper)
		name = n1+n2+n3+n4+n5+n6+n7+n8
		c1 = random.choice(char_ita_upper)
		c2 = random.choice(char_ita_upper)
		c3 = random.choice(char_ita_upper)
		c4 = random.choice(char_ita_upper)
		c5 = random.choice(char_ita_upper)
		c6 = random.choice(char_ita_upper)
		c7 = random.choice(char_ita_upper)
		surname = c1+c2+c3+c4+c5+c6+c7
		f.write("BEGIN:VCARD\r\n")
		f.write("VERSION:3.0\r\n")
		f.write("PRODID:-//Apple Inc.//iOS 12.4//EN\r\n") #forse non necessario per creare il file vcf
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
	print("\nContatti ITA con lettere maiuscole creati.\n")

def contatti_ita_mixed():
	f = open("contatti_ita_lower.vcf", "w+")
	num_contact = int(input("Quanti contatti vuoi creare: "))
	for i in range(1,num_contact+1):
		n1 = random.choice(char_ita_upper)
		n2 = random.choice(char_ita)
		n3 = random.choice(char_ita)
		n4 = random.choice(char_ita)
		n5 = random.choice(char_ita)
		n6 = random.choice(char_ita)
		n7 = random.choice(char_ita)
		n8 = random.choice(char_ita)
		name = n1+n2+n3+n4+n5+n6+n7+n8
		c1 = random.choice(char_ita_upper)
		c2 = random.choice(char_ita)
		c3 = random.choice(char_ita)
		c4 = random.choice(char_ita)
		c5 = random.choice(char_ita)
		c6 = random.choice(char_ita)
		c7 = random.choice(char_ita)
		surname = c1+c2+c3+c4+c5+c6+c7
		f.write("BEGIN:VCARD\r\n")
		f.write("VERSION:3.0\r\n")
		f.write("PRODID:-//Apple Inc.//iOS 12.4//EN\r\n") #forse non necessario per creare il file vcf
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
	print("\nContatti ITA con lettere mixed creati.\n")

def contatti_china():
	f = open("contatti_ita_lower.vcf", "w+")
	num_contact = int(input("Quanti contatti vuoi creare: "))
	for i in range(1,num_contact+1):
		n1 = random.choice(char_china)
		n2 = random.choice(char_china)
		n3 = random.choice(char_china)
		n4 = random.choice(char_china)
		n5 = random.choice(char_china)
		n6 = random.choice(char_china)
		n7 = random.choice(char_china)
		n8 = random.choice(char_china)
		name = n1+n2+n3+n4+n5+n6+n7+n8
		c1 = random.choice(char_china)
		c2 = random.choice(char_china)
		c3 = random.choice(char_china)
		c4 = random.choice(char_china)
		c5 = random.choice(char_china)
		c6 = random.choice(char_china)
		c7 = random.choice(char_china)
		surname = c1+c2+c3+c4+c5+c6+c7
		f.write("BEGIN:VCARD\r\n")
		f.write("VERSION:3.0\r\n")
		f.write("PRODID:-//Apple Inc.//iOS 12.4//EN\r\n") #forse non necessario per creare il file vcf
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
	print("\nContatti China created.\n")

def contatti_japan():
	f = open("contatti_ita_lower.vcf", "w+")
	num_contact = int(input("Quanti contatti vuoi creare: "))
	for i in range(1,num_contact+1):
		n1 = random.choice(char_japan)
		n2 = random.choice(char_japan)
		n3 = random.choice(char_japan)
		n4 = random.choice(char_japan)
		n5 = random.choice(char_japan)
		n6 = random.choice(char_japan)
		n7 = random.choice(char_japan)
		n8 = random.choice(char_japan)
		name = n1+n2+n3+n4+n5+n6+n7+n8
		c1 = random.choice(char_japan)
		c2 = random.choice(char_japan)
		c3 = random.choice(char_japan)
		c4 = random.choice(char_japan)
		c5 = random.choice(char_japan)
		c6 = random.choice(char_japan)
		c7 = random.choice(char_japan)
		surname = c1+c2+c3+c4+c5+c6+c7
		f.write("BEGIN:VCARD\r\n")
		f.write("VERSION:3.0\r\n")
		f.write("PRODID:-//Apple Inc.//iOS 12.4//EN\r\n") #forse non necessario per creare il file vcf
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
	print("\nContatti Japan created.\n")

def contatti_korea():
	print("\nCreo contatti korea.")

def contatti_special():
	print("\nCreo contatti special.")

def contatti_special_mixed():
	print("\nCreo contatti special mixed.")

def contatti_upper_latin():
	f = open("contatti_upper_latin.vcf", "w+")
	for i in char_ita_upper:
		for j in char_ita_upper:
			name = i
			surname =j
			f.write("BEGIN:VCARD\r\n")
			f.write("VERSION:3.0\r\n")
			f.write("PRODID:-//Apple Inc.//iOS 12.4//EN\r\n") #forse non necessario per creare il file vcf
			tel = str(generate_number())
			f.write("N:"+name+";"+surname+";;;\r\n")
			f.write("FN:"+name+" "+surname+"\r\n")
			f.write("TEL;type=WORK;type=VOICE:"+tel2[:3]+" "+tel2[-7:]+"\r\n")
			f.write("REV:2019-07-03T09:25:15Z\r\n")
			f.write("END:VCARD\r\n")
	f.close()
	print("\nCreo contatti latin upper.")


def menu():
	while(1):
		print("This program create a VCF file for testing.")
		a = input("1 - Ita lower char\n2 - Ita upper char\n3 - Ita mixed\n4 - China\n5- Japan\n6 - Korea\n7- Special Char\n8 - Special Char Mixed\n9 - Upper Latin Char\n10 - Contatti reali\nb - Exit\n")
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
		elif a == "9":
			contatti_upper_latin()
		elif a == "10":
			contatti_reali()
		else:
			print("Esco dal programma.")
			exit()


if __name__ == '__main__':
	try:
		menu()
	except KeyboardInterrupt:
		print("Esco dal programma.")
		exit()