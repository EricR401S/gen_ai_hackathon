# gen_ai_hackathon
# Team 33 Compositive Drawing Generator


## Overview

With the global economic downturn in recent years, societal security has become an increasingly severe issue that urban residents are more concerned about. The crime rate is continuously rising, but the number of police officers maintaining law and order hasn't kept pace. When the police force cannot keep up, the rights and interests of citizens cannot be protected in a timely manner. 

In the harrowing aftermath of a crime, the ability to swiftly identify an assailant is crucial. Traditional identification processes, which rely on a forensic artist, can be protracted and are hindered by the rapidly diminishing recollections of a distressed victim.

Solution: Our tool revolutionizes this process by generating immediate visual representations from victims' verbal accounts, providing essential visual aids during the critical initial hours following an incident.

## Workflow

![workflow](<Blank diagram (1).png>)

When a user fills out a form in the website, the app.py file on GitHub automatically generates a piece of text and sends it to Dalle. Dalle then creates an image based on this text and returns it to GitHub, where it is automatically downloaded to the local system.


CTA: Discover how our Forensic Sketch Helper modernizes the conventional approach to witness testimony, contributing to the safety of our communities.

## Features
1. Accessible Interface: A straightforward platform that facilitates the input of descriptive details, either through text or voice recordings.
2. Automated Drawing Generation: Utilizes advanced AI to convert descriptions into composite sketches.
3. Immediate Assistance: Provides a rapid tool for victims to help law enforcement capture essential details before they fade.
4. Accuracy and Detail: Adheres to law enforcement sketching standards with comprehensive facial detail options.

This generator is designed according to the police sketching standards with 19 facial detail dimensions. Users can freely fill in the description for each part in the table, capturing the image of the criminal in their mind accurately. Moreover, as we used Streamlit to create our website, users can access this feature anywhere with WI-FI connectivity. From now on, if you are robbed or harmed, you can call 911 and immediately receive a URL link sent by the police. This allows you to quickly sketch the appearance of the perpetrator who should be punished before the memory fades.

## How It Works
1. The victim or a representative inputs descriptive details into our interface, using either text or voice recording.
2. Our backend processes the input and communicates with Dalle, an AI specializing in image creation.
3. Dalle crafts a visual sketch based on the provided description and relays it back to our system.
4. The image is available for download or can be directly used for reporting purposes.

## Getting Started
1. Clone the repository: git clone https://github.com/YourRepoLinkHere
2. Install prerequisites: Python, Git, Dalle-related packages
3. Install dependencies: pip install -r requirements.txt
4. Launch the application: python app.py

## Usage
- Navigate to the application and input the descriptive details via the available methods.
- Initiate the composite drawing process.
- Use the resulting image to aid law enforcement in their investigation.

## Progress and Learning
- Mastery of the Streamlit framework has been replaced by broader web development techniques.
- Our journey with Dalle has highlighted the delicate balance of creating prompts that produce accurate representations.
- The project underscores the significant role of thematic and emotive language in AI-generated artwork.
- Techniques such as using RAG databases simplify and optimize the text transcription process by contextualizing the prompts.

## Future Directions

Enhancements will be focused on:
- Further refining the accuracy and quality of the sketches.
- Integrating databases for improved descriptive inputs.
- Streamlining the process from description to generation for even faster results.

Contact
For inquiries or feedback, please contact us at: ejr41@duke.edu

