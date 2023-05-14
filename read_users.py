from models import Session, User


def main():
    session = Session()
    query = session.query(User).filter(User.salary>9000)# filtorwanie po kolumnach             #.order_by(User.salary.desc())#.limit(10) # jeżeli chcemy pierwsze 10 rekordów
    for row in query.order_by(User.salary.desc()):                       #.limit(5):  #.offset(1): # tak też można, 5 uzytkownikow poza 1
        print(row.id, row.first_name, row.last_name, row.email, row.salary) # dostaniemy instancje klasy user





if __name__ == '__main__':
    main()