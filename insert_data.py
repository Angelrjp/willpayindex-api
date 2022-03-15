from flask import Flask
from app import app
from src.models import UserIncome, UserInfo, db

def insert_dummy_data():
    with app.app_context():
        # UserInfo.create('123456', '30', 'M', '3124345454', 'Bogotá')
        users = [
            UserInfo(
                user_id=1,
                age=20,
                gender='M',
                phone='+573134551010',
                city='Bogota',
                income=UserIncome(monthly_income=1500000,monthly_expenses=1400000)
            ),
            UserInfo(
                user_id=2,
                age=20,
                gender='M',
                phone='+573134551010',
                city='Bogota',
                income=UserIncome(monthly_income=1500000,monthly_expenses=1400000)
            ),
            UserInfo(
                user_id=3,
                age=20,
                gender='M',
                phone='+573134551010',
                city='Bogota',
                income=UserIncome(monthly_income=1500000,monthly_expenses=1400000)
            ),
            UserInfo(
                user_id=4,
                age=20,
                gender='M',
                phone='+573134551010',
                city='Bogota',
                income=UserIncome(monthly_income=1500000,monthly_expenses=1400000)
            )
        ]
        db.session.add_all(users)
        db.session.commit()

if __name__ == "__main__":
    insert_dummy_data()