from datetime import date


class RBReservation:
    def __init__(self, reservation_id: int | None = None,
                 object_id: int | None = None,
                 user_id: int | None = None):
        self.id = reservation_id
        self.object_id = object_id
        self.user_id = user_id

    def to_dict(self) -> dict:
        data = {'id': self.id,
                'object_id': self.object_id,
                'user_id': self.user_id}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data