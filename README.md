# eximrce

Simple python socket connection to test if exim is vulnerable to CVE-2019-10149. 
The payload simply touch a file in /root/lweximtest. Output will be slow
depending on server's reply and not knowing how to properly use python's socket module. Would love a lesson on how to speed it up. Only tested on cPanel boxes.

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

**If you are not able to update exim, at least put this ACL in exim.conf so ${run{ can't be run.**
```
acl_check_rcpt:
deny message = Restricted characters in address
domains = +local_domains
local_parts = ^[.] : ^.*[\$@%!/|]

deny message = Restricted characters in address
domains = !+local_domains
local_parts = ^[./|] : ^.*[\$@%!] : ^.*/\\.\\./

acl_check_mail:
drop message = Restricted characters in address
condition = ${if match{$sender_address}{\N.*\$.*run.*\N}{1}{0}}}
```
