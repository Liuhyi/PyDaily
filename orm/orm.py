import sqlite3

# 字段基类，代表数据库的字段
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


# 元类负责将字段和表结构映射
class ModelMeta(type):
    def __new__(cls, name, bases, class_dict):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, class_dict)

        table_name = class_dict.get('table_name', name.lower())
        fields = {}
        primary_key = None
        builtin_primary_key = False

        # 收集字段和主键信息
        for key, value in class_dict.items():
            if isinstance(value, Field):
                fields[key] = value
                if value.primary_key:
                    primary_key = key

        # 如果没有用户设置的主键字段，设置 `id` 作为默认自增主键
        if primary_key is None:
            fields['id'] = IntegerField(primary_key=True)
            primary_key = 'id'
            builtin_primary_key = True

        # 更新类属性
        class_dict['_table_name'] = table_name
        class_dict['_fields'] = fields
        class_dict['_primary_key'] = primary_key
        class_dict['_builtin_primary_key'] = builtin_primary_key

        return super().__new__(cls, name, bases, class_dict)


# 基础模型类，封装通用的 ORM 操作
class BaseModel(metaclass=ModelMeta):
    _connection = sqlite3.connect('database.db')
    _cursor = _connection.cursor()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create_table(cls):
        columns = []
        for name, field in cls._fields.items():
            definition = f'{name} {field.field_type}'
            if field.primary_key:
                definition += ' PRIMARY KEY'
                # 仅在系统默认 `id` 为主键时添加自增属性
                if cls._builtin_primary_key:
                    definition += ' AUTOINCREMENT'
            if field.default is not None:
                definition += f' DEFAULT {field.default}'
            columns.append(definition)

        sql = f'CREATE TABLE IF NOT EXISTS {cls._table_name} ({", ".join(columns)})'
        cls._cursor.execute(sql)

    def save(self, overwrite=False):
        # 构建列和占位符
        columns = ', '.join([col for col in self._fields.keys() if col != 'id' or self._builtin_primary_key])
        placeholders = ', '.join(['?' for _ in self._fields.keys() if _ != 'id' or self._builtin_primary_key])
        values = [getattr(self, column, None) for column in self._fields.keys() if column != 'id' or self._builtin_primary_key]

        # 获取主键值
        pk_value = getattr(self, self._primary_key, None)

        if pk_value is not None:
            # 查询记录是否已存在
            self._cursor.execute(
                f'SELECT 1 FROM {self._table_name} WHERE {self._primary_key} = ?', (pk_value,)
            )
            if self._cursor.fetchone():
                if overwrite:
                    # 执行更新操作
                    update_clause = ', '.join([f'{col}=?' for col in self._fields.keys() if col != self._primary_key])
                    sql = f'UPDATE {self._table_name} SET {update_clause} WHERE {self._primary_key} = ?'
                    values.append(pk_value)
                    self._cursor.execute(sql, values)
                    self._connection.commit()
                else:
                    # 不覆盖，提示警告
                    print(f"\033[91mWarning: Record with primary key {pk_value} already exists. Not overwriting.\033[0m")
                return

        # 插入新记录
        sql = f'INSERT INTO {self._table_name} ({columns}) VALUES ({placeholders})'
        self._cursor.execute(sql, values)
        self._connection.commit()

    @classmethod
    def get(cls, **kwargs):
        condition = ' AND '.join([f'{k}=?' for k in kwargs.keys()])
        sql = f'SELECT * FROM {cls._table_name} WHERE {condition}'
        cls._cursor.execute(sql, tuple(kwargs.values()))
        return cls._cursor.fetchone()

    @classmethod
    def all(cls):
        sql = f'SELECT * FROM {cls._table_name}'
        cls._cursor.execute(sql)
        return cls._cursor.fetchall()

    def delete(self):
        pk_value = getattr(self, self._primary_key)
        sql = f'DELETE FROM {self._table_name} WHERE {self._primary_key} = ?'
        self._cursor.execute(sql, (pk_value,))
        self._connection.commit()


# 示例模型类
class User(BaseModel):
    table_name = 'users'
    id = IntegerField(primary_key=True)  # 用户自定义主键 `id`
    name = StringField(max_length=100)
    age = IntegerField(default=0)


# 测试代码
if __name__ == '__main__':
    User.create_table()

    # 插入一些用户
    user1 = User(id=1, name='Alice', age=25)
    user1.save(overwrite=True)

    user2 = User(id=1, name='Bob', age=30)
    user2.save(overwrite=False)  # 不覆盖

    user3 = User(id=2, name='Charlie', age=35)
    user3.save(overwrite=True)  # 覆盖

    users = User.all()
    print(f'All Users: {users}')
