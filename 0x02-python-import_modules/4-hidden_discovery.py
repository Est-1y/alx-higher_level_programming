#!/usr/bin/python3
pyc_file_path = 'hidden_4.pyc'

module_spec = importlib.util.spec_from_file_location('hidden_4', pyc_file_path)

module = importlib.util.module_from_spec(module_spec)

module_spec.loader.exec_module(module)

module_names = [name for name in dir(module) if not name.startswith('__')]

module_names.sort()

for name in module_names:
    print(name)
