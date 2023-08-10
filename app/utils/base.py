from datetime import datetime
from flask import jsonify
from app import db

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    active = db.Column(db.Boolean, default=True)

    def to_json(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.to_json()

    def insert(self, request):
        data = request.form.to_dict()

        # Проверяем, что все данные введены
        if data:
            # Создаем новый объект модели с данными
            new_object = self(**data)

            # Добавляем его в базу данных
            db.session.add(new_object)
            db.session.commit()

            # Возвращаем сообщение об успехе
            return jsonify({"msg": f"Новый объект {self.__name__} успешно добавлен"})
        else:
            # Возвращаем сообщение об ошибке
            return jsonify({"msg": f"Пожалуйста, заполните все поля"})

    def update(self, request):
        # Проверяем, что все данные введены
        if self:
            # Проверяем, что объект существует
            if object:
                # Обновляем атрибуты объекта с данными
                for key, value in request.items():
                    setattr(object, key, value)

                # Сохраняем изменения в базе данных
                db.session.commit()

                # Возвращаем сообщение об успехе
                return f"Объект {self.__name__} успешно обновлен"
            else:
                # Возвращаем сообщение об ошибке
                return f"Объект {self.__name__} не найден"
        else:
            # Возвращаем сообщение об ошибке
            return "Пожалуйста, заполните все поля"