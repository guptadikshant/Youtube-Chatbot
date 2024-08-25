# Setup
## For Windows
1) First make sure you have latest versio of  **Visual C++ Redistributable**. If you don't have then download it using **visual studio community 2022** from this [site](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170). This will resolve the issue of **_fbgemm.dll_** not found error.
2) Also need to install **ffmpeg** for audio processing
3) Once this is done clone this repo and follow below steps
    - Open the cloned repo in any of the IDE
    - Create an virtual environment by either using python's venv module or conda. It upto you which one you prefer.
    I created the virtual environment using python's venv module
    ```python
    python venv <name of the environment>
    ```
    Once the virtual environment created, we need to activate it using the below command
    ```python
    venv\Scripts\activate
    ```
    And then install all the requirements
    ```python
    pip install -r requirements.txt
    ```
        