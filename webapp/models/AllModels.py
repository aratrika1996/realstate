import datetime
from webapp import db 
from sqlalchemy import DateTime
from werkzeug.security import generate_password_hash, check_password_hash
  
class UserModel(db.Model):

  #nombre tabla
  __tablename__ = 'users'

  #columns
  id = db.Column(db.Integer, primary_key=True)
  fullname= db.Column(db.String(80), nullable=True)
  username= db.Column(db.String(80), unique=True, nullable=True)
  email = db.Column(db.String(256), unique=True, nullable=True)
  password = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  
  #init data
  def __init__(self, fullname, username, email, password):

    #declare data
    self.fullname = fullname
    self.username = username
    self.email = email
    self.password = self.create_password(password)

  #Generate Hash password
  def create_password(self, password):
    return generate_password_hash(password)

  #Verifique hash password
  def verify_password(self, password):
    return check_password_hash(self.password, password)
  
''' 
  ###############################################
  ################ ADMIN MODEL #################
  ###############################################
'''
class AdminModel(db.Model):

  #nombre tabla
  __tablename__ = 'admin'

  #columns
  admin_id = db.Column(db.Integer, primary_key=True)
  first_name= db.Column(db.String(50), nullable=True)
  last_name= db.Column(db.String(50), nullable=True)
  email = db.Column(db.String(50), unique=True, nullable=False)
  encrypted_password = db.Column(db.String(200), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  
  #init data
  def __init__(self,first_name,last_name,email,encrypted_password):

    #declare data
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.encrypted_password = self.create_password(encrypted_password)

  #Generate Hash password
  def create_password(self, encrypted_password):
    return generate_password_hash(encrypted_password)

''' 
  ###############################################
  ################ TENANT MODEL #################
  ###############################################
'''
class TenantModel(db.Model):
  #nombre tabla
  __tablename__ = 'tenant'

  #columns
  tenant_id = db.Column(db.Integer, primary_key=True)
  first_name= db.Column(db.String(50), nullable=True)
  last_name= db.Column(db.String(50), nullable=True)
  email = db.Column(db.String(100), unique=True, nullable=False)
  encrypted_password = db.Column(db.String(100), nullable=False)
  rental_unit_id = db.Column(db.Integer, nullable=True)
  lease_document_url = db.Column(db.String(100), nullable=True)
  id_document_url = db.Column(db.String(100), nullable=True)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  
  #init data
  def __init__(self,first_name,last_name,email,encrypted_password):

    #declare data
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.encrypted_password = self.create_password(encrypted_password)

  #Generate Hash password
  def create_password(self, encrypted_password):
    return generate_password_hash(encrypted_password)


''' 
  ###############################################
  ################ LEASE MODEL #################
  ###############################################
'''
class TenantModel(db.Model):
  #nombre tabla
  __tablename__ = 'lease'

  #columns
  lease_id = db.Column(db.Integer, primary_key=True)
  lease_document_url= db.Column(db.String(200), nullable=True)
  start_date= db.Column(db.DateTime(), nullable=True)
  end_date= db.Column(db.DateTime(), nullable=True)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  
  #init data
  def __init__(self,first_name,last_name,email,encrypted_password):

    #declare data
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.encrypted_password = self.create_password(encrypted_password)

  #Generate Hash password
  def create_password(self, encrypted_password):
    return generate_password_hash(encrypted_password)


''' 
  ###############################################
  ############# TENANT-LEASE MODEL ##############
  ###############################################
'''
class TenantLeaseModel(db.Model):
  #nombre tabla
  __tablename__ = 'tenant_lease'

  #columns
  tenant_lease_id = db.Column(db.Integer, primary_key=True)
  lease_id = db.Column(db.Integer, db.ForeignKey('tenant.tenant_id'), primary_key=True)
  tenant_id = db.Column(db.Integer, db.ForeignKey('lease.lease_id'), primary_key=True)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.now)
  
  #init data
  def __init__(self, lease_id, tenant_id):

    #declare data
    self.lease_id = lease_id
    self.tenant_id = tenant_id