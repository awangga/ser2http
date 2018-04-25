import pyqrcode
import cilok
import config
config.urlpost
config.urlformat

semuaalat = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for alat in semuaalat:
	hasilenc = cilok.urlEncode16(str(config.urlformat+alat))
	hasilnya = config.urlpost+hasilenc
	print hasilnya
	url = pyqrcode.create(hasilnya)
	url.svg(alat+'.svg', scale=8)