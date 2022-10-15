import uvicorn
from fastapi import FastAPI
from starlette.responses import Response
import subprocess

app = FastAPI()


@app.get("/health")
def get_version():
    try:
        subprocess.call("systemctl is-active --quiet ipsec", shell=True)
    except subprocess.CalledProcessError as exc:
        print("error code", exc.returncode, exc.output)
        return Response("ipsec service is Down", status_code=500)

    try:
        subprocess.call("systemctl is-active --quiet xl2tpd", shell=True)
    except subprocess.CalledProcessError as exc:
        print("error code", exc.returncode, exc.output)
        return Response("xl2tpd service is Down", status_code=500)

    return Response("System is healthy", status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
