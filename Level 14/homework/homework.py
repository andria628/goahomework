# < > - მეტობა ან ნაკლებობა
# == - უდრის,ტოლობა
# != - არ უდრის
# <= - ნაკლებობა ან ტოლობა
# >= - მეტობა ან ტოლობა
# = - ტოლობა 
# + - მიმატება
# - გამოკლება
# * - გამრავლება
# / გაყოფა
#             true                  false                       true
print((True and not False) or (False and True) or (not (False or False) and True))
# ჯამში გამოიტანს : true
#         true              false
print((True or not (False and True)))
# ჯამში გამოიტანს : True
#           true                    false               true                                               true 
print((True and not False) or (False and True) or (not (False or False) and True) and (True or not (False and True)))
# ჯამში გამოიტანს : true
