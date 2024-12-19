# Asynchronous Message Queue with FastAPI & WebSocket

This project implements an asynchronous message queue system that facilitates communication between microservices and front-end clients. It supports both backend services (using FastAPI) and front-end WebSocket-based clients for real-time updates. The system includes features such as message publishing, subscribing, message filtering, retries for failed messages, and appropriate exception handling.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Running the Microservices](#running-the-microservices)
    - [Testing the System](#testing-the-system)
5. [Architecture](#architecture)
6. [Project Structure](#project-structure)
7. [Dependencies](#dependencies)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction

This project demonstrates the implementation of an asynchronous message queue using Python. It includes:
- **Message Queue**: Asynchronous publish and subscribe system with support for message filtering and retries.
- **FastAPI Microservices**: Two services that communicate through the message queue.
- **WebSocket Support**: Front-end clients can connect via WebSocket to receive real-time updates.
- **Retries**: Failed messages are retried automatically.

The system is designed to help decouple microservices and support real-time communication for web clients.

---

## Features

- **Publish/Subscribe System**: Microservices can publish messages to topics, and clients can subscribe to receive messages.
- **Message Filtering**: Subscribers can filter messages based on custom logic.
- **Retry Logic**: Failed messages can be retried automatically.
- **WebSocket for Real-Time Updates**: Front-end clients can subscribe to WebSocket channels for real-time updates.
- **FastAPI Microservices**: Includes two FastAPI services that demonstrate the usage of the message queue.
- **Automated Setup**: A Python script automates the setup and execution of services.

---

## Installation

To install and set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/async-message-queue.git
   cd async-message-queue
