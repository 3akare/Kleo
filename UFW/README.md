# UFW implementation in an Alpine Environment

## Introduction  
The assignment focuses on reviewing and implementing a firewall. For this project, I chose **Uncomplicated Firewall (UFW)** due to its simplicity and efficiency in managing firewall rules. To simulate the implementation, I used **Docker** with **Alpine Linux** as the base operating system, configured multiple Python servers, and applied UFW rules to enforce network security.

---
## How to Use  

### 1. Pull the Docker Image  
Retrieve the image from Docker Hub using the following command:  
```bash  
docker pull 3akare/ufw-enabled-alpine
```  

### 2. Run the Image  
Run the Docker image in interactive mode:  
```bash  
docker run --privileged --cap-add=NET_ADMIN --cap-add=NET_RAW -p 8080-8083:8080-8083 -it ufw-enabled-alpine:v1
```  

### 3. Enable the Firewall  
Once in the Alpine environment, enable UFW (it is disabled by default):  
```bash  
# terminal 1
ufw enable  
```  

### 4. Configure Default Rules  
Set the default rules for incoming and outgoing traffic:  
```bash  
# terminal 1
ufw default deny incoming  
ufw default allow outgoing  
```  

### 5. Run a Server  
Navigate to the development folder:  
```bash  
# terminal 1
cd /development 
```  
Run the first server script (`server-0.py`) on port **8080**:  
```bash  
# terminal 1
python3 server-0.py  
```  

### 6. Allow Port 8080  
Enable access to port 8080 using UFW:  
```bash  
# terminal 1
ufw allow 8080  
```  

### 7. Test Access to the Server  
In a separate terminal session, run:  
```bash  
# terminal 2
curl localhost:8080  
```  
You will receive the message:  
```bash
# terminal 2
"Server 0 is live, on port 8080%"
```  

### 8. Deny Port 8080  
In the first terminal session, block access to port 8080:  
```bash  
# terminal 1
ufw deny 8080  
```  

### 9. Verify Port Blocking  
Return to the second terminal session and run:  
```bash  
# terminal 2
curl localhost:8080  
```  
You will now receive a message indicating that the connection is blocked:  
```bash
"Connection refused"
```
### Additional
```bash
ufw show added #list of ufw rules enabled
```
---
 ## Implementation Details

### Environment Setup  
1. **Docker Image:**  
   - Base OS: **Alpine Linux** (chosen for its lightweight nature, ~5 MB).  
   - Installed essential tools and dependencies:  
     - Python (to run the servers).  
     - Python packages: **Flask** (for setting up the web servers).  
     - **UFW** (for firewall configuration and testing).  

2. **Network Configuration:**  
   - Opened ports **8080** to **8084** for communication between containers.

---

### Server Setup  
1. Created four Python servers using Flask, each running on separate ports:  
   - **8080**  
   - **8081**  
   - **8082**  
   - **8083**  

2. Verified that all servers were functioning correctly before applying firewall rules.

---

### UFW Rules Implementation  
1. Installed and enabled UFW on the container.  
2. Configured UFW rules:  
   - Allowed necessary internal communication between containers.  
   - Blocked external access to the servers (from outside the container).  

3. Verified that the firewall was active and the rules were enforced properly.

---

### Testing and Verification  
1. Turned on all Python servers simultaneously.  
2. Tested access to each server:  
   - Verified that they were **accessible internally** within the Docker environment.  
   - Ensured they were **inaccessible externally**, confirming UFW rules were applied effectively.

---

## Observations  
- **Performance:**  
  - Using Alpine significantly reduced the image size and allowed precise control over installed packages.  
- **UFW Functionality:**  
  - Easy to configure and manage firewall rules, making it ideal for this lightweight Docker setup.  
- **Docker Compatibility:**  
  - Docker's networking capabilities complemented the firewall, isolating containerized services from external threats.  

---

## Conclusion  
This implementation demonstrates the effective use of UFW as a firewall in a Dockerized environment. By leveraging lightweight tools like Alpine and Flask, I successfully created and secured multiple servers. UFW proved to be an uncomplicated yet powerful solution for ensuring network security.