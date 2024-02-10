#  dataiku-technical-assessment-submission_Anthony_Bolton
Dataiku Technical Assessment: "Millennium Falcon Challenge" by Anthony Bolton

# What are the Odds?

## Overview

The Millennium Falcon Odds Calculator is built on a robust technical foundation, employing [Vue.js](https://vuejs.org/)
 for the frontend to create a dynamic and engaging user interface, and [Flask](https://flask.palletsprojects.com/en/3.0.x/), a [Python](https://www.python.org/) micro web framework, for the backend to handle complex calculations and data processing. The application integrates [Axios](https://v2.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html?redirect=true) for efficient HTTP requests, ensuring seamless communication between the client and server sides. With [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/), it addresses cross-origin resource sharing, facilitating the frontend's access to the backend across different domains. This combination of technologies not only enhances the user experience by providing real-time interactions but also ensures that the application's architecture is scalable, maintainable, and capable of evolving with future enhancements.

The application is designed to ensure consistent user experience on both mobile and web platforms. 

### Video Demonstration ###
To access a demonstration video of this application, navigate to the following google drive link:
https://drive.google.com/file/d/15dlA8gHc-z0paoAz4BhMVtS9FCya1eHB/view

### Screenshot Demonstration ###
Below are screenshots the the application: 

![Screenshot of the web application](assets\demo2.png)
**Screenshot of the web application**

![Both millennium-falcon.json and empire.json uploaded and tested for Example 2 on the original Github - returning the correct result](assets\demo1.png)
**Both millennium-falcon.json and empire.json uploaded and tested for Example 2 on the original Github - returning the correct result**

![Screenshot of the mobile application](assets\demo_phone.png)
**Screenshot of the mobile application**

## Requirements
1. ### To program C3PO to compute the odds that the Millennium Falcon reaches Endor in time and saves the galaxy - given two JSON files. 

- To navitage to the C3PO Class:
```sh
cd server/c3po/c3po.py
```
The C3PO Class takes in two JSON files as inputs: Navigation Data of the Millennium Falcon(millennium-falcon.json) and Empire countdown and Bounty Hunter invasion plan data(empire.js) 
- To test the C3PO Class with the app, find example/testcases given from [the question github](https://github.com/dataiku/millenium-falcon-challenge-simple) in:
```sh
cd server/tests/json_tests
```
- Example Millennium Falcon file: millennium-falcon_0.json
- Example Empire files in the correct order: empire_0.json(Output: 0), empire_1.json(Output: 0.81), empire_2.json(Output: 0.9) and empire_2.json(Output: 1).
2. ### Correctness with respect to the given specification
- The C3PO Class **passes all given testcases** and correctly return the output to the frontend.
- **Additional testcases** are implemented to check edge cases and various scenarios (However, the original testcases cover a well-rounded amount of cases)
- Implemented **unit testing** for given testcases to ensure robustness and correctness of the algorithm in the backend before deploying.

Evaluation:
- Given additional time, conducting more unit testing would strengthen the robustness of the algorithm. This approach ensures that the algorithm performs reliably across various scenarios and inputs, ultimately enhancing the overall quality and reliability of the software.

3. ### User experience 
- A **full-stack application** has been implemented to ensure seamless interactions between client-side and server-side. Users are able to use this app from both web and mobile interfaces.
- The **UI/UX is well designed**, which **reduces the learning curve** for end-users and decreases the frequency and severity of support cases. **User Interface** is Star wars themed and **visually appealing.**
- **Clear and concise instructions** on how to use the app. Data validation and error handling are also implemented to guide users. (e.g. user uploads incorrect file format)

Evaluation:
- The input format exclusively supports JSON files. However, recognizing that non-technical users may lack familiarity with or access to raw JSON files, there is potential to introduce manual data entry options for navigation, countdown, and bounty hunter information. Implementing such features would not only improve user experience but also broaden the accessibility of the application to a wider audience.

3. ### Ease of deploying and operate
- The app leverages Flask for backend **simplicity** and Vue.js for a dynamic frontend, ensuring **easy deployment and scalability**. Its architecture supports quick setup and smooth scaling to accommodate user growth, making it practical for field deployment.
- The app is **able to support customers on a daily basis and it is easy to maintain.** Flask's extensive documentation and large community ensure that developers and support teams have access to the resources they need to troubleshoot and enhance the application. Similarly, Vue.js's comprehensive documentation and component-based architecture make it easy for teams to update the UI or add new features without extensive downtime.
- The README.md of this repository includes **comprehensive documentation** including description and instructions of the app and the technical architecture. Easy for engineers to understand and carry on contributing to the project.

Evaluation:
- Given additional time, I would create a more formal and comprehensive Software Design Documentation. This documentation would cover both technical and non-technical aspects of the project to enhance its comprehensibility and ensure its long-term viability for further development.
4. ### Code Quality
- The codebase prioritizes **readability and cleanliness**. It employs clear and **meaningful function and variable names**, as well as adopts a concise and understandable code style and structure. Additionally, it incorporates essential comments where necessary to further enhance comprehension.
## Backend

Built with Flask, a lightweight WSGI web application framework in Python. It is easy to use and extends into a complex application. Flask-CORS is employed for handling Cross-Origin Resource Sharing (CORS), making AJAX requests possible from the frontend to the backend.

The C3PO Class in implemented with Python, taking in JSON files as inputs from client-side Vue.js and returning the odds of success for the Millennium Falcon to save the galaxy to the frontend. 

## Frontend

The frontend is crafted with Vue.js, a versatile JavaScript framework for building UIs and single-page applications. Axios is used for promise-based HTTP client to make requests to the backend.

The following features are implemented:

## Instructions

### Prerequisites

1. Before starting, ensure you have **Python** with **pip** and **Node.js** with **npm** installed on your system. 
2. It is recommended to use a **virtual environment** for the Python packages.
3. **Make sure that the local ports 8080 and 8081 are available on your system**. The Vue.js front-end application will utilize port 8080, while the Flask backend server will operate on port 8081. 

### Client-Side Setup

Install client dependencies with npm:

```sh
cd client
npm install
```
### Server-Side Setup
Set up the server dependencies using pip:
```sh
cd server
pip install -r requirements.txt
```
### Running the Application
To run the application from the client directory:
```sh
cd client
npm start
```
### Running Unit Tests on the C3PO Class from backend
Run the following command in root directory:
```sh
pytest -v --durations=0 server/tests/test_c3po.py
```

