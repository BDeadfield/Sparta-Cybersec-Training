
# N-Tier and REST API

**Presentation / View** is compromised of either a graphical user interface or a command line interface that the user will utilize in order to interact with software.

**Application / Business** is compromised of the software code itself.

**Data** is compromised of any inputs / outputs of external data to the software. This can include .txt and .json files as well as databases.

## One-Tier Architecture

One-tier architecture is when software is deployed directly on a client's machine rather than utilzing a server as an intermediary.

## Two-Tier Architecture

Two-tier architecture is similar to one-tier, however in this situation the data will be stored externally in a server, where this data will be able to be accessed by multiple user simultaneously.

## Three-Tier Architecture

Three-tier architecture utilzes a client machine in order to display the view / presentation, whereas a server will handle the application / business processing and will interact with another server in order to input / output data.

## N-Tier Architecture

N-Tier Architecture is similar to three-tier architecture, however in this scenario a web server is used in between the client's presentation / view and a server's application / business processing in order to deliver the applicaiton. This is known as N-Tier architecture due to the fact that there can be multiple web servers working to deliver an applicaiton.


## REST

Rest stand for Representational State Transfer. It is an arhitectural style for applications and is primiarily used to build web services that are lightweight, maintainable and scalabvle. Services based on REST are known as RESTful services. REST is not dependent on any protocol, but almost every RESTful service uses HTTP / HTTPS as an underlying protcol.

RESTful services should have the following properties:

**Representation and Data Flow** requires you to define your data sources, which could be anything from a .txt file to a database.

**HTTP Messages & Verb** is the structure in which communication is formed between a client and host. Using HTTP, the system will work on a simple client / server request / response methodology.

*HTTP Verbs:*
- GET: Read
- POST: Create
- PUT: Update / Replace
- PATCH: Update / Modify
- DELETE: Delete

*HTTP Codes:*
- 1xx = Information
- 2xx = Successful resposne
- 3xx = Redirect to another URL
- 4xx = Client error
- 5xx = Server error

**URL's & Naming Resources** is key in regards to the R - Representational part of REST. As an example, when exposing a customer database to partners and third-parties it may be displayed as: http://ourservice/customer/1 or http://oursservice/customer?id=1 and would yield the following in it's response body: {'ID': '1', 'firstname': 'Joe', 'surname': 'Bloggs', 'email': 'joe.b@gmail.com',}

**Statelessness** means that your RESTful service does not maintain or hold the state of a previous request unlike the stateful methodology. It will treat every call as a new request and it will be handled as such.
