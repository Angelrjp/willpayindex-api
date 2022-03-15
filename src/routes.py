from datetime import datetime

from flask import Flask, jsonify
from sqlalchemy import event
from sqlalchemy.engine import Engine
from src.models import UserInfo, UserIncome, db

from src.indicators import will_pay_index
from flask import Blueprint, render_template

bp = Blueprint('will-pay-index', __name__)

@bp.route("/api/v1/users/<int:user_id>/will-pay-index/", methods=["GET"])
def user_will_pay_index(user_id):
    user = UserInfo.query.filter_by(user_id=user_id).first()

    if user is not None:
        response = { 
            'age': user.age,
            'gender': user.gender,
            'monthly_income': user.income.monthly_income,
            'monthly_expenses': user.income.monthly_expenses,
        }
        response["will_pay_index"] = will_pay_index(user.gender, user.age, user.income.monthly_income, user.income.monthly_expenses)
        response["timestamp"] = datetime.now()
        response["message"] = "Index Calculado"
        status_code = 200

    else:
        response = {"id": user_id, "message": "Usuario no encontrado"}
        status_code = 404

    return jsonify(response), status_code