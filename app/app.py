import pathlib
import sys

p = pathlib.Path(__file__).resolve().parent.parent
sys.path.append('{}/'.format(p))

import uvicorn

from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse


def func():
    html_content = """
    <html>
        <head>
            <title>V3 Recommender System</title>
        </head>
        <body>
            This is <strong>Predicting part of V3 rXys</strong>. Check <a href="/docs">the link</a> for more details. <br>
            Copyright © 2022 <a href="https://rosetta.ai">rosetta.ai</a>. All rights reserved.
        </body>
    </html>
    """
    return html_content

app = FastAPI()


@app.get("/")
async def root():
    
    html_content = func()
    return HTMLResponse(html_content)


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8051, reload='debug' == 'debug')
