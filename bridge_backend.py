# FastAPI bridge to connect the mobile app with PARAM Porul Slurm login nodes
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import paramiko

app = FastAPI(title="PARAM Porul HPC Bridge API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SlurmRequest(BaseModel):
    username: str
    password: str = None
    node: str = "login01.paramporul.nitt.edu"

@app.post("/api/queue")
def get_queue(req: SlurmRequest):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(req.node, username=req.username, password=req.password, timeout=10)
        stdin, stdout, stderr = ssh.exec_command(f"squeue -u {req.username} --format='%i|%j|%T|%M|%D|%R'")
        out = stdout.read().decode()
        ssh.close()
        return {"status": "success", "queue": out}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
