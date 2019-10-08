from jinja2 import Template, Environment, FileSystemLoader
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

# Open Region num .csv
with open ("regions-num.csv") as file_reg_num:
    buffer = file_reg_num.readlines()

# Create list with reg num
regnum = list()
for i in buffer:
    regnum.append(i.rstrip('\n').split(';'))
buffer.clear()

# Open template
templateLoader = FileSystemLoader(searchpath='./templates')
templateEnv = Environment(loader=templateLoader)
template = templateEnv.get_template('conf_template.j2')

# Generate configs
for i in regnum:
    file_name = './configs/EX3400-' + i[0] + '.conf'
    hostname = 'foms-sw-' + i[1]
    conf_file = open(file_name,'w')
    conf_file.writelines(template.render(ip=i[1],hostname=hostname))
    conf_file.close()

'''
# Test connect to JunOS
with Device(host="172.29.154.101", port="22", user="slipko", password="SlipKo89@gmail.com") as dev:
    pprint(dev.facts)
'''
