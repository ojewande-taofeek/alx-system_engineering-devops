# 0x01. Shell, permissions

This an ALX SE Programme project

## Resources
**Read or watch:**

## Permissions
**man or help:**

- chmod
- sudo
- su
- chown
- chgrp
- id
- groups
- whoami
- adduser
- useradd
- addgroup
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google:**

## Permissions
- What do the commands chmod, sudo, su, chown, chgrp do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user chown a file
- How to run a command with root privileges
- How to change user ID or become superuser
## Other Man Pages
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid
## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Commands
>**Disclaimer: This is provided as a practice, no intent to share the solution**

**Note: The first line for each task is #!/bin/bash**
| File name | Commands |
| --------- | -------- |
| 0-iam_betty | su betty |
| 1-who_am_i | whoami |
| 2-groups | groups |
| 3-new_owner | sudo chown betty hello |
| 4-empty | touch hello |
| 5-execute | chmod u+x hello |
| 6-multiple_permissions | chmod 754 hello |
| 7-everybody | chmod a+x hello |
| 8-James_Bond | chmod 007 hello |
| 9-John_Doe | chmod 753 hello |