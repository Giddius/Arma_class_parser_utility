from gidtools.gidtriumvirate import GidSQLBuilder


db = GidSQLBuilder.get_database()


one = (db.executor('SELECT * FROM "cfgweapons_items_tbl"'), 'CfgWeapons')
two = (db.executor('SELECT * FROM "cfgvehicles_items_tbl"'), 'CfgVehicles')
three = (db.executor('SELECT * FROM "cfgunitinsignia_items_tbl"'), 'CfgUnitInsignia')
four = (db.executor('SELECT * FROM "cfgfactionclasses_items_tbl"'), 'CfgFactionClasses')

_list = [one, two, three, four]
for i in _list:
    print(i[1] + ' --> ' + str(len(i[0])))

_len = 0

for i in _list:
    _len += len(i)


print('----------')
print(str(_len))
