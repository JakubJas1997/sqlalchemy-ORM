from models import User, Session



def main():
    session = Session()
    user = User(
        first_name = "Kristian",
        last_name = "Bool",
        email="kristian.bool@gmail.com"
    )

    session.add(user)
    session.commit() #bez tego nie poleci do bazy danych


if __name__ == "__main__":
    main()