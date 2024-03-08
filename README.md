# BTP405_project1

Student name: Austin Ngo
Student ID: 128725223


Project 1

1.	Product Vision and Management (Chapter 1): 

For (target customer): Individuals and healthcare professionals seeking a secure and centralized solution to manage health information effortlessly.

Who (statement of the need or opportunity): Struggle with fragmented health records and the challenge of securely sharing information with healthcare providers.

The (product name) is a (product category): The PHR system is a cloud-based application for managing personal health records.

That (key benefit, compelling reason to buy): Allows users to seamlessly add, view, and share health data with healthcare providers securely, enhancing collaboration and improving healthcare outcomes.

Unlike (primary competitive alternative): Traditional paper-based health records or fragmented digital solutions lacking comprehensive features and security measures.

Our product (statement of primary differentiation): Differentiates itself by employing a microservices architecture for scalability, emphasizing security and privacy, and focusing on user needs through agile methodologies, personas, and user stories.

2.	 Agile Software Engineering (Chapter 2)
  
 
 

 
 

3.	 User-Centered Design (Chapter 3):

Personas: 

-	Patient Persona:
Name: Sarah Thompson
Age: 35
Occupation: Marketing Executive
Scenario: Sarah wants to manage her health information conveniently and securely. She needs a platform where she can keep track of her medical history, appointments, and prescriptions. Sarah also values the ability to share relevant information with her healthcare providers to receive personalized care.

-	Doctor Persona:
Name: Dr. Michael Rodriguez
Specialization: Family Medicine
Scenario: Dr. Rodriguez needs access to comprehensive patient health records to provide accurate diagnoses and treatment plans. He requires a system that allows him to view patient medical history, lab results, and medication lists in real-time. Dr. Rodriguez also values features that enable secure communication with patients and other healthcare professionals.

-	Health Administrator Persona:
Name: Emily Parker
Role: Health Information Manager
Scenario: Emily is responsible for managing health records and ensuring compliance with regulatory requirements. She needs a system that facilitates efficient data entry, retrieval, and sharing while maintaining strict security and privacy controls. Emily also values features that streamline administrative tasks such as generating reports and conducting audits.

User Stories:

-	Patient User Story:
As a patient, I want to easily access my medical records and appointments from any device, so I can stay informed about my health status and upcoming appointments.
-	Doctor User Story:
As a doctor, I want to quickly review patient medical history and test results during appointments, so I can provide accurate diagnoses and treatment recommendations.
-	Health Administrator User Story:
As a health administrator, I want to efficiently manage user access permissions and audit logs, so I can ensure compliance with regulatory requirements and protect patient confidentiality.

Scenarios:

-	Patient Scenario:
Sarah needs to schedule a follow-up appointment with her doctor after receiving her lab test results. She logs into the PHR system to view her test results and available appointment slots, then schedules an appointment that fits her schedule.
-	Doctor Scenario:
During a patient visit, Dr. Rodriguez needs to prescribe medication for a chronic condition. He accesses the PHR system to review the patient's medication history and allergies, then selects the appropriate medication and dosage for the patient.
-	Health Administrator Scenario:
Emily receives a request from a patient to access their medical records. She logs into the PHR system, verifies the patient's identity, and grants access to the requested records while ensuring compliance with privacy regulations.Seeks a secure platform to share health data with healthcare providers, ensuring continuity of care for her family.

4.	Software Architecture (Chapter 4)
The system is structured as a collection of loosely coupled microservices, each responsible for specific functionalities such as user authentication, data storage, and access control. This architecture enhances scalability and maintainability by allowing independent deployment and scaling of individual services.

Security Layers: Security measures are implemented at multiple layers of the architecture, including network security, authentication, authorization, and data encryption. Access to sensitive health information is restricted based on user roles and permissions, ensuring compliance with healthcare regulations such as HIPAA.

Scalability: The system is designed to handle a large volume of users and data by leveraging cloud-based services for horizontal scaling. Load balancers distribute incoming traffic across multiple instances of microservices, ensuring optimal performance during peak usage periods.

Interoperability: The use of standardized protocols and data formats facilitates interoperability with existing healthcare systems and third-party applications. APIs are provided to enable seamless integration with electronic health records (EHR) systems and healthcare provider networks.

5.	Cloud-Based Software Engineering (Chapter 5):
Leverage cloud services for hosting, data storage, and scalability. Utilize virtualization and containers for deployment and isolation of microservices.

6.	Microservices Architecture (Chapter 6):
Structure the application as a collection of loosely coupled services that implement specific business functions. Employ RESTful services for communication between microservices.

7.	Security and Privacy (Chapter 7):
Implement comprehensive security measures, including authentication,authorization, encryption, and privacy-preserving features. Ensure the system isresilient against common attacks and protects users' sensitive healthinformation
