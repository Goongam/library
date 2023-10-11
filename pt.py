from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 멤버 및 책 정보를 저장하는 딕셔너리
members = {}
books = {}

# 홈 페이지
@app.route('/')
def home():
    return render_template('index.html', members=members, books=books)

# 멤버 추가
@app.route('/add_member', methods=['POST'])
def add_member():
    member_name = request.form.get('member_name')
    member_phone = request.form.get('member_phone')
    members[member_name] = {'phone': member_phone, 'books': []}
    return redirect(url_for('home'))

# 멤버 삭제
@app.route('/delete_member', methods=['POST'])
def delete_member():
    member_name = request.form.get('member_name')
    if member_name in members:
        del members[member_name]
    return redirect(url_for('home'))

# 책 추가
@app.route('/add_book', methods=['POST'])
def add_book():
    book_title = request.form.get('book_title')
    books[book_title] = 'Available'
    return redirect(url_for('home'))

# 책 삭제
@app.route('/delete_book', methods=['POST'])
def delete_book():
    book_title = request.form.get('book_title')
    if book_title in books:
        del books[book_title]
    return redirect(url_for('home'))

# 책 대출
@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    member_name = request.form.get('member_name')
    book_title = request.form.get('book_title')
    if member_name in members and book_title in books and books[book_title] == 'Available':
        members[member_name]['books'].append(book_title)
        books[book_title] = 'Borrowed'
    return redirect(url_for('home'))

# 책 반납
@app.route('/return_book', methods=['POST'])
def return_book():
    member_name = request.form.get('member_name')
    book_title = request.form.get('book_title')
    if member_name in members and book_title in members[member_name]['books'] and books[book_title] == 'Borrowed':
        members[member_name]['books'].remove(book_title)
        books[book_title] = 'Available'
    return redirect(url_for('home'))

# 맨 밑에 멤버 정보와 책 상태 정보를 나타내는 페이지로 이동
@app.route('/members_and_books')
def members_and_books():
    return render_template('members_and_books.html', members=members, books=books)

if __name__ == '__main__':
    app.run(debug=True)

#변경사항...

