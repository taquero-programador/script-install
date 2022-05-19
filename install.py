#!/usr/bin/env python3

import os

name_bench = input('Name for bench init: ') # nombre del directorio para el proyecto
site_name = input('Name for site: ') # nombre del site
db_name = input('Name for Database: ') # nombre de la base de datos

os.system(f"bench init {name_bench or 'frappe-bench'} --frappe-branch version-13\
	&& cd {name_bench or 'frappe-bench'} &&\
	bench get-app https://git.gonext.com.mx/frappe/frappe.git --branch prod &&\
	rm -rf apps/frappe/frappe/integrations/doctype/twilio_settings &&\
	bench get-app https://git.gonext.com.mx/frappe/erpnext.git --branch prod &&\
	bench get-app https://git.gonext.com.mx/ibravo/Mobile.git --branch dev &&\
	bench get-app https://git.gonext.com.mx/valsa/e_billing.git --branch prod &&\
	bench get-app https://git.gonext.com.mx/valsa/sales_drive.git --branch prod &&\
	bench get-app https://git.gonext.com.mx/valsa/edi.git --branch prod &&\
	bench get-app https://git.gonext.com.mx/valsa/cheque_management.git --branch prod &&\
	bench get-app https://git.gonext.com.mx/valsa/valsa.git --branch prod &&\
	bench get-app https://git.gonext.com.mx/valsa/logistics.git --branch prod &&\
	bench new-site {site_name or 'valsa.site'} --db-name {db_name or 'valsa_site_db'} &&\
	touch sites/currentsite.txt && echo '{site_name or 'valsa.site'}' > sites/currentsite.txt &&\
	bench --site {site_name or 'valsa.site'} set-config developer_mode true &&\
	bench --site {site_name or 'valsa.site'} install-app frappe erpnext mobile e_billing sales_drive edi cheque_management logistics valsa")