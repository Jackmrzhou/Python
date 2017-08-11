import pymysql

conn = pymysql.connect(
	host = "localhost",
	port = 3306,
	user = "root",
	password = "password",
	db = "ormtest",
	charset = "utf8",
	cursorclass = pymysql.cursors.DictCursor
	)
cursor = conn.cursor()

class  ModelMetaclass(type):

	def __new__(cls, name, bases, attrs):

		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)

		mapper = dict()
		fields = []

		for key, value in attrs.items():
			if isinstance(value, Field):
				mapper[key] = value
				fields.append(key)
				#The mapper is just like name ==> SteingField 
				#or {name : StringField}
				if value.primary_key:
					primarykey = key
		if not primarykey:
			raise("primarykey not found!")
		for key in mapper.keys():
			attrs.pop(key)
			#remove such as username after mapping
		attrs['__mapper__'] = mapper
		attrs['__table__'] = '`'+name+'`'
		attrs['__field__'] = fields
		attrs['__primarykey__'] = primarykey
		#bulid new attributes
		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):

	def __init__(self,**kw):
		super(Model, self).__init__(**kw)

	def __setattr__(self, key, value):
		self[key] = value

	def __getattr__(self, key):
		try:
			return self[key]
		except:
			raise('Model Object has no attribute {}'.format(key))

	def create(self):
		try:
			column_list = []
			for f in self.__mapper__.keys():
				s = '%s %s' %(f.name, f.column_type)
				column_list.append(s)
			column_list.append('primary key ({})'.format(self.__mapper__[self.__primarykey__].name))
			sql = 'create table {}({})'.format(self.__table__,','.join(column_list))
			cursor.execute(sql)
			print("Table Create Successfully!")
		except Exception as e:
			raise e

	def insert(self):

		args = list(map(lambda k: self[k], self.__field__))
		Field_list = list(map(lambda k: self.__mapper__[k], self.__field__))
		
		try:	
			sql = 'insert into {} ({}) values (%s{})'\
				.format(self.__table__, ','.join(x.name for x in Field_list),',%s'*(len(args)-1))
			cursor.execute(sql,args)
		except Exception as e:
			raise e

	@classmethod
	def query(cls,**kw):
		try:
			new_key_list = list(map(lambda k:cls.__mapper__[k].name, kw.keys()))
			k_s = '=%s,'.join(new_key_list) +'=%s'
			sql = 'select {} from {} where {}'\
				.format(','.join(cls.__mapper__[x].name for x in cls.__mapper__.keys()),
						cls.__table__,
						' and'.join(k_s.split(',')))
			args = list(kw.values())
			cursor.execute(sql, args)
			result = cursor.fetchall()

			return result
		except Exception as e:
			raise e
		
	def update(self, **kw):
		try:
			new_key_list = list(map(lambda k:self.__mapper__[k].name, kw.keys()))
			k_s = '=%s,'.join(new_key_list) +'=%s'
			sql = 'update {} set {} where {}'.format(self.__table__,k_s,
													 self.__mapper__[self.__primarykey__].name+'=%s')
			args = list(kw.values())
			args.append(self[self.__primarykey__])
			cursor.execute(sql, args)
		except Exception as e:
			raise e

	@classmethod
	def update_all(cls, **kw):
		try:
			new_key_list = list(map(lambda k:cls.__mapper__[k].name, kw.keys()))
			k_s = '=%s,'.join(new_key_list) +'=%s'
			sql = 'update {} set {}'.format(cls.__table__,k_s)
			args = list(kw.values())
			cursor.execute(sql, args)
		except Exception as e:
			raise e

	@classmethod
	def delete(cls,**kw):
		try:
			new_key_list = list(map(lambda k:cls.__mapper__[k].name, kw.keys()))
			k_s = '=%s,'.join(new_key_list) +'=%s'
			sql = 'delete from {} where {}'.format(cls.__table__,' and'.join(k_s.split(',')))
			args = list(kw.values())
			cursor.execute(sql, args)
		except Exception as e:
			raise e

	@classmethod
	def query_all(cls):
		try:
			cursor.execute('select * from {}'.format(cls.__table__))
			result = cursor.fetchall()
			return result
		except Exception as e:
			raise e

	@classmethod
	def commit(cls):
		try:
			conn.commit()
			print(cls.__table__ + 'table has changed!')
		except Exception as e:
			raise e

class Field(object):

	def __init__(self, name, column_type, primary_key):
		self.name = '`' + name + '`'
		#防止使用保留字符而报错
		self.column_type = column_type
		self.primary_key = primary_key

	def __repr__(self):
		return '<{} Field.>'.format(self.name)

class StringField(Field):

	def __init__(self, name = None, column_type = 'varchar(50)', primary_key = False):
		super().__init__(name, column_type, primary_key)

class IntegerField(Field):

	def __init__(self, name = None, column_type = 'Integer', primary_key = False):
		super().__init__(name, column_type, primary_key)

class TextField(Field):

	def __init__(self, name = None, column_type = 'Text', primary_key = False):
		super().__init__(name, column_type, primary_key)

if __name__ == '__main__':
	
	#ORM test
	class User(Model):
		id = IntegerField('id', primary_key = True)
		name = StringField('username')

	u = User(id = 2, name = 'jack_zhou')
	try:
		u.update(name = 'jack-zhou')
		User.commit()
	finally:
		cursor.close()
		conn.close()