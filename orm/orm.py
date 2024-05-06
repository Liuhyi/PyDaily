import sqlite3


class Field:
    def __init__(self, field_type, primary_key=False, default=None):
        self.field_type = field_type
        self.primary_key = primary_key
        self.default = default


class IntegerField(Field):
    def __init__(self, primary_key=False, default=None):
        super().__init__('INTEGER', primary_key, default)


class StringField(Field):
    def __init__(self, max_length=255, default=None):
        super().__init__(f'VARCHAR({max_length})', False, default)


class ModelMeta(type):
    def __new__(cls, name, bases, class_dict):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, class_dict)

        table_name = class_dict.get('table_name', name.lower())
        fields = {}
        primary_key = None
        builtin_primary_key = False

        for key, value in class_dict.items():
            if isinstance(value, Field):
                fields[key] = value
                if value.primary_key:
                    primary_key = key
        for key in fields.keys():
            class_dict.pop(key)

        if primary_key is None:
            _fields = {'id': IntegerField(primary_key=True)}
            _fields.update(fields)
            fields = _fields
            primary_key = 'id'
            builtin_primary_key = True

        class_dict['_table_name'] = table_name
        class_dict['_fields'] = fields
        class_dict['_primary_key'] = primary_key
        class_dict['_builtin_primary_key'] = builtin_primary_key

        return super().__new__(cls, name, bases, class_dict)


class BaseModel(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def _get_connection(cls):
        return sqlite3.connect('database_id.db')

    @classmethod
    def create_table(cls):
        columns = []
        for name, field in cls._fields.items():
            definition = f'{name} {field.field_type}'
            if field.primary_key:
                definition += ' PRIMARY KEY'
                if cls._builtin_primary_key:
                    definition += ' AUTOINCREMENT'
            if field.default is not None:
                definition += f' DEFAULT {field.default}'
            columns.append(definition)

        sql = f'CREATE TABLE IF NOT EXISTS {cls._table_name} ({", ".join(columns)})'
        try:
            with cls._get_connection() as conn:
                conn.execute(sql)
        except sqlite3.Error as e:
            print(f"Error creating table {cls._table_name}: {e}")

    def save(self, overwrite=False):
        cls = self.__class__
        columns = ', '.join([col for col in cls._fields.keys()])
        placeholders = ', '.join(['?' for _ in cls._fields.keys()])
        values = [getattr(self, column, None) for column in cls._fields.keys()]
        pk_value = getattr(self, cls._primary_key, None)

        try:
            with cls._get_connection() as conn:
                cursor = conn.cursor()
                if pk_value is not None:
                    cursor.execute(
                        f'SELECT 1 FROM {cls._table_name} WHERE {cls._primary_key} = ?', (pk_value,)
                    )
                    if cursor.fetchone():
                        if overwrite:
                            update_clause = ', '.join([f'{col}=?' for col in cls._fields.keys()])
                            sql = f'UPDATE {cls._table_name} SET {update_clause} WHERE {cls._primary_key} = ?'
                            values.append(pk_value)
                            cursor.execute(sql, values)
                        else:
                            print(
                                f"\033[91mWarning: Record with primary key {pk_value} already exists. Not overwriting.\033[0m")
                        return
                sql = f'INSERT INTO {cls._table_name} ({columns}) VALUES ({placeholders})'
                cursor.execute(sql, values)
        except sqlite3.Error as e:
            print(f"Error saving to {cls._table_name}: {e}")

    @classmethod
    def get(cls, **kwargs):
        condition = ' AND '.join([f'{k}=?' for k in kwargs.keys()])
        sql = f'SELECT * FROM {cls._table_name} WHERE {condition}'
        try:
            with cls._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, tuple(kwargs.values()))
                return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error fetching from {cls._table_name}: {e}")

    @classmethod
    def all(cls):
        sql = f'SELECT * FROM {cls._table_name}'
        try:
            with cls._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching all from {cls._table_name}: {e}")

    def delete(self):
        pk_value = getattr(self, self._primary_key)
        sql = f'DELETE FROM {self._table_name} WHERE {self._primary_key} = ?'
        try:
            with self._get_connection() as conn:
                conn.execute(sql, (pk_value,))
        except sqlite3.Error as e:
            print(f"Error deleting from {self._table_name}: {e}")


class User(BaseModel):
    table_name = 'users'
    name = StringField(max_length=100)
    age = IntegerField(default=0)
    job = StringField(max_length=100, default='Programmer')


if __name__ == '__main__':
    User.create_table()

    for i in range(23):
        user = User(name=f'User-{i}', age=20 + i, job='Engineer')
        user.save()
    users = User.all()
    for user in users:
        print(user)
    print(User.get(name='User-1'))
