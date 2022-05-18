#!/bin/sh
bench get-app https://git.gonext.com.mx/frappe/frappe.git --branch prod &&
rm -rf apps/frappe/frappe/integrations/doctype/twilio_settings &&
bench get-app https://git.gonext.com.mx/frappe/erpnext.git --branch prod &&
bench get-app https://git.gonext.com.mx/ibravo/Mobile.git --branch dev &&
bench get-app https://git.gonext.com.mx/valsa/e_billing.git --branch prod &&
bench get-app https://git.gonext.com.mx/valsa/sales_drive.git --branch prod &&
bench get-app https://git.gonext.com.mx/valsa/edi.git --branch prod &&
bench get-app https://git.gonext.com.mx/valsa/cheque_management.git --branch prod &&
bench get-app https://git.gonext.com.mx/valsa/valsa.git --branch prod &&
bench get-app https://git.gonext.com.mx/valsa/logistics.git --branch prod &&
bench new-site valsa.site --db-name valsa_db_mx &&
touch sites/currentsite.txt && echo 'valsa.site' > sites/currentsite.txt &&
bench --site valsa.site set-config developer_mode true &&
bench --site valsa.site install-app frappe erpnext mobile e_billing sales_drive edi cheque_management logistics valsa
