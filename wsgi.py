#!/usr/bin/python3
import importlib

application = importlib.import_module('api.v1.app').app

if __name__ == "__main__":
    application.run()
