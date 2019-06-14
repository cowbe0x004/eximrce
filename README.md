# eximrce

Simple python socket connection to test if exim is vulnerable to CVE-2019-10149. 
The payload simply touch a file in /root/lweximtest. Output will be slow
depending on server's reply.

**Run locally on suspected server. This checks for indication of compromise.**
```
curl -s https://raw.githubusercontent.com/cowbe0x004/eximrce-CVE-2019-10149/master/eximioc.sh |bash
```

**Run remotely. Testing for remote code execution.**
```
git clone https://github.com/cowbe0x004/eximrce-CVE-2019-10149
cd eximrce-CVE-2019-10149
python eximrce.py <HOST> <PORT>
```
**If /root/lweximtest exists on the server, remote code execution is possible.**
