from models import Session, User
import random

def main():
    session = Session()
    users = session.query(User).all()

    lucky_user = random.choice(users)
    print(f"The lucky user is {lucky_user} with {lucky_user.id}")
    print(f"His/Her salary is {lucky_user.salary}")
    old_salary = lucky_user.salary
    lucky_user.salary *= 1.15

    session.add(lucky_user)
    session.commit()

    result = session.query(User).get(lucky_user.id)
    assert result.salary != old_salary, "Salary was not updated"


if __name__ == '__main__':
    main()