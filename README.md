



# Vehicle Detection and Counting System using OpenCV

![OpenCV Logo](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=opencv&logoColor=white)
![Python Logo](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-4db6ac?style=for-the-badge)
![Deep Learning](https://img.shields.io/badge/Deep-Learning-FF6F00?style=for-the-badge)
![Haar Cascade](https://img.shields.io/badge/Haar-Cascade-007A8D?style=for-the-badge)
![MIT License Logo](https://img.shields.io/badge/MIT-License-red?style=for-the-badge)


## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Video Reference](#video-reference)
6. [Documentation](#documentation)
7. [Developer Information](#developer-information)
8. [Training Vectors and Videos](#training-vectors-and-videos)
9. [Images](#images)
10. [License](#license)

## Introduction
This project implements a sophisticated vehicle detection and counting system using OpenCV, leveraging a pre-trained Haar Cascade classifier (`cars.xml`). It provides robust capabilities for detecting vehicles in both images and video streams, offering real-time monitoring and analysis.

## Installation
Follow these steps to set up the project:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Haar Cascade Classifier:**
   Obtain `cars.xml` from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## Usage
### Vehicle Detection from Image
```bash
python vehicle_detection_image.py --image path/to/your/image.jpg
```

### Vehicle Detection from Video
```bash
python vehicle_detection_video.py --video path/to/your/video.mp4
```

## Features
- Detection and counting of vehicles in images and video streams.
- Real-time visualization with bounding boxes around detected vehicles.
- Configurable parameters for cascade classifier tuning.

  ![Vehicle Image](Source/vec.jpg)

## Video Reference
Watch the vehicle detection system in action: [Video Link](https://www.example.com/video)

## Documentation
For detailed documentation and research paper, refer to [Vehicle Detection and Counting System Documentation](https://www.canva.com/design/DAGII0M8RI4/jkV_iCriFL3ZnMikVJeY9Q/view).

## Developer Information
- **Developer:** Yuvraj Singh Chowdhary
- **Email:** chowdharyyuvrajsingh@gmail.com
- **LinkedIn:** [Connect with me](https://www.linkedin.com/in/yuvrajsinghchowdhary/)

## Training Vectors and Videos
The repository includes essential resources:
- Training vectors
- Sample videos
- Shell scripts for video processing

These resources facilitate configuration and testing of the system's functionalities.

## Images

![Traffic Image](Source/traff.jpg)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.



