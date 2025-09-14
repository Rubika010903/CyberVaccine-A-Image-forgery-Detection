# CYBERVACCINE - A IMAGE FORGERY DETECTION SYSTEM

Today, people frequently interact with their families, friends, and colleagues through online social networks (OSN).People enjoy posting and sharing their photos in online communities, blogs, and content sharing sites.

The problem addressed in this project is the susceptibility of digital images to tampering, which compromises security and privacy. Traditional image forgery detection methods face challenges in reproducing original content after manipulation. 

This project introduces an advanced Photo Forgery Detector System leveraging Invertible Neural Networks. 

The system, comprising the Cyber Vaccinator, Vaccine Validator, Forgery Detector Phase for Tamper Detection, and Self Recovery Phase for Image Self-Recovery, aims to proactively immunize images against various attacks. 

To ensure lossless recovery, Run-Length Encoding (RLE) is employed as a final step to compare the original image and the recovered image.


## Table of content
Problem Definition
Existing System
Disadvantages
Proposed System
Advantages
Software Requirements
Modules List
1. Social Networking Web App
2. End User Interface
3. Adversarial Simulation: Training Against Threats
4. PFDNet Middleware
5. Quality Assurance
6. Notification
Software Requirements


## Problem Definition
Recently, many online social networking websites provide photo sharing features that offer users options to upload and share their photos with an assortment of people.

Photo sharing provides users with great convenience, but still brings them serious threats of privacy leakage.

Rapid advancements in digital tools make image editing easy and free. The main problem is the compromised credibility of digital images due to the ease of manipulation through advanced digital image processing tools. 

This vulnerability leads to the creation and dissemination of maliciously fabricated images, fostering the potential for misinformation and influencing public opinion, especially on online social networks. 

Additionally, the susceptibility of readers to well-crafted fake images exacerbates the issue, posing a threat to the integrity of online content and the smooth functioning of social networks.


## Existing System
Watermarking Techniques
Embedding watermarks in images to detect tampering by analyzing alterations in the watermark pattern.

Digital Signatures
Using cryptographic techniques to add a digital signature to images, ensuring integrity and authenticity.

Copy-Move Detection
Identifying duplicated or manipulated regions within an image by detecting identical patterns.

Forensic Hashing
Generating cryptographic hash values for images to verify their integrity and detect tampering.

Steganalysis Techniques
Analyzing hidden information or data embedded within images to detect tampering or alterations.

Image Forensics using Machine Learning
Employing machine learning algorithms to analyze patterns, features, and inconsistencies indicative of tampering.

Biometric-Based Authentication
Incorporating biometric features within images for authentication, making tampering more challenging without affecting the biometric data.

Image Phylogeny
Examining the evolutionary relationships between images to identify common ancestry and potential tampering.



## Disadvantages 

Limited robustness against advanced tampering techniques.
Sensitivity to image compression leading to potential false alerts.
Computational complexity, hindering real-time implementation.
Vulnerability to sophisticated steganography methods.
Occurrence of false positives/negatives affecting detection accuracy.
Challenges in generalizing across diverse image types.


## Proposed System
The proposed system, PFDNet is a robust solution aimed at ensuring the authenticity and integrity of digital images shared on social networking platforms. The system is designed to protect against image tampering, detect forgery, and recover altered images seamlessly. 

Cyber Vaccinator Module
This module acts as a preventive mechanism to safeguard digital images. It applies imperceptible perturbations to the structure of images, making them tamper-resistant. By proactively protecting images, it ensures that unauthorized modifications are minimized.

Forgery Detector Phase
The Forgery Detector module leverages advanced deep learning techniques, such as PFDNet, to detect and localize tampered regions within images. This module operates with high precision, ensuring that any unauthorized alterations are accurately identified and localized.

Self Recovery Phase
The Self Recovery module is responsible for restoring tampered images to a state close to their original form. By employing Discrete Cosine Transform algorithms, it enables the seamless recovery of altered content, ensuring minimal loss of quality or data.

Quality Assurance
To ensure the integrity of recovered images, the Quality Assurance employs techniques like Run-Length Encoding (RLE). This module verifies the completeness and quality of restored images, enhancing user trust and confidence in the system.


## Advantages
Tamper Resilience: Enhances resistance against unauthorized alterations.
Ensures recovery without loss of original image information.
Improves the security of digital images against tampering threats.
Applicable across domains such as forensics and digital communication.
Maintains the authenticity of recovered images.
Effectively addresses challenges posed by compressed or low-resolution images.

