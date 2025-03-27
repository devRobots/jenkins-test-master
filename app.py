import importlib

logfunctions = importlib.import_module("b2b-modules.logfunctions")
logfunctions.log_message("100", "Funciona!")
