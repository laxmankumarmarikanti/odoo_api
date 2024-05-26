# import xmlrpc 
import xmlrpc.client

#auth details
base_url = "http://127.0.0.1:8069" 
database_name = "odoo"
user_name = "admin"
password = "admin"

# for common endpoint
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(base_url))
# user Authentication
user_id = common.authenticate(database_name,user_name,password, {}) #user id
# models endpoint
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(base_url))
# model name
model_name = 'res.partner'
# method name 'search_read' method to get the data
method = 'search_read'
domain = []

fields = ['name','phone','street','state_id']

items = models.execute_kw(database_name, user_id, password, model_name, method, [domain,fields])
