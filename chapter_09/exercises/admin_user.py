from admin import Admin
from privileges import Privileges

admin_user = Admin('john', 'doe', 'canada', 'jdoe')
admin_user.privileges.show_privileges()
