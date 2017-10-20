---
layout: post
title:  "How ssh works"
date:   2017-10-14
---

Summarized from [here](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process).

## What is SSH

* Secure shell to administer remote servers
* Lets you have a cryptographically secured connection between two parties

## Encryption tools

* Asymmetric key: 
...* Used during initial key exchange process to set up the symmetric encryption.
...* SSH key pais are used to authenticate a client to a server.
	Client uploads public key to the server it wants to access.
	Server's `~/.ssh/authorized_keys` file contains the client's public key.

* Symmetric key: Used to encrypt data sent between server and client during a session.

## Symmetrical cipher systems recognized

* AES
* Blowfish
* 3DES
* ArcFour

Server and client can decide on a list of supported ciphers to use

## How it works

* Server 
...* listens on a port for connections
...* Negotiates secure connection
...* Authenticates client
...* Spawn environment if credentials accepted

* Client
...* Begin TCP handshake with server
...* Negotiate secure connection
...* Verify server's identify
...* Provide authentication credentials

## Negotiating encryption for session

* Client makes TCP connection to server
* Server responds with protocols it supports => client ensures it can match one of them
* Server provides public host key => client ensures this is the server it wants access to
* Negotiate a symmetric `session key` using Diffie-Hellman. All further communication will be encrypted with this key.

## How a server authenticates a client

Method 1 (inscure)
* Server asks client for password
* Client sends password over, encrypted with the `session key `

Method 2 (secure)
* Client sends his public key over
* Server checks `~/.ssh/authorized_keys` to make sure the client is authorized to log in
* Assuming the client is authorized,
	Server generates a `nonce` and uses the client's public key to encrypt the `nonce`,
	then sends it to the client
* Client uses his private key to recover `nonce`
* Client calculates `client_secret = MD5(nonce + session key)` and send `client_secret` it to the server
* Server checks that `client_secret = MD5(nonce + session key)`
























































