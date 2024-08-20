class RBObject:
    def __init__(self, object_id: int | None = None,
                 category_id: int | None = None):
        self.id = object_id
        self.category_id = category_id

    def to_dict(self) -> dict:
        data = {'id': self.id,
                'category_id': self.category_id}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data