## Deploy a model with vLLM
1. Install vLLM with `pip install vllm`
2. Follow this [link](https://github.com/QwenLM/Qwen2.5?tab=readme-ov-file#vllm) to deploy and serve a model locally
3. Follow this [link](https://github.com/QwenLM/Qwen-Agent) to customize an agent to query the model

## Set up SSH Tunnel for <your_machine> -> <Axes> -> <GPU VM>
### On local machine:
1. `ssh-keygen -t ed25519 -C "<your_email>"`
2. `ssh-copy-id -i ~/.ssh/id_ed25519.pub <your_id>@axes.cs.virginia.edu`
3. then `ssh <your_id>@axes.cs.virginia.edu` to login axes server

### On axes:
1. SSH to the GPU VM
2. copy your local machine's ssh key to `~/.ssh/authorized_keys`

### Then you will be able to ssh to the GPU VM with 
1. `ssh -J <your_id>@axes.cs.virginia.edu ubuntu@<your_vm_ip>`
2. ports mapping `ssh -L 9000:<your_vm_ip>:8000 -J <your_id>@axes.cs.virginia.edu ubuntu@<your_vm_ip>`
