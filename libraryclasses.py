class BookNotFoundError(Exception):
	pass

#———————————————————————————————————————————————————————————————————————————

class Book:
	
	def __init__(self, title, author, publish_date, rating, price):
		if not Book.is_valid_publish_date(publish_date):
			raise ValueError(f"Invalid publish date: {publish_date}. Use MM.YYYY")
				
		self.title = title
		self.author = author
		self.publish_date = publish_date
		self.rating = rating
		self.price = price
		self.is_borrowed = False

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, value):
		if not (1 <= value <= 5):
			raise ValueError(f"Rating is {value}, it should be: 1 <= rating <= 5")
		self._rating = value

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, value):
		if value < 0:
			raise ValueError(f"Price is {value}, it should be: 0 <= Price")
		self._price = value

	@staticmethod
	def is_valid_publish_date(publish_date):
		try:
			datetime.strptime(publish_date, "%m.%Y")
			return True
		except ValueError:
			return False

	def __str__(self):
		status = "Borrowed" if self.is_borrowed else "Available"   
		return (f"{self.title} - {self.author} ({self.publish_date}) | Rating: {self.rating}/5 | Price: {self.price:.2f} | {status}")
#———————————————————————————————————————————————————————————————————————————

class Library:
	
	def __init__(self):
		self.books = []

	def add_book(self, book):
		for b in self.books:
			if b.title == book.title and b.author == book.author:
				raise ValueError(f"'{book.title}' is already in library")
		self.books.append(book)

	def find_book(self, title):
		for b in self.books:
			if b.title == title:
				return b
		raise BookNotFoundError(f"'{title}' is not in library")

	def borrow_book(self, title):
		book = self.find_book(title)

		if book.is_borrowed:
			raise ValueError(f"'{title}' is already borrowed")
		else :
			book.is_borrowed = True

	def __len__(self):
		return len(self.books)

	def __str__(self):
		if len(self.books) == 0:
			return "There are not books in library yet"

		result = "The Books are in Library : \n"
		for book in self.books:
			result += f"{book}\n"
		return result

