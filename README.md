# Azure Two-Tier Web Application

## Project Overview

The goal of this project is to develop a deeper understanding of Docker, Jenkins, and how to automate application deployments.

I'll be working with a two-tier web application consisting of a Flask application and a MySQL database. My focus is understanding how the components work together, how to containerize them, and how to automate the build, testing, and deployment process.

I'm taking a slower approach to this project. I could follow a tutorial and get everything running, but that doesn't mean I understand what I just built or why.

My goal is to sharpen my engineering skills, understand the decisions behind the technology, and continue developing toward a lead engineering role.

## Business Problem

Manual deployments require human effort, which introduces opportunities for mistakes.

Docker helps address the "it works on my computer" problem by packaging an application with its runtime and dependencies into a consistent image.

Jenkins will help automate the process of pulling code from GitHub, building it, testing it, and eventually deploying it.

I want to understand not just how to automate deployments, but how to make them reliable and what to do when something fails.

## Original Project and Credit

**Original author:** Prashant Gohel

**Original repository:** https://github.com/prashantgohel321/DevOps-Project-Two-Tier-Flask-App

I did not create the original Flask application. I'm using Prashant Gohel's project as a reference for this learning exercise.

The original repository includes:

- `app.py` — Flask application
- `templates/` — HTML templates
- `message.sql` — Database SQL
- `requirement.txt` — Python dependencies
- `Dockerfile` — Container build instructions
- `docker-compose.yml` — Multi-container configuration
- `Jenkinsfile` — CI/CD pipeline

I plan to study the application files to understand how the web application communicates with its database.

Her project uses AWS EC2. I'm choosing Microsoft Azure for my implementation.

I also intend to work through my own Docker configuration, Jenkins pipeline, Azure infrastructure, and deployment decisions rather than simply copying her completed solution.

No application code from the original repository has been incorporated into this project yet. I'll verify reuse permissions before doing so.

The goal is to learn the engineering work, not take credit for somebody else's project.

## Planned Technologies

- **Azure** — Cloud infrastructure
- **Docker** — Containerization
- **Docker Compose** — Managing the application and database containers
- **Jenkins** — CI/CD automation
- **GitHub** — Source control
- **Python Flask** — Web application
- **MySQL** — Database

These are the technologies I plan to work with. I'm not claiming to have implemented all of them in this project yet.

## Current Progress

**Phase 1 — Project Planning**

Completed:
- Created the local project directory structure.
- Started documenting the project goals and business problem.
- Identified the original application and credited its author.

Not completed:
- Application setup
- Docker containerization
- Azure deployment
- Jenkins CI/CD pipeline
- Automated testing

## Next Steps

1. Review the application and database requirements.
2. Design the Azure environment.
3. Work through containerizing the application.
4. Test the application and database communication.
5. Build and test the Jenkins pipeline.
6. Document what works, what breaks, and what I learned.

I'll update this README as I make progress. I want it to reflect what I've actually done and understand, not just what I plan to accomplish.