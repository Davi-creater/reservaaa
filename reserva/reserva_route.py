from flask import Blueprint, request, jsonify
from reserva_model import Reserva
from database import db

routes = Blueprint("routes", __name__)

@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.json

    reserva = Reserva(
        turma_id=dados.get("turma_id"),
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201

@routes.route("/reservas", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            "id": r.id,
            "turma_id": r.turma_id,
            "sala": r.sala,
            "data": str(r.data),
            "hora_inicio": str(r.hora_inicio),
            "hora_fim": str(r.hora_fim)
        } for r in reservas
    ])
