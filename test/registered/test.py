import subprocess

repo_url = "https://github.com/marysteven/pic"
runner_name = "python-runner"

cmd = [
    "./config.sh",
    "--url", repo_url,
    "--token", "B7NVQL5ARFLN72NX5O2RNBTJV2F3S",
    "--name", runner_name,
    "--work", "_work",
    "--unattended"
]

subprocess.run(cmd)

register_cuda_ci(stage-a-test-1,suite="stage-a-test-1")
