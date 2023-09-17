# import required libraries
from bs4 import BeautifulSoup
import requests as req
from tkinter import messagebox


# create class for web scraper
class Scraper:
	def __init__(self):
		# constructor

		# page content code 
		self.content = None
		
		# page parser flag
		self.parser_flag = 'lxml'
		
		# dictionary
		self.dictionary = {}
		
	# request the page and return the content of web page
	def requester(self, page_number=1):
		
		web_page = page_number
		web_url = f'https://mir.az/tr/kitap/page/{web_page}/'
		
		# request
		r = req.get(web_url)
		
		# if status code is 200
		if r.status_code == 200:
			messagebox.showinfo('Bilgi', 'Bağlantı Başarılı')
			
			# get content of page
			self.content = r.content

		else:
			messagebox.showerror('HATA', 'Bağlantı Başarısız, İnternet Bağlantısını Kontrol Ediniz')
		
	# parser function
	def parser(self):
			
			self.dictionary.clear()
			
			# content and flag will be used in the func
			parsed_web_page = BeautifulSoup(self.content, self.parser_flag)
			
			# find the divs and names
			all_books_names = parsed_web_page.find_all('a', attrs={'class': 'item-link'})
			
			all_books_names = [i.get('title') for i in all_books_names]
			
			# indexes 
			indexes = range(1, len(all_books_names)+1)
			
			# create dictionary
			for key, value in zip(indexes, all_books_names):
				
				# dictionary creation
				self.dictionary[key] = value
			
			return self.dictionary
				
# buton fonksiyonu ile sayfa değiştirip ona göre alacağız
"""deneme = Scraper()
deneme.requester()
deneme.parser()"""

			
			
			
			
			


