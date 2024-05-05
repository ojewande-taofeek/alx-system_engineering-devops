<center> <h1> 0x0B. SSH </h1> </center>
<br>
Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using <strong>ssh</strong>. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a <a href="https://intranet.alxswe.com/rltoken/UQIQV4HJGvBv0qrHhlDFaQ"> previous project</a> shared in your <a href="https://intranet.alxswe.com/rltoken/8ZlNV0J-sa-dijhmhJolOg">intranet profile.</a>
<br>
You can access your server information in the <a href="https://intranet.alxswe.com/rltoken/e2_s_pXwBVuYbhrvoesfrg">my servers</a> section of the intranet, each line with contains the IP and username you should use to connect via ssh.
<br>
<b>Note</b>: Your server is configured with an Ubuntu 20.04 LTS environment.

<center><h2>Resources</h3></center>
<strong>Read or watch:</strong>
<ul>
<li>What is a (physical) server - text</li>
<li>What is a (physical) server - video</li>
<li>SSH essentials</li>
<li>SSH Config File</li>
<li>Public Key Authentication for SSH</li>
<li>How Secure Shell Works</li>
<li>SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)</li>
</ul>
<ul>
<center><h3>For reference:</h3></center>

<li>Understanding the SSH Encryption and Connection Process</li>
<li>Secure Shell Wiki</li>
<li>IETF RFC 4251 (Description of the SSH Protocol)</li>
<li>Internet Engineering Task Force</li>
<li>Request for Comments</li>
</ul>
<strong>man or help:</strong>
<ul>
<li>ssh</li>
<li>ssh-keygen</li>
<li>env</li>
</ul>

<center><h2>Learning Objectives</h2></center>
At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/0Wgw_i87NIVCfUcRzdZgkg">explain to anyone</a>, <strong>without the help of Google:</strong>
<br>
<center><h2>General</h2></center>
<ul>
<li>What is a server</li>
<li>Where servers usually live</li>
<li>What is SSH</li>
<li>How to create an SSH RSA key pair</li>
<li>How to connect to a remote host using an SSH RSA key pair</li>
<li>The advantage of using #!/usr/bin/env bash instead of /bin/bash</li>
</ul>
<br>
<center><h2>Copyright - Plagiarism</h2></center>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.</li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
<br>
<center><h2>Requirements</h2></center>
<center><h3>General</h3></center>
<ul>
<li>Allowed editors: vi, vim, emacs
<li>All your files will be interpren Ubuntu 20.04 LTS</li>
<li>All your files should end with  line</li>
<li>A README.md file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>
