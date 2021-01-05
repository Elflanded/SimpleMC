import logging
import requests


class Http:


    def sendRequest(url):
        payload = requests.get(str(url))
        statusCode = payload.status_code
        content = payload.content
        if statusCode is not 200:
            return logging.error(f"[MinecraftAPI][GET] Something went wrong. Error: {statusCode}")
        return content


    def postRequest(url, payload):
        payload = requests.post(str(url), data=payload)
        statusCode = payload.status_code
        content = payload.content
        if statusCode is not 200:
            return logging.error(f"[MinecraftAPI][POST] Something went wrong. Error: {statusCode}")
        return content