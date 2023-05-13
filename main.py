import json

import quart
import quart_cors
from quart import request
from OEISPlugin import OEISPlugin

app = quart_cors.cors(quart.Quart(__name__),
                      allow_origin="https://chat.openai.com")

plugin = OEISPlugin()


@app.get("/process/<string:message>")
async def process(message):
    print(message)
    response = plugin.process(message)
    print(response)
    return quart.Response(response=json.dumps(response), status=200)


@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")


def main():
    app.run(debug=True, host="0.0.0.0", port=5003)


if __name__ == "__main__":
    main()
