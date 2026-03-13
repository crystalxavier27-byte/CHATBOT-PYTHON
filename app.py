from flask import Flask, request, jsonify, render_template
from groq import Groq

app = Flask(__name__)

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

client = Groq(api_key=GROQ_API_KEY)

with open("knowledge.txt", "r", encoding="utf-8") as file:
    knowledge = file.read()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message").lower()

    if user_message in ["hi","hello","hey"]:
        return jsonify({"reply":"Hello 👋 I am CloudOps Assistant. Ask me anything about DevOps, CI/CD, Docker or Kubernetes."})

    qa_pairs = {

    "what is devops":"DevOps is a practice that combines software development and IT operations to improve collaboration and speed of software delivery.",
    "what is continuous integration":"Continuous Integration is the practice of frequently merging code changes into a shared repository.",
    "what is continuous delivery":"Continuous Delivery automatically prepares code for release after testing.",
    "what is continuous deployment":"Continuous Deployment automatically releases code changes to production.",
    "what is a ci cd pipeline":"A CI/CD pipeline automates building, testing, and deploying applications.",
    "what is jenkins":"Jenkins is an open source automation server used for CI/CD.",
    "what is jenkins pipeline":"A Jenkins pipeline defines the stages of software delivery using code.",
    "what is jenkinsfile":"A Jenkinsfile is a script that defines Jenkins pipeline stages.",
    "what are jenkins plugins":"Jenkins plugins extend Jenkins functionality.",
    "why ci cd is important":"CI/CD improves speed, quality, and reliability of software delivery.",

    "what is automated testing":"Automated testing uses tools to automatically test applications.",
    "what is cloud automation":"Cloud automation manages cloud infrastructure automatically.",
    "what is terraform":"Terraform is an Infrastructure as Code tool used to create and manage cloud infrastructure.",
    "what are terraform features":"Terraform features include automation, version control and multi cloud support.",
    "what is ansible":"Ansible is an automation tool for configuration management.",
    "what is ansible playbook":"An Ansible playbook is a YAML file containing automation tasks.",
    "what is aws cloudformation":"AWS CloudFormation allows infrastructure creation using templates.",
    "what is infrastructure as code":"Infrastructure as Code manages infrastructure using code instead of manual processes.",
    "why iac is important":"IaC improves automation, scalability and consistency.",
    "what are automation tools":"Automation tools include Jenkins, Terraform, Ansible and Puppet.",

    "what is provisioning":"Provisioning is setting up IT infrastructure resources.",
    "what is a container":"A container packages an application with its dependencies.",
    "what is docker":"Docker is a containerization platform.",
    "what is kubernetes":"Kubernetes is a container orchestration platform.",
    "what is a docker image":"A Docker image is a template used to create containers.",
    "what is a pod in kubernetes":"A Pod is the smallest deployable unit in Kubernetes.",
    "what is container orchestration":"Container orchestration manages container deployment and scaling.",
    "what is kubernetes cluster":"A Kubernetes cluster is a group of nodes running containers.",
    "what is a dockerfile":"A Dockerfile defines instructions to build a Docker image.",
    "what is monitoring":"Monitoring tracks system performance.",

    "what is logging":"Logging records system activities.",
    "what are monitoring tools":"Monitoring tools include Prometheus, Grafana and Nagios.",
    "what is prometheus":"Prometheus is a monitoring system for collecting metrics.",
    "what is grafana":"Grafana is a visualization dashboard for monitoring data.",
    "what is scalability":"Scalability is the ability to handle increasing workload.",
    "what is load balancing":"Load balancing distributes traffic across multiple servers.",
    "what is high availability":"High availability ensures systems remain operational with minimal downtime.",
    "what is devsecops":"DevSecOps integrates security into DevOps.",
    "what is git":"Git is a distributed version control system.",
    "what is github":"GitHub hosts Git repositories for collaboration.",

    "what is version control":"Version control tracks code changes.",
    "what is microservices":"Microservices architecture builds applications as independent services.",
    "what is rollback":"Rollback means reverting to a previous version.",
    "what is build automation":"Build automation compiles and packages code automatically.",
    "what is configuration management":"Configuration management maintains system consistency.",
    "what is virtualization":"Virtualization allows multiple operating systems on one machine.",
    "what is cloud computing":"Cloud computing delivers computing services via the internet.",
    "what are cloud providers":"Major cloud providers include AWS, Azure and Google Cloud.",
    "what is aws":"AWS is Amazon's cloud computing platform.",
    "what is azure":"Azure is Microsoft's cloud platform.",

    "what is google cloud":"Google Cloud provides cloud computing services.",
    "what is docker hub":"Docker Hub stores Docker images.",
    "what is kubectl":"Kubectl is the command line tool for Kubernetes.",
    "what is helm":"Helm is a package manager for Kubernetes.",
    "what is service discovery":"Service discovery allows services to find each other.",
    "what is api gateway":"API Gateway manages API traffic.",
    "what is devops lifecycle":"DevOps lifecycle includes planning, coding, building, testing, releasing and monitoring.",
    "what is site reliability engineering":"SRE applies software engineering principles to operations.",
    "what is fault tolerance":"Fault tolerance ensures systems continue working after failure.",
    "what is disaster recovery":"Disaster recovery restores systems after failure.",

    "what is latency":"Latency is delay between request and response.",
    "what is throughput":"Throughput is the amount of data processed in time.",
    "what is serverless computing":"Serverless allows running code without managing servers.",
    "what is aws lambda":"AWS Lambda runs code without servers.",
    "what is container registry":"Container registry stores container images.",
    "what is cluster autoscaling":"Cluster autoscaling automatically adjusts nodes.",
    "what is node in kubernetes":"A node is a worker machine in Kubernetes.",
    "what is deployment in kubernetes":"A deployment manages pod updates.",
    "what is kubernetes service":"A Kubernetes service exposes pods.",
    "what is ingress":"Ingress manages external access to Kubernetes.",

    "what is secret management":"Secret management stores sensitive data securely.",
    "what is configuration drift":"Configuration drift occurs when systems deviate from intended setup.",
    "what is immutable infrastructure":"Immutable infrastructure replaces servers instead of modifying them.",
    "what is artifact":"An artifact is the output of a build process.",
    "what is release management":"Release management controls deployment to production.",
    "what is dev environment":"Development environment is used by developers to write code.",
    "what is staging environment":"Staging environment tests before production.",
    "what is production environment":"Production environment is used by real users.",
    "what is metrics":"Metrics are numerical system measurements.",
    "what is alerting":"Alerting notifies teams about system issues."
    }

    if user_message in qa_pairs:
        return jsonify({"reply": qa_pairs[user_message]})

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"system",
                "content":"You are a CloudOps assistant. Only answer DevOps, CI/CD, Docker, Kubernetes and Cloud questions. If question is unrelated say it is outside the scope."
            },
            {
                "role":"user",
                "content":f"Answer from this data:\n{knowledge}\n\nQuestion:{user_message}"
            }
        ],
    )

    bot_reply = completion.choices[0].message.content

    return jsonify({"reply":bot_reply})


if __name__ == "__main__":
    app.run(debug=True)