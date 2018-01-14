---
layout: post
title:  "File transfer protocols"
date:   2018-01-08
---

How to transfer files to and from a remote server.
Summarized from [here](https://blog.devolutions.net/2016/5/ftps-sftp-or-ftp-over-ssh).

## SFTP - SSH File Transfer Protocol

Secure communication protocol that was build for the purpose of allowing file transfer. 
Industry recommended protocol when working with remote servers.

## FTP over SSH

FTP protocol tunneled through an SSH connection.
Rarely used because FTP needs more than one connection to work. 

## FTP

The original file transfer protocol, insecure as it sends passwords
over the network in plaintext.
No one uses it now... or if they do, they shouldn't.