## Softtware Requirements

![image alt](https://github.com/Rubika0109/cybervaccine-A-Image-Forgery-Detection-System/blob/e0cfcdf8c0d006cc11079de5ace4565e042b2380/Screenshot%20(62).png)




## Modules List
1. Social Networking Web App
2. End User Interface
3.Adversarial Simulation: Training Against Threats
          3.1 Copy-Move Attacks
          3.2 Splicing Attacks
          3.3 In painting Attacks
4. PFDNet Middleware
          4.1 Cyber Vaccinator: Preserving Media Authenticity
          4.2 Vaccine Validator: Safeguarding Digital Content
          4.3 Forgery Detector with Tamper Detection and Localization
          4.4 Self Recovery for Image Self-Recovery: Restoration and Resilience
5. Quality Assurance
          5.1 Run Length Encoding
          5.2 PSNR (Peak Signal-to-Noise Ratio) Calculation
6. Notification Module


## Social Networking Web App
Social networking web application is fully developed using Python, Flask and MySQL. Bootstrap and Wampserver 2i provide users with a secure, responsive and complete experience. 

This user authentication module guarantees secure access, employing features such as user registration, login, password hashing, and two-factor authentication.

The heart of the platform lies in the Media Sharing module, where users can seamlessly upload and share images, creating a dynamic and visually appealing environment.

Connection Management facilitates user interactions, incorporating friend requests, group creation, and an effective notification system.


## End User Interface
Login
Enables users to log into their accounts using valid credentials. A secure authentication process grants access to the user`s personalized space within the social network.

Apply Digital Attack on Shared Image
Users can experiment with various tampering techniques, enhancing their understanding of potential threats.

Share Tampered Image or Photo to Other Social Networks
      This feature extends the reach of tampered content beyond the immediate social network, showcasing the potential impact of digital attacks.

Receive Notifications
Notifies users of relevant activities, such as new friend requests, shared content, or interactions with their posts. 


## Adversarial Simulation: Training Against Threats
1. Copy-Move Attacks
Copy-move attacks involve the unauthorized duplication of specific regions within an image. 

2. Splicing Attacks
Splicing attacks entail the fusion of content from different sources into a single image. 

3. In painting Attacks
In painting attacks involve the intricate process of reconstructing missing or tampered areas within an image.


## PFDNet Middleware
The core processing layer of the system, PFDNet Middleware, integrates key functionalities for image integrity.

1 Cyber Vaccinator: Preserving Media Authenticity
Applies imperceptible perturbations to images, making them tamper-resistant and safeguarding their authenticity.

2 Vaccine Validator: Safeguarding Digital Content
Ensures that the applied perturbations remain intact and validates the resistance of the media against tampering attempts.

3 Forgery Detector with Tamper Detection and Localization

Leverages deep learning techniques to detect unauthorized modifications, accurately localize tampered regions, and provide detailed insights.

4 Self-Recovery for Image Self-Recovery: Restoration and Resilience

Employs algorithms like Discrete Cosine Transform (DCT) to restore tampered content close to its original form, ensuring resilience and data integrity.


##  Quality Assurance
This module ensures that recovered images meet high standards of integrity and quality.

1 Run-Length Encoding
Verifies the completeness of restored images by analyzing data patterns.

2 PSNR (Peak Signal-to-Noise Ratio) Calculation
Measures the quality of recovered images by comparing them to their original state, ensuring minimal degradation.


##  Notification
An email notification is sent to the user who shared the vaccinated image. The email informs the user about the shared image and includes a prompt to take action.

The email includes a clear prompt asking the user to make a decision regarding the shared image.

Based on the user`s decision, the system takes appropriate actions. If the user chooses to remove the image, the system initiates the removal process.

After the user makes a decision, a confirmation message is sent to the user to acknowledge their choice.

## Software Requirements
1. Operating System: Windows 10/11 or Linux (Ubuntu).
2. Python: Version 3.6 or higher 
3. Flask: For backend development.
4. Bootstrap: For frontend design.
5. WampServer: Apache server (Windows) for Local Deployment.
6. MySQL: For database management.
7. NumPy: For numerical operations.
8. TensorFlow/PyTorch: For deep learning (used in the forgery detection and recovery).
9. OpenCV: For image processing.
10. Scikit-learn: For machine learning.
11. Matplotlib/Seaborn: For visualizations.
12. Pillow: For image processing.



















   








