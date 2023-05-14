from sqlalchemy import and_ , or_
from models import Session, User


def main():
    session = Session()
    query = session.query(User).filter(
        User.salary.between(5000,6000)).order_by(
        User.salary.desc())
    for row in query.limit(3):
        print(row.id,
              row.first_name,
              row.last_name,
              row.email,
              row.salary)
    print('-------------------------')
    user = session.query(User).filter(
        User.first_name.like('J%')
    ).first()
    print(user)

    print('-------------------------')
    sql_question = session.query(User.id,
                                 User.email,
                                 User.creation_date).filter(and_(
        User.salary.between(5000,6000),
        User.first_name.like("J%"))
    ).order_by(User.salary.desc(),
               User.creation_date.asc())
    for r in sql_question:
        print(r)






# first() - zwraca None jezeli wynik pusty jezeli niepusty to pierwszy lepszy
# nie wygeneruje bledu

# one() - jezeli bedzie wiecej niz jeden wynik to się wywala i sypie blad tak samo jak jest pusta

#scalar() - oczekuje ze w wyniku jeden element, wiecej niż jeden wynik powoduje wywrotke, jezeli w wyniku nie bedzie nic to się nie wywala daje None





if __name__ == '__main__':
    main()