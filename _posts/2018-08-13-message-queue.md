---
type: post
title: "Message queue"
date: 2018-08-13
---

Summarized from [here](https://aws.amazon.com/message-queue/).

## Introduction

Used in serverless and microservices architectures in modern clouds,
to communicate between the distributed applications.

Different parts of a system can communicate asynchronously,
as a message can be temporarity stored on the message queue's buffer
until a consumer is ready to process it.
Thus message queues are commonly used to buffer/batch work, or smooth spike workloads.

## One-to-one communications

Many producers and consumers can use a message queue,
but each message is processed only once by a single consumer. 

