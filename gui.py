from tkinter import *
from freepdfbooks import Scraper

# create scraper object
scraper = Scraper()


# class for gui
class Gui(Tk):
	def __init__(self):
		super().__init__()
		
		# cost 
		self.title('Free Books Pdf')
		self.geometry('1500x1000+100+10')
		
		# main label
		self.main_label = Label(master=self, text='Free Books Pdf', font=('Times New Roman', 20))
		self.main_label.pack(padx=10, pady=10)
		
		# page number artırma azaltma yapılacak
		self.page_number = 1
		
		self.variable_labels = {}
		
		# page number label and buttons
		self.page_number_label = Label(master=self, text=str(self.page_number), font=("Times New Roman", 14))
		self.page_number_increase_button = Button(master=self, text=">", command=self.increase)
		self.page_number_decrease_button = Button(master=self, text="<", command=self.decrease)
		
		# button packs
		
		self.page_number_increase_button.pack(padx=10, pady=10, side=RIGHT)
		self.page_number_label.pack(padx=10, pady=10, side=RIGHT)
		self.page_number_decrease_button.pack(padx=10, pady=10, side=RIGHT)
		
		
		# bind the button
		self.run_program()
		
	def run_program(self, page_num=1):
		
		# get page content with scraper
		scraper.requester(page_number=page_num)
		
		#
		for i in self.variable_labels.values():
			i.pack_forget()
		
		# label variables section 
		self.variable_labels = {}

		response_dictionary = scraper.parser()
	
		# with for loop create labels
		for i in response_dictionary.keys():
			self.variable_labels[f"book_name_{i}"] = Label(master=self, text=response_dictionary[i])
		for k in self.variable_labels.keys():
			self.variable_labels[k].pack(padx=5, pady=5, anchor="nw")
		
		
	# increase button function
	def increase(self):
		
		# get label number
		number = int(self.page_number_label.cget("text"))
		new_number = number+1
		
		# upgrade label
		self.page_number_label.configure(text=str(new_number))
		
		# upgrade books names
		self.run_program(page_num=new_number)
	
	# decrease button
	def decrease(self):
		# get label number
		number = int(self.page_number_label.cget("text"))
		new_number = number-1
		
		if new_number  <= 0:
			pass
		else:
			# upgrade label
			self.page_number_label.configure(text=str(new_number))
		
			# upgrade books names
			self.run_program(page_num=new_number)
		
	
		

app = Gui()
app.mainloop()